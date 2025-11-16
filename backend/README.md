# Dushime School Complex - Backend (FastAPI)

This is a lightweight FastAPI backend scaffold for the Dushime School Complex informational site.

Quick start (PowerShell):

1. Create a virtual environment and install deps:

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -r backend\requirements.txt
```

2. Run the app (from repository root):

```powershell
uvicorn backend.app.main:app --reload --port 8000
```

3. Open docs: http://127.0.0.1:8000/docs

Notes:
- SQLite DB file `dushime.db` will be created in the repo root by default.
- Configure SMTP and other settings in a `.env` file at the repo root.
- This scaffold is intentionally small; add authentication, tests, and production settings for a portfolio-ready project.

Docker
------

Run the backend in Docker (recommended for isolation and a consistent dev environment).

Build + run using docker-compose (from repository root):

```powershell
docker-compose up --build
```

Or build and run the backend image manually:

```powershell
docker build -t dushime-backend ./backend
docker run --rm -p 8000:8000 --env-file .env dushime-backend
```

Notes about Docker setup:
- The `backend/Dockerfile` installs dependencies and runs `uvicorn`.
- `docker-compose.yml` mounts `./backend` into the container so you can edit code on the host and see changes (good for development).
- If you want a persistent SQLite database outside the container, map a host folder to the container and update `DATABASE_URL` in `.env` to point to the mounted location.

PostgreSQL with Docker Compose
------------------------------

The included `docker-compose.yml` brings up a Postgres service named `db` and sets the `DATABASE_URL` for the backend to point at it.

So running:

```powershell
docker-compose up --build
```

will start both Postgres and the backend. The compose file sets the example URL:

```
postgresql://postgres:postgres@db:5432/dushime
```

If you prefer to use SQLite locally instead of Postgres, change `DATABASE_URL` in the repo `.env` (or remove the `environment` override in `docker-compose.yml`).
