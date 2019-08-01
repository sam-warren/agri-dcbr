import Vue from "vue";
import Vuex, { StoreOptions } from "vuex";

import { profile } from "./registration";
import { operationDetails } from "./registration";
import { breedingDetails } from "./registration";
import { animalIdentification } from "./registration";
import { RootState } from "./types";

Vue.use(Vuex);

const store: StoreOptions<RootState> = {
  state: {
    version: "1.0.0"
  },
  modules: {
    profile,
    operationDetails,
    breedingDetails,
    animalIdentification
  }
};

export default new Vuex.Store<RootState>(store);
