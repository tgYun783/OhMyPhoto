from passlib.context import CryptContext

# bcrypt 암호화 방식을 사용
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    """일반 비밀번호와 해시된 비밀번호를 비교"""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    """일반 비밀번호를 해시값으로 변환"""
    return pwd_context.hash(password)