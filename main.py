import os
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from prisma import Prisma

app = FastAPI()

# Enable CORS so your frontend javascript can talk to your backend cleanly
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1. Initialize Prisma Client
prisma = Prisma()

@app.on_event("startup")
async def startup():
    await prisma.connect()

@app.on_event("shutdown")
async def shutdown():
    if prisma.is_connected():
        await prisma.disconnect()

# Helper function to read HTML files directly and bypass Jinja2's Python 3.14 bug
def render_template(filename: str) -> str:
    path = os.path.join("templates", filename)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

# --- DIRECT FIXED ROUTES FOR CSS AND JS ASSETS ---

@app.get("/static/style.css")
@app.get("/style.css")
async def get_css():
    # Explicitly looks for style.css right in your main project folder
    return FileResponse("style.css", media_type="text/css")

@app.get("/static/theme.js")
@app.get("/theme.js")
async def get_js():
    # Explicitly looks for theme.js right in your main project folder
    return FileResponse("theme.js", media_type="application/javascript")

# --- NAVIGATION ROUTES ---

@app.get("/", response_class=HTMLResponse)
async def home():
    return render_template("home.html")

@app.get("/about", response_class=HTMLResponse)
async def about():
    return render_template("about.html")

@app.get("/login", response_class=HTMLResponse)
async def login():
    return render_template("login.html")

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard():
    return render_template("dashboard.html")

@app.get("/description.html", response_class=HTMLResponse)
async def description_fallback():
    return render_template("description.html")

# --- API ROUTES FOR DATA ---

@app.get("/api/reviews")
async def get_reviews_api():
    reviews = await prisma.review.find_many(order={"createdAt": "desc"})
    return reviews

@app.post("/api/reviews")
async def create_review_api(
    text: str = Form(...), 
    user: str = Form(...), 
    sentiment: str = Form(...), 
    score: float = Form(...)
):
    await prisma.review.create(
        data={
            "text": text,
            "user": user,
            "sentiment": sentiment,
            "score": score
        }
    )
    return RedirectResponse(url="/dashboard", status_code=303)