# SelfCourse AI — Personal Learning Platform Generator

[![Python](https://img.shields.io/badge/Python-3.12-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-backend-009688)](https://fastapi.tiangolo.com/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)](https://www.sqlite.org/)
[![Status](https://img.shields.io/badge/Status-Early%20Development-yellow)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A personal, privacy-first learning platform that turns your own study materials (`.docx`, `.pdf`, `.pptx`, `.txt`) into a structured, interactive course — similar to Coursera, but built entirely around content you already own.

The system automatically splits large materials into modules and lessons, generates quizzes based strictly on the provided content, tracks completion progress and quiz scores, and archives a course once it's fully completed. Materials can include personally paid courses and private notes, so the architecture is designed to keep that content off third-party servers wherever possible.

## Project Status

🚧 **Early-stage personal project — actively building the MVP.**
Current state: backend skeleton (FastAPI) running locally with a working health-check endpoint. Core features (auth, file parsing, AI generation) are in progress — see [Roadmap](#roadmap) below.

## Project Highlights

- Turns any `.docx` / `.pdf` / `.pptx` / `.txt` material into a structured course of modules and lessons
- Auto-generated quizzes (single choice, multiple choice, short answer) based only on the source material
- Automatic progress tracking — % completed + average quiz score
- Auto-archiving when a course reaches 100% completion, with manual unarchive option
- **Local-first architecture** — the AI processing step runs on-device by default, so private/paid course content doesn't have to leave the user's machine
- Designed and built solo, with AI-assisted development

## Technologies

| Layer | Technology | Status |
|---|---|---|
| Backend API | Python + FastAPI | ✅ skeleton running |
| Database | SQLite (SQLAlchemy) | 🔜 planned |
| Authentication | JWT + bcrypt | 🔜 planned |
| File parsing | python-docx, python-pptx, pdfplumber / PyMuPDF | 🔜 planned |
| AI generation | Ollama (local LLM), optional no-retention cloud API fallback | 🔜 planned |
| Frontend | React + Tailwind CSS, packaged as a PWA | 🔜 planned |
| Deployment | Local-first (Docker Compose) or free-tier cloud | 🔜 planned |

## Planned Features

### Account Management
- Registration/login (email + password, hashed)
- Personal dashboard with three tabs: active, not started, archived courses

### Material Upload
- Support for `.docx`, `.doc`, `.pptx`, `.pdf`, `.txt`
- Multiple files combined into a single course
- Ability to edit a course later — add/remove material, with progress and quizzes recalculated accordingly

### Course Generation
- Automatic text extraction, structure-aware (headings, slides, paragraphs)
- Automatic splitting into modules/lessons for large materials
- Lesson text generated strictly from the source material — no invented facts
- Auto-generated quiz per module, with the option to regenerate if quality is unsatisfactory

### Progress & Evaluation
- % completed = lessons completed / total lessons
- Average quiz score per course
- Progress bar at course and module level

### Archiving
- Automatic archiving at 100% completion + all quizzes passed
- Archived courses are read-only with a final score
- Manual "unarchive" to retake a course

## Data Model

```
User            — id, name, email, password_hash, created_at
Course          — id, user_id, title, status [not_started|active|archived]
Module          — id, course_id, title, order_index
Lesson          — id, module_id, title, content_text, order_index, is_completed
Quiz            — id, module_id, questions[]
Question        — id, quiz_id, type [single|multi|short], text, options[], correct_answer
QuizAttempt     — id, quiz_id, user_id, score, answers[], completed_at
ProgressRecord  — course_id, percent_completed, average_score, updated_at
```

## Architecture

```
[ Client: Web / PWA (desktop + mobile) ]
              │  HTTPS / secure tunnel
              ▼
[ Backend API (auth, courses, progress) ]
              │
     ┌────────┼─────────────┐
     ▼        ▼              ▼
[File        [AI generation [Database
 parser]      module]        (encrypted)]
     │        │
     ▼        ▼
[docx/pdf/  [Local LLM
 pptx/txt   (Ollama) OR
 → text]    no-retention API]
```

The AI module is isolated from the outside world by default (local model), so private materials don't have to leave the user's device. A cloud AI API is only an optional fallback.

## Privacy & Security

- No user data or course content is sent to third-party services without explicit consent
- If an external AI API is ever used, it must follow a strict no-retention / no-training policy
- Course content encrypted at rest (planned: AES-256)
- Passwords stored hashed only (bcrypt)
- Client–server connection over HTTPS / a secure tunnel, even on a local network

## Repository Structure

```
selfcourse-ai/
├── backend/          # FastAPI application
│   ├── venv/
│   └── main.py
├── frontend/          # React PWA (planned)
├── docs/              # Technical specification & planning docs
└── README.md
```

## Getting Started (current state)

```bash
cd backend
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate  # macOS/Linux
pip install fastapi "uvicorn[standard]"
uvicorn main:app --reload
```

Then open:
- `http://127.0.0.1:8000/health` — health-check endpoint
- `http://127.0.0.1:8000/docs` — interactive Swagger API docs

## Roadmap

- [x] Project skeleton & FastAPI health endpoint
- [ ] SQLAlchemy models (User, Course, Module, Lesson, Quiz, Question, ProgressRecord)
- [ ] JWT authentication (register/login)
- [ ] File upload & text extraction pipeline (docx/pptx/pdf/txt)
- [ ] Local LLM integration (Ollama) for lesson & quiz generation
- [ ] Progress tracking, scoring & auto-archiving logic
- [ ] React + Tailwind frontend, packaged as a PWA
- [ ] End-to-end testing & local-first deployment

## Documentation

The full technical specification — functional and non-functional requirements, data model, architecture, tech stack rationale, risks, and a step-by-step development plan — is available in [`docs/`](docs/).

## What I'm Learning

- Backend API design with FastAPI
- Prompt engineering for structured, fact-constrained content generation
- Local LLM integration (Ollama) and privacy-first system design
- File parsing across multiple document formats
- Full-stack project planning and self-managed iterative development

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

**Author:** Mariia Stepanova
**Type:** Personal project / portfolio case
**Year:** 2026
