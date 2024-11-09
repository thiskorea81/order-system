import { createRouter, createWebHistory } from "vue-router";
import OrderForm from "@/components/OrderFrom.vue";
import OrderConfirmation from "@/components/OrderConfirmation.vue";

const routes = [
  {
    path: "/",
    name: "OrderForm",
    component: OrderForm,
  },
  {
    path: "/confirmation",
    name: "OrderConfirmation",
    component: OrderConfirmation,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
