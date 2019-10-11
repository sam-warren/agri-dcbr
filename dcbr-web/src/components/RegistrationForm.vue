<template>
  <div class="grey lighten-4">
    <v-content class="mx-4 mb-4 my-4">
      <v-container fluid>
        <div>
          <h1
            v-if="this.$store.getters['routeProtection/formType'] === 'register' && this.$props.formType==='register'"
          >Register</h1>
          <h1
            v-if="this.$store.getters['routeProtection/formType'] === 'register' && this.$props.formType==='review'"
          >Review your Information</h1>
          <h1
            v-if="this.$store.getters['routeProtection/formType'] === 'renewal' && this.$props.formType ==='register'"
          >Renew your Certification</h1>
          <h1
            v-if="this.$store.getters['routeProtection/formType'] === 'renewal' && this.$props.formType==='review'"
          >Review your Information</h1>
        </div>
        <div>
          <v-subheader
            v-if="this.$store.getters['routeProtection/formType'] === 'register' && this.$props.formType==='register'"
          >Fill out the form as accurately as possible. For help, see the Ministry of Agriculture Website.</v-subheader>
          <v-subheader
            v-if="this.$store.getters['routeProtection/formType'] === 'register' && this.$props.formType==='review'"
          >Please ensure the information you entered is accurate. It is a crime to enter false information.</v-subheader>
          <v-subheader
            v-if="this.$store.getters['routeProtection/formType'] === 'renewal' && this.$props.formType==='register'"
          >Fill out the form as accurately as possible. For help, see the Ministry of Agriculture Website.</v-subheader>
          <v-subheader
            v-if="this.$store.getters['routeProtection/formType'] === 'renewal' && this.$props.formType==='review'"
          >Please ensure the information you entered is accurate. It is a crime to enter false information.</v-subheader>
        </div>
        <div v-if="this.$store.getters['routeProtection/formType'] === 'renewal'">
          <RenewalForm />
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
        <div v-if="hasErrors">
          <div>
            <v-tooltip bottom>
              <template v-slot:activator="{on}">
                <div v-on="on">
                  <v-btn
                    large
                    block
                    round
                    mt-5
                    class="blue darken-4 white--text"
                    disabled
                  >Review & Submit</v-btn>
                </div>
              </template>
              <span>{{error}}</span>
            </v-tooltip>
          </div>
        </div>
        <div v-else>
          <div>
            <v-btn large block round mt-5 class="primary" @click="navToReview()">Review & Submit</v-btn>
          </div>
        </div>
      </v-container>
    </v-content>

    <v-content class="mx-4 mb-4 my-4" v-if="this.$props.formType === 'review'">
      <v-container fluid>
        <TermsAndConditions />
        <div v-if="hasErrors">
          <div>
            <v-tooltip bottom>
              <template v-slot:activator="{on}">
                <div v-on="on">
                  <v-btn large block round mt-5 class="blue darken-4 white--text" disabled>Submit</v-btn>
                </div>
              </template>
              <span>{{error}}</span>
            </v-tooltip>
          </div>
        </div>
        <div v-else>
          <div>
            <v-btn large block round mt-5 class="primary" @click="submitRegistration()">Submit</v-btn>
          </div>
        </div>
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
import TermsAndConditions from "@/components/TermsAndConditions";
import RenewalForm from "@/components/RenewalForm";
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
    TermsAndConditions,
    RenewalForm
  },
  data() {
    return {
      e6: 1,
      error: "",
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
      let addresses = [
        {
          address_type: "MAIL",
          street_num: this.$store.getters["profile/streetNumber"],
          suite: this.$store.getters["profile/aptNumber"],
          street_name: this.$store.getters["profile/streetName"],
          POBox: this.$store.getters["profile/poBox"],
          city: this.$store.getters["profile/city"],
          postal_code: this.$store.getters["profile/postalCode"],
          region: this.$store.getters["profile/homeRegion"]
        }
      ];
      let renewalDetails = [
        {
          first_name: this.$store.getters["renewal/firstName"],
          middle_name: this.$store.getters["renewal/middleName"],
          last_name: this.$store.getters["renewal/lastName"],
          previous_registration_number: this.$store.getters[
            "renewal/registrationNumber"
          ]
        }
      ];
      if (this.$store.getters["routeProtection/formType"] === "register") {
        renewalDetails = [];
      }
      this.$store.getters["operationLocations/locations"].forEach(location => {
        addresses.push({
          address_type: "OPN",
          street_num: location.streetNumber,
          suite: location.aptNumber,
          street_name: location.streetName,
          city: location.city,
          postal_code: location.postalCode,
          region: location.region
        });
      });
      let riskFactors = [];
      if (this.$store.getters["operationDetails/animalType"] == "DOG") {
        riskFactors.push({
          animal_type: "DOG",
          num_breeds: this.$store.getters["operationDetails/numDogBreeds"],
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
          num_animals: this.$store.getters["breedingDetails/numDogs"]
        });
      } else if (this.$store.getters["operationDetails/animalType"] == "CAT") {
        riskFactors.push({
          animal_type: "CAT",
          num_breeds: this.$store.getters["operationDetails/numCatBreeds"],
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
          num_animals: this.$store.getters["breedingDetails/numCats"]
        });
      } else {
        riskFactors.push(
          {
            animal_type: "DOG",
            num_breeds: this.$store.getters["operationDetails/numDogBreeds"],
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
            num_animals: this.$store.getters["breedingDetails/numDogs"]
          },
          {
            animal_type: "CAT",
            num_breeds: this.$store.getters["operationDetails/numCatBreeds"],
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
            num_animals: this.$store.getters["breedingDetails/numCats"]
          }
        );
      }
      let obj = {
        operator_status: "ACTIVE",
        registration_number: "",
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
            assoc_name: this.$store.getters["operationDetails/assocName"]
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
            accidental_breeding:
              this.$store.getters["operationDetails/accidentalBreeding"] ===
              "true",
            num_workers: this.$store.getters["operationDetails/numWorkers"],
            animal_type: this.$store.getters["operationDetails/animalType"],
            has_vet: this.$store.getters["operationDetails/hasVet"] === "true",
            has_perm_id:
              this.$store.getters["animalIdentification/hasPermId"] === "true",
            perm_id_type: this.$store.getters[
              "animalIdentification/permIdType"
            ],
            perm_id_other: this.$store.getters[
              "animalIdentification/otherPermIdType"
            ]
          }
        ],
        renewals: renewalDetails
      };
      console.log(obj);
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
      get: function() {
        this.error = "";
        // profile
        if (this.$store.getters["routeProtection/formType"] === "renewal") {
          if (
            this.$store.getters["renewal/firstName"] === "" ||
            this.$store.getters["renewal/firstName"].length > 32
          ) {
            this.error = "First name must meet requirements";
            return true;
          }
          if (this.$store.getters["renewal/middleName"].length > 50) {
            this.error = "Middle name must meet requirements";
            return true;
          }
          if (
            this.$store.getters["renewal/lastName"] === "" ||
            this.$store.getters["renewal/lastName"].length > 50
          ) {
            this.error = "Last name must meet requirements";
            return true;
          }
          if (
            this.$store.getters["renewal/registrationNumber"] === "" ||
            this.$store.getters["renewal/registrationNumber"].length > 20
          ) {
            this.error = "Registration number must meet requirements";
            return true;
          }
          if (this.$store.getters["renewal/registrationDate"] === "") {
            this.error = "Expiry date must meet requirements";
            return true;
          }
        }

        if (
          this.$store.getters["profile/firstName"] === "" ||
          this.$store.getters["profile/firstName"].length > 50
        ) {
          this.error = "First name must meet requirements";
          return true;
        }
        if (this.$store.getters["profile/middleName"].length > 50) {
          this.error = "Middle name must meet requirements";
          return true;
        }
        if (
          this.$store.getters["profile/lastName"] === "" ||
          this.$store.getters["profile/lastName"].length > 50
        ) {
          this.error = "Last name must meet requirements";
          return true;
        }
        if (
          this.$store.getters["profile/email"] === "" ||
          /.+@.+/.test(this.$store.getters["profile/email"]) === false ||
          this.$store.getters["profile/email"].length > 32
        ) {
          this.error = "Personal email must meet requirements";
          return true;
        }
        if (
          this.$store.getters["profile/streetNumber"] <= 0 ||
          this.$store.getters["profile/streetNumber"] > 2147483647
        ) {
          this.error = "Street number must meet requirements";
          return true;
        }
        if (this.$store.getters["profile/aptNumber"].length > 32) {
          this.error = "Apt/Suite must meet requirements";
          return true;
        }
        if (
          this.$store.getters["profile/streetName"] === "" ||
          this.$store.getters["profile/streetName"].length > 32
        ) {
          this.error = "Street name must meet requirements";
          return true;
        }
        if (
          this.$store.getters["profile/poBox"].length > 32
        ) {
          this.error = "P.O. Box must meet requirements";
          return true;
        }
        if (
          this.$store.getters["profile/city"] === "" ||
          this.$store.getters["profile/city"].length > 32
        ) {
          this.error = "City must meet requirements";
          return true;
        }
        if (
          this.$store.getters["profile/postalCode"] === "" ||
          /^[ABCEGHJKLMNPRSTVXYabceghjklmnprstvxy]{1}\d{1}[A-Za-z]{1}[ ]{0,1}\d{1}[A-Za-z]{1}\d{1}$/.test(
            this.$store.getters["profile/postalCode"]
          ) === false
        ) {
          this.error = "Postal code must meet requirements";
          return true;
        }
        if (this.$store.getters["profile/homeRegion"] === "") {
          this.error = "Home region must meet requirements";
          return true;
        }
        if (
          this.$store.getters["profile/phone"] === "" ||
          /^\D?(\d{3})\D?\D?(\d{3})\D?(\d{4})$/.test(
            this.$store.getters["profile/phone"]
          ) === false
        ) {
          this.error = "Personal phone must meet requirements";
          return true;
        }
        if (this.$store.getters["profile/commType"] == "") {
          this.error = "Please select a preferred communication type";
          return true;
        }

        // operationDetails
        if (this.$store.getters["operationDetails/operationName"].length > 50) {
          this.error = "Operation name must meet requirements";
          return true;
        }
        if (
          /^$|(((((ht|f)tp(s?))\:\/\/)?)+(www\.){1}\S+)+(\.{1}\w{2,})/.test(
            this.$store.getters["operationDetails/opWebsite"]
          ) === false ||
          this.$store.getters["operationDetails/opWebsite"].length > 4000
        ) {
          this.error = "Operation website must meet requirements";
          return true;
        }
        if (this.$store.getters["operationDetails/operationType"] === "") {
          this.error =
            "Please select an operator type (breeder / seller / both)";
          return true;
        }
        if (this.$store.getters["operationDetails/animalType"] === "") {
          this.error = "Please select an animal type (cat / dog / both)";
          return true;
        }
        if (this.$store.getters["operationDetails/accidentalBreeding"] === "") {
          this.error =
            "Please select whether or not you've had an accidental breeding";
          return true;
        }
        if (this.$store.getters["operationDetails/hasVet"] === "") {
          this.error =
            "Please select whether or not you have a client veterinary relationship";
          return true;
        }
        if (
          this.$store.getters["operationDetails/numDogBreeds"] < 0 ||
          this.$store.getters["operationDetails/numDogBreeds"] > 2147483647
        ) {
          this.error = "Number of dog breeds must meet requirements";
          return true;
        }
        if (
          this.$store.getters["operationDetails/numCatBreeds"] < 0 ||
          this.$store.getters["operationDetails/numCatBreeds"] > 2147483647
        ) {
          this.error = "Number of cat breeds must meet requirements";
          return true;
        }
        if (
          this.$store.getters["operationDetails/numWorkers"] < 1 ||
          this.$store.getters["operationDetails/numWorkers"] > 2147483647
        ) {
          this.error = "Number of workers must meet requirements";
          return true;
        }
        if (this.$store.getters["operationDetails/assocName"].length > 50) {
          this.error = "Association name must meet requirements";
          return true;
        }

        // breedingDetails
        if (
          this.$store.getters["breedingDetails/numCats"] < 0 ||
          this.$store.getters["breedingDetails/numCats"] > 2147483647
        ) {
          this.error = "Number of cats must meet requirements";
          return true;
        }
        if (
          this.$store.getters["breedingDetails/femaleIntactCatNum"] < 0 ||
          this.$store.getters["breedingDetails/femaleIntactCatNum"] > 2147483647
        ) {
          this.error = "Number of intact female cats must meet requirements";
          return true;
        }
        if (
          this.$store.getters["breedingDetails/littersQueened"] < 0 ||
          this.$store.getters["breedingDetails/littersQueened"] > 2147483647
        ) {
          this.error = "Number of litters queened must meet requirements";
          return true;
        }
        if (
          this.$store.getters["breedingDetails/catsTransferred"] < 0 ||
          this.$store.getters["breedingDetails/catsTransferred"] > 2147483647
        ) {
          this.error = "Number of cats transferred must meet requirements";
          return true;
        }
        if (
          this.$store.getters["breedingDetails/catsSold"] < 0 ||
          this.$store.getters["breedingDetails/catsSold"] < 0 > 2147483647
        ) {
          this.error = "Number of cats sold must meet requirements";
          return true;
        }
        if (
          this.$store.getters["breedingDetails/catsTraded"] < 0 ||
          this.$store.getters["breedingDetails/catsTraded"] < 0 > 2147483647
        ) {
          this.error = "Number of cats traded must meet requirements";
          return true;
        }
        if (
          this.$store.getters["breedingDetails/catsLeased"] < 0 ||
          this.$store.getters["breedingDetails/catsLeased"] < 0 > 2147483647
        ) {
          this.error = "Number of cats leased must meet requirements";
          return true;
        }
        if (
          this.$store.getters["breedingDetails/numDogs"] < 0 ||
          this.$store.getters["breedingDetails/numDogs"] > 2147483647
        ) {
          this.error = "Number of dogs must meet requirements";
          return true;
        }
        if (
          this.$store.getters["breedingDetails/femaleIntactDogNum"] < 0 ||
          this.$store.getters["breedingDetails/femaleIntactDogNum"] > 2147483647
        ) {
          this.error = "Number of intact female dogs must meet requirements";
          return true;
        }
        if (
          this.$store.getters["breedingDetails/littersWhelped"] < 0 ||
          this.$store.getters["breedingDetails/littersWhelped"] > 2147483647
        ) {
          this.error = "Number of litters whelped must meet requirements";
          return true;
        }
        if (
          this.$store.getters["breedingDetails/dogsTransferred"] < 0 ||
          this.$store.getters["breedingDetails/dogsTransferred"] > 2147483647
        ) {
          this.error = "Number of dogs transferred must meet requirements";
          return true;
        }
        if (
          this.$store.getters["breedingDetails/dogsSold"] < 0 ||
          this.$store.getters["breedingDetails/dogsSold"] > 2147483647
        ) {
          this.error = "Number of dogs sold must meet requirements";
          return true;
        }
        if (
          this.$store.getters["breedingDetails/dogsTraded"] < 0 ||
          this.$store.getters["breedingDetails/dogsTraded"] > 2147483647
        ) {
          this.error = "Number of dogs traded must meet requirements";
          return true;
        }
        if (
          this.$store.getters["breedingDetails/dogsLeased"] < 0 ||
          this.$store.getters["breedingDetails/dogsLeased"] > 2147483647
        ) {
          this.error = "Number of dogs leased must meet requirements";
          return true;
        }

        // operationLocations
        let locationNumber = 0;
        let hasError = false;
        this.$store.getters["operationLocations/locations"].forEach(
          location => {
            locationNumber++;
            if (
              location.streetNumber <= 0 ||
              location.streetNumber > 2147483647
            ) {
              this.error =
                "Street number of location " +
                locationNumber +
                " must meet requirements";
              hasError = true;
            } else if (location.aptNumber.length > 32) {
              this.error =
                "Apt/suite of location " +
                locationNumber +
                " must meet requirements";
              hasError = true;
            } else if (
              location.streetName === "" ||
              location.streetName.length > 32
            ) {
              this.error =
                "Street name of location " +
                locationNumber +
                " must meet requirements";
              hasError = true;
            } else if (location.city === "" || location.city.length > 32) {
              this.error =
                "City of location " +
                locationNumber +
                " must meet requirements";
              hasError = true;
            } else if (
              location.postalCode === "" ||
              /^[ABCEGHJKLMNPRSTVXYabceghjklmnprstvxy]{1}\d{1}[A-Za-z]{1}[ ]{0,1}\d{1}[A-Za-z]{1}\d{1}$/.test(
                location.postalCode
              ) === false
            ) {
              this.error =
                "Postal code of location " +
                locationNumber +
                "must meet requirements";
              hasError = true;
            } else if (location.region === "") {
              this.error =
                "Region of location " +
                locationNumber +
                " must meet requirements";
              hasError = true;
            }
          }
        );
        if (hasError) {
          return true;
        }

        // animalIdentification
        if (this.$store.getters["animalIdentification/hasPermId"] === "") {
          this.error =
            "Please select whether or not you maintain permanent identification of your animals";
          return true;
        }
        if (this.$store.getters["animalIdentification/hasPermId"] === "true") {
          let hasError = false;
          if (
            this.$store.getters["animalIdentification/permIdType"] ===
            "NOT_APPLICABLE"
          ) {
            this.error = "Please select a type of permanent identification";
            hasError = true;
          } else if (
            this.$store.getters["animalIdentification/permIdType"] === "OTHER"
          ) {
            if (
              this.$store.getters["animalIdentification/otherPermIdType"] ===
                "" ||
              this.$store.getters["animalIdentification/otherPermIdType"]
                .length > 15
            ) {
              this.error =
                "'Other' permanent identification must meet requirements";
              hasError = true;
            }
          }
          if (hasError === true) {
            return true;
          }
        }

        // termsAndConditions
        if (
          !this.$store.getters["termsAndConditions/hasAgreed"] &&
          this.$props.formType === "review"
        ) {
          this.error = "Please accept the terms and conditions to continue";
          return true;
        }
        return false;
      }
    }
  }
};
</script>