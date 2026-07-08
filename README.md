# AI-Assisted-guest-review-sentiment-classifier
# AI-Assisted Guest Review Sentiment Classifier

A production-ready full-stack web application designed to collect, manage, and analyze guest reviews. The application uses a Python FastAPI backend to process text strings, calculate AI-driven sentiment analysis metrics, and serve an interactive multi-page frontend alongside a live analytics dashboard.

---

## 📅 Project Timeline & Milestone Progress

### 🔹 Week 1: Core Static Frontend Design
* Built the semantic markup structure for a multi-page web application across 4 distinct views (`home.html`, `about.html`, `login.html`, and `dashboard.html`).
* Engineered a centralized global stylesheet (`style.css`) establishing a clean, unified aesthetic utilizing modern flexbox layouts and responsive grids.

### 🔹 Week 2: Dynamic Interactivity & Theming
* Implemented a universal dark/light mode toggle via client-side JavaScript (`theme.js`), preserving user view preferences using local browser storage mechanisms.
* Added dynamic frontend validations to all text inputs and review submission fields to prevent empty data handling.

### 🔹 Week 3: Backend Framework Initialization
* Constructed a high-performance Python backend server using **FastAPI** and **Uvicorn**.
* Engineered the core web routing protocols to serve static web assets, scripts, stylesheets, and template views directly from the python pipeline.

### 🔹 Week 4: API Engineering & Documentation Testing
* Built out a complete set of 6 foundational RESTful API endpoints implementing mock operational data structures (in-memory lists).
* Formulated a strict Postman API collection workspace to simulate real-world request patterns, successfully exporting and embedding data interactions into a validated `collection.json` manifest file.

### 🔹 Week 5: Database Integration & Schema Migration (Current)
* Migrated the application's core structural architecture from temporary, volatile mock lists over to a persistent, enterprise-grade relational database powered by **PostgreSQL**.
* Configured and deployed **Prisma Client Python** to enforce strict compile-time data typing and automated database migrations.

---

## 📂 Project Structure

```text
AI-Assisted-guest-review-sentiment-classifier/
├── main.py                 # FastAPI backend server application
├── schema.prisma           # Prisma database architecture configuration
├── .env                    # Private local environment variables (Hidden)
├── .env.example            # Public environment structural template
├── collection.json         # Exported Postman API test collection records
├── W5_SchemaDiagram.png    # Visual schema mapping database entities
├── style.css               # Centralized global design stylesheets
├── theme.js                # Core JavaScript managing light/dark view states
└── templates/              # Client-side interface components
    ├── home.html           # Main introduction and entry page
    ├── about.html          # Project background and informational page
    ├── login.html          # Gateway interface for secure credential entries
    └── dashboard.html      # Primary metric visualizations and control table
