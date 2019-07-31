import { ActionTree } from "vuex";

import { RootState } from "../types";
import { RegistrationState } from "./types";

export const actions: ActionTree<RegistrationState, RootState> = {
  //actions - profile
  firstName(context: any, payload: string) {
    context.commit("firstName", payload);
  },
  middleName(context: any, payload: string) {
    context.commit("middleName", payload);
  },
  lastName(context: any, payload: string) {
    context.commit("lastName", payload);
  },
  commType(context: any, payload: string) {
    context.commit("commType", payload);
  },
  phone(context: any, payload: string) {
    context.commit("phone", payload);
  },
  email(context: any, payload: string) {
    context.commit("email", payload);
  },

  streetNumber(context: any, payload: string) {
    context.commit("streetNumber", payload);
  },
  aptNumber(context: any, payload: string) {
    context.commit("aptNumber", payload);
  },
  streetName(context: any, payload: string) {
    context.commit("streetName", payload);
  },
  city(context: any, payload: string) {
    context.commit("city", payload);
  },
  postalCode(context: any, payload: string) {
    context.commit("postalCode", payload);
  },
  homeAsOperation(context: any, payload: string) {
      context.commit("homeAsOperation", payload);
  }
};
