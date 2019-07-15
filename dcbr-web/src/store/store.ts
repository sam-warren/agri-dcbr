import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export const store = new Vuex.Store({
    state: {
        operationType: "BREEDER",
    },

    mutations: {
        setOperationType(state: {operationType: String}, payload: String) {
            state.operationType = payload;
        },
    },

    actions: {
        setOperationTypeAction(context: any, payload: any) {
            context.commit('setOperationType', payload)
        },
    },

    getters: {
        currentOperationType (state: {operationType: String}) {
            return state.operationType;
        },
    },
});