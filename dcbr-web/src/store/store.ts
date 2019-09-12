import Vue from "vue";
import VuexPersistence from "vuex-persist"
import Vuex, { StoreOptions } from "vuex";

import { profile, operationDetails, operationLocations, breedingDetails, animalIdentification, termsAndConditions, routeProtection } from "./registration";
import { RootState } from "./types";

Vue.use(Vuex);

const vuexLocalStorage = new VuexPersistence<RootState>({
  storage: window.localStorage
})

const store: StoreOptions<RootState> = {
  plugins: [
    vuexLocalStorage.plugin
  ],
  state: {
    version: "1.0.0"
  },
  modules: {
    profile,
    operationDetails,
    operationLocations,
    breedingDetails,
    animalIdentification,
    termsAndConditions,
    routeProtection
  }
};

export default new Vuex.Store<RootState>(store);

