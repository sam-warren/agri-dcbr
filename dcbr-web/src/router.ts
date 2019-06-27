import Vue from "vue";
import Router from "vue-router";

import Home from "./views/Home.vue";
import OperationRegistration from "./views/OperationRegistration.vue";

Vue.use(Router);

// export default new Router({
//   mode: 'history',
//   base: process.env.BASE_URL,
//   routes: [],
// });

const router = new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/secret",
      name: "secret",
      component: () =>
        // import(/* webpackChunkName: "secret" */ "./views/Secret.vue"),
        import("./views/Secret.vue"),
      meta: {
        requiresAuth: false
      }
    },
    {
      path: "/register",
      name: "register",
      // component: () =>
      //   import(
      //     /* webpackChunkName: "register" */ "./views/OperatorRegistration.vue"
      //   ),
      //   import("./views/OperatorRegistration.vue"),
      // meta: {
      //   requiresAuth: false
      // }
      component: OperationRegistration
    }
  ]
});

// router.beforeEach((to, from, next) => {
//   if (to.matched.some(record => record.meta.requiresAuth)) {
//     if (router.app.$keycloak.authenticated) {
//       next();
//     } else {
//       const loginUrl = router.app.$keycloak.createLoginUrl();
//       window.location.replace(loginUrl);
//     }
//   } else {
//     next();
//   }
// });

export default router;
