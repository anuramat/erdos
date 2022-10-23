from fastapi import Depends
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app import models
from app.config import settings
from app.database import get_db


def create_token(user: models.User) -> str:
    # HACK for some reason not working
    # data = schemas.UserData.from_orm(user)
    data = {"email": user.email, "id": user.id}
    return jwt.encode(data, settings.JWT_SECRET, algorithm=settings.JWT_ALGO)


def verify_token(token: str, db: Session = Depends(get_db)) -> bool:
    try:
        data = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGO])
        user = db.query(models.User).filter_by(**data).first()
        if user is not None:
            return True
    except JWTError:
        return False
    return False
