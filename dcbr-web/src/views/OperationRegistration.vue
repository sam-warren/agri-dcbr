<template>
  <div class="grey lighten-4">
    <v-stepper flat>
      <v-stepper-header>
        <v-stepper-step complete editable step="1">Registration</v-stepper-step>

        <v-divider></v-divider>

        <v-stepper-step step="2">Payment($0)</v-stepper-step>

        <v-divider></v-divider>

        <v-stepper-step step="3">Review & submit</v-stepper-step>
      </v-stepper-header>
    </v-stepper>

    <v-content class="mx-4 mb-4 my-4">
      <v-container fluid>
        <div>
          <Profile ref="profile" />
        </div>

        <div editable :complete="e6 > 2" step="2">
          <OperationDetails ref="operationdetails" />
        </div>
        <BreedingDetails ref="breedingdetails" />
        <!-- OPERATION LOCATION MENU -->
        <div>
          <MenuOperationLocation />
        </div>
        <div>
          <AnimalIdentification ref="animalidentification" />
        </div>

        <v-btn
          large
          block
          round
          mt-5
          class="blue darken-4 white--text"
          @click="submitRegistration()"
          :disabled="hasErrors"
        >Submit</v-btn>
      </v-container>
    </v-content>
  </div>
</template>


<script>
import OperationDetails from "@/components/OperationDetails";
import Profile from "@/components/Profile";
import OperationLocation from "@/components/OperationLocation";
import AnimalIdentification from "@/components/AnimalIdentification";
import BreedingDetails from "@/components/BreedingDetails";
import MenuOperationLocation from "@/components/MenuOperationLocation";
import axios from "axios";
export default {
  name: "App",
  components: {
    Profile,
    OperationDetails,
    OperationLocation,
    AnimalIdentification,
    BreedingDetails,
    MenuOperationLocation
  },
  data() {
    return {
      e6: 1,
    };
  },
  methods: {
    submitRegistration() {
      console.log("Submit clicked");
      
      let addresses = [
        {
          address_type: "PRI",
          street_num: this.$store.getters["profile/streetNumber"],
          suite: this.$store.getters["profile/aptNumber"],
          street_name: this.$store.getters["profile/streetName"],
          city: this.$store.getters["profile/city"],
          postal_code: this.$store.getters["profile/postalCode"]
        }
      ];
      this.$store.getters["operationLocations/locations"].forEach(location => {
        addresses.push({
          address_type: "OPN",
          street_num: location.streetNumber,
          suite: location.aptNumber,
          street_name: location.streetName,
          city: location.city,
          postal_code: location.postalCode
        });
      });
      let riskFactors = [];
      if (this.$store.getters["breedingDetails/animalType"] == "DOG") {
        riskFactors.push({
          animal_type: "DOG",
          num_breeds: this.$store.getters["breedingDetails/numDogBreeds"],
          num_females_intact: this.$store.getters["breedingDetails/femaleIntactDogNum"],
          num_litter: this.$store.getters["breedingDetails/littersWhelped"],
          num_sold: this.$store.getters["breedingDetails/dogsSold"],
          num_transferred: this.$store.getters["breedingDetails/dogsTransferred"],
          num_traded: this.$store.getters["breedingDetails/dogsTraded"],
          num_leased: this.$store.getters["breedingDetails/dogsLeased"],
        });
      }
      else if (this.$store.getters["breedingDetails/animalType"] == "CAT") {
        riskFactors.push({
          animal_type: "CAT",
          num_breeds: this.$store.getters["breedingDetails/numCatBreeds"],
          num_females_intact: this.$store.getters["breedingDetails/femaleIntactCatNum"],
          num_litter: this.$store.getters["breedingDetails/littersQueened"],
          num_sold: this.$store.getters["breedingDetails/catsSold"],
          num_transferred: this.$store.getters["breedingDetails/catsTransferred"],
          num_traded: this.$store.getters["breedingDetails/catsTraded"],
          num_leased: this.$store.getters["breedingDetails/catsLeased"],
        })
      } else {
          riskFactors.push({
          animal_type: "DOG",
          num_breeds: this.$store.getters["breedingDetails/numDogBreeds"],
          num_females_intact: this.$store.getters["breedingDetails/femaleIntactDogNum"],
          num_litter: this.$store.getters["breedingDetails/littersWhelped"],
          num_sold: this.$store.getters["breedingDetails/dogsSold"],
          num_transferred: this.$store.getters["breedingDetails/dogsTransferred"],
          num_traded: this.$store.getters["breedingDetails/dogsTraded"],
          num_leased: this.$store.getters["breedingDetails/dogsLeased"],
        },
        {
          animal_type: "CAT",
          num_breeds: this.$store.getters["breedingDetails/numCatBreeds"],
          num_females_intact: this.$store.getters["breedingDetails/femaleIntactCatNum"],
          num_litter: this.$store.getters["breedingDetails/littersQueened"],
          num_sold: this.$store.getters["breedingDetails/catsSold"],
          num_transferred: this.$store.getters["breedingDetails/catsTransferred"],
          num_traded: this.$store.getters["breedingDetails/catsTraded"],
          num_leased: this.$store.getters["breedingDetails/catsLeased"],
        })
      }
      let obj = {
        operator_status: "ACTIVE",
        operator: {
          first_name: this.$store.getters["profile/firstName"],
          middle_name: this.$store.getters["profile/middleName"],
          last_name: this.$store.getters["profile/lastName"],
          comm_pref: this.$store.getters["profile/commType"],
          phone_num: this.$store.getters["profile/phone"],
          email_address: this.$store.getters["profile/email"],
          operation_type: this.$store.getters["operationDetails/operationType"],
          operation_name: this.$store.getters["operationDetails/operationName"],
          operation_URL: this.$store.getters["operationDetails/opWebsite"]
        },
        addresses: addresses,
        associations: [
          {
            assoc_name: this.$store.getters["operationDetails/assocName"],
            membership_num: this.$store.getters[
              "operationDetails/assocMembership"
            ],
            assoc_URL: this.$store.getters["operationDetails/assocWebsite"]
          }
        ],
        animal_risk_factors: riskFactors,
        operation_risk_factors: [
          {
            accidental_breeding: this.$store.getters[
              "breedingDetails/accidentalBreeding"
            ],
            num_workers: this.$store.getters["breedingDetails/numWorkers"],
            animal_type: this.$store.getters["breedingDetails/animalType"],
            has_vet: this.$store.getters["breedingDetails/hasVet"],
            has_perm_id: this.$store.getters["animalIdentification/hasPermId"],
            perm_id_type: this.$store.getters[
              "animalIdentification/permIdType"
            ],
            perm_id_other: this.$store.getters[
              "animalIdentification/otherPermIdType"
            ]
          }
        ]
      };
      console.log(obj);
      if (!this.hasErrors) {
        axios
          .post("/api/registration_Number/", obj)
          .then(response => {
            console.log(response);
          })
          .catch(e => {
            this.errors.push(e);
          });
        this.$router.push("payment");
      }
    }
  },
  computed: {
    // error checking
    hasErrors: {
      get: function () {
        // profile
        if (this.$store.getters["profile/firstName"] === "" || this.$store.getters["profile/firstName"].length > 50) {
          console.log("(1) REQUIREMENTS NOT FULFILLED!");
          return true;
        } if (this.$store.getters["profile/middleName"].length > 50) {
          console.log("(2) REQUIREMENTS NOT FULFILLED!");
          return true;
        } if (this.$store.getters["profile/lastName"] === "" || this.$store.getters["profile/lastName"].length > 50) {
          console.log("(3) REQUIREMENTS NOT FULFILLED!");
          return true;
        } if (this.$store.getters["profile/email"] === "" || /.+@.+/.test(this.$store.getters["profile/email"]) === false) {
          console.log("(4) REQUIREMENTS NOT FULFILLED!");
          return true;
        } if (this.$store.getters["profile/streetNumber"] <= 0) {
          console.log("(5) REQUIREMENTS NOT FULFILLED!");
          return true;
        } if (this.$store.getters["profile/aptNumber"].length > 32) {
          console.log("(6) REQUIREMENTS NOT FULFILLED!");
          return true; 
        } if (this.$store.getters["profile/streetName"] === "" || this.$store.getters["profile/streetName"].length > 32) {
          console.log("(7) REQUIREMENTS NOT FULFILLED!");
          return true;
        } if (this.$store.getters["profile/city"] === "" || this.$store.getters["profile/city"].length > 32) {
          console.log("(8) REQUIREMENTS NOT FULFILLED!");
          return true;
        } if (this.$store.getters["profile/postalCode"] === "" || /^[ABCEGHJKLMNPRSTVXYabceghjklmnprstvxy]{1}\d{1}[A-Za-z]{1}[ ]{0,1}\d{1}[A-Za-z]{1}\d{1}$/.test(this.$store.getters["profile/postalCode"]) === false) {
          console.log("(9) REQUIREMENTS NOT FULFILLED!");
          return true;
        } if (this.$store.getters["profile/phone"] === "" || /^\D?(\d{3})\D?\D?(\d{3})\D?(\d{4})$/.test(this.$store.getters["profile/phone"]) === false) {
          console.log("(10) REQUIREMENTS NOT FULFILLED!");
          return true;
        } if (this.$store.getters["profile/commType"] == "") {
          console.log("(11) REQUIREMENTS NOT FULFILLED!");
          return true;
        }
        
        // operationDetails
        if (this.$store.getters["operationDetails/operationName"].length > 50) {
          console.log("(12) REQUIREMENTS NOT FULFILLED!");
          return true;
        } if (/(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})/.test(this.$store.getters["operationDetails/opWebsite"]) === false) {
          console.log("(13) REQUIREMENTS NOT FULFILLED!");
          return true;
        } if (this.$store.getters["operationDetails/operationType"] === "") {
          console.log("(14) REQUIREMENTS NOT FULFILLED!");
          return true;
        } if (this.$store.getters["operationDetails/animalType"] === "") {
          console.log("(15) REQUIREMENTS NOT FULFILLED!");
          return true;
        } if (this.$store.getters["operationDetails/accidentalBreeding"] === "") {
          console.log("(16) REQUIREMENTS NOT FULFILLED!");
          return true;
        } if (this.$store.getters["operationDetails/hasVet"] === "") {
          console.log("(17) REQUIREMENTS NOT FULFILLED!");
          return true;
        } if (this.$store.getters["operationDetails/numDogBreeds"] < 0) {
          console.log("(18) REQUIREMENTS NOT FULFILLED!");
          return true;
        } if (this.$store.getters["operationDetails/numCatBreeds"] < 0) {
          console.log("(19) REQUIREMENTS NOT FULFILLED!");
          return true;
        } if (this.$store.getters["operationDetails/numWorkers"] < 0) {
          console.log("(20) REQUIREMENTS NOT FULFILLED!");
          return true;
        } if (this.$store.getters["operationDetails/assocName"].length > 50) {
          console.log("(21) REQUIREMENTS NOT FULFILLED!");
          return true;
        } if (this.$store.getters["operationDetails/assocMembership"].length > 20) {
          console.log("(22) REQUIREMENTS NOT FULFILLED!");
          return true;
        } if (this.$store.getters["operationDetails/assocWebsite"].length > 50) {
          console.log("(23) REQUIREMENTS NOT FULFILLED!");
          return true;
        } if (/^(|https?:\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?)$/.test(this.$store.getters["operationDetails/assocWebsite"]) === false) {
          console.log("(24) REQUIREMENTS NOT FULFILLED!");
          return true;
        }

        // breedingDetails
        if (this.$store.getters["breedingDetails/femaleIntactCatNum"] < 0) {
          console.log("(25) REQUIREMENTS NOT FULFILLED!");
          return true;
        } if (this.$store.getters["breedingDetails/littersQueened"] < 0) {
          console.log("(26) REQUIREMENTS NOT FULFILLED!");
          return true;
        } if (this.$store.getters["breedingDetails/catsTransferred"] < 0) {
          console.log("(27) REQUIREMENTS NOT FULFILLED!");
          return true;
        } if (this.$store.getters["breedingDetails/catsSold"] < 0) {
          console.log("(28) REQUIREMENTS NOT FULFILLED!");
          return true;
        } if (this.$store.getters["breedingDetails/catsTraded"] < 0) {
          console.log("(29) REQUIREMENTS NOT FULFILLED!");
          return true;
        } if (this.$store.getters["breedingDetails/catsLeased"] < 0) {
          console.log("(30) REQUIREMENTS NOT FULFILLED!");
          return true;
        } if (this.$store.getters["breedingDetails/femaleIntactDogNum"] < 0) {
          console.log("(31) REQUIREMENTS NOT FULFILLED!");
          return true;
        } if (this.$store.getters["breedingDetails/littersWhelped"] < 0) {
          console.log("(32) REQUIREMENTS NOT FULFILLED!");
          return true;
        } if (this.$store.getters["breedingDetails/dogsTransferred"] < 0) {
          console.log("(33) REQUIREMENTS NOT FULFILLED!");
          return true;
        } if (this.$store.getters["breedingDetails/dogsSold"] < 0) {
          console.log("(34) REQUIREMENTS NOT FULFILLED!");
          return true;
        } if (this.$store.getters["breedingDetails/dogsTraded"] < 0) {
          console.log("(35) REQUIREMENTS NOT FULFILLED!");
          return true;
        } if (this.$store.getters["breedingDetails/dogsLeased"] < 0) {
          console.log("(36) REQUIREMENTS NOT FULFILLED!");
          return true;
        }
        
        // operationLocations
        if (this.$store.getters["operationLocations/hasAdditionalLocations"] === "") {
          console.log("(37) REQUIREMENTS NOT FULFILLED!");
          return true;
        }
        if (this.$store.getters["operationLocations/hasAdditionalLocations"] === "true") {
          console.log("Has additional locations")
          let containsError = false;
          this.$store.getters["operationLocations/locations"].forEach(location => {
            console.log("LOCATION: ", location)
            if (location.streetNumber <= 0) {
              console.log("(38) REQUIREMENTS NOT FULFILLED!");
              containsError = true;
            } else if (location.aptNumber.length > 32) {
              console.log("(39) REQUIREMENTS NOT FULFILLED!");
              containsError = true;
            } else if (location.streetName === "" || location.streetName.length > 32) {
              console.log("(40) REQUIREMENTS NOT FULFILLED!");
              containsError = true;
            } else if (location.city === "" || location.city.length > 32) {
              console.log("(41) REQUIREMENTS NOT FULFILLED!");
              containsError = true;
            } else if (location.postalCode === "" || /^[ABCEGHJKLMNPRSTVXYabceghjklmnprstvxy]{1}\d{1}[A-Za-z]{1}[ ]{0,1}\d{1}[A-Za-z]{1}\d{1}$/.test(location.postalCode) === false) {
              console.log("(42) REQUIREMENTS NOT FULFILLED!");
              containsError = true;
            }
          });
          return containsError;
        } 

        // animalIdentification
        if (this.$store.getters["animalIdentification/hasPermId"] === "") {
          console.log("(43) REQUIREMENTS NOT FULFILLED!");
          return true;
        } if (this.$store.getters["animalIdentification/hasPermId"] === "true") {
          let hasError = false;
          if (this.$store.getters["animalIdentification/permIdType"] === "") {
            console.log("(44) REQUIREMENTS NOT FULFILLED")
            hasError = true;
          } else if (this.$store.getters["animalIdentification/permIdType"] === "OTHER"){
            if (this.$store.getters["animalIdentification/otherPermIdType"] === "" || this.$store.getters["animalIdentification/otherPermIdType"].length > 15) {
              console.log("(45) REQUIREMENTS NOT FULFILLED!");
              hasError = true
            }
          }
          return hasError;
        }
        console.log("REQUIREMENTS FULFILLED!");
        return false;
      }
    },
  }
};
</script>