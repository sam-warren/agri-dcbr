<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">AGRI site</router-link>|
      <router-link to="/preamble">Preamble</router-link>|
      <router-link to="/register">Registration</router-link>|
      <router-link to="/payment">Payment</router-link>|
      <router-link to="/review">Review</router-link>|
      <router-link to="/confirmation">Confirmation</router-link>
      <br>
      <br>
      <!-- <button @click="$keycloak.logoutFn" v-if="$keycloak.authenticated">Log out</button> -->
    </div>
    <router-view/>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar";
import OperationDetails from "@/components/OperationDetails";
import Profile from "@/components/Profile";
import OpLocation from "@/components/OpLocation";
import OpLocation2 from "@/components/OpLocation2";
import AnimalIdentification from "@/components/AnimalIdentification";
import BreedingDetails from "@/components/BreedingDetails";
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
    AnimalIdentification,
    BreedingDetails,
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
        .post("/api/operator/", {
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
              num_dogs_intact: this.$refs.breedingdetails.femaleDogNum,
              num_litter_whelped: this.$refs.breedingdetails.littersWhelped,
              num_cats_intact: this.$refs.breedingdetails.femaleIntactCat,
              num_litter_queened: this.$refs.breedingdetails.littersQueened,
              num_dog_sold: this.$refs.breedingdetails.dogsSold,
              num_dog_transferred: this.$refs.breedingdetails.dogsTransferred,
              num_dog_traded: this.$refs.breedingdetails.dogsTraded,
              num_dog_leased: this.$refs.breedingdetails.dogsLeased,
              num_cat_sold: this.$refs.breedingdetails.catsSold,
              num_cat_transferred: this.$refs.breedingdetails.catsTransferred,
              num_cat_traded: this.$refs.breedingdetails.catsTraded,
              num_cat_leased: this.$refs.breedingdetails.catsLeased
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
              has_perm_id: this.$refs.animalidentification.hasId,
              perm_id_type: this.$refs.animalidentification.idType,
              perm_id_other: this.$refs.animalidentification.otherId
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
<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
}
#nav a {
  font-weight: bold;
  color: #2c3e50;
}
#nav a.router-link-exact-active {
  color: #42b983;
}
</style>