import { Module } from "vuex";

import { RootState } from "../types";
import { actions } from "./actions";
import { getters } from "./getters";
import { mutations } from "./mutations";
import { RegistrationState, OperationLocationsTypes } from "./types";
import { ProfileTypes } from "./types";
import { OperationDetailsTypes } from "./types";
import { BreedingDetailsTypes } from "./types";
import { AnimalIdentificationTypes } from "./types";

export const ProfileState: ProfileTypes = {
  firstName: "",
  middleName: "",
  lastName: "",
  commType: "",
  phone: "",
  email: "",
  streetNumber: 0,
  aptNumber: "",
  streetName: "",
  city: "",
  postalCode: "",
  homeAsOperation: false,
  error: false
};

export const OperationDetailsState: OperationDetailsTypes = {
  operationName: "",
  opWebsite: "",
  operationType: "",
  assocName: "",
  assocMembership: 0,
  assocWebsite: "",
  accidentalBreeding: false,
  numWorkers: 0,
  animalType: "0",
  numDogBreeds: 0,
  numCatBreeds: 0,
  hasVet: false,
  error: false
};

export const OperationLocationsState: OperationLocationsTypes = {
  hasAdditionalLocations: false,
  locations: []
};

export const BreedingDetailsState: BreedingDetailsTypes = {
  femaleIntactDogNum: 0,
  femaleIntactCatNum: 0,
  littersWhelped: 0,
  littersQueened: 0,
  dogsSold: 0,
  dogsTransferred: 0,
  dogsTraded: 0,
  dogsLeased: 0,
  catsSold: 0,
  catsTransferred: 0,
  catsTraded: 0,
  catsLeased: 0,
  error: false
};

export const AnimalIdentificationState: AnimalIdentificationTypes = {
  hasPermId: false,
  permIdType: "",
  otherPermIdType: "",
  error: false
};

export const state: RegistrationState = {
  profile: ProfileState,
  operationDetails: OperationDetailsState,
  operationLocations: OperationLocationsState,
  breedingDetails: BreedingDetailsState,
  animalIdentification: AnimalIdentificationState,
  error: false
};

const namespaced: boolean = true;

export const profile: Module<RegistrationState, RootState> = {
  namespaced,
  state,
  getters,
  actions,
  mutations
};

export const operationDetails: Module<RegistrationState, RootState> = {
  namespaced,
  state,
  getters,
  actions,
  mutations
};

export const operationLocations: Module<RegistrationState, RootState> = {
  namespaced,
  state,
  getters,
  actions,
  mutations
};

export const breedingDetails: Module<RegistrationState, RootState> = {
  namespaced,
  state,
  getters,
  actions,
  mutations
};

export const animalIdentification: Module<RegistrationState, RootState> = {
  namespaced,
  state,
  getters,
  actions,
  mutations
};
