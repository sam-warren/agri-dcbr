import { Module } from "vuex";

import { RootState } from "../types";
import { actions } from "./actions";
import { getters } from "./getters";
import { mutations } from "./mutations";
import { RegistrationState } from "./types";
import { ProfileTypes } from "./types";
import { OperationDetailsTypes } from "./types"
import { BreedingDetailsTypes } from "./types"
import { AnimalIdentificationTypes } from "./types"

export const ProfileState: ProfileTypes = {
  firstName: "John",
  middleName: "Ray",
  lastName: "Johnson",
  commType: "Email",
  phone: "2501234567",
  email: "johnrj@gmail.com",
  streetNumber: 123,
  aptNumber: "456",
  streetName: "Imaginary",
  city: "CodeTown",
  postalCode: "A1B2C3",
  homeAsOperation: true,
  error: false
}

export const OperationDetailsState: OperationDetailsTypes = {
  operationName: "Quartech Breeders Ltd.",
  opWebsite: "www.google.com",
  operationType: "BREEDER&SELLER",
  assocName: "Quartech",
  assocMembership: 142,
  assocWebsite: "www.quartech.com",
  accidentalBreeding: true,
  numWorkers: 14,
  animalType: "DOG&CAT",
  numDogBreeds: 10,
  numCatBreeds: 4,
  hasVet: true,
  error: false
}

export const BreedingDetailsState: BreedingDetailsTypes = {
  femaleIntactDogNum: 23,
  femaleIntactCatNum: 15,
  littersWhelped: 4,
  littersQueened: 3,
  dogsSold: 3,
  dogsTransferred: 4,
  dogsTraded: 2,
  dogsLeased: 0,
  catsSold: 3,
  catsTransferred: 2,
  catsTraded: 0,
  catsLeased: 6,
  error: false
}

export const AnimalIdentificationState: AnimalIdentificationTypes = {
  hasPermId: true,
  permIdType: "OTHER",
  otherPermIdType: "Files",
  error: false
}

export const state: RegistrationState = {
  profile: ProfileState,
  operationDetails: OperationDetailsState,
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
  mutations,
};

export const operationDetails: Module<RegistrationState, RootState> = {
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