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
          <!-- INTACT BREEDING CAT -->
          <v-layout mx-2 mt-4>
            <v-subheader>How many intact breeding female cats over the age of xxxx months do you have?</v-subheader>
          </v-layout>

          <v-layout row wrap ma-2>
            <v-flex xs12 md4>
              <v-text-field
                v-model.number="femaleIntactCatNum"
                type="number"
                label="Number of Female Cats"
              ></v-text-field>
            </v-flex>
          </v-layout>
          <!-- Type of Animal -->
          <v-layout mx-2 mt-4>
            <v-subheader>How many litters were queened in one calendar year overall (all female cats combined)?</v-subheader>
          </v-layout>

          <v-layout row wrap ma-2>
            <v-flex xs12 md4>
              <v-text-field v-model.number="littersQueened" type="number" label="Queened Litters"></v-text-field>
            </v-flex>
          </v-layout>

          <v-layout mx-2 mt-4>
            <v-subheader>What numnber of kittens did you ............... in the previous calendar year?</v-subheader>
          </v-layout>

          <v-layout row wrap ma-2>
            <v-flex xs12 md4>
              <v-text-field v-model.number="catsTransferred" type="number" label="Transfer"></v-text-field>
            </v-flex>
            <v-flex xs12 md4>
              <v-text-field v-model.number="catsSold" type="number" label="Sell"></v-text-field>
            </v-flex>
            <v-flex xs12 md4>
              <v-text-field v-model.number="catsTraded" type="number" label="Trade"></v-text-field>
            </v-flex>
            <v-flex xs12 md4>
              <v-text-field v-model.number="catsLeased" type="number" label="Lease"></v-text-field>
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
    }
  }
};
</script>