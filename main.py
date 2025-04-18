from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controller import user_controller
from service import user_service

app = FastAPI()
app.include_router(user_controller.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins= ["*"],
    allow_credentials= True,
    allow_methods= ["*"],
    allow_headers= ["*"],
)

dummy_data = [
    ("red8732", "senha123"),
    ("a7x", "123456789"),
    ("slipknot", "abc"),
    ("s0ad_", "safepassword")
]

for username, password in dummy_data:
    user_service.create_user(username, password)

@app.get("/")
def root():
    return {"message": "API rodando com sucesso! 🚀"}