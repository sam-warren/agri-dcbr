<template>
  <v-container grid-list-md text-xs-center>
    <v-layout row wrap>
      <v-flex>
        <v-card-title primary-title>
          <div>
            <h2>Breeding Details</h2>
          </div>
        </v-card-title>

        <v-card flat>
          <Cats v-if="this.animalType != 'DOG'"/>
          <Dogs v-if="this.animalType != 'CAT'"/>
          <!-- <Breeder /> -->
          <!-- <Seller /> -->
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import Seller from "@/components/Breeding/Seller";
import Breeder from "@/components/Breeding/Breeder";
import Cats from "@/components/Breeding/Cats";
import Dogs from "@/components/Breeding/Dogs";

export default {
  components: {
    Seller,
    Breeder,
    Cats,
    Dogs
  },
  computed: {
    animalType: {
      // getter
      get() {
        return this.$store.getters["operationDetails/animalType"]
      },
    }
  }
};
</script>