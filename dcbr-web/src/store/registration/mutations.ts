import { MutationTree } from "vuex";

import { RegistrationState } from "../registration/types";

export const mutations: MutationTree<RegistrationState> = {
  firstName(state: any, payload: string) {
    state.error = false;
    state.profile!.firstName = payload;
  },
  middleName(state: any, payload: string) {
    state.error = false;
    state.profile!.middleName = payload;
  },
  lastName(state: any, payload: string) {
    state.error = false;
    state.profile!.lastName = payload;
  },
  commType(state: any, payload: string) {
    state.error = false;
    state.profile!.commType = payload;
  },
  phone(state: any, payload: string) {
    state.error = false;
    state.profile!.phone = payload;
  },
  email(state: any, payload: string) {
    state.error = false;
    state.profile!.email = payload;
  },
  streetNumber(state: any, payload: number) {
    state.error = false;
    state.profile!.streetNumber = payload;
  },
  aptNumber(state: any, payload: number) {
    state.error = false;
    state.profile!.aptNumber = payload;
  },
  streetName(state: any, payload: string) {
    state.error = false;
    state.profile!.streetName = payload;
  },
  city(state: any, payload: string) {
    state.error = false;
    state.profile!.city = payload;
  },
  postalCode(state: any, payload: string) {
    state.error = false;
    state.profile!.postalCode = payload;
  }
};
