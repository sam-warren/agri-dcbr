import { GetterTree } from "vuex";

import { RootState } from "../types";
import { OperationDetailsTypes, OperationLocationsTypes, BreedingDetailsTypes, AnimalIdentificationTypes, TermsAndConditionsTypes, RenewalTypes, RouteProtectionTypes } from "./types";
import { Location } from "./types";
import { ProfileTypes } from "./types";

export const ProfileGetters: GetterTree<ProfileTypes, RootState> = {
  // Profile
  firstName(state: ProfileTypes): string {
    return state!.firstName || "";
  },
  middleName(state: ProfileTypes): string {
    return state!.middleName || "";
  },
  lastName(state: ProfileTypes): string {
    return state!.lastName || "";
  },
  commType(state: ProfileTypes): string {
    return state!.commType || "";
  },
  phone(state: ProfileTypes): string {
    return state!.phone || "";
  },
  email(state: ProfileTypes): string {
    return state!.email || "";
  },
  streetNumber(state: ProfileTypes): number {
    return state!.streetNumber || 0;
  },
  aptNumber(state: ProfileTypes): string {
    return state!.aptNumber || "";
  },
  streetName(state: ProfileTypes): string {
    return state!.streetName || "";
  },
  city(state: ProfileTypes): string {
    return state!.city || "";
  },
  postalCode(state: ProfileTypes): string {
    return state!.postalCode || "";
  },
  poBox(state: ProfileTypes): string {
    return state!.poBox || "";
  },
  homeRegion(state: ProfileTypes): string {
    return state!.homeRegion || "";
  },
  sameAsOperation(state: ProfileTypes): string {
    return state!.sameAsOperation || "";
  }
};

export const OperationDetailsGetters: GetterTree<OperationDetailsTypes, RootState> = {
  // Operation Details
  operationName(state: OperationDetailsTypes): string {
    return state!.operationName || "";
  },
  operationType(state: OperationDetailsTypes): string {
    return state!.operationType || "";
  },
  opWebsite(state: OperationDetailsTypes): string {
    return state!.opWebsite || "";
  },
  assocName(state: OperationDetailsTypes): string {
    return state!.assocName || "";
  },
  accidentalBreeding(state: OperationDetailsTypes): string {
    return state!.accidentalBreeding || "";
  },
  numWorkers(state: OperationDetailsTypes): number {
    return state!.numWorkers || 0;
  },
  animalType(state: OperationDetailsTypes): string {
    return state!.animalType || "";
  },
  numDogBreeds(state: OperationDetailsTypes): number {
    return state!.numDogBreeds || 0;
  },
  numCatBreeds(state: OperationDetailsTypes): number {
    return state!.numCatBreeds || 0;
  },
  hasVet(state: OperationDetailsTypes): string {
    return state!.hasVet || "";
  },
};

export const OperationLocationsGetters: GetterTree<OperationLocationsTypes, RootState> = {
  // Operation Locations
  locations(state: OperationLocationsTypes): Location[] {
    return state!.locations || [];
  },
};

export const BreedingDetailsGetters: GetterTree<BreedingDetailsTypes, RootState> = {
  // Breeding Details
  femaleIntactDogNum(state: BreedingDetailsTypes): number {
    return state!.femaleIntactDogNum || 0;
  },
  femaleIntactCatNum(state: BreedingDetailsTypes): number {
    return state!.femaleIntactCatNum || 0;
  },
  littersWhelped(state: BreedingDetailsTypes): number {
    return state!.littersWhelped || 0;
  },
  littersQueened(state: BreedingDetailsTypes): number {
    return state!.littersQueened || 0;
  },
  dogsTransferred(state: BreedingDetailsTypes): number {
    return state!.dogsTransferred || 0;
  },
  dogsSold(state: BreedingDetailsTypes): number {
    return state!.dogsSold || 0;
  },
  dogsTraded(state: BreedingDetailsTypes): number {
    return state!.dogsTraded || 0;
  },
  dogsLeased(state: BreedingDetailsTypes): number {
    return state!.dogsLeased || 0;
  },
  catsTransferred(state: BreedingDetailsTypes): number {
    return state!.catsTransferred || 0;
  },
  catsSold(state: BreedingDetailsTypes): number {
    return state!.catsSold || 0;
  },
  catsTraded(state: BreedingDetailsTypes): number {
    return state!.catsTraded || 0;
  },
  catsLeased(state: BreedingDetailsTypes): number {
    return state!.catsLeased || 0;
  },
  numCats(state: BreedingDetailsTypes): number {
    return state!.numCats || 0;
  },
  numDogs(state: BreedingDetailsTypes): number {
    return state!.numDogs || 0;
  },
}

export const AnimalIdentificationGetters: GetterTree<AnimalIdentificationTypes, RootState> = {
  // Animal Identification
  hasPermId(state: AnimalIdentificationTypes): string {
    return state!.hasPermId || "";
  },
  permIdType(state: AnimalIdentificationTypes): string {
    return state!.permIdType || "NOT_APPLICABLE";
  },
  otherPermIdType(state: AnimalIdentificationTypes): string {
    return state!.otherPermIdType || "";
  },
}

export const TermsAndConditionsGetters: GetterTree<TermsAndConditionsTypes, RootState> = {
  // Terms and Conditions
  hasAgreed(state: TermsAndConditionsTypes): boolean {
    return state!.hasAgreed || false;
  },
}

export const RenewalGetters: GetterTree<RenewalTypes, RootState> = {
  // Renewal
  firstName(state: RenewalTypes): string {
    return state!.firstName || "";
  },
  middleName(state: RenewalTypes): string {
    return state!.middleName || "";
  },
  lastName(state: RenewalTypes): string {
    return state!.lastName || "";
  },
  registrationNumber(state: RenewalTypes): string {
    return state!.registrationNumber || "";
  },
  expiryDate(state: RenewalTypes): string {
    return state!.expiryDate || "";
  },
}

export const RouteProtectionGetters: GetterTree<RouteProtectionTypes, RootState> = {
  // Route Protection
  registerFormOk(state: RouteProtectionTypes): boolean {
    return state!.registerFormOk || false;
  },
  reviewFormOk(state: RouteProtectionTypes): boolean {
    return state!.reviewFormOk || false;
  },
  formType(state: RouteProtectionTypes): string {
    return state!.formType || "";
  }
};
