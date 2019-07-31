import { GetterTree } from "vuex";

import { RootState } from "../types";
import { RegistrationState } from "./types";

export const getters: GetterTree<RegistrationState, RootState> = {
  //getters - profile
  firstName(state: RegistrationState): string {
    const { profile } = state;
    return profile!.firstName || "";
  },
  middleName(state: RegistrationState): string {
    const { profile } = state;
    return profile!.middleName || "";
  },
  lastName(state: RegistrationState): string {
    const { profile } = state;
    return profile!.lastName || "";
  },
  commType(state: RegistrationState): string {
    const { profile } = state;
    return profile!.commType || "";
  },
  phone(state: RegistrationState): string {
    const { profile } = state;
    return profile!.phone || "";
  },
  email(state: RegistrationState): string {
    const { profile } = state;
    return profile!.email || "";
  },
  streetNumber(state: RegistrationState): number {
    const { profile } = state;
    return profile!.streetNumber || 0;
  },
  aptNumber(state: RegistrationState): number {
    const { profile } = state;
    return profile!.aptNumber || 0;
  },
  streetName(state: RegistrationState): string {
    const { profile } = state;
    return profile!.streetName || "";
  },
  city(state: RegistrationState): string {
    const { profile } = state;
    return profile!.city || "";
  },
  postalCode(state: RegistrationState): string {
    const { profile } = state;
    return profile!.postalCode || "";
  },
  homeAsOperation(state: RegistrationState): boolean {
    const { profile } = state;
    return profile!.homeAsOperation || false;
  }
};
