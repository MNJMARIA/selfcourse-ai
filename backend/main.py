from fastapi import FastAPI

app = FastAPI(title = "SelfCourse AI")

@app.get("/health")
def health():
    return {"status": "ok", "project": "SelfCourse AI"}
