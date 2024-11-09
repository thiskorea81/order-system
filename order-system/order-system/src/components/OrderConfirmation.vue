<template>
    <div class="confirmation">
      <h2>주문이 성공적으로 접수되었습니다!</h2>
      <p>주문 내역을 확인해 주셔서 감사합니다.</p>
      <router-link to="/">홈으로 돌아가기</router-link>
    </div>
  </template>
  
  <script>
  export default {
    name: "OrderConfirmation",
  };
  </script>
  
  <style scoped>
  .confirmation {
    text-align: center;
    padding: 20px;
  }
  </style>
  