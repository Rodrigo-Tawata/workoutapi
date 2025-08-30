from fastapi import FastAPI
from workout_api.routers import api_router

app = FastAPI(title='WorkoutApi')
app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "WorkoutApi está rodando 🚀"}