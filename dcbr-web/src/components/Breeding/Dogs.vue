<template>
  <v-form v-model="valid">
    <v-container grid-list-md text-xs-center>
      <v-layout row wrap>
        <v-flex>
          <v-card-title primary-title>
            <v-layout>
              <h4>Dog Breeder</h4>
            </v-layout>
          </v-card-title>
          <v-card flat>
            <v-layout mx-2 mt-4>
              <v-subheader>What is the approximate total number of dogs at your establishment?</v-subheader>
            </v-layout>
            
            <v-layout row wrap ma-2>
              <v-flex xs12 md4>
                <v-text-field v-model.number="numDogs" mask="#########" :rules="numberRules" label="Number of Dogs"></v-text-field>
              </v-flex>
            </v-layout>
            <!-- INTACT BREEDING DOG -->
            <v-layout mx-2 mt-4>
              <v-subheader>How many intact breeding female dogs over the age of eight months do you have at your operation(s)?</v-subheader>
            </v-layout>

            <v-layout row wrap ma-2>
              <v-flex xs12 md4>
                <v-text-field
                  v-model.number="femaleIntactDogNum"
                  mask="#########"
                  :rules="numberRules"
                  label="Number of Female Dogs"
                ></v-text-field>
              </v-flex>
            </v-layout>
            <!-- Type of Animal -->
            <v-layout mx-2 mt-4>
              <v-subheader>Over the past 12 months, how many litters were whelped in your operation(s)?</v-subheader>
            </v-layout>

            <v-layout row wrap ma-2>
              <v-flex xs12 md4>
                <v-text-field v-model.number="littersWhelped" mask="#########" :rules="numberRules" label="Whelped Litters"></v-text-field>
              </v-flex>
            </v-layout>

            <v-layout mx-2 mt-4>
              <v-subheader>Over the past 12 months, how many puppies did your operation …………?</v-subheader>
            </v-layout>

            <v-layout row wrap ma-2>
              <v-flex xs12 md4>
                <v-text-field v-model.number="dogsTransferred" mask="#########" :rules="numberRules" label="Transfer"></v-text-field>
              </v-flex>
              <v-flex xs12 md4>
                <v-text-field v-model.number="dogsSold" mask="#########" :rules="numberRules" label="Sell"></v-text-field>
              </v-flex>
              <v-flex xs12 md4>
                <v-text-field v-model.number="dogsTraded" mask="#########" :rules="numberRules" label="Trade"></v-text-field>
              </v-flex>
              <v-flex xs12 md4>
                <v-text-field v-model.number="dogsLeased" mask="#########" :rules="numberRules" label="Lease"></v-text-field>
              </v-flex>
            </v-layout>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-form>
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
    femaleIntactDogNum: {
      // getter
      get() {
        return this.$store.getters["breedingDetails/femaleIntactDogNum"] || "";
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("breedingDetails/femaleIntactDogNum", value);
      }
    },
    littersWhelped: {
      // getter
      get() {
        return this.$store.getters["breedingDetails/littersWhelped"] || "";
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("breedingDetails/littersWhelped", value);
      }
    },
    dogsTransferred: {
      // getter
      get() {
        return this.$store.getters["breedingDetails/dogsTransferred"] || "";
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("breedingDetails/dogsTransferred", value);
      }
    },
    dogsSold: {
      // getter
      get() {
        return this.$store.getters["breedingDetails/dogsSold"] || "";
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("breedingDetails/dogsSold", value);
      }
    },
    dogsTraded: {
      // getter
      get() {
        return this.$store.getters["breedingDetails/dogsTraded"] || "";
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("breedingDetails/dogsTraded", value);
      }
    },
    dogsLeased: {
      // getter
      get() {
        return this.$store.getters["breedingDetails/dogsLeased"] || "";
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("breedingDetails/dogsLeased", value);
      }
    },
    numDogs: {
      // getter
      get() {
        return this.$store.getters["breedingDetails/numDogs"] || "";
      },
      // setter
      set(value) {
        console.log(value)
        this.$store.dispatch("breedingDetails/numDogs", value);
      }
    }
  }
};
</script>