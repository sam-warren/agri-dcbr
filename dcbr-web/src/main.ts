import './plugins/vuetify';
import './registerServiceWorker';

import VueKeycloakJs from '@dsb-norge/vue-keycloak-js';
import Vue from 'vue';

import App from './App.vue';
import router from './router';

Vue.config.productionTip = false;

console.log('*****', process.env);

Vue.use(VueKeycloakJs, {
  config: {
    // url: 'http://localhost:8888/auth',
    // clientId: 'vue-app-test',
    // realm: 'uicn0kkh'
    url: process.env.VUE_APP_KEYCLOAK_AUTH_URL,
    clientId: process.env.VUE_APP_KEYCLOAK_CLIENT_ID,
    realm: process.env.VUE_APP_KEYCLOAK_REALM
  },
  onReady: (keycloak: any) => {
    new Vue({
      router,
      render: h => h(App)
    }).$mount('#app');
  }
});
