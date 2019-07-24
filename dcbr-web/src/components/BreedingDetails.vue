<template>
  <v-container grid-list-md text-xs-center>
    <v-layout row wrap>
      <v-card-title primary-title>
        <div>
          <h2>Breeding Details</h2>
        </div>
      </v-card-title>
      <v-flex xs12>
        <v-card flat>
          <v-form v-model="valid">
            <v-container>
              <!-- INTACT BREEDING DOG -->
              <v-layout mx-2 mt-4>
                <subheader>How many intact breeding female dogs over the age of eight months do you have?</subheader>
              </v-layout>

              <v-layout row wrap ma-2>
                <v-flex xs12 md4>
                  <v-text-field
                    v-model.number="femaleIntactDogNum"
                    type="number"
                    label="Number of Female Dogs"
                    name="femaleIntactDogNum"
                  ></v-text-field>
                </v-flex>
              </v-layout>
              <!-- INTACT BREEDING CAT -->
              <v-layout mx-2 mt-4>
                <subheader>How many intact breeding female cats over the age of xxxx months do you have?</subheader>
              </v-layout>

              <v-layout row wrap ma-2>
                <v-flex xs12 md4>
                  <v-text-field
                    v-model.number="femaleIntactCatNum"
                    type="number"
                    label="Number of Female Cats"
                    name="femaleIntactCatNum"
                  ></v-text-field>
                </v-flex>
              </v-layout>
              <!-- Type of Animal -->
              <v-layout mx-2 mt-4>
                <subheader>How many litters were whelped in one calendar year overall (all female dogs combined)?</subheader>
              </v-layout>

              <v-layout row wrap ma-2>
                <v-flex xs12 md4>
                  <v-text-field
                    v-model.number="littersWhelped"
                    type="number"
                    label="Whelped Litters"
                    name="littersWhelped"
                  ></v-text-field>
                </v-flex>
              </v-layout>
              <!-- Type of Animal -->
              <v-layout mx-2 mt-4>
                <subheader>How many litters were queened in one calendar year overall (all female cats combined)?</subheader>
              </v-layout>

              <v-layout row wrap ma-2>
                <v-flex xs12 md4>
                  <v-text-field
                    v-model.number="littersQueened"
                    type="number"
                    label="Queened Litters"
                    name="littersQueened"
                  ></v-text-field>
                </v-flex>
              </v-layout>

              <v-layout mx-2 mt-4>
                <subheader>What number of puppies did you ............... in the previous calendar year?</subheader>
              </v-layout>

              <v-layout row wrap ma-2>
                <v-flex xs12 md4>
                  <v-text-field
                    v-model.number="dogsTransferred"
                    type="number"
                    label="Transfer"
                    name="dogsTransferred"
                  ></v-text-field>
                </v-flex>
                <v-flex xs12 md4>
                  <v-text-field
                    v-model.number="dogsSold"
                    type="number"
                    label="Sell"
                    name="dogsSold"
                  ></v-text-field>
                </v-flex>
                <v-flex xs12 md4>
                  <v-text-field
                    v-model.number="dogsTraded"
                    type="number"
                    label="Trade"
                    name="dogsTraded"
                  ></v-text-field>
                </v-flex>
                <v-flex xs12 md4>
                  <v-text-field
                    v-model.number="dogsLeased"
                    type="number"
                    label="Lease"
                    name="dogsLeased"
                  ></v-text-field>
                </v-flex>
              </v-layout>
              <v-layout mx-2 mt-4>
                <subheader>What numnber of kittens did you ............... in the previous calendar year?</subheader>
              </v-layout>

              <v-layout row wrap ma-2>
                <v-flex xs12 md4>
                  <v-text-field
                    v-model.number="catsTransferred"
                    type="number"
                    label="Transfer"
                    name="catsTransferred"
                  ></v-text-field>
                </v-flex>
                <v-flex xs12 md4>
                  <v-text-field
                    v-model.number="catsSold"
                    type="number"
                    label="Sell"
                    name="catsSold"
                  ></v-text-field>
                </v-flex>
                <v-flex xs12 md4>
                  <v-text-field
                    v-model.number="catsTraded"
                    type="number"
                    label="Trade"
                    name="catsTraded"
                  ></v-text-field>
                </v-flex>
                <v-flex xs12 md4>
                  <v-text-field
                    v-model.number="catsLeased"
                    type="number"
                    label="Lease"
                    name="catsLeased"
                  ></v-text-field>
                </v-flex>
              </v-layout>
            </v-container>
          </v-form>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
import { mapState } from "vuex";

export default {
  data: () => ({
    valid: false,

    nameRules: [
      v => !!v || "Name is required",
      v => v.length <= 50 || "Name must be less than 50 characters"
    ],

    emailRules: [
      v => !!v || "E-mail is required",
      v => /.+@.+/.test(v) || "E-mail must be valid"
    ]
  }),

  computed: {
    femaleIntactDogNum: {
      // getter
      get() {
        return this.$store.getters.femaleIntactDogNum;
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("femaleIntactDogNum", value);
      }
    },

    femaleIntactCatNum: {
      // getter
      get() {
        return this.$store.getters.femaleIntactCatNum;
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("femaleIntactCatNum", value);
      }
    },
    littersWhelped: {
      // getter
      get() {
        return this.$store.getters.littersWhelped;
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("littersWhelped", value);
      }
    },

    littersQueened: {
      // getter
      get() {
        return this.$store.getters.littersQueened;
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("littersQueened", value);
      }
    },
    dogsTransferred: {
      // getter
      get() {
        return this.$store.getters.dogsTransferred;
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("dogsTransferred", value);
      }
    },
    dogsSold: {
      // getter
      get() {
        return this.$store.getters.dogsSold;
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("dogsSold", value);
      }
    },
    dogsTraded: {
      // getter
      get() {
        return this.$store.getters.dogsTraded;
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("dogsTraded", value);
      }
    },
    dogsLeased: {
      // getter
      get() {
        return this.$store.getters.dogsLeased;
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("dogsLeased", value);
      }
    },
    catsTransferred: {
      // getter
      get() {
        return this.$store.getters.catsTransferred;
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("catsTransferred", value);
      }
    },
    catsSold: {
      // getter
      get() {
        return this.$store.getters.catsSold;
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("catsSold", value);
      }
    },
    catsTraded: {
      // getter
      get() {
        return this.$store.getters.catsTraded;
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("catsTraded", value);
      }
    },
    catsLeased: {
      // getter
      get() {
        return this.$store.getters.catsLeased;
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("catsLeased", value);
      }
    }
  }
};
</script>
