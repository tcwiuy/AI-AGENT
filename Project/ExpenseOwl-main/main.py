import os
from fastapi import FastAPI
from dotenv import load_dotenv

# Load biến môi trường từ file .env
load_dotenv()

APP_NAME = os.getenv("APP_NAME", "Expense Service")
PORT = int(os.getenv("PORT", 8001))

app = FastAPI(
    title=APP_NAME,
    description="Microservice quản lý chi tiêu",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": f"Chào mừng đến với {APP_NAME}!"}

@app.get("/api/v1/health")
def health_check():
    return {
        "service": "expense-service",
        "status": "UP",
        "environment": os.getenv("APP_ENV", "development")
    }

if __name__ == "__main__":
    import uvicorn
    # Chạy server với port lấy từ .env
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, reload=True)