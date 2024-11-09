<template>
  <div id="app">
    <h1>웹 주문 시스템</h1>
    <router-view />
  </div>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "App",
});
</script>
