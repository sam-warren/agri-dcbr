import { GetterTree } from "vuex";

import { RootState } from "../types";
import { RegistrationState } from "./types";

export const getters: GetterTree<RegistrationState, RootState> = {
  //getters - profile
  firstName(state): string {
    const { profile } = state;
    return profile!.firstName || "";
  },
  middleName(state): string {
    const { profile } = state;
    return profile!.middleName || "";
  },
  lastName(state): string {
    const { profile } = state;
    return profile!.lastName || "";
  },
  commType(state): string {
    const { profile } = state;
    return profile!.commType || "";
  },
  phone(state): string {
    const { profile } = state;
    return profile!.phone || "";
  },
  email(state): string {
    const { profile } = state;
    return profile!.email || "";
  },
  streetNumber(state): number {
    const { profile } = state;
    return profile!.streetNumber || 0;
  },
  aptNumber(state): number {
    const { profile } = state;
    return profile!.aptNumber || 0;
  },
  streetName(state): string {
    const { profile } = state;
    return profile!.streetName || "";
  },
  city(state): string {
    const { profile } = state;
    return profile!.city || "";
  },
  postalCode(state): string {
    const { profile } = state;
    return profile!.postalCode || "";
  }
};
