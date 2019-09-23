import { ActionTree } from "vuex";

import { RootState } from "../types";
import { ProfileTypes, OperationDetailsTypes, OperationLocationsTypes, BreedingDetailsTypes, AnimalIdentificationTypes, TermsAndConditionsTypes, RouteProtectionTypes, RenewalTypes } from "./types";
import { Location } from "./types";

export const ProfileActions: ActionTree<ProfileTypes, RootState> = {
  // Profile
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
  streetNumber(context: any, payload: number) {
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
  homeRegion(context: any, payload: string) {
    context.commit("homeRegion", payload);
  },
};

export const OperationDetailsActions: ActionTree<OperationDetailsTypes, RootState> = {
  // Operation Details
  operationName(context: any, payload: string) {
    context.commit("operationName", payload);
  },
  operationType(context: any, payload: string) {
    context.commit("operationType", payload);
  },
  opWebsite(context: any, payload: string) {
    context.commit("opWebsite", payload);
  },
  assocName(context: any, payload: string) {
    context.commit("assocName", payload);
  },
  accidentalBreeding(context: any, payload: string) {
    context.commit("accidentalBreeding", payload);
  },
  numWorkers(context: any, payload: number) {
    context.commit("numWorkers", payload);
  },
  animalType(context: any, payload: string) {
    context.commit("animalType", payload);
  },
  numDogBreeds(context: any, payload: number) {
   context.commit("numDogBreeds", payload);
  },
  numCatBreeds(context: any, payload: number) {
   context.commit("numCatBreeds", payload);
  },
  hasVet(context: any, payload: string) {
    context.commit("hasVet", payload);
  },
};

export const OperationLocationsActions: ActionTree<OperationLocationsTypes, RootState> = {
  // Operation Locations
  hasAdditionalLocations(context: any, payload: string) {
    context.commit("hasAdditionalLocations", payload);
  },
  locations(context: any, payload: { operation: string }) {
    context.commit("locations", payload);
  },
  updateLocationProperty(context: any, payload: {index: number, property: string, value: any}) {
    context.commit("updateLocationProperty", payload);
  },
};

export const BreedingDetailsActions: ActionTree<BreedingDetailsTypes, RootState> = {
  // Breeding Details
  femaleIntactDogNum(context: any, payload: number) {
    context.commit("femaleIntactDogNum", payload);
  },
  femaleIntactCatNum(context: any, payload: number) {
    context.commit("femaleIntactCatNum", payload);
  },
  littersWhelped(context: any, payload: number) {
    context.commit("littersWhelped", payload);
  },
  littersQueened(context: any, payload: number) {
    context.commit("littersQueened", payload);
  },
  dogsTransferred(context: any, payload: number) {
    context.commit("dogsTransferred", payload);
  },
  dogsSold(context: any, payload: number) {
    context.commit("dogsSold", payload);
  },
  dogsTraded(context: any, payload: number) {
    context.commit("dogsTraded", payload);
  },
  dogsLeased(context: any, payload: number) {
    context.commit("dogsLeased", payload);
  },
  catsTransferred(context: any, payload: number) {
    context.commit("catsTransferred", payload);
  },
  catsSold(context: any, payload: number) {
    context.commit("catsSold", payload);
  },
  catsTraded(context: any, payload: number) {
    context.commit("catsTraded", payload);
  },
  catsLeased(context: any, payload: number) {
    context.commit("catsLeased", payload);
  },
  numCats(context: any, payload: number) {
    context.commit("numCats", payload);
  },
  numDogs(context: any, payload: number) {
    context.commit("numDogs", payload);
  },
};

export const AnimalIdentificationActions: ActionTree<AnimalIdentificationTypes, RootState> = {
  // Animal Identification
  hasPermId(context: any, payload: string) {
    context.commit("hasPermId", payload);
  },
  permIdType(context: any, payload: string) {
    context.commit("permIdType", payload);
  },
  otherPermIdType(context: any, payload: string) {
    context.commit("otherPermIdType", payload);
  },
};

export const TermsAndConditionsActions: ActionTree<TermsAndConditionsTypes, RootState> = {
  // Terms and Conditions
  hasAgreed(context: any, payload: boolean) {
    context.commit("hasAgreed", payload);
  },
};

export const RouteProtectionActions: ActionTree<RouteProtectionTypes, RootState> = {
  // Route Protection
  registerFormOk(context: any, payload: boolean) {
    context.commit("registerFormOk", payload);
  },
  reviewFormOk(context: any, payload: boolean) {
    context.commit("reviewFormOk", payload);
  },
  formType(context: any, payload: string) {
    context.commit("formType", payload);
  },
};

export const RenewalActions: ActionTree<RenewalTypes, RootState> = {
  // Renewal
  renewalFirstName(context: any, payload: string) {
    context.commit("renewalFirstName", payload);
  },
  renewalMiddleName(context: any, payload: string) {
    context.commit("renewalMiddleName", payload);
  },
  renewalLastName(context: any, payload: string) {
    context.commit("renewalLastName", payload);
  },
  registrationNumber(context: any, payload: string) {
    context.commit("registrationNumber", payload);
  },
  expiryDate(context: any, payload: string) {
    context.commit("expiryDate", payload);
  },
}

export const ResetFormActions: ActionTree<{ resetForm: any }, RootState> = {
  // Reset Form
  resetForm(context: any) {
    context.commit("resetForm")
  }
};
