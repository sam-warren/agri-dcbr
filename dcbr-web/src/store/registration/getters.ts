import { GetterTree } from "vuex";

import { RootState } from "../types";
import { RegistrationState } from "./types";

export const getters: GetterTree<RegistrationState, RootState> = {
  //getters - profile
  firstName(state: any): string {
    const { profile } = state;
    return profile!.firstName || "";
  },
  middleName(state: any): string {
    const { profile } = state;
    return profile!.middleName || "";
  },
  lastName(state: any): string {
    const { profile } = state;
    return profile!.lastName || "";
  },
  commType(state: any): string {
    const { profile } = state;
    return profile!.commType || "";
  },
  phone(state: any): string {
    const { profile } = state;
    return profile!.phone || "";
  },
  email(state: any): string {
    const { profile } = state;
    return profile!.email || "";
  },
  streetNumber(state: any): number {
    const { profile } = state;
    return profile!.streetNumber || 0;
  },
  aptNumber(state: any): number {
    const { profile } = state;
    return profile!.aptNumber || 0;
  },
  streetName(state: any): string {
    const { profile } = state;
    return profile!.streetName || "";
  },
  city(state: any): string {
    const { profile } = state;
    return profile!.city || "";
  },
  postalCode(state: any): string {
    const { profile } = state;
    return profile!.postalCode || "";
  }
};
