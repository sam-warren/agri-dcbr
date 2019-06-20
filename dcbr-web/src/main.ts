import './plugins/vuetify';
import './registerServiceWorker';

import VueKeycloakJs from '@dsb-norge/vue-keycloak-js';
import Axios from 'axios';
import Vue from 'vue';

import App from './App.vue';
import router from './router';

Axios.get('/keycloak-config.json').then(response => {
  Vue.config.productionTip = false;

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
