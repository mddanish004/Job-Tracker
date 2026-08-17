from fastapi import FastAPI
from app.routers import health, info, applications


app = FastAPI(
    title="Job Application Tracker API",
    version="1.0.0",
)


app.include_router(health.router)
app.include_router(info.router, prefix="/api/v1")
app.include_router(applications.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {
        "message": "Job Application Tracker API"
    }