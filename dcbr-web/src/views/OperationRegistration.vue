<template>
  <v-app class="grey lighten-4">
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
        <!-- <v-btn @click="prepopulate()">
          <v-btn-text>prepopulate</v-btn-text>
          <v-icon dark>add</v-icon>
        </v-btn>-->

        <v-stepper non-linear v-model="e6" vertical>
          <v-stepper-step editable :complete="e6 > 1" step="1">Profile</v-stepper-step>
          <v-stepper-content step="1">
            <Profile ref="profile" />
          </v-stepper-content>

          <v-stepper-step editable :complete="e6 > 2" step="2">Operation Details</v-stepper-step>
          <v-stepper-content step="2">
            <OperationDetails ref="operationdetails" />
          </v-stepper-content>

          <v-stepper-step editable :complete="e6 > 3" step="3">Operation Locations</v-stepper-step>

          <v-stepper-content step="3">
            <v-layout mt-4>
              <subheader>Do you have additional operation locations?</subheader>
            </v-layout>
            <v-radio-group v-model="row" row>
              <v-radio label="Yes" value="radio-1"></v-radio>
              <v-radio label="No" value="radio-2"></v-radio>
            </v-radio-group>
            <!-- <OperationLocation ref="operationlocation" /> -->
            <v-card-title primary-title>
              <h2>Operation Location(s)</h2>
            </v-card-title>

            <!-- <div v-for="(child, index) in children">
              <component :is="child" :key="child.name" v-bind:number="index+1"></component>
            </div>-->

            <div v-for="(location, index) in locations">
              <OperationLocation ref="operationlocation1" v-bind:number="index+1" />
            </div>

            <v-btn @click="addLocation()">
              <v-btn-text>Add</v-btn-text>
              <v-icon dark>add</v-icon>
            </v-btn>

            <v-btn @click="removeLocation()">
              <v-btn-text>Remove</v-btn-text>
              <v-icon dark>remove</v-icon>
            </v-btn>
          </v-stepper-content>

          <v-stepper-step editable :complete="e6 > 4" step="4">Animal Identification</v-stepper-step>
          <AnimalIdentification ref="animalidentification" />

          <v-stepper-step editable :complete="e6 > 5" step="5">Breeding Details</v-stepper-step>
          <BreedingDetails ref="breedingdetails" />
        </v-stepper>

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
  </v-app>
</template>


<script>
import OperationDetails from "@/components/OperationDetails";
import Profile from "@/components/Profile";
import OperationLocation from "@/components/OperationLocation";
import AnimalIdentification from "@/components/AnimalIdentification";
import BreedingDetails from "@/components/BreedingDetails";
//import Footer from "@/components/Footer";
import axios from "axios";

export default {
  name: "App",
  components: {
    Profile,
    OperationDetails,
    OperationLocation,
    AnimalIdentification,
    BreedingDetails
  },
  data() {
    return {
      e6: 1,
      errors: [],
      locations: []
    };
  },
  methods: {
    createOperator() {
      console.log("Submit clicked");

      axios
        .post("http://localhost:8080/api/operator/", {
          // for localhost, use "http://localhost:8080/api/operator"
          // before deploying to Openshift, use "/api/operator"
          first_name: this.$store.getters.firstName,
          middle_name: this.$store.getters.middleName,
          last_name: this.$store.getters.lastName,
          comm_pref: this.$store.getters.commType,
          phone_num: this.$store.getters.phone,
          email_address: this.$store.getters.email,
          operation_type: this.$store.getters.operationType,
          operation_name: this.$store.getters.operationName,
          operation_URL: this.store.getters.opWebsite,

          addresses: [
            {
              type: "PRI",
              street_num: this.$store.getters.streetNumber,
              suite: this.$store.getters.aptNumber,
              street_name: this.$store.getters.streetName,
              city: this.$store.getters.city,
              postal_code: this.$store.getters.postalCode
            }
          ],
          associations: [
            {
              assoc_name: this.$store.getterss.assocName,
              membership_num: this.$store.getters.assocMembership,
              assoc_URL: this.$store.getters.assocWebsite
            }
          ],
          risk_factor_animals: [
            {
              num_dogs_intact: this.$store.getters.femaleIntactDogNum,
              num_litter_whelped: this.$store.getters.littersWhelped,
              num_cats_intact: this.$store.getters.femaleIntactCatNum,
              num_litter_queened: this.$store.getters.littersQueened,
              num_dog_sold: this.$store.getters.dogsSold,
              num_dog_transferred: this.$store.getters.dogsTransferred,
              num_dog_traded: this.$store.getters.dogsTraded,
              num_dog_leased: this.$store.getters.dogsLeased,
              num_cat_sold: this.$store.getters.catsSold,
              num_cat_transferred: this.$store.getters.catsTransferred,
              num_cat_traded: this.$store.getters.catsTraded,
              num_cat_leased: this.$store.getterss.catsLeased,
            }
          ],
          risk_factor_operations: [
            {
              accidental_breeding: this.$store.getters.accidentalBreeding,
              num_workers: this.$store.getters.numWorkers,
              animal_type: this.$store.getters.animalType,
              num_breeds_dogs: this.$store.getters.numDogBreeds,
              num_breeds_cats: this.$store.getters.numCatBreeds,
              has_vet: this.$store.getters.hasVet,
              has_perm_id: this.$store.getters.hasPermId,
              perm_id_type: this.$store.getters.permIdType,
              perm_id_other: this.$store.getters.otherPermIdType
            }
          ]
        })
        .then(response => {})
        .catch(e => {
          this.errors.push(e);
        });
      this.$router.push("payment");
    },
    addLocation() {
      this.locations.push(OperationLocation);
    },
    removeLocation() {
      this.locations.pop();
    }
  }
};
</script>

