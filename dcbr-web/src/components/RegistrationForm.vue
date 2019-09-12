<template>
  <div class="grey lighten-4">
    <v-content class="mx-4 mb-4 my-4">
      <v-container fluid>
        <div>
            <h1 v-if="this.$props.formType==='register'">Register</h1>
            <h1 v-if="this.$props.formType==='review'">Review your Information</h1>
        </div>
        <div>
            <v-subheader v-if="this.$props.formType==='register'">Fill out the form as accurately as possible. For help, see the Ministry of Agriculture Website.</v-subheader>
            <v-subheader v-if="this.$props.formType==='review'">Please ensure the information you entered is accurate. It is a crime to enter false information.</v-subheader>
        </div>
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
      </v-container>
    </v-content>
    
    <v-content class="mx-4 mb-4 my-4" v-if="this.$props.formType === 'register'">
     <v-container fluid>
        <v-btn
          large 
          block
          round
          mt-5
          class="blue darken-4 white--text"
          @click="navToReview()"
          :disabled="hasErrors"
        >Review & Submit</v-btn>
      </v-container>
    </v-content>

    <v-content class="mx-4 mb-4 my-4" v-if="this.$props.formType === 'review'">
     <v-container fluid>
        <TermsAndConditions/>
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
import TermsAndConditions from "@/components/TermsAndConditions"
import axios from "axios";
export default {
  name: "App",
  components: {
    Profile,
    OperationDetails,
    OperationLocation,
    AnimalIdentification,
    BreedingDetails,
    MenuOperationLocation,
    TermsAndConditions
  },
  data() {
    return {
      e6: 1,
      errors: []
    };
  },
  props: {
    formType: String
  },
  methods: {
    navToReview() {
        this.$store.dispatch("routeProtection/registerFormOk", true);
        this.$router.push("review");
    },
    submitRegistration() {
      console.log("Submit clicked");
      console.log(this.$store.getters["breedingDetails/numDogs"], this.$store.getters["breedingDetails/numCats"]);
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
          num_females_intact: this.$store.getters[
            "breedingDetails/femaleIntactDogNum"
          ],
          num_litter: this.$store.getters["breedingDetails/littersWhelped"],
          num_sold: this.$store.getters["breedingDetails/dogsSold"],
          num_transferred: this.$store.getters[
            "breedingDetails/dogsTransferred"
          ],
          num_traded: this.$store.getters["breedingDetails/dogsTraded"],
          num_leased: this.$store.getters["breedingDetails/dogsLeased"],
          num_animals: this.$store.getters["breedingDetails/numDogs"],
        });
      } else if (this.$store.getters["breedingDetails/animalType"] == "CAT") {
        riskFactors.push({
          animal_type: "CAT",
          num_breeds: this.$store.getters["breedingDetails/numCatBreeds"],
          num_females_intact: this.$store.getters[
            "breedingDetails/femaleIntactCatNum"
          ],
          num_litter: this.$store.getters["breedingDetails/littersQueened"],
          num_sold: this.$store.getters["breedingDetails/catsSold"],
          num_transferred: this.$store.getters[
            "breedingDetails/catsTransferred"
          ],
          num_traded: this.$store.getters["breedingDetails/catsTraded"],
          num_leased: this.$store.getters["breedingDetails/catsLeased"],
          num_animals: this.$store.getters["breedingDetails/numCats"],
        });
      } else {
        riskFactors.push(
          {
            animal_type: "DOG",
            num_breeds: this.$store.getters["breedingDetails/numDogBreeds"],
            num_females_intact: this.$store.getters[
              "breedingDetails/femaleIntactDogNum"
            ],
            num_litter: this.$store.getters["breedingDetails/littersWhelped"],
            num_sold: this.$store.getters["breedingDetails/dogsSold"],
            num_transferred: this.$store.getters[
              "breedingDetails/dogsTransferred"
            ],
            num_traded: this.$store.getters["breedingDetails/dogsTraded"],
            num_leased: this.$store.getters["breedingDetails/dogsLeased"],
            num_animals: this.$store.getters["breedingDetails/numDogs"],
          },
          {
            animal_type: "CAT",
            num_breeds: this.$store.getters["breedingDetails/numCatBreeds"],
            num_females_intact: this.$store.getters[
              "breedingDetails/femaleIntactCatNum"
            ],
            num_litter: this.$store.getters["breedingDetails/littersQueened"],
            num_sold: this.$store.getters["breedingDetails/catsSold"],
            num_transferred: this.$store.getters[
              "breedingDetails/catsTransferred"
            ],
            num_traded: this.$store.getters["breedingDetails/catsTraded"],
            num_leased: this.$store.getters["breedingDetails/catsLeased"],
            num_animals: this.$store.getters["breedingDetails/numCats"],
          }
        );
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
        renewals: [
          {
            first_name: "",
            middle_name: "",
            last_name: "",
            previous_registration_number: ""
          }
        ],
        animal_risk_factors: riskFactors,
        operation_risk_factors: [
          {
            accidental_breeding: (this.$store.getters["operationDetails/accidentalBreeding"] === "true"),
            num_workers: this.$store.getters["breedingDetails/numWorkers"],
            animal_type: this.$store.getters["breedingDetails/animalType"],
            has_vet: (this.$store.getters["operationDetails/hasVet"] === "true"),
            has_perm_id: (this.$store.getters["animalIdentification/hasPermId"] === "true"),
            perm_id_type: this.$store.getters[
              "animalIdentification/permIdType"
            ],
            perm_id_other: this.$store.getters[
              "animalIdentification/otherPermIdType"
            ]
          }
        ]
      };
      console.log(obj.operation_risk_factors);
      if (!this.hasErrors) {
        axios
          .post("/api/register/", obj)
          .then(response => {
            console.log(response);
          })
          .catch(e => {
            this.errors.push(e);
          });
        this.$store.dispatch("routeProtection/reviewFormOk", true);
        this.$router.push("confirmation");
      }
    }
  },
  computed: {
    // error checking
    hasErrors: {
      get: function () {
        // profile
        if (this.$store.getters["profile/firstName"] === "" || this.$store.getters["profile/firstName"].length > 50) {
          return true;
        } if (this.$store.getters["profile/middleName"].length > 50) {
          return true;
        } if (this.$store.getters["profile/lastName"] === "" || this.$store.getters["profile/lastName"].length > 50) {
          return true;
        } if (this.$store.getters["profile/email"] === "" || /.+@.+/.test(this.$store.getters["profile/email"]) === false || this.$store.getters["profile/email"].length > 32) {
          return true;
        } if (this.$store.getters["profile/streetNumber"] <= 0 || this.$store.getters["profile/streetNumber"] > 2147483647) {
          return true;
        } if (this.$store.getters["profile/aptNumber"].length > 32) {
          return true; 
        } if (this.$store.getters["profile/streetName"] === "" || this.$store.getters["profile/streetName"].length > 32) {
          return true;
        } if (this.$store.getters["profile/city"] === "" || this.$store.getters["profile/city"].length > 32) {
          return true;
        } if (this.$store.getters["profile/postalCode"] === "" || /^[ABCEGHJKLMNPRSTVXYabceghjklmnprstvxy]{1}\d{1}[A-Za-z]{1}[ ]{0,1}\d{1}[A-Za-z]{1}\d{1}$/.test(this.$store.getters["profile/postalCode"]) === false) {
          return true;
        } if (this.$store.getters["profile/phone"] === "" || /^\D?(\d{3})\D?\D?(\d{3})\D?(\d{4})$/.test(this.$store.getters["profile/phone"]) === false) {
          return true;
        } if (this.$store.getters["profile/commType"] == "") {
          return true;
        }
        
        // operationDetails
        if (this.$store.getters["operationDetails/operationName"].length > 50) {
          return true;
        } if (/^(|https?:\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?)$/.test(this.$store.getters["operationDetails/opWebsite"]) === false || this.$store.getters["operationDetails/opWebsite"].length > 4000) {
          return true;
        } if (this.$store.getters["operationDetails/operationType"] === "") {
          return true;
        } if (this.$store.getters["operationDetails/animalType"] === "") {
          return true;
        } if (this.$store.getters["operationDetails/accidentalBreeding"] === "") {
          return true;
        } if (this.$store.getters["operationDetails/hasVet"] === "") {
          return true;
        } if (this.$store.getters["operationDetails/numDogBreeds"] < 0 || this.$store.getters["operationDetails/numDogBreeds"] > 2147483647) {
          return true;
        } if (this.$store.getters["operationDetails/numCatBreeds"] < 0 || this.$store.getters["operationDetails/numCatBreeds"] > 2147483647) {
          return true;
        } if (this.$store.getters["operationDetails/numWorkers"] < 0 || this.$store.getters["operationDetails/numWorkers"] > 2147483647) {
          return true;
        } if (this.$store.getters["operationDetails/assocName"].length > 50) {
          return true;
        } if (this.$store.getters["operationDetails/assocMembership"].length > 20) {
          return true;
        } if (this.$store.getters["operationDetails/assocWebsite"].length > 50) {
          return true;
        } if (/^(|https?:\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?)$/.test(this.$store.getters["operationDetails/assocWebsite"]) === false || this.$store.getters["operationDetails/assocWebsite"].length > 50) {
          return true;
        }

        // breedingDetails
        if (this.$store.getters["breedingDetails/femaleIntactCatNum"] < 0 || this.$store.getters["breedingDetails/femaleIntactCatNum"] > 2147483647) {
          return true;
        } if (this.$store.getters["breedingDetails/littersQueened"] < 0 || this.$store.getters["breedingDetails/littersQueened"] > 2147483647) {
          return true;
        } if (this.$store.getters["breedingDetails/catsTransferred"] < 0 || this.$store.getters["breedingDetails/catsTransferred"] > 2147483647) {
          return true;
        } if (this.$store.getters["breedingDetails/catsSold"] < 0 || this.$store.getters["breedingDetails/catsSold"] < 0 > 2147483647) {
          return true;
        } if (this.$store.getters["breedingDetails/catsTraded"] < 0 || this.$store.getters["breedingDetails/catsTraded"] < 0 > 2147483647) {
          return true;
        } if (this.$store.getters["breedingDetails/catsLeased"] < 0 || this.$store.getters["breedingDetails/catsLeased"] < 0 > 2147483647) {
          return true;
        } if (this.$store.getters["breedingDetails/femaleIntactDogNum"] < 0 || this.$store.getters["breedingDetails/femaleIntactDogNum"] > 2147483647) {
          return true;
        } if (this.$store.getters["breedingDetails/littersWhelped"] < 0 || this.$store.getters["breedingDetails/littersWhelped"] > 2147483647) {
          return true;
        } if (this.$store.getters["breedingDetails/dogsTransferred"] < 0 || this.$store.getters["breedingDetails/dogsTransferred"] > 2147483647) {
          return true;
        } if (this.$store.getters["breedingDetails/dogsSold"] < 0 || this.$store.getters["breedingDetails/dogsSold"] > 2147483647) {
          return true;
        } if (this.$store.getters["breedingDetails/dogsTraded"] < 0 || this.$store.getters["breedingDetails/dogsTraded"] > 2147483647) {
          return true;
        } if (this.$store.getters["breedingDetails/dogsLeased"] < 0 || this.$store.getters["breedingDetails/dogsLeased"] > 2147483647) {
          return true;
        } if (this.$store.getters["breedingDetails/dogsLeased"] < 0 || this.$store.getters["breedingDetails/dogsLeased"] > 2147483647) {
          return true;
        } if (this.$store.getters["breedingDetails/numCats"] < 0 || this.$store.getters["breedingDetails/numCats"] > 2147483647) {
          return true;
        } if (this.$store.getters["breedingDetails/numDogs"] < 0 || this.$store.getters["breedingDetails/numDogs"] > 2147483647) {
          return true;
        }
        
        // operationLocations
        if (this.$store.getters["operationLocations/hasAdditionalLocations"] === "") {
          return true;
        }
        if (this.$store.getters["operationLocations/hasAdditionalLocations"] === "true") {
          let hasError = false;
          this.$store.getters["operationLocations/locations"].forEach(location => {
            if (location.streetNumber <= 0 || location.streetNumber > 2147483647) {
              hasError = true;
            } else if (location.aptNumber.length > 32) {
              hasError = true;
            } else if (location.streetName === "" || location.streetName.length > 32) {
              hasError = true;
            } else if (location.city === "" || location.city.length > 32) {
              hasError = true;
            } else if (location.postalCode === "" || /^[ABCEGHJKLMNPRSTVXYabceghjklmnprstvxy]{1}\d{1}[A-Za-z]{1}[ ]{0,1}\d{1}[A-Za-z]{1}\d{1}$/.test(location.postalCode) === false) {
              hasError = true;
            }
          });
          return hasError;
        } 

        // termsAndConditions
        if (this.$store.getters["termsAndConditions/hasAgreed"] === false && this.$props.formType==="review") {
            return true;
        }

        // animalIdentification
        if (this.$store.getters["animalIdentification/hasPermId"] === "") {
          return true;
        } if (this.$store.getters["animalIdentification/hasPermId"] === "true") {
          let hasError = false;
          if (this.$store.getters["animalIdentification/permIdType"] === "") {
            hasError = true;
          } else if (this.$store.getters["animalIdentification/permIdType"] === "OTHER"){
            if (this.$store.getters["animalIdentification/otherPermIdType"] === "" || this.$store.getters["animalIdentification/otherPermIdType"].length > 15) {
              hasError = true
            }
          }
          return hasError;
        }

        
        
        return false;
      },
    },
  }
};
</script>