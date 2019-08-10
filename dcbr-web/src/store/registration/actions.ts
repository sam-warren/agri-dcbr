import { ActionTree } from "vuex";

import { RootState } from "../types";
import { RegistrationState } from "./types";

export const actions: ActionTree<RegistrationState, RootState> = {
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
  },

  // Operation Details
  operationName(context: any, payload: any) {
    context.commit("operationName", payload);
  },
  operationType(context: any, payload: any) {
    context.commit("operationType", payload);
  },
  opWebsite(context: any, payload: any) {
    context.commit("opWebsite", payload);
  },
  assocName(context: any, payload: any) {
    context.commit("assocName", payload);
  },
  assocMembership(context: any, payload: any) {
    context.commit("assocMembership", payload);
  },
  assocWebsite(context: any, payload: any) {
    context.commit("assocWebsite", payload);
  },
  accidentalBreeding(context: any, payload: any) {
    context.commit("accidentalBreeding", payload);
  },
  numWorkers(context: any, payload: any) {
    context.commit("numWorkers", payload);
  },
  animalType(context: any, payload: any) {
    context.commit("animalType", payload);
  },
  numDogBreeds(context: any, payload: any) {
   context.commit("numDogBreeds", payload);
  },
  numCatBreeds(context: any, payload: any) {
   context.commit("numCatBreeds", payload);
  },
  hasVet(context: any, payload: any) {
    context.commit("hasVet", payload);
  },

  // Breeding Details
  femaleIntactDogNum(context: any, payload: any) {
    context.commit("femaleIntactDogNum", payload);
  },
  femaleIntactCatNum(context: any, payload: any) {
    context.commit("femaleIntactCatNum", payload);
  },
  littersWhelped(context: any, payload: any) {
    context.commit("littersWhelped", payload);
  },
  littersQueened(context: any, payload: any) {
    context.commit("littersQueened", payload);
  },
  dogsTransferred(context: any, payload: any) {
    context.commit("dogsTransferred", payload);
  },
  dogsSold(context: any, payload: any) {
    context.commit("dogsSold", payload);
  },
  dogsTraded(context: any, payload: any) {
    context.commit("dogsTraded", payload);
  },
  dogsLeased(context: any, payload: any) {
    context.commit("dogsLeased", payload);
  },
  catsTransferred(context: any, payload: any) {
    context.commit("catsTransferred", payload);
  },
  catsSold(context: any, payload: any) {
    context.commit("catsSold", payload);
  },
  catsTraded(context: any, payload: any) {
    context.commit("catsTraded", payload);
  },
  catsLeased(context: any, payload: any) {
    context.commit("catsLeased", payload);
  },

  // Animal Identification
  hasPermId(context: any, payload: any) {
    context.commit("hasPermId", payload);
  },
  permIdType(context: any, payload: any) {
    context.commit("permIdType", payload);
  },
  otherPermIdType(context: any, payload: any) {
    context.commit("otherPermIdType", payload);
  },
};
