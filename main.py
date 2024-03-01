import uvicorn
from fastapi import FastAPI, APIRouter
from views.question import router as question_router
from views.answer import router as answer_router
from views.result import router as result_router
from settings import settings

app = FastAPI(title="Interview Bot API", version="1.0.0")


@app.get("/")
def read_root():
    # print(">>>>>>>>>>>>>> HELLO", settings.postgres_db)
    return {"Hello": "World"}


api_router = APIRouter()
api_router.include_router(question_router)
api_router.include_router(answer_router)
api_router.include_router(result_router)

app.include_router(api_router, prefix="/api",)

# Run python main.py
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)
