import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export const store = new Vuex.Store({
         //    Filled out for testing purposes
         state: {
           //Profile
           firstName: "John",
           middleName: "David",
           lastName: "Smith",
           commType: "Mail",
           phone: "234-234-2311",
           email: "john@smith.com",
           streetNumber: "1",
           aptNumber: "2",
           streetName: "Douglas",
           city: "Duncan",
           postalCode: "V6R 5T6",

           //OperationDetails
           operationName: "John's puppies",
           opWebsite: "https://abcdogs.com",
           operationType: "BREEDER&SELLER",
           assocName: "ABC Assoc",
           assocMembership: "1234",
           assocWebsite: "https://www.dce-associations.com",
           accidentalBreeding: "false",
           numWorkers: 1,
           animalType: "DOG",

           //Breeding Details
           femaleIntactDogNum: 1,
           femaleIntactCatNum: 3,
           littersWhelped: 2,
           littersQueened: 4,
           dogsSold: 5,
           dogsTransferred: 6,
           dogsTraded: 7,
           dogsLeased: 8,
           catsSold: 9,
           catsTransferred: 10,
           catsTraded: 11,
           catsLeased: 12,

           //not wired up

           numDogBreeds: 1,
           numCatBreeds: 2,
           hasVet: "false",
           hasPermId: "true",
           permIdType: "MICROCHIP",
           otherPermIdType: "future ID"
         },
         //  ----------------------------------------

         mutations: {
           //mutations - profile
           firstName(state: { firstName: String }, payload: String) {
             state.firstName = payload;
           },
           middleName(state: { middleName: String }, payload: String) {
             state.middleName = payload;
           },
           lastName(state: { lastName: String }, payload: String) {
             state.lastName = payload;
           },
           commType(state: { commType: String }, payload: String) {
             state.commType = payload;
           },
           phone(state: { phone: String }, payload: String) {
             state.phone = payload;
           },
           email(state: { email: String }, payload: String) {
             state.email = payload;
           },
           streetNumber(
             state: { streetNumber: String },
             payload: String
           ) {
             state.streetNumber = payload;
           },
           aptNumber(state: { aptNumber: String }, payload: String) {
             state.aptNumber = payload;
           },
           streetName(state: { streetName: String }, payload: String) {
             state.streetName = payload;
           },
           city(state: { city: String }, payload: String) {
             state.city = payload;
           },
           postalCode(state: { postalCode: String }, payload: String) {
             state.postalCode = payload;
           },

           //Mutations - operation details

           operationName(
             state: { operationName: String },
             payload: String
           ) {
             state.operationName = payload;
           },
           operationType(
             state: { operationType: String },
             payload: String
           ) {
             state.operationType = payload;
           },
           opWebsite(state: { opWebsite: String }, payload: String) {
             state.opWebsite = payload;
           },
           assocName(state: { assocName: String }, payload: String) {
             state.assocName = payload;
           },
           assocMembership(
             state: { assocMembership: String },
             payload: String
           ) {
             state.assocMembership = payload;
           },
           assocWebsite(
             state: { assocWebsite: String },
             payload: String
           ) {
             state.assocWebsite = payload;
           },
           accidentalBreeding(
             state: { accidentalBreeding: String },
             payload: String
           ) {
             state.accidentalBreeding = payload;
           },
           numWorkers(state: { numWorkers: String }, payload: String) {
             state.numWorkers = payload;
           },
           animalType(state: { animalType: String }, payload: String) {
             state.animalType = payload;
           },

           //Mutations - breeding details
           femaleIntactDogNum(
             state: { femaleIntactDogNum: String },
             payload: String
           ) {
             state.femaleIntactDogNum = payload;
           },
           femaleIntactCatNum(
             state: { femaleIntactCatNum: String },
             payload: String
           ) {
             state.femaleIntactCatNum = payload;
           },
           littersWhelped(
             state: { littersWhelped: String },
             payload: String
           ) {
             state.littersWhelped = payload;
           },
           littersQueened(
             state: { littersQueened: String },
             payload: String
           ) {
             state.littersQueened = payload;
           },
           dogsTransferred(
             state: { dogsTransferred: String },
             payload: String
           ) {
             state.dogsTransferred = payload;
           },
           dogsSold(state: { dogsSold: String }, payload: String) {
             state.dogsSold = payload;
           },
           dogsTraded(state: { dogsTraded: String }, payload: String) {
             state.dogsTraded = payload;
           },
           dogsLeased(state: { dogsLeased: String }, payload: String) {
             state.dogsLeased = payload;
           },
           catsTransferred(
             state: { catsTransferred: String },
             payload: String
           ) {
             state.catsTransferred = payload;
           },
           catsSold(state: { catsSold: String }, payload: String) {
             state.catsSold = payload;
           },
           catsTraded(state: { catsTraded: String }, payload: String) {
             state.catsTraded = payload;
           },
           catsLeased(state: { catsLeased: String }, payload: String) {
             state.catsLeased = payload;
           }
         },

         actions: {
           //actions - profile
           firstName(context: any, payload: any) {
             context.commit("firstName", payload);
           },
           middleName(context: any, payload: any) {
             context.commit("middleName", payload);
           },
           lastName(context: any, payload: any) {
             context.commit("lastName", payload);
           },
           commType(context: any, payload: any) {
             context.commit("commType", payload);
           },
           phone(context: any, payload: any) {
             context.commit("phone", payload);
           },
           email(context: any, payload: any) {
             context.commit("email", payload);
           },

           streetNumber(context: any, payload: any) {
             context.commit("streetNumber", payload);
           },
           aptNumber(context: any, payload: any) {
             context.commit("aptNumber", payload);
           },
           streetName(context: any, payload: any) {
             context.commit("streetName", payload);
           },
           city(context: any, payload: any) {
             context.commit("city", payload);
           },
           postalCode(context: any, payload: any) {
             context.commit("postalCode", payload);
           },

           //action - operation details

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

           //action - breeding details
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
           }
         },

         getters: {
           //getters - profile
           firstName(state: { firstName: String }) {
             return state.firstName;
           },
           middleName(state: { middleName: String }) {
             return state.middleName;
           },
           lastName(state: { lastName: String }) {
             return state.lastName;
           },
           commType(state: { commType: String }) {
             return state.commType;
           },
           phone(state: { phone: String }) {
             return state.phone;
           },
           email(state: { email: String }) {
             return state.email;
           },
           streetNumber(state: { streetNumber: String }) {
             return state.streetNumber;
           },
           aptNumber(state: { aptNumber: String }) {
             return state.aptNumber;
           },
           streetName(state: { streetName: String }) {
             return state.streetName;
           },
           city(state: { city: String }) {
             return state.city;
           },
           postalCode(state: { postalCode: String }) {
             return state.postalCode;
           },

           //getters - operation details
           operationName(state: { operationName: String }) {
             return state.operationName;
           },
           operationType(state: { operationType: String }) {
             return state.operationType;
           },
           opWebsite(state: { opWebsite: String }) {
             return state.opWebsite;
           },
           assocName(state: { assocName: String }) {
             return state.assocName;
           },
           assocMembership(state: { assocMembership: String }) {
             return state.assocMembership;
           },
           assocWebsite(state: { assocWebsite: String }) {
             return state.assocWebsite;
           },
           accidentalBreeding(state: { accidentalBreeding: String }) {
             return state.accidentalBreeding;
           },
           numWorkers(state: { numWorkers: String }) {
             return state.numWorkers;
           },
           animalType(state: { animalType: String }) {
             return state.animalType;
           },

           //getters - breeding details
           femaleIntactDogNum(state: { femaleIntactDogNum: String }) {
             return state.femaleIntactDogNum;
           },
           femaleIntactCatNum(state: { femaleIntactCatNum: String }) {
             return state.femaleIntactCatNum;
           },
           littersWhelped(state: { littersWhelped: String }) {
             return state.littersWhelped;
           },
           littersQueened(state: { littersQueened: String }) {
             return state.littersQueened;
           },
           dogsTransferred(state: { dogsTransferred: String }) {
             return state.dogsTransferred;
           },
           dogsSold(state: { dogsSold: String }) {
             return state.dogsSold;
           },
           dogsTraded(state: { dogsTraded: String }) {
             return state.dogsTraded;
           },
           dogsLeased(state: { dogsLeased: String }) {
             return state.dogsLeased;
           },
           catsTransferred(state: { catsTransferred: String }) {
             return state.catsTransferred;
           },
           catsSold(state: { catsSold: String }) {
             return state.catsSold;
           },
           catsTraded(state: { catsTraded: String }) {
             return state.catsTraded;
           },
           catsLeased(state: { catsLeased: String }) {
             return state.catsLeased;
           }
         }
       });
