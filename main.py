import uvicorn
from fastapi import FastAPI, APIRouter, Request
from views.question import router as question_router
from views.answer import router as answer_router
from views.result import router as result_router
from database.db import engine, Base
from fastapi.responses import JSONResponse
from exceptions.base import NotFoundError


app = FastAPI(title="Interview Bot API", version="1.0.0")

Base.metadata.create_all(bind=engine)


api_router = APIRouter()
api_router.include_router(question_router)
api_router.include_router(answer_router)
api_router.include_router(result_router)

app.include_router(api_router, prefix="/api",)


@app.exception_handler(NotFoundError)
def exception_handler(request: Request, exc: NotFoundError):
    return JSONResponse(
        status_code=404,
        content={"message": f"{exc.details}"},
    )


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)