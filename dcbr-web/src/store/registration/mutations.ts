import { MutationTree } from 'vuex';

import { RegistrationState } from '../registration/types';

export const mutations: MutationTree<RegistrationState> = {
  firstName(state, payload: string) {
    state.error = false;
    state.profile!.firstName = payload;
  },
  middleName(state, payload: string) {
    state.error = false;
    state.profile!.middleName = payload;
  },
  lastName(state, payload: string) {
    state.error = false;
    state.profile!.lastName = payload;
  },
  commType(state, payload: string) {
    state.error = false;
    state.profile!.commType = payload;
  },
  phone(state, payload: string) {
    state.error = false;
    state.profile!.phone = payload;
  },
  email(state, payload: string) {
    state.error = false;
    state.profile!.email = payload;
  },
  streetNumber(state, payload: number) {
    state.error = false;
    state.profile!.streetNumber = payload;
  },
  aptNumber(state, payload: number) {
    state.error = false;
    state.profile!.aptNumber = payload;
  },
  streetName(state, payload: string) {
    state.error = false;
    state.profile!.streetName = payload;
  },
  city(state, payload: string) {
    state.error = false;
    state.profile!.city = payload;
  },
  postalCode(state, payload: string) {
    state.error = false;
    state.profile!.postalCode = payload;
  }
};
