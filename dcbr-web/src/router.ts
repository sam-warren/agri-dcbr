import store from "@/store/store";
import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

const router = new Router({
  mode: "history",
  base: process.env.BASE_URL,
  scrollBehavior() {
    return { x: 0, y: 0 };
  },
  routes: [
    {
      path: "/",
      name: "index",
      component: () => import(/* webpackChunkName: "home" */ "./views/Home.vue"),
      meta: {
        requiresAuth: false
      }
    },
    {
      path: "/preamble",
      name: "preamble",
      component: () => import(/* webpackChunkName: "preamble" */ "./views/Preamble.vue"),
      meta: {
        requiresAuth: false
      },
    },
    {
      path: "/register",
      name: "register",
      component: () => import(/* webpackChunkName: "registration" */ "./views/OperationRegistration.vue"),
    },
    {
      path: "/review",
      name: "review",
      component: () => import(/* webpackChunkName: "review" */ "./views/Review.vue"),
      meta: {
        requiresAuth: false
      }
    },
    {
      path: "/confirmation",
      name: "confirmation",
      component: () => import(/* webpackChunkName: "confirmation" */ "./views/Confirmation.vue"),
      meta: {
        requiresAuth: false
      }
    }
  ]
});

router.beforeEach((to: any, from: any, next: any) => {
  if (to.path === "/preamble") {
    if (store.getters["routeProtection/formType"] !== "register") {
      next(from.fullPath)
    } else {
      next();
    }
  } else if (to.path === "/register") {
    console.log(from.fullPath)
    if (store.getters["routeProtection/formType"] === "") {
      next(from.fullPath)
    } else {
      next();
    }
  } else if (to.path === "/review") {
    console.log(from.path)
    if (!store.getters["routeProtection/registerFormOk"]) {
      next(from.fullPath)
    } else {
      next();
    }
  } else if (to.path === "/confirmation") {
    console.log(from.fullPath)
    if (!store.getters["routeProtection/reviewFormOk"]) {
      next(from.fullPath)
    } else {
      next();
    }
  } else {
    next()
  } 
});

export default router;
