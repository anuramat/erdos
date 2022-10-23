from app import database, models, schemas
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.oauth2 import create_token
from app import utils

router = APIRouter(tags=["Authentication"])


@router.post("/register")
def register(
    user_creds: schemas.UserCreds,
    db: Session = Depends(database.get_db),
):

    user = db.query(models.User).filter_by(email=user_creds.email).first()

    if user is not None:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f'User with email "{user_creds.email}" already exists',
        )

    email = user_creds.email
    hashed = utils.calc_hash(user_creds.password)

    user = models.User(email=email, hashed=hashed)

    db.add(user)
    db.commit()

    return "registration ok"


@router.post("/login")
def login(
    user_creds: schemas.UserCreds,
    db: Session = Depends(database.get_db),
):

    user = db.query(models.User).filter_by(email=user_creds.email).first()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f'User with email "{user_creds.email}" doesn\'t exist',
        )

    if utils.verify_hash(user_creds.password, user.hashed):
        return create_token(user)
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Incorrect password"
        )
