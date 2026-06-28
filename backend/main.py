# backend/main.py
import os
from typing import Optional, List
from fastapi import FastAPI, HTTPException, status, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import uvicorn


# 1. Load configuration from environment file
load_dotenv()
PORT = int(os.getenv("PORT", 5000))
HOST = os.getenv("HOST", "127.0.0.1")

app = FastAPI(
    title="AI Guest Review Sentiment Classifier API",
    description="Backend API primitives tracking evaluation matrix arrays.",
    version="1.0.0"
)

# 2. Configure CORS Middleware
# This allows your frontend (running on ports like 3000 or 5173) to securely communicate with this server
# 2. Configure CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=False,  # Set to False for local testing to prevent 403 errors
    allow_methods=["*"],  # Allows GET, POST, PUT, DELETE
    allow_headers=["*"],  # Allows all headers
)

# 3. Define the Core Data Model (Schema Validation)
class Review(BaseModel):
    id: int
    text: str = Field(..., min_length=5, description="The structural context text string of the review.")
    user: str = Field(..., description="The user node identifying the submitter.")
    sentiment: str = Field(..., description="Classification tier: Positive, Neutral, or Negative.")
    score: float = Field(..., ge=-1.0, le=1.0, description="Sentiment metric tracking weight parameter.")

# Class wrapper model specifically optimized for post updates (so ID isn't required in payload)
class ReviewCreateUpdate(BaseModel):
    text: str
    user: str
    sentiment: str
    score: float

# 4. Initialize In-Memory Data Store Array Reference
in_memory_reviews_db: List[Review] = [
    Review(id=1, text="The stay was amazing! The staff was very helpful and the room was spotless.", user="John D.", sentiment="Positive", score=0.92),
    Review(id=2, text="The hotel is okay. It's clean and the location is good, but breakfast can be better.", user="Sarah K.", sentiment="Neutral", score=0.48),
    Review(id=3, text="Very disappointed with the service. The room was not clean and staff rude.", user="Michael T.", sentiment="Negative", score=-0.86)
]

# =====================================================================
# 5. DESIGNING THE 6 REST ENDPOINTS
# =====================================================================

# ENDPOINT 1: GET ALL REVIEWS
@app.get("/api/reviews", response_model=List[Review], status_code=status.HTTP_200_OK)
def get_all_reviews():
    """Fetches the full dataset tracking active review parameters."""
    return in_memory_reviews_db


# ENDPOINT 2: SEARCH REVIEWS (Query parameters filter tracking)
@app.get("/api/reviews/search", response_model=List[Review], status_code=status.HTTP_200_OK)
def search_reviews(q: str = Query(..., min_length=1, description="The text token search query parameter string")):
    """Filters data structures matching a token search parameter string match."""
    filtered_results = [
        review for review in in_memory_reviews_db 
        if q.lower() in review.text.lower() or q.lower() in review.user.lower()
    ]
    return filtered_results


# ENDPOINT 3: GET SINGLE REVIEW BY ID
@app.get("/api/reviews/{review_id}", response_model=Review, status_code=status.HTTP_200_OK)
def get_review_by_id(review_id: int):
    """Fetches one explicit review record matching an input ID parameter node."""
    for review in in_memory_reviews_db:
        if review.id == review_id:
            return review
    # Basic Exception Handler Response triggered cleanly
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Review record matching ID node [{review_id}] was not found inside database index."
    )


# ENDPOINT 4: POST CREATE A NEW REVIEW
@app.post("/api/reviews", response_model=Review, status_code=status.HTTP_201_CREATED)
def create_review(payload: ReviewCreateUpdate):
    """Submits a fresh review object array to server memory matrix."""
    # Data auto validation happens automatically via Pydantic model configuration rules
    if not payload.text.strip():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Review text cannot be blank.")
        
    # Generate incremental primary index key tracking rule
    new_id = max([r.id for r in in_memory_reviews_db], default=0) + 1
    
    new_review = Review(
        id=new_id,
        text=payload.text,
        user=payload.user,
        sentiment=payload.sentiment,
        score=payload.score
    )
    in_memory_reviews_db.append(new_review)
    return new_review


# ENDPOINT 5: PUT UPDATE AN EXISTING REVIEW
@app.put("/api/reviews/{review_id}", response_model=Review, status_code=status.HTTP_200_OK)
def update_review(review_id: int, payload: ReviewCreateUpdate):
    """Modifies context parameters of an existing entity match inside memory arrays."""
    for index, review in enumerate(in_memory_reviews_db):
        if review.id == review_id:
            updated_review = Review(
                id=review_id,
                text=payload.text,
                user=payload.user,
                sentiment=payload.sentiment,
                score=payload.score
            )
            in_memory_reviews_db[index] = updated_review
            return updated_review
            
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Cannot execute parameter update. Target index ID [{review_id}] does not exist."
    )


# ENDPOINT 6: DELETE A SPECIFIC REVIEW
@app.delete("/api/reviews/{review_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_review(review_id: int):
    """Purges an entries record index out of memory framework completely."""
    global in_memory_reviews_db
    for index, review in enumerate(in_memory_reviews_db):
        if review.id == review_id:
            in_memory_reviews_db.pop(index)
            # 204 No Content responds with an empty body state output
            return
            
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Cannot execute delete routing pipeline. Target index ID [{review_id}] does not exist."
    )

# 6. Fallback Script Hook Initialization for Uvicorn Wrapper Execution Node
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host=HOST, port=PORT, reload=True)