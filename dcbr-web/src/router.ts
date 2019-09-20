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
      path: "/home",
      name: "home",
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
      }
    },
    {
      path: "/register",
      name: "register",
      component: () => import(/* webpackChunkName: "registration" */ "./views/OperationRegistration.vue"),
      meta: {
        requiresAuth: false
      }
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
  if (to.path === "/") {
    if (store.getters["routeProtection/formType"] === "") {
      if (!(from.path === "/home")) {
        next("/home");
      } else {
        next();
      }
    } else {
      next();
    }
  } else if (to.path === "/review") {
    if (!store.getters["routeProtection/registerFormOk"]) {
      if (!(from.path === "/home")) {
        next("/home");
      } else {
        next();
      }
    } else {
      next();
    }
  } else if (to.path === "/confirmation") {
    if (!store.getters["routeProtection/reviewFormOk"]) {
      if (!(from.path === "/home")) {
        next("/home");
      } else {
        next();
      }
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;
