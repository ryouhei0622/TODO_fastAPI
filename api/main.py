from fastapi import FastAPI

app = FastAPI()


# @app.get("/hello")
# async def hello():
#     return {"message": "hello world!"}


from fastapi import FastAPI

from api.routers import done, task

app = FastAPI()
app.include_router(task.router)
app.include_router(done.router)
