from passlib.context import CryptContext
password_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

def hash_password(password: str):
    # Converts plain-text password into a hash
    return password_context.hash(password)

def verify_password(plain_password: str, hash_password: str):
    # Checks whether a plain password matches the stored hash
    return password_context.verify(plain_password,hash_password)


password = "secret123"

hashed = hash_password(password)

print("Original:", password)
print("Hashed:", hashed)

print(
    "Correct:",
    verify_password("secret123", hashed)
)

print(
    "Wrong:",
    verify_password("wrongpassword", hashed)
)
