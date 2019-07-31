import { MutationTree } from "vuex";

import { RegistrationState } from "../registration/types";

export const mutations: MutationTree<RegistrationState> = {
  firstName(state: RegistrationState, payload: string) {
    state.error = false;
    state.profile!.firstName = payload;
  },
  middleName(state: RegistrationState, payload: string) {
    state.error = false;
    state.profile!.middleName = payload;
  },
  lastName(state: RegistrationState, payload: string) {
    state.error = false;
    state.profile!.lastName = payload;
  },
  commType(state: RegistrationState, payload: string) {
    state.error = false;
    state.profile!.commType = payload;
  },
  phone(state: RegistrationState, payload: string) {
    state.error = false;
    state.profile!.phone = payload;
  },
  email(state: RegistrationState, payload: string) {
    state.error = false;
    state.profile!.email = payload;
  },
  streetNumber(state: RegistrationState, payload: number) {
    state.error = false;
    state.profile!.streetNumber = payload;
  },
  aptNumber(state: RegistrationState, payload: number) {
    state.error = false;
    state.profile!.aptNumber = payload;
  },
  streetName(state: RegistrationState, payload: string) {
    state.error = false;
    state.profile!.streetName = payload;
  },
  city(state: RegistrationState, payload: string) {
    state.error = false;
    state.profile!.city = payload;
  },
  postalCode(state: RegistrationState, payload: string) {
    state.error = false;
    state.profile!.postalCode = payload;
  },
  homeAsOperation(state: RegistrationState, payload: boolean) {
    state.error = false;
    state.profile!.homeAsOperation = payload;
    console.log("VUEX: homeAsOperation updated to " + payload);
  }
};
