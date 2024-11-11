<template>
    <div class="order-form">
      <h2>주문하기</h2>
      <form @submit.prevent="submitOrder">
        <div>
          <label for="name">이름:</label>
          <input type="text" v-model="name" id="name" required />
        </div>
        <div>
          <label for="item">상품명:</label>
          <input type="text" v-model="item" id="item" required />
        </div>
        <div>
          <label for="quantity">수량:</label>
          <input type="number" v-model="quantity" id="quantity" min="1" required />
        </div>
        <button type="submit">주문 제출</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: "OrderForm",
    data() {
      return {
        name: "",
        item: "",
        quantity: 1,
      };
    },
    methods: {
      async submitOrder() {
        const orderData = {
          name: this.name,
          item: this.item,
          quantity: this.quantity,
        };
        try {
          const response = await fetch("http://127.0.0.1:8000/order", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(orderData),
          });
          const result = await response.json();
          console.log(result); // 서버로부터 받은 응답을 콘솔에 출력합니다.
          this.$router.push("/confirmation");
        } catch (error) {
          console.error("주문 전송 중 오류가 발생했습니다:", error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .order-form {
    max-width: 400px;
    margin: 20px auto;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 5px;
  }
  .order-form div {
    margin-bottom: 10px;
  }
  </style>
  