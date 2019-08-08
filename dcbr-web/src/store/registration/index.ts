import { Module } from "vuex";

import { RootState } from "../types";
import { actions } from "./actions";
import { getters } from "./getters";
import { mutations } from "./mutations";
import { RegistrationState } from "./types";

export const state: RegistrationState = {
  profile: {
    firstName: "John",
    middleName: "Ray",
    lastName: "Johnson",
    commType: "Email",
    phone: "2501234567",
    email: "johnrj@gmail.com",
    streetNumber: 123,
    aptNumber: 456,
    streetName: "Imaginary",
    city: "CodeTown",
    postalCode: "A1B2C3",
    homeAsOperation: true,
  },

  operationDetails: {
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
    hasVet: true
  },

  breedingDetails: {
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
    catsLeased: 6
  },

  animalIdentification: {
    hasPermId: true,
    permIdType: "OTHER",
    otherPermIdType: "Paper & pen"
  },

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