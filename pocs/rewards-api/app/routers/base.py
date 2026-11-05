from fastapi import APIRouter, Request

from app import security as auth
from app.models import Login
from app.services import user as service

router = APIRouter()


@router.get("/")
async def root(request: Request) -> dict[str, str]:
    return {"name": request.app.title, "version": request.app.version, "docs": "/docs"}


@router.post("/auth")
async def get_token(login: Login):
    user = await service.find(email=login.username, include_password=True)
    if not user or not auth.check_password(plain=login.password, hashed=user.get("password")):
        raise auth.EXCEPTION_INVALID_CREDENTIALS
    return auth.create_token(subject=user.get("email"), mood=user.get("mood", ""))
