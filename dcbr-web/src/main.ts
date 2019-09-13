import "./plugins/vuetify";
import "./registerServiceWorker";

import router from "@/router";
import store from "@/store/store";
import Vue from "vue";
import VuexPersist from "vuex-persist"

import App from "./App.vue";

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
