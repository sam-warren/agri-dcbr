<template>
  <v-app class="grey lighten-4">
    <Navbar/>
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
        <v-stepper non-linear v-model="e6" vertical>
          <v-stepper-step editable :complete="e6 > 1" step="1">Profile</v-stepper-step>

          <v-stepper-content step="1">
            <Profile ref="profile"/>
          </v-stepper-content>

          <v-stepper-step editable :complete="e6 > 2" step="2">Operation Details</v-stepper-step>

          <v-stepper-content step="2">
            <OperationDetails ref="operationdetails"/>
          </v-stepper-content>

          <v-stepper-step editable :complete="e6 > 3" step="3">Operation Location(s)</v-stepper-step>

          <v-stepper-content step="3">
            <v-layout mt-4>
              <subheader>Is your operation location(s) different than your home address?</subheader>
            </v-layout>
            <v-radio-group v-model="row" row>
              <v-radio label="Yes" value="radio-1"></v-radio>
              <v-radio label="No" value="radio-2"></v-radio>
            </v-radio-group>
            <OpLocation/>
            <OpLocation2/>
          </v-stepper-content>

          <!-- <v-stepper-step editable :complete="e6 > 4" step="4">Veterinary Relationship</v-stepper-step>
          <v-stepper-content step="4">
            
            <Vet/>
          </v-stepper-content>-->

          <v-stepper-step editable :complete="e6 > 4" step="4">Animal Identification</v-stepper-step>
          <v-stepper-content step="4">
            <PetId/>
          </v-stepper-content>
          <v-stepper-step editable :complete="e6 > 5" step="5">Breeding Details</v-stepper-step>
          <v-stepper-content step="5">
            <Breeding/>
          </v-stepper-content>
        </v-stepper>

        <v-btn
          large
          block
          round
          mt-5
          class="blue darken-4 white--text"
          @click.native="createOperator"
        >Next</v-btn>
      </v-container>
    </v-content>
    <Footer/>
  </v-app>
</template>

<script>
import Navbar from "@/components/Navbar";
import OperationDetails from "@/components/OperationDetails";
import Profile from "@/components/Profile";
import OpLocation from "@/components/OpLocation";
import OpLocation2 from "@/components/OpLocation2";
// import Vet from "@/components/Vet";
import PetId from "@/components/PetId";
import Breeding from "@/components/Breeding";
import Footer from "@/components/Footer";
import axios from "axios";

export default {
  name: "App",
  components: {
    Navbar,
    Profile,
    OperationDetails,
    OpLocation,
    OpLocation2,
    // Vet,
    PetId,
    Breeding,
    Footer
  },
  data() {
    return {
      e6: 1,
      errors: []
    };
  },
  methods: {
    createOperator() {
      console.log("Next clicked");
      axios
        .post(`http://localhost:8080/api/operator/`, {
          first_name: this.$refs.profile.firstname,
          middle_name: this.$refs.profile.middlename,
          last_name: this.$refs.profile.lastname,
          comm_pref: this.$refs.profile.commType,
          phone_num: this.$refs.profile.phone,
          email_address: this.$refs.profile.email,
          operation_type: this.$refs.operationdetails.operationType,
          operation_name: this.$refs.operationdetails.operationName,
          operation_URL: this.$refs.operationdetails.opWebsite,

          addresses: [
            {
              type: "PRI",
              street_num: this.$refs.profile.streetNumber,
              suite: this.$refs.profile.aptNumber,
              street_name: this.$refs.profile.streetName,
              city: this.$refs.profile.city,
              postal_code: this.$refs.profile.postalCode
            }
          ],
          associations: [
            {
              assoc_name: this.$refs.operationdetails.assocName,
              membership_num: this.$refs.operationdetails.assocMembership,
              assoc_URL: this.$refs.operationdetails.assocWebsite
            }
          ],
          risk_factor_animals: [
            {
              num_dogs_intact: 0,
              num_litter_whelped: 0,
              num_cats_intact: 0,
              num_litter_queened: 0,
              num_sold: 0,
              num_transferred: 0,
              num_traded: 0,
              num_leased: 0
            }
          ],
          risk_factor_operations: [
            {
              accidental_breeding: this.$refs.operationdetails.accident,
              num_workers: this.$refs.operationdetails.numWorkers,
              animal_type: this.$refs.operationdetails.animalType,
              num_breeds_dogs: this.$refs.operationdetails.numDogBreeds,
              num_breeds_cats: this.$refs.operationdetails.numCatBreeds,
              has_vet: this.$refs.operationdetails.hasVet,
              has_perm_id: true,
              perm_id_type: "TATTOO",
              perm_id_other: "string"
            }
          ]
        })
        .then(response => {})
        .catch(e => {
          this.errors.push(e);
        });
    }
  }
};
</script>