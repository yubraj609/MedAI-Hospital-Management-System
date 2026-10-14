# MediAI — AI-Based Hospital Management System

This project is a final-year B.Tech full-stack medical management system built with React, Express, and a Python AI service.

## Project Structure

- `client/` — React frontend
- `server/` — Node.js + Express backend
- `ai-service/` — FastAPI AI service
- `uploads/` — uploaded patient files

## Tech Stack

- Frontend: React + Vite
- Backend: Node.js + Express
- AI: Python + FastAPI
- Database: MongoDB (planned)
- Auth: JWT + bcrypt (planned)

## Run Frontend

```bash
cd client
npm install
npm run dev
```

## Run Backend

```bash
cd server
npm install
PORT=5001 npm run dev
```

On Windows PowerShell:

```powershell
cd server
npm install
$env:PORT = 5001
npm run dev
```

The app uses port 5001 by default to avoid conflicts with other local services.

## Run AI Service

```bash
cd ai-service
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install fastapi uvicorn pydantic
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

## Features Included in this Starter

- Admin dashboard style
- Doctor directory
- Appointment booking UI
- Patient records view
- AI assistant interface
- Backend health endpoint
- AI symptom checker endpoint

## Next Improvements

- Add authentication and role-based access control
- Integrate MongoDB models
- Add doctor/patient CRUD APIs
- Add PDF report upload and summarization
- Add notification and audit log modules
- Add ML disease prediction models

## Final-Year Project Focus

This starter gives you a real implementation foundation for:
- SRS
- ER Diagram
- UML diagrams
- Project report
- Demo app
- Resume-ready architecture
