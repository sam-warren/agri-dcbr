import { Module } from "vuex";

import { RootState } from "../types";
import { ProfileActions, OperationDetailsActions, OperationLocationsActions, BreedingDetailsActions, AnimalIdentificationActions, TermsAndConditionsActions, RouteProtectionActions, RenewalActions } from "./actions";
import { ProfileGetters, OperationDetailsGetters, OperationLocationsGetters, BreedingDetailsGetters, AnimalIdentificationGetters, TermsAndConditionsGetters, RouteProtectionGetters, RenewalGetters } from "./getters";
import { ProfileMutations, OperationDetailsMutations, OperationLocationsMutations, BreedingDetailsMutations, AnimalIdentificationMutations, TermsAndConditionsMutations, RouteProtectionMutations, RenewalMutations } from "./mutations";
import { ProfileTypes, OperationDetailsTypes, OperationLocationsTypes, BreedingDetailsTypes, AnimalIdentificationTypes, TermsAndConditionsTypes, RouteProtectionTypes, RenewalTypes } from "./types";
import { ProfileState, OperationDetailsState, OperationLocationsState, BreedingDetailsState, AnimalIdentificationState, TermsAndConditionsState, RouteProtectionState, RenewalState } from "./state"

const namespaced: boolean = true;

export const profile: Module<ProfileTypes, RootState> = {
  namespaced,
  state: ProfileState,
  getters: ProfileGetters,
  actions: ProfileActions,
  mutations: ProfileMutations
};

export const operationDetails: Module<OperationDetailsTypes, RootState> = {
  namespaced,
  state: OperationDetailsState, 
  getters: OperationDetailsGetters,
  actions: OperationDetailsActions,
  mutations: OperationDetailsMutations
};

export const operationLocations: Module<OperationLocationsTypes, RootState> = {
  namespaced,
  state: OperationLocationsState,
  getters: OperationLocationsGetters,
  actions: OperationLocationsActions,
  mutations: OperationLocationsMutations
};

export const breedingDetails: Module<BreedingDetailsTypes, RootState> = {
  namespaced,
  state: BreedingDetailsState,
  getters: BreedingDetailsGetters,
  actions: BreedingDetailsActions,
  mutations: BreedingDetailsMutations
};

export const animalIdentification: Module<AnimalIdentificationTypes, RootState> = {
  namespaced,
  state: AnimalIdentificationState,
  getters: AnimalIdentificationGetters,
  actions: AnimalIdentificationActions,
  mutations: AnimalIdentificationMutations
};

export const termsAndConditions: Module<TermsAndConditionsTypes, RootState> = {
  namespaced,
  state: TermsAndConditionsState,
  getters: TermsAndConditionsGetters,
  actions: TermsAndConditionsActions,
  mutations: TermsAndConditionsMutations
}

export const routeProtection: Module<RouteProtectionTypes, RootState> = {
  namespaced,
  state: RouteProtectionState,
  getters: RouteProtectionGetters,
  actions: RouteProtectionActions,
  mutations: RouteProtectionMutations,
}

export const renewal: Module<RenewalTypes, RootState> = {
  namespaced,
  state: RenewalState,
  getters: RenewalGetters,
  actions: RenewalActions,
  mutations: RenewalMutations,
}