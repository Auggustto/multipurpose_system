from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

### import schemas of routers ###
from app.routers.start import routers
from app.routers.user_router import user_routers
from app.routers.login_router import user_login_routers
from app.routers.tasks_router import tasks_routers
from app.routers.category_router import category_routers


app = FastAPI(
    title="API multipurpose system",
    description="This is a versatile and multifunctional API designed to meet various management needs. With it, you can register and manage everything from task lists to financial control, providing a unique and efficient solution to organize your activities and finances in one place.",
    version="1.0.0"
    )

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    max_age=3600
)

### include all routers ###
app.include_router(router=routers)
app.include_router(router=user_routers)
app.include_router(router=user_login_routers)
app.include_router(router=tasks_routers)
app.include_router(router=category_routers)
