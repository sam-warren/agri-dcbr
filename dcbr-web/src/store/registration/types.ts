export interface ProfileTypes {
  firstName: string;
  middleName: string;
  lastName: string;
  commType: string;
  phone: string;
  email: string;
  streetNumber: number;
  aptNumber: number;
  streetName: string;
  city: string;
  postalCode: string;
  homeAsOperation: boolean;
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
}

export interface BreedingDetailsTypes {
  femaleIntactDogNum: number,
  femaleIntactCatNum: number,
  littersWhelped: number,
  littersQueened: number,
  dogsSold: number,
  dogsTransferred: number,
  dogsTraded: number,
  dogsLeased: number,
  catsSold: number,
  catsTransferred: number,
  catsTraded: number,
  catsLeased: number,
}

export interface AnimalIdentificationTypes {
  hasPermId: boolean,
  permIdType: string,
  otherPermIdType: string
}

export interface RegistrationState {
  profile?: ProfileTypes;
  operationDetails?: OperationDetailsTypes;
  breedingDetails?: BreedingDetailsTypes;
  animalIdentification?: AnimalIdentificationTypes;
  error: boolean;
}
