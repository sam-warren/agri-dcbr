import Vue from "vue";
import Vuex, { StoreOptions } from "vuex";

import { profile, operationDetails, operationLocations, breedingDetails, animalIdentification, app } from "./registration";
import { RootState } from "./types";

Vue.use(Vuex);

const store: StoreOptions<RootState> = {
  state: {
    version: "1.0.0"
  },
  modules: {
    app,
    profile,
    operationDetails,
    operationLocations,
    breedingDetails,
    animalIdentification
  }
};

export default new Vuex.Store<RootState>(store);

