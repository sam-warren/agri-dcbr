import { ProfileTypes, OperationDetailsTypes, OperationLocationsTypes, BreedingDetailsTypes, AnimalIdentificationTypes, RouteProtectionTypes, RenewalTypes, TermsAndConditionsTypes } from "./types"

export const ProfileState: ProfileTypes = {
    // firstName: "John",
    // middleName: "Alexander",
    // lastName: "Macdonald",
    // commType: "Email",
    // phone: "1234567890",
    // email: "jam@gov.bc.ca",
    // streetNumber: 123,
    // aptNumber: "2B",
    // streetName: "Government St",
    // city: "Langley",
    // postalCode: "V4W1J1",
    // homeRegion: "Cariboo"
    // error: false
  
    firstName: "",
    middleName: "",
    lastName: "",
    commType: "",
    phone: "",
    email: "",
    streetNumber: 0,
    aptNumber: "",
    streetName: "",
    city: "",
    postalCode: "",
    homeRegion: "",
    error: false
  };
  
  export const OperationDetailsState: OperationDetailsTypes = {
    // operationName: "JaM Breeding Co.",
    // opWebsite: "https://www.jambreeding.gov.bc.ca",
    // operationType: "BREEDER",
    // assocName: "Canada Breeding",
    // accidentalBreeding: "false",
    // numWorkers: 142,
    // animalType: "DOG&CAT",
    // numDogBreeds: 12,
    // numCatBreeds: 16,
    // hasVet: "true",
    // error: false
  
    operationName: "",
    opWebsite: "",
    operationType: "",
    assocName: "",
    accidentalBreeding: "",
    numWorkers: 0,
    animalType: "",
    numDogBreeds: 0,
    numCatBreeds: 0,
    hasVet: "",
    error: false
  };
  
  export const OperationLocationsState: OperationLocationsTypes = {
    // locations: [
    //   {
    //     streetName: "Fake St",
    //     aptNumber: "B",
    //     streetNumber: 12345,
    //     city: "Victoria",
    //     postalCode: "r1r1r1",
    //     region: "Capital"
    //   }
    // ],
    // error: false
    locations: [],
    error: false
  };
  
  export const BreedingDetailsState: BreedingDetailsTypes = {
    // femaleIntactDogNum: 52,
    // femaleIntactCatNum: 43,
    // littersWhelped: 6,
    // littersQueened: 5,
    // dogsSold: 16,
    // dogsTransferred: 11,
    // dogsTraded: 6,
    // dogsLeased: 2,
    // catsSold: 20,
    // catsTransferred: 5,
    // catsTraded: 2,
    // catsLeased: 0,
    // numCats: 133,
    // numDogs: 390,
    // error: false
  
    femaleIntactDogNum: 0,
    femaleIntactCatNum: 0,
    littersWhelped: 0,
    littersQueened: 0,
    dogsSold: 0,
    dogsTransferred: 0,
    dogsTraded: 0,
    dogsLeased: 0,
    catsSold: 0,
    catsTransferred: 0,
    catsTraded: 0,
    catsLeased: 0,
    numCats: 0,
    numDogs: 0,
    error: false
  };
  
  export const AnimalIdentificationState: AnimalIdentificationTypes = {
    // hasPermId: "true",
    // permIdType: "OTHER",
    // otherPermIdType: "Paper",
    // error: false
  
    hasPermId: "",
    permIdType: "NOT_APPLICABLE",
    otherPermIdType: "",
    error: false
  };
  
  export const TermsAndConditionsState: TermsAndConditionsTypes = {
    hasAgreed: false,
    error: false
  }
  
  export const RouteProtectionState: RouteProtectionTypes = {
    registerFormOk: false,
    reviewFormOk: false,
    formType: "",
    error: false
  }
  
  export const RenewalState: RenewalTypes = {
    firstName: "",
    middleName: "",
    lastName: "",
    registrationNumber: "",
    expiryDate: "",
    error: false
  
    // firstName: "Sam",
    // middleName: "Robert",
    // lastName: "Warren",
    // registrationNumber: "3135-1234-1111",
    // expiryDate: "",
    // error: false
  }