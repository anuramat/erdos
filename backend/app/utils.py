from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def calc_hash(plain):
    return pwd_context.hash(plain)


def verify_hash(plain, hashed):
    return pwd_context.verify(plain, hashed)
