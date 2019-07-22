import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export const store = new Vuex.Store({
  state: {
    operationType: undefined
  },

  mutations: {
    setOperationType(state: { operationType: String }, payload: String) {
      state.operationType = payload;
    }
  },

  actions: {
    setOperationType(context: any, payload: any) {
      context.commit("setOperationType", payload);
    }
  },

  getters: {
    operationType(state: { operationType: String }) {
      return state.operationType;
    }
  }
});
