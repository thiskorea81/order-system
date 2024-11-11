<template>
  <div id="app">
    <h1>웹 주문 시스템</h1>
    <router-view />
    <OrderList />
  </div>
</template>

<script>
import OrderList from "./components/OrderList.vue";

export default {
  name: "App",
  components: {
    OrderList,
  },
};
</script>
