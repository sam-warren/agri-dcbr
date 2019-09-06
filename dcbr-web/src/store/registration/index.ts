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
  firstName: "John",
  middleName: "Alexander",
  lastName: "Macdonald",
  commType: "Email",
  phone: "1234567890",
  email: "jam@gov.bc.ca",
  streetNumber: 123,
  aptNumber: "2B",
  streetName: "Government St",
  city: "Langley",
  postalCode: "V4W1J1",
  homeAsOperation: "true",
  error: false

  // firstName: "",
  // middleName: "",
  // lastName: "",
  // commType: "",
  // phone: "",
  // email: "",
  // streetNumber: 0,
  // aptNumber: "",
  // streetName: "",
  // city: "",
  // postalCode: "",
  // homeAsOperation: "",
  // error: false
};

export const OperationDetailsState: OperationDetailsTypes = {
  operationName: "JaM Breeding Co.",
  opWebsite: "https://www.jambreeding.gov.bc.ca",
  operationType: "BREEDER",
  assocName: "Canada Breeding",
  assocMembership: 14819,
  assocWebsite: "https://www.canadabreeding.gov.bc.ca",
  accidentalBreeding: "false",
  numWorkers: 142,
  animalType: "DOG&CAT",
  numDogBreeds: 12,
  numCatBreeds: 16,
  hasVet: "true",
  error: false

  // operationName: "",
  // opWebsite: "",
  // operationType: "",
  // assocName: "",
  // assocMembership: 0,
  // assocWebsite: "",
  // accidentalBreeding: "",
  // numWorkers: 0,
  // animalType: "",
  // numDogBreeds: 0,
  // numCatBreeds: 0,
  // hasVet: "",
  // error: false
};

export const OperationLocationsState: OperationLocationsTypes = {
  hasAdditionalLocations: "false",
  locations: [],
  error: false

  // hasAdditionalLocations: "",
  // locations: [],
  // error: false
};

export const BreedingDetailsState: BreedingDetailsTypes = {
  femaleIntactDogNum: 52,
  femaleIntactCatNum: 43,
  littersWhelped: 6,
  littersQueened: 5,
  dogsSold: 16,
  dogsTransferred: 11,
  dogsTraded: 6,
  dogsLeased: 2,
  catsSold: 20,
  catsTransferred: 5,
  catsTraded: 2,
  catsLeased: 0,
  error: false

  // femaleIntactDogNum: 0,
  // femaleIntactCatNum: 0,
  // littersWhelped: 0,
  // littersQueened: 0,
  // dogsSold: 0,
  // dogsTransferred: 0,
  // dogsTraded: 0,
  // dogsLeased: 0,
  // catsSold: 0,
  // catsTransferred: 0,
  // catsTraded: 0,
  // catsLeased: 0,
  // error: false
};

export const AnimalIdentificationState: AnimalIdentificationTypes = {
  hasPermId: "true",
  permIdType: "OTHER",
  otherPermIdType: "Paper",
  error: false

  // hasPermId: "",
  // permIdType: "",
  // otherPermIdType: "",
  // error: false
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
