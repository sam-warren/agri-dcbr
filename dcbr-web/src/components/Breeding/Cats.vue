<template>
  <v-container grid-list-md text-xs-center>
    <v-layout row wrap>
      <v-flex>
        <v-card-title primary-title>
          <v-layout>
            <h4>Cat Breeder</h4>
          </v-layout>
        </v-card-title>
        <v-card flat>
          <v-layout mx-2 mt-4>
            <v-subheader>What is the approximate total number of cats at your establishment?</v-subheader>
          </v-layout>
          
          <v-layout row wrap ma-2>
            <v-flex xs12 md4>
              <v-text-field v-model.number="numCats" :rules="numberRules" type="number" label="Number of Cats"></v-text-field>
            </v-flex>
          </v-layout>

          <!-- INTACT BREEDING CAT -->
          <v-layout mx-2 mt-4>
            <v-subheader>How many intact breeding female cats over the age of five months do you have at your operation(s)?</v-subheader>
          </v-layout>

          <v-layout row wrap ma-2>
            <v-flex xs12 md4>
              <v-text-field
                v-model.number="femaleIntactCatNum"
                :rules="numberRules"
                type="number"
                label="Number of Female Cats"
              ></v-text-field>
            </v-flex>
          </v-layout>
          <!-- Type of Animal -->
          <v-layout mx-2 mt-4>
            <v-subheader>Over the past 12 months, how many litters were queened in your operation(s)?</v-subheader>
          </v-layout>

          <v-layout row wrap ma-2>
            <v-flex xs12 md4>
              <v-text-field v-model.number="littersQueened" :rules="numberRules" type="number" label="Queened Litters"></v-text-field>
            </v-flex>
          </v-layout>

          <v-layout mx-2 mt-4>
            <v-subheader>Over the past 12 months, how many kittens did your operation …………?</v-subheader>
          </v-layout>

          <v-layout row wrap ma-2>
            <v-flex xs12 md4>
              <v-text-field v-model.number="catsTransferred" :rules="numberRules" type="number" label="Transfer"></v-text-field>
            </v-flex>
            <v-flex xs12 md4>
              <v-text-field v-model.number="catsSold" :rules="numberRules" type="number" label="Sell"></v-text-field>
            </v-flex>
            <v-flex xs12 md4>
              <v-text-field v-model.number="catsTraded" :rules="numberRules" type="number" label="Trade"></v-text-field>
            </v-flex>
            <v-flex xs12 md4>
              <v-text-field v-model.number="catsLeased" :rules="numberRules" type="number" label="Lease"></v-text-field>
            </v-flex>
          </v-layout>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    valid: false,
    numberRules: [
      v => v >= 0 || "Number cannot be negative",
      v => v <= 2147483647 || "Number must be less than 2147483647"
    ],
  }),
  computed: {
    femaleIntactCatNum: {
      // getter
      get() {
        return this.$store.getters["breedingDetails/femaleIntactCatNum"] || "";
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("breedingDetails/femaleIntactCatNum", value);
      }
    },
    littersQueened: {
      // getter
      get() {
        return this.$store.getters["breedingDetails/littersQueened"] || "";
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("breedingDetails/littersQueened", value);
      }
    },
    catsTransferred: {
      // getter
      get() {
        return this.$store.getters["breedingDetails/catsTransferred"] || "";
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("breedingDetails/catsTransferred", value);
      }
    },
    catsSold: {
      // getter
      get() {
        return this.$store.getters["breedingDetails/catsSold"] || "";
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("breedingDetails/catsSold", value);
      }
    },
    catsTraded: {
      // getter
      get() {
        return this.$store.getters["breedingDetails/catsTraded"] || "";
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("breedingDetails/catsTraded", value);
      }
    },
    catsLeased: {
      // getter
      get() {
        return this.$store.getters["breedingDetails/catsLeased"] || "";
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("breedingDetails/catsLeased", value);
      }
    },
    numCats: {
      // getter
      get() {
        return this.$store.getters["breedingDetails/numCats"] || "";
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("breedingDetails/numCats", value);
      }
    }
  }
};
</script>