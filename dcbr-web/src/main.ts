import './plugins/vuetify';
import './registerServiceWorker';

import VueKeycloakJs from '@dsb-norge/vue-keycloak-js';
import Axios from 'axios';
import Vue from 'vue';

import App from './App.vue';
import router from './router';

Vue.config.productionTip = false;

if (process.env.NODE_ENV === 'development') {
  Vue.use(VueKeycloakJs, {
    config: {
      url: 'https://sso-dev.pathfinder.gov.bc.ca/auth',
      clientId: 'dcbr-web',
      realm: 'uicn0kkh'
    },
    onReady: (keycloak: any) => {
      new Vue({
        router,
        render: h => h(App)
      }).$mount('#app');
    }
  });
} else {
  Axios.get('/keycloak-config.json').then(response => {
    Vue.use(VueKeycloakJs, {
      config: response.data,
      onReady: (keycloak: any) => {
        new Vue({
          router,
          render: h => h(App)
        }).$mount('#app');
      }
    });
  });
}
