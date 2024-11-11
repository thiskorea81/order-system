<template>
    <div class="order-list">
      <h2>주문 목록</h2>
      <ul>
        <li v-for="(order, index) in orders" :key="index">
          {{ order.name }} - {{ order.item }} (수량: {{ order.quantity }})
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: "OrderList",
    data() {
      return {
        orders: [],
      };
    },
    async created() {
      try {
        const response = await fetch("http://127.0.0.1:8000/orders");
        const data = await response.json();
        this.orders = data.orders;
      } catch (error) {
        console.error("주문 목록을 불러오는 중 오류가 발생했습니다:", error);
      }
    },
  };
  </script>
  
  <style scoped>
  .order-list {
    max-width: 400px;
    margin: 20px auto;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 5px;
  }
  </style>
  