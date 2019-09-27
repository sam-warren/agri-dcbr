import { MutationTree } from "vuex";
import { ProfileTypes, Location, OperationDetailsTypes, OperationLocationsTypes, BreedingDetailsTypes, AnimalIdentificationTypes, TermsAndConditionsTypes, RouteProtectionTypes, RenewalTypes } from "../registration/types";
// import { ProfileState, OperationDetailsState, OperationLocationsState, BreedingDetailsState, AnimalIdentificationState, TermsAndConditionsState, RouteProtectionState, RenewalState } from "./state"

export const ProfileMutations: MutationTree<ProfileTypes> = {
  // Profile
  firstName(state: ProfileTypes, payload: string) {
    state.error = false;
    state.firstName = payload;
  },
  middleName(state: ProfileTypes, payload: string) {
    state.error = false;
    state.middleName = payload;
  },
  lastName(state: ProfileTypes, payload: string) {
    state.error = false;
    state.lastName = payload;
  },
  commType(state: ProfileTypes, payload: string) {
    state.error = false;
    state.commType = payload;
  },
  phone(state: ProfileTypes, payload: string) {
    state.error = false;
    state.phone = payload;
  },
  email(state: ProfileTypes, payload: string) {
    state.error = false;
    state.email = payload;
  },
  streetNumber(state: ProfileTypes, payload: number) {
    state.error = false;
    state.streetNumber = payload;
  },
  aptNumber(state: ProfileTypes, payload: string) {
    state.error = false;
    state.aptNumber = payload;
  },
  streetName(state: ProfileTypes, payload: string) {
    state.error = false;
    state.streetName = payload;
  },
  city(state: ProfileTypes, payload: string) {
    state.error = false;
    state.city = payload;
  },
  postalCode(state: ProfileTypes, payload: string) {
    state.error = false;
    state.postalCode = payload;
  },
  poBox(state: ProfileTypes, payload: string) {
    state.error = false;
    state.poBox = payload;
  },
  homeRegion(state: ProfileTypes, payload: string) {
    state.error = false;
    state.homeRegion = payload;
  },
  sameAsOperation(state: ProfileTypes, payload: string) {
    state.error = false;
    state.sameAsOperation = payload;
  },
  resetForm(state: ProfileTypes) {
    state.firstName = "";
    state.middleName = "";
    state.lastName = "";
    state.commType = "";
    state.phone = "";
    state.email = "";
    state.streetNumber = 0;
    state.aptNumber = "";
    state.streetName = "";
    state.city = "";
    state.postalCode = "";
    state.poBox = "";
    state.homeRegion = "";
  }
}

export const OperationDetailsMutations: MutationTree<OperationDetailsTypes> = {
  // Operation Details
  operationName(state: OperationDetailsTypes, payload: string) {
    state.error = false;
    state.operationName = payload;
  },
  operationType(state: OperationDetailsTypes, payload: string) {
    state.error = false;
    state.operationType = payload;
  },
  opWebsite(state: OperationDetailsTypes, payload: string) {
    state.error = false;
    state.opWebsite = payload;
  },
  assocName(state: OperationDetailsTypes, payload: string) {
    state.error = false;
    state.assocName = payload;
  },
  accidentalBreeding(state: OperationDetailsTypes, payload: string) {
    state.error = false;
    state.accidentalBreeding = payload;
  },
  numWorkers(state: OperationDetailsTypes, payload: number) {
    state.error = false;
    state.numWorkers = payload;
  },
  animalType(state: OperationDetailsTypes, payload: string) {
    state.error = false;
    state.animalType = payload;
  },
  numDogBreeds(state: OperationDetailsTypes, payload: number) {
    state.error = false;
    state.numDogBreeds = payload;
  },
  numCatBreeds(state: OperationDetailsTypes, payload: number) {
    state.error = false;
    state.numCatBreeds = payload;
  },
  hasVet(state: OperationDetailsTypes, payload: string) {
    state.error = false;
    state.hasVet = payload;
  },
  resetForm(state: OperationDetailsTypes) {
    state.operationName = "";
    state.operationType = "";
    state.opWebsite = "";
    state.assocName = "";
    state.accidentalBreeding = "";
    state.numWorkers = 0;
    state.animalType = "";
    state.numDogBreeds = 0;
    state.numCatBreeds = 0;
    state.hasVet = "";
  }
}

export const OperationLocationsMutations: MutationTree<OperationLocationsTypes> = {
  // Operation Locations
  locations(state: OperationLocationsTypes, payload: { operation: string }) {
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
      state.locations!.push(newLocation);
    } else if (payload.operation === "remove") {
      state.locations!.pop();
    } else {
      console.error("Could not perform requested mutation: add/remove location.");
    }
    // state.locations = payload;
  },
  updateLocationProperty(state: OperationLocationsTypes, payload: {index: number, property: string, value: any}) {
    state.error = false;
    if (state && state && state.locations) {
      let location: any = state.locations[payload.index];
      location[payload.property] = payload.value;
      state.locations[payload.index] = location;
    }
  },
  resetForm(state: OperationLocationsTypes) {
    state.locations = [];
  }
}

export const BreedingDetailsMutations: MutationTree<BreedingDetailsTypes> = {
  // Breeding Details
  femaleIntactDogNum(state: BreedingDetailsTypes, payload: number) {
    state.error = false;
    state.femaleIntactDogNum = payload;
  },
  femaleIntactCatNum(state: BreedingDetailsTypes, payload: number) {
    state.error = false;
    state.femaleIntactCatNum = payload;
  },
  littersWhelped(state: BreedingDetailsTypes, payload: number) {
    state.error = false;
    state.littersWhelped = payload;
  },
  littersQueened(state: BreedingDetailsTypes, payload: number) {
    state.error = false;
    state.littersQueened = payload;
  },
  dogsTransferred(state: BreedingDetailsTypes, payload: number) {
    state.error = false;
    state.dogsTransferred = payload;
  },
  dogsSold(state: BreedingDetailsTypes, payload: number) {
    state.error = false;
    state.dogsSold = payload;
  },
  dogsTraded(state: BreedingDetailsTypes, payload: number) {
    state.error = false;
    state.dogsTraded = payload;
  },
  dogsLeased(state: BreedingDetailsTypes, payload: number) {
    state.error = false;
    state.dogsLeased = payload;
  },
  catsTransferred(state: BreedingDetailsTypes, payload: number) {
    state.error = false;
    state.catsTransferred = payload;
  },
  catsSold(state: BreedingDetailsTypes, payload: number) {
    state.error = false;
    state.catsSold = payload;
  },
  catsTraded(state: BreedingDetailsTypes, payload: number) {
    state.error = false;
    state.catsTraded = payload;
  },
  catsLeased(state: BreedingDetailsTypes, payload: number) {
    state.error = false;
    state.catsLeased = payload;
  },
  numCats(state: BreedingDetailsTypes, payload: number) {
    state.error = false;
    state.numCats = payload;
  },
  numDogs(state: BreedingDetailsTypes, payload: number) {
    state.error = false;
    state.numDogs = payload;
  },
  resetForm(state: BreedingDetailsTypes) {
    state.error = false;
    state.femaleIntactDogNum = 0;
    state.femaleIntactCatNum = 0;
    state.littersQueened = 0;
    state.littersWhelped = 0;
    state.dogsTransferred = 0;
    state.dogsSold = 0;
    state.dogsTraded = 0;
    state.dogsLeased = 0;
    state.catsTransferred = 0;
    state.catsSold = 0;
    state.catsTraded = 0;
    state.catsLeased = 0;
    state.numCats = 0;
    state.numDogs = 0;
  }
}

export const AnimalIdentificationMutations: MutationTree<AnimalIdentificationTypes> = {
  // Animal Identification
  hasPermId(state: AnimalIdentificationTypes, payload: string) {
    state.error = false;
    state.hasPermId = payload;
  },
  permIdType(state: AnimalIdentificationTypes, payload: string) {
    state.error = false;
    state.permIdType = payload;
  },
  otherPermIdType(state: AnimalIdentificationTypes, payload: string) {
    state.error = false;
    state.otherPermIdType = payload;
  },
  resetForm(state: AnimalIdentificationTypes) {
    state.error = false;
    state.hasPermId = "";
    state.permIdType = "NOT_APPLICABLE";
    state.otherPermIdType = "";
  }
}

export const TermsAndConditionsMutations: MutationTree<TermsAndConditionsTypes> = {
  // Terms and Conditions
  hasAgreed(state: TermsAndConditionsTypes, payload: boolean) {
    state.error = false;
    state.hasAgreed = payload;
  },
  resetForm(state: TermsAndConditionsTypes) {
    state.error = false;
    state.hasAgreed = false;
  }
}

export const RouteProtectionMutations: MutationTree<RouteProtectionTypes> = {
  // Route Protection
  registerFormOk(state: RouteProtectionTypes, payload: boolean) {
    state.error = false;
    state.registerFormOk = payload;
  },
  reviewFormOk(state: RouteProtectionTypes, payload: boolean) {
    state.error = false;
    state.reviewFormOk = payload;
  },
  formType(state: RouteProtectionTypes, payload: string) {
    state.error = false;
    state.formType = payload;
  },
  resetForm(state: RouteProtectionTypes) {
    state.error = false;
    state.registerFormOk = false;
    state.reviewFormOk = false;
    state.formType = "";
  }
}

export const RenewalMutations: MutationTree<RenewalTypes> = {
  // Renewal
  firstName(state: RenewalTypes, payload: string) {
    state.error = false;
    state.firstName = payload;
  },
  middleName(state: RenewalTypes, payload: string) {
    state.error = false;
    state.middleName = payload;
  },
  lastName(state: RenewalTypes, payload: string) {
    state.error = false;
    state.lastName = payload;
  },
  registrationNumber(state: RenewalTypes, payload: string) {
    state.error = false;
    state.registrationNumber = payload;
  },
  expiryDate(state: RenewalTypes, payload: string) {
    state.error = false;
    state.expiryDate = payload;
  },
  resetForm(state: RenewalTypes) {
    state.error = false;
    state.firstName = "";
    state.middleName = "";
    state.lastName = "";
    state.registrationNumber = "";
    state.expiryDate = "";
  }
}