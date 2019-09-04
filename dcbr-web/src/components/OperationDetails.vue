<template>
  <v-container grid-list-md text-xs-center>
    <v-layout row wrap>
      <v-card-title primary-title>
        <div>
          <h2>Operation Details</h2>
        </div>
      </v-card-title>
      <v-flex xs12>
        <v-card flat>
          <v-form v-model="valid">
            <v-container>
              <!--OPERATION DETAILS-NAME  -->
              <v-layout mx-2 mt-4>
                <v-subheader>Does your operation run under a specific name? i.e "business name" (Optional)</v-subheader>
              </v-layout>
              <v-layout row wrap mx-2>
                <v-flex xs12 md4 mr-5>
                  <v-text-field v-model="operationName" :rules="notRequiredNameRules" label="Operation Name" name="operationName" counter=50></v-text-field>
                </v-flex>

                <v-flex xs12 md4>
                  <v-text-field v-model="opWebsite" :rules="websiteRules" label="Link to your Website " name="opWebsite"></v-text-field>
                </v-flex>
              </v-layout>
              <!-- Type of Operator -->
              <v-layout mx-2 mt-4>
                <v-subheader>What type of operator are you?</v-subheader>
              </v-layout>
              <v-layout mx-2>
                <v-radio-group v-model="operationType" name="operationType" row>
                  <!-- <v-radio label="Breeder" value="BREEDER" id="BREEDER"></v-radio> -->
                  <v-radio label="Breeder" value="BREEDER"></v-radio>
                  <v-radio label="Seller" value="SELLER"></v-radio>
                  <v-radio label="Breeder & Seller" value="BREEDER&SELLER"></v-radio>
                </v-radio-group>
              </v-layout>
              <!-- Type of Animal -->
              <v-layout mx-2 mt-4>
                <v-subheader>What type of animal do you work with?</v-subheader>
              </v-layout>
              <v-layout mx-2>
                <v-radio-group v-model="animalType" row>
                  <v-radio label="Dogs" value="DOG"></v-radio>
                  <v-radio label="Cats" value="CAT"></v-radio>
                  <v-radio label="Dogs&Cats" value="DOG&CAT"></v-radio>
                </v-radio-group>
              </v-layout>
              <!-- ACCIDENTAL BREEDING -->
              <v-layout mx-2 mt-4>
                <v-subheader>Over the past calendar year, did you have an accidental breeding?</v-subheader>
              </v-layout>
              <v-layout mx-2>
                <v-radio-group v-model="accidentalBreeding" name="accidentalBreeding" row>
                  <v-radio label="Yes" value="true"></v-radio>
                  <v-radio label="No" value="false"></v-radio>
                </v-radio-group>
              </v-layout>
              <!-- VET RELATIONSHIP -->
              <v-layout mx-2 mt-4>
                <v-subheader>Do you have a client veterinary relationship?</v-subheader>
              </v-layout>
              <v-layout mx-2>
                <v-radio-group v-model="hasVet" row>
                  <v-radio label="Yes" value="true"></v-radio>
                  <v-radio label="No" value="false"></v-radio>
                </v-radio-group>
              </v-layout>

              <!-- How many breeds -->
              <v-layout mx-2 mt-4>
                <v-subheader>How many breeds of animals are you currently breeding/selling?</v-subheader>
              </v-layout>
              <v-layout row wrap mx-2>
                <v-flex xs12 md4 lg6 v-if="this.animalType !== 'CAT'">
                  <v-text-field
                    v-model.number="numDogBreeds"
                    type="number"
                    :rules="numberRules"
                    label="Number of Dog Breeds"
                    name="numDogBreeds"
                  ></v-text-field>
                </v-flex>
                <v-flex xs12 md4 lg6 v-if="this.animalType !== 'DOG'">
                  <v-text-field
                    v-model.number="numCatBreeds"
                    type="number"
                    :rules="numberRules"
                    label="Number of Cat Breeds"
                    name="numCatBreeds"
                  ></v-text-field>
                </v-flex>
              </v-layout>
              <!-- NUMBER OF EMPLOYEES -->
              <v-layout mx-2 mt-4>
                <v-subheader>How many people are currently working in your operation including yourself?</v-subheader>
              </v-layout>
              <v-layout row wrap mx-2>
                <v-flex xs12 md4 lg6>
                  <v-text-field
                    v-model.number="numWorkers"
                    type="number"
                    :rules="numberRules"
                    label="Number of workers"
                    name="numWorkers"
                  ></v-text-field>
                </v-flex>
              </v-layout>
              <!--ASSOCIATION REALTION -->
              <v-layout mx-2 mt-4>
                <v-subheader>Are you a member of a relevant breeding or selling association? (Optional)</v-subheader>
              </v-layout>
              <v-layout row wrap ma-2>
                <v-flex xs12 md4>
                  <v-text-field v-model="assocName" :rules="notRequiredNameRules" label="Association Name" name="assocName" counter=50></v-text-field>
                </v-flex>
                <v-flex xs12 md4>
                  <v-text-field
                    v-model="assocMembership"
                    :rules="membershipNumberRules"
                    label="Membership #"
                    name="assocMembership"
                    counter=20
                  ></v-text-field>
                </v-flex>
                <v-flex xs12 md4>
                  <v-text-field v-model="assocWebsite" :rules="websiteRules" label="Website " name="assocWebsite"></v-text-field>
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
    accidentalBreedingVisited: false,
    hasVetVisited: false,
    nameRules: [
      v => !!v || "Name is required",
      v => v.length <= 50 || "Name must be less than 50 characters"
    ],
    notRequiredNameRules: [
      v => v.length <= 50 || "Name must be less than 50 characters"
    ],
    emailRules: [
      v => !!v || "E-mail is required",
      v => /.+@.+/.test(v) || "E-mail must be valid"
    ],
    websiteRules: [
      v => /^(|https?:\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?)$/.test(v) || "URL must be valid",
      v => v.length <= 4000 || "Url must be less than 4000 characters"
    ],
    numberRules: [
      v => v >= 0 || "Number cannot be negative",
      v => v <= 2147483647 || "Number must be less than 2147483647"
    ],
    membershipNumberRules: [
      v => v.length <= 20 || "Membership number must be less than 20 characters"
    ],
  }),

  computed: {
    ...mapState({
      operationDetails: state => state.operationDetails
    }),
    operationName: {
      // getter
      get() {
        return this.$store.getters["operationDetails/operationName"];
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("operationDetails/operationName", value);
      }
    },

    operationType: {
      // getter
      get() {
        return this.$store.getters["operationDetails/operationType"];
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("operationDetails/operationType", value);
      }
    },
    opWebsite: {
      // getter
      get() {
        return this.$store.getters["operationDetails/opWebsite"];
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("operationDetails/opWebsite", value);
      }
    },
    assocName: {
      // getter
      get() {
        return this.$store.getters["operationDetails/assocName"];
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("operationDetails/assocName", value);
      }
    },
    assocMembership: {
      // getter
      get() {
        return this.$store.getters["operationDetails/assocMembership"] || "";
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("operationDetails/assocMembership", value);
      }
    },
    assocWebsite: {
      // getter
      get() {
        return this.$store.getters["operationDetails/assocWebsite"];
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("operationDetails/assocWebsite", value);
      }
    },
    accidentalBreeding: {
      // getter
      get() {
        return this.$store.getters["operationDetails/accidentalBreeding"];
      },
      // setter
      set(value) {
        this.$store.dispatch("operationDetails/accidentalBreeding", value);
      }
    },
    hasVet: {
      // getter
      get() {
        return this.$store.getters["operationDetails/hasVet"];
      },
      // setter
      set(value) {
        this.$store.dispatch("operationDetails/hasVet", value);
      }
    },
    numDogBreeds: {
      // getter
      get() {
        return this.$store.getters["operationDetails/numDogBreeds"] || "";
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("operationDetails/numDogBreeds", value);
      }
    },
    numCatBreeds: {
      // getter
      get() {
        return this.$store.getters["operationDetails/numCatBreeds"] || "";
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("operationDetails/numCatBreeds", value);
      }
    },
    numWorkers: {
      // getter
      get() {
        return this.$store.getters["operationDetails/numWorkers"] || "";
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("operationDetails/numWorkers", value);
      }
    },
    animalType: {
      // getter
      get() {
        return this.$store.getters["operationDetails/animalType"];
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("operationDetails/animalType", value);
        if (value === "DOG") {
          this.$store.dispatch("operationDetails/numCatBreeds", 0)
          this.$store.dispatch("breedingDetails/catsLeased", 0);
          this.$store.dispatch("breedingDetails/catsSold", 0);
          this.$store.dispatch("breedingDetails/catsTraded", 0);
          this.$store.dispatch("breedingDetails/catsTransferred", 0);
          this.$store.dispatch("breedingDetails/femaleIntactCatNum", 0);
          this.$store.dispatch("breedingDetails/littersQueened", 0);
        } else if (value === "CAT") {
          this.$store.dispatch("operationDetails/numDogBreeds", 0)
          this.$store.dispatch("breedingDetails/dogsLeased", 0);
          this.$store.dispatch("breedingDetails/dogsSold", 0);
          this.$store.dispatch("breedingDetails/dogsTraded", 0);
          this.$store.dispatch("breedingDetails/dogsTransferred", 0);
          this.$store.dispatch("breedingDetails/femaleIntactDogNum", 0);
          this.$store.dispatch("breedingDetails/littersWhelped", 0);
        }
      }
    }
  },
  methods: {}
};
</script>
 