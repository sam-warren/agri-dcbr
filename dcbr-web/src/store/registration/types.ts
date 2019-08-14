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
  homeAsOperation: boolean;
  error: boolean;
}

export interface OperationDetailsTypes {
  operationName: string;
  opWebsite: string;
  operationType: string;
  assocName: string;
  assocMembership: number;
  assocWebsite: string;
  accidentalBreeding: boolean;
  numWorkers: number;
  animalType: string;
  numDogBreeds: number;
  numCatBreeds: number;
  hasVet: boolean;
  error: boolean;
}

export interface OperationLocationsTypes {
  hasAdditionalLocations: boolean;
  locations: Location[]
}

export interface Location {
  streetNumber: number, 
  aptNumber: string, 
  streetName: string, 
  city: string, 
  postalCode: string
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
  error: boolean;
}

export interface AnimalIdentificationTypes {
  hasPermId: boolean;
  permIdType: string;
  otherPermIdType: string
  error: boolean;
}

export interface RegistrationState {
  profile?: ProfileTypes;
  operationDetails?: OperationDetailsTypes;
  operationLocations?: OperationLocationsTypes;
  breedingDetails?: BreedingDetailsTypes;
  animalIdentification?: AnimalIdentificationTypes;
  error: boolean;
}
