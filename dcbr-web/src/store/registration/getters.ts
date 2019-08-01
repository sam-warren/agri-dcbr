import { GetterTree } from "vuex";

import { RootState } from "../types";
import { RegistrationState } from "./types";

export const getters: GetterTree<RegistrationState, RootState> = {
  // Profile
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
  },

  // Operation Details
  operationName(state: RegistrationState): string {
    const { operationDetails } = state;
    return operationDetails!.operationName || "";
  },
  operationType(state: RegistrationState): string {
    const { operationDetails } = state;
    return operationDetails!.operationType || "";
  },
  opWebsite(state: RegistrationState): string {
    const { operationDetails } = state;
    return operationDetails!.opWebsite || "";
  },
  assocName(state: RegistrationState): string {
    const { operationDetails } = state;
    return operationDetails!.assocName || "";
  },
  assocMembership(state: RegistrationState): number {
    const { operationDetails } = state;
    return operationDetails!.assocMembership || 0;
  },
  assocWebsite(state: RegistrationState): string {
    const { operationDetails } = state;
    return operationDetails!.assocWebsite || "";
  },
  accidentalBreeding(state: RegistrationState): boolean {
    const { operationDetails } = state;
    return operationDetails!.accidentalBreeding || false;
  },
  numWorkers(state: RegistrationState): number {
    const { operationDetails } = state;
    return operationDetails!.numWorkers || 0;
  },
  animalType(state: RegistrationState): string {
    const { operationDetails } = state;
    return operationDetails!.animalType || "";
  },
  numDogBreeds(state: RegistrationState): number {
    const { operationDetails } = state;
    return operationDetails!.numDogBreeds || 0;
  },
  numCatBreeds(state: RegistrationState): number {
    const { operationDetails } = state;
    return operationDetails!.numCatBreeds || 0;
  },
  hasVet(state: RegistrationState): boolean {
    const { operationDetails } = state;
    return operationDetails!.hasVet || false;
  },

  // Breeding Details
  femaleIntactDogNum(state: RegistrationState): number {
    const { breedingDetails } = state;
    return breedingDetails!.femaleIntactDogNum || 0;
  },
  femaleIntactCatNum(state: RegistrationState): number {
    const { breedingDetails } = state;
    return breedingDetails!.femaleIntactCatNum || 0;
  },
  littersWhelped(state: RegistrationState): number {
    const { breedingDetails } = state;
    return breedingDetails!.littersWhelped || 0;
  },
  littersQueened(state: RegistrationState): number {
    const { breedingDetails } = state;
    return breedingDetails!.littersQueened || 0;
  },
  dogsTransferred(state: RegistrationState): number {
    const { breedingDetails } = state;
    return breedingDetails!.dogsTransferred || 0;
  },
  dogsSold(state: RegistrationState): number {
    const { breedingDetails } = state;
    return breedingDetails!.dogsSold || 0;
  },
  dogsTraded(state: RegistrationState): number {
    const { breedingDetails } = state;
    return breedingDetails!.dogsTraded || 0;
  },
  dogsLeased(state: RegistrationState): number {
    const { breedingDetails } = state;
    return breedingDetails!.dogsLeased || 0;
  },
  catsTransferred(state: RegistrationState): number {
    const { breedingDetails } = state;
    return breedingDetails!.catsTransferred || 0;
  },
  catsSold(state: RegistrationState): number {
    const { breedingDetails } = state;
    return breedingDetails!.catsSold || 0;
  },
  catsTraded(state: RegistrationState): number {
    const { breedingDetails } = state;
    return breedingDetails!.catsTraded || 0;
  },
  catsLeased(state: RegistrationState): number {
    const { breedingDetails } = state;
    return breedingDetails!.catsLeased || 0;
  },
 
  // Animal Identification
  hasPermId(state: RegistrationState): boolean {
    const { animalIdentification } = state;
    return animalIdentification!.hasPermId || false;
  },
  permIdType(state: RegistrationState): string {
    const { animalIdentification } = state;
    return animalIdentification!.permIdType || "";
  },
  otherPermIdType(state: RegistrationState): string {
    const { animalIdentification } = state;
    return animalIdentification!.otherPermIdType || "";
  },
};
