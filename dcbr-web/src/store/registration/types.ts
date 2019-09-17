export interface ProfileTypes {
  firstName: string;
  middleName: string;
  lastName: string;
  commType: string;
  phone: string;
  email: string;
  streetNumber: number;
  aptNumber: string;
  streetName: string;
  city: string;
  postalCode: string;
  homeRegion: string;
  error: boolean;
}

export interface OperationDetailsTypes {
  operationName: string;
  opWebsite: string;
  operationType: string;
  assocName: string;
  assocMembership: number;
  assocWebsite: string;
  accidentalBreeding: string;
  numWorkers: number;
  animalType: string;
  numDogBreeds: number;
  numCatBreeds: number;
  hasVet: string;
  error: boolean;
}

export interface OperationLocationsTypes {
  hasAdditionalLocations: string;
  locations: Location[];
  error: boolean;
}

export interface Location {
  streetNumber: number;
  aptNumber: string;
  streetName: string;
  city: string; 
  postalCode: string;
  region: string;
}

export interface BreedingDetailsTypes {
  femaleIntactDogNum: number;
  femaleIntactCatNum: number;
  littersWhelped: number;
  littersQueened: number;
  dogsSold: number;
  dogsTransferred: number;
  dogsTraded: number;
  dogsLeased: number;
  catsSold: number;
  catsTransferred: number;
  catsTraded: number;
  catsLeased: number;
  numCats: number;
  numDogs: number;
  error: boolean;
}

export interface AnimalIdentificationTypes {
  hasPermId: string;
  permIdType: string;
  otherPermIdType: string;
  error: boolean;
}

export interface TermsAndConditionsTypes {
  hasAgreed: boolean;
  error: boolean;
}

export interface RouteProtectionTypes {
  registerFormOk: boolean;
  reviewFormOk: boolean;
  error: boolean;
}

export interface RenewalTypes {
  renewalFirstName: string;
  renewalMiddleName: string;
  renewalLastName: string;
  registrationNumber: string;
}

export interface RegistrationState {
  profile?: ProfileTypes;
  operationDetails?: OperationDetailsTypes;
  operationLocations?: OperationLocationsTypes;
  breedingDetails?: BreedingDetailsTypes;
  animalIdentification?: AnimalIdentificationTypes;
  termsAndConditions?: TermsAndConditionsTypes;  
  routeProtection?: RouteProtectionTypes;
  renewal?: RenewalTypes;
  error: boolean;
}
