import { MutationTree } from "vuex";
import { RegistrationState, Location } from "../registration/types";

export const mutations: MutationTree<RegistrationState> = {
  // Profile
  firstName(state: RegistrationState, payload: string) {
    state.error = false;
    state.profile!.firstName = payload;
  },
  middleName(state: RegistrationState, payload: string) {
    state.error = false;
    state.profile!.middleName = payload;
  },
  lastName(state: RegistrationState, payload: string) {
    state.error = false;
    state.profile!.lastName = payload;
  },
  commType(state: RegistrationState, payload: string) {
    state.error = false;
    state.profile!.commType = payload;
  },
  phone(state: RegistrationState, payload: string) {
    state.error = false;
    state.profile!.phone = payload;
  },
  email(state: RegistrationState, payload: string) {
    state.error = false;
    state.profile!.email = payload;
  },
  streetNumber(state: RegistrationState, payload: number) {
    state.error = false;
    state.profile!.streetNumber = payload;
  },
  aptNumber(state: RegistrationState, payload: string) {
    state.error = false;
    state.profile!.aptNumber = payload;
  },
  streetName(state: RegistrationState, payload: string) {
    state.error = false;
    state.profile!.streetName = payload;
  },
  city(state: RegistrationState, payload: string) {
    state.error = false;
    state.profile!.city = payload;
  },
  postalCode(state: RegistrationState, payload: string) {
    state.error = false;
    state.profile!.postalCode = payload;
  },

  // Operation Details
  operationName(state: RegistrationState, payload: string) {
    state.error = false;
    state.operationDetails!.operationName = payload;
  },
  operationType(state: RegistrationState, payload: string) {
    state.error = false;
    state.operationDetails!.operationType = payload;
  },
  opWebsite(state: RegistrationState, payload: string) {
    state.error = false;
    state.operationDetails!.opWebsite = payload;
  },
  assocName(state: RegistrationState, payload: string) {
    state.error = false;
    state.operationDetails!.assocName = payload;
  },
  assocMembership(state: RegistrationState, payload: number) {
    state.error = false;
    state.operationDetails!.assocMembership = payload;
  },
  assocWebsite(state: RegistrationState, payload: string) {
    state.error = false;
    state.operationDetails!.assocWebsite = payload;
  },
  accidentalBreeding(state: RegistrationState, payload: string) {
    state.error = false;
    state.operationDetails!.accidentalBreeding = payload;
  },
  numWorkers(state: RegistrationState, payload: number) {
    state.error = false;
    state.operationDetails!.numWorkers = payload;
  },
  animalType(state: RegistrationState, payload: string) {
    state.error = false;
    state.operationDetails!.animalType = payload;
  },
  numDogBreeds(state: RegistrationState, payload: number) {
    state.error = false;
    state.operationDetails!.numDogBreeds = payload;
  },
  numCatBreeds(state: RegistrationState, payload: number) {
    state.error = false;
    state.operationDetails!.numCatBreeds = payload;
  },
  hasVet(state: RegistrationState, payload: string) {
    state.error = false;
    state.operationDetails!.hasVet = payload;
  },

  // Operation Locations
  hasAdditionalLocations(state: RegistrationState, payload: string) {
    state.error = false;
    state.operationLocations!.hasAdditionalLocations = payload;
    state.operationLocations!.locations = [];
  },
  locations(state: RegistrationState, payload: { operation: string }) {
    state.error = false;
    if (payload.operation === "add") {
      let newLocation: Location = {
        streetNumber: 0, 
        aptNumber: "", 
        streetName: "", 
        city: "", 
        postalCode: ""
      }
      state.operationLocations!.locations.push(newLocation);
    } else if (payload.operation === "remove") {
      state.operationLocations!.locations.pop();
    } else {
      console.error("Could not perform requested mutation: add/remove location.");
    }
    // state.operationLocations!.locations = payload;
  },
  updateLocationProperty(state: RegistrationState, payload: {index: number, property: string, value: any}) {
    state.error = false;
    if (state && state.operationLocations && state.operationLocations.locations) {
      let location: any = state.operationLocations.locations[payload.index];
      location[payload.property] = payload.value;
      state.operationLocations.locations[payload.index] = location;
    }
  },

  // Breeding Details
  femaleIntactDogNum(state: RegistrationState, payload: number) {
    state.error = false;
    state.breedingDetails!.femaleIntactDogNum = payload;
  },
  femaleIntactCatNum(state: RegistrationState, payload: number) {
    state.error = false;
    state.breedingDetails!.femaleIntactCatNum = payload;
  },
  littersWhelped(state: RegistrationState, payload: number) {
    state.error = false;
    state.breedingDetails!.littersWhelped = payload;
  },
  littersQueened(state: RegistrationState, payload: number) {
    state.error = false;
    state.breedingDetails!.littersQueened = payload;
  },
  dogsTransferred(state: RegistrationState, payload: number) {
    state.error = false;
    state.breedingDetails!.dogsTransferred = payload;
  },
  dogsSold(state: RegistrationState, payload: number) {
    state.error = false;
    state.breedingDetails!.dogsSold = payload;
  },
  dogsTraded(state: RegistrationState, payload: number) {
    state.error = false;
    state.breedingDetails!.dogsTraded = payload;
  },
  dogsLeased(state: RegistrationState, payload: number) {
    state.error = false;
    state.breedingDetails!.dogsLeased = payload;
  },
  catsTransferred(state: RegistrationState, payload: number) {
    state.error = false;
    state.breedingDetails!.catsTransferred = payload;
  },
  catsSold(state: RegistrationState, payload: number) {
    state.error = false;
    state.breedingDetails!.catsSold = payload;
  },
  catsTraded(state: RegistrationState, payload: number) {
    state.error = false;
    state.breedingDetails!.catsTraded = payload;
  },
  catsLeased(state: RegistrationState, payload: number) {
    state.error = false;
    state.breedingDetails!.catsLeased = payload;
  },

  // Animal Identification
  hasPermId(state: RegistrationState, payload: string) {
    state.error = false;
    state.animalIdentification!.hasPermId = payload;
  },
  permIdType(state: RegistrationState, payload: string) {
    state.error = false;
    state.animalIdentification!.permIdType = payload;
  },
  otherPermIdType(state: RegistrationState, payload: string) {
    state.error = false;
    state.animalIdentification!.otherPermIdType = payload;
  },
};
