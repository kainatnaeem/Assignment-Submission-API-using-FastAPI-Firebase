from fastapi import FastAPI
import uvicorn
from routes.user_route import router as auth_router
from routes.assignment_route import router as assignment_router
from routes.submission_route import router as submission_router
app = FastAPI()
app.include_router(auth_router)
app.include_router(assignment_router)
app.include_router(submission_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload = True)