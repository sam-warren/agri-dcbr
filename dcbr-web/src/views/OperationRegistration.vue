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
          @click="createOperator()"
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
      errors: [],
    };
  },
  methods: {
    createOperator() {
      console.log("Submit clicked");
      let addresses = [ 
        {
          type: "PRI",
          street_num: this.$store.getters["profile/streetNumber"], 
          suite: this.$store.getters["profile/aptNumber"],
          street_name: this.$store.getters["profile/streetName"],
          city: this.$store.getters["profile/city"],
          postal_code: this.$store.getters["profile/postalCode"]
        },
      ];
      this.$store.getters["operationLocations/locations"].forEach((location) => {
        addresses.push({
          type: "OPN",
          street_num: location.streetNumber,
          suite: location.aptNumber,
          street_name: location.streetName,
          city: location.city,
          postal_code: location.postalCode
        });
      });
      let obj = {
        first_name: this.$store.getters["profile/firstName"],
        middle_name: this.$store.getters["profile/middleName"],
        last_name: this.$store.getters["profile/lastName"],
        comm_pref: this.$store.getters["profile/commType"],
        phone_num: this.$store.getters["profile/phone"],
        email_address: this.$store.getters["profile/email"],
        operation_type: this.$store.getters["operationDetails/operationType"],
        operation_name: this.$store.getters["operationDetails/operationName"],
        operation_URL: this.$store.getters["operationDetails/opWebsite"],

        addresses: addresses,
        associations: [
          {
            assoc_name: this.$store.getters["operationDetails/assocName"],
            membership_num: this.$store.getters["operationDetails/assocMembership"],
            assoc_URL: this.$store.getters["operationDetails/assocWebsite"]
          }
        ],
        risk_factor_animals: [
          {
            num_dogs_intact: this.$store.getters["breedingDetails/femaleIntactDogNum"],
            num_litter_whelped: this.$store.getters["breedingDetails/littersWhelped"],
            num_cats_intact: this.$store.getters["breedingDetails/femaleIntactCatNum"],
            num_litter_queened: this.$store.getters["breedingDetails/littersQueened"],
            num_dog_sold: this.$store.getters["breedingDetails/dogsSold"],
            num_dog_transferred: this.$store.getters["breedingDetails/dogsTransferred"],
            num_dog_traded: this.$store.getters["breedingDetails/dogsTraded"],
            num_dog_leased: this.$store.getters["breedingDetails/dogsLeased"],
            num_cat_sold: this.$store.getters["breedingDetails/catsSold"],
            num_cat_transferred: this.$store.getters["breedingDetails/catsTransferred"],
            num_cat_traded: this.$store.getters["breedingDetails/catsTraded"],
            num_cat_leased: this.$store.getters["breedingDetails/catsLeased"]
          }
        ],
        risk_factor_operations: [
          {
            accidental_breeding: this.$store.getters["breedingDetails/accidentalBreeding"],
            num_workers: this.$store.getters["breedingDetails/numWorkers"],
            animal_type: this.$store.getters["breedingDetails/animalType"],
            num_breeds_dogs: this.$store.getters["breedingDetails/numDogBreeds"],
            num_breeds_cats: this.$store.getters["breedingDetails/numCatBreeds"],
            has_vet: this.$store.getters["breedingDetails/hasVet"],
            has_perm_id: this.$store.getters["animalIdentification/hasPermId"],
            perm_id_type: this.$store.getters["animalIdentification/permIdType"],
            perm_id_other: this.$store.getters["animalIdentification/otherPermIdType"]
          }
        ]
      };
      console.log(obj);
      axios
        .post("/api/operator/", obj)
        .then(response => {console.log(response)})
        .catch(e => {
          this.errors.push(e);
        });
      this.$router.push("payment");
    },
  },
};
</script>

