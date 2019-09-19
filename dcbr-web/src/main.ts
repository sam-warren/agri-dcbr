import "./plugins/vuetify";
import "./registerServiceWorker";

import router from "@/router";
import store from "@/store/store";
import Vue from "vue";
import VueTheMask from "vue-the-mask";
import VuexPersist from "vuex-persist"

import App from "./App.vue";
Vue.use(VueTheMask);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
