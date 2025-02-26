from os import access

from fastapi import APIRouter, Response, HTTPException, Depends
from app.users.service import UserService
from app.users.schemas import SUserAuth
from app.users.auth import get_password_hash, verify_password
from app.users.models import Users
from app.users.auth import authenticate_user, create_access_token
from app.users.dependencies import get_current_user
from app.users.dependencies import get_current_user_admin
from app.users.exceptions import UserAlreadyExistsException, IncorrectEmailOrPasswordException

router = APIRouter(
    prefix="/auth",
    tags=["Авторизация / Пользователи"]
)


@router.get("/users", description="Получить всех пользователей")
async def get_users():
    return await UserService.find_all()


@router.post("/register", description="Регистрация пользователя")
async def register_user(user_data: SUserAuth):
    existing_user = await UserService.find_one_or_none(email=user_data.email)
    if existing_user:
        raise UserAlreadyExists
    else:
        hashed_password = get_password_hash(user_data.password)
        await UserService.add(email=user_data.email, hashed_password=hashed_password)


@router.post("/login", description="Вход пользователя")
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise IncorrectEmailOrPasswordException
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("booking_access_token", access_token, httponly=True)
    return access_token


@router.post("/logout", description="Выход пользователя")
async def logout_user(response: Response):
    response.delete_cookie("booking_access_token")
    return "Пользователь вышел"


@router.get("/me")
async def get_me_user(current_user: Users = Depends(get_current_user)):
    return current_user


@router.get("/all")
async def get_all_user(current_user: Users = Depends(get_current_user_admin)):
    return await UserService.find_all()
