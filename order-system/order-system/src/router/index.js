import { createRouter, createWebHistory } from "vue-router";
import OrderForm from "@/components/OrderForm.vue";
import OrderConfirmation from "@/components/OrderConfirmation.vue";
import OrderList from "@/components/OrderList.vue";

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
  {
    path: "/orders",
    name: "OrderList",
    component: OrderList,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
