from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app import models
from app.config import settings
from app.database import get_db

# TODO generates wrong autodocumentation (field names)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def create_token(user: models.User) -> str:
    # HACK for some reason not working
    # data = schemas.UserData.from_orm(user)
    data = {"email": user.email, "id": user.id}
    return jwt.encode(data, settings.JWT_SECRET, algorithm=settings.JWT_ALGO)


def verify_token(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status.HTTP_401_UNAUTHORIZED, detail=f"Invalid credentials"
    )
    try:
        data = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGO])
        user = db.query(models.User).filter_by(**data).first()
        if user is None:
            raise credentials_exception
        return user.id
    except:
        raise credentials_exception
