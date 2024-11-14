from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI()

# CORS 설정
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
    notes: Optional[str] = None
    status: str = Field(default="대기 중")  # 주문 상태 필드 추가, 기본값은 "대기 중"

# 임시로 주문을 저장할 리스트
orders: List[Order] = []

# 주문 접수 엔드포인트
@app.post("/order")
async def create_order(order: Order):
    orders.append(order)  # 주문 데이터를 리스트에 저장
    return {"message": "Order received", "order": order}

# 모든 주문 조회 엔드포인트
@app.get("/orders")
async def get_orders():
    return {"orders": orders}
