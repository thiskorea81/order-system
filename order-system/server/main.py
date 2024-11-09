from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS 설정 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vue.js가 실행 중인 포트
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 주문 데이터 구조 정의
class Order(BaseModel):
    name: str
    item: str
    quantity: int

# 주문 접수 엔드포인트
@app.post("/order")
async def create_order(order: Order):
    return {"message": "Order received", "order": order}
