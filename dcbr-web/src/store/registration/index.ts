import { Module } from "vuex";

import { RootState } from "../types";
import { actions } from "./actions";
import { getters } from "./getters";
import { mutations } from "./mutations";
import { RegistrationState } from "./types";

export const state: RegistrationState = {
  profile: {
    firstName: "John",
    middleName: "Ray",
    lastName: "Johnson",
    commType: "Email",
    phone: "2501234567",
    email: "johnrj@gmail.com",
    streetNumber: 123,
    aptNumber: 456,
    streetName: "Imaginary",
    city: "CodeTown",
    postalCode: "A1B2C3",
    homeAsOperation: true,
  },
  error: false
};

const namespaced: boolean = true;

export const profile: Module<RegistrationState, RootState> = {
  namespaced,
  state,
  getters,
  actions,
  mutations
};
