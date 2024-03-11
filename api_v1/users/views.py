from fastapi import APIRouter, HTTPException, status
from .schemas import UserGet, UserCreate, UserUpdate
from . import crud

user_router = APIRouter(prefix="users/", tags=["Пользователи"])


@user_router.get("/", response_model=list[UserGet])
async def get_users(session):
    return await crud.get_users(session=session)


@user_router.post("/", response_model=UserGet)
async def create_user(session, user: UserCreate):
    return await crud.create_user(session=session, user=user)


@user_router.get("/{user_id}/")
async def get_user_by_id(user_id: int, session):
    user = crud.get_user_by_id(session=session, user_id=user_id)
    if user is not None:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Пользователь с id = {user_id} не найдет в системе"
    )

