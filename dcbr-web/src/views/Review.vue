<template>
  <v-container grid-list-md text-xs-center>
    <v-layout row wrap>

    </v-layout>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      first_name: this.$store.getters["profile/firstName"],
      middle_name: this.$store.getters["profile/middleName"],
      last_name: this.$store.getters["profile/lastName"],
      comm_pref: this.$store.getters["profile/commType"],
      phone_num: this.$store.getters["profile/phone"],
      personal_email_address: this.$store.getters["profile/email"],
      operation_type: this.$store.getters["operationDetails/operationType"],
      operation_name: this.$store.getters["operationDetails/operationName"],
      operation_URL: this.$store.getters["operationDetails/opWebsite"],
      assoc_name: this.$store.getters["operationDetails/assocName"],
      membership_num: this.$store.getters["operationDetails/assocMembership"],
      assoc_URL: this.$store.getters["operationDetails/assocWebsite"],
      animal_type: this.$store.getters["breedingDetails/animalType"],
      num_dog_breeds: this.$store.getters["breedingDetails/numDogBreeds"],
      num_dog_females_intact: this.$store.getters["breedingDetails/femaleIntactDogNum"],
      num_litter_whelped: this.$store.getters["breedingDetails/littersWhelped"],
      num_dogs_sold: this.$store.getters["breedingDetails/dogsSold"],
      num_dogs_transferred: this.$store.getters["breedingDetails/dogsTransferred"],
      num_dogs_traded: this.$store.getters["breedingDetails/dogsTraded"],
      num_dogs_leased: this.$store.getters["breedingDetails/dogsLeased"],
      num_cat_breeds: this.$store.getters["breedingDetails/numCatBreeds"],
      num_cat_females_intact: this.$store.getters["breedingDetails/femaleIntactCatNum"],
      num_litter_queened: this.$store.getters["breedingDetails/littersQueened"],
      num_cats_sold: this.$store.getters["breedingDetails/catsSold"],
      num_cats_transferred: this.$store.getters["breedingDetails/catsTransferred"],
      num_cats_traded: this.$store.getters["breedingDetails/catsTraded"],
      num_cats_leased: this.$store.getters["breedingDetails/catsLeased"],
      has_additional_locations: this.$store.getters["operationLocations/hasAdditionalLocations"],
      operation_locations: this.$store.getters["operationLocations/locations"],
    };
  },
  computed: {
  },
  methods: {
  }
};
</script>