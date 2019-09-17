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
  homeRegion(state: RegistrationState, payload: string) {
    state.error = false;
    state.profile!.homeRegion = payload;
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
        postalCode: "",
        region: ""
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
  numCats(state: RegistrationState, payload: number) {
    state.error = false;
    state.breedingDetails!.numCats = payload;
  },
  numDogs(state: RegistrationState, payload: number) {
    state.error = false;
    state.breedingDetails!.numDogs = payload;
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

  // Terms and Conditions
  hasAgreed(state: RegistrationState, payload: boolean) {
    state.error = false;
    state.termsAndConditions!.hasAgreed = payload;
  },

  // Route Protection
  registerFormOk(state: RegistrationState, payload: boolean) {
    state.error = false;
    state.routeProtection!.registerFormOk = payload;
  },
  reviewFormOk(state: RegistrationState, payload: boolean) {
    state.error = false;
    state.routeProtection!.reviewFormOk = payload;
  },

  resetForm(state: RegistrationState) {
    state.profile!.firstName = "";
    state.profile!.middleName = "";
    state.profile!.lastName = "" ;
    state.profile!.commType = "";
    state.profile!.phone = "";
    state.profile!.email = "";
    state.profile!.streetNumber = 0;
    state.profile!.aptNumber = "";
    state.profile!.streetName = "";
    state.profile!.city = "";
    state.profile!.postalCode = "";
    state.profile!.homeRegion = "";
    
    state.operationDetails!.operationName = "";
    state.operationDetails!.opWebsite = "";
    state.operationDetails!.operationType = "";
    state.operationDetails!.assocName = "";
    state.operationDetails!.accidentalBreeding = "";
    state.operationDetails!.numWorkers = 0;
    state.operationDetails!.animalType = "";
    state.operationDetails!.numDogBreeds = 0;
    state.operationDetails!.numCatBreeds = 0;
    state.operationDetails!.hasVet = "";

    state.operationLocations!.hasAdditionalLocations = "";
    state.operationLocations!.locations = [];

    state.breedingDetails!.femaleIntactDogNum = 0;
    state.breedingDetails!.femaleIntactCatNum = 0;
    state.breedingDetails!.littersWhelped = 0;
    state.breedingDetails!.littersQueened = 0;
    state.breedingDetails!.dogsSold = 0;
    state.breedingDetails!.dogsTransferred = 0;
    state.breedingDetails!.dogsTraded = 0;
    state.breedingDetails!.dogsLeased = 0;
    state.breedingDetails!.catsSold = 0;
    state.breedingDetails!.catsTransferred = 0;
    state.breedingDetails!.catsTraded = 0;
    state.breedingDetails!.catsLeased = 0;
    state.breedingDetails!.numCats = 0;
    state.breedingDetails!.numDogs = 0;

    state.animalIdentification!.hasPermId = "";
    state.animalIdentification!.permIdType = "NOT_APPLICABLE";
    state.animalIdentification!.otherPermIdType = "";

    state.termsAndConditions!.hasAgreed = false;

    state.routeProtection!.registerFormOk = false;
    state.routeProtection!.reviewFormOk = false;
  }
};
