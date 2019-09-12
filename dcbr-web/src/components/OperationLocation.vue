<template>
  <v-container grid-list-md text-xs-center>
    <v-layout row wrap>
      <!-- <v-card-title primary-title>
        <h2>Operation Location(s)</h2>
      </v-card-title>-->
      <v-flex xs12>
        <v-card flat>
          <v-form v-model="valid">
            <v-container>
              <!-- Home address section  -->

              <v-layout row mt-3 mx-2>
                <h4>Address {{number+1}}</h4>
              </v-layout>
              <v-layout row wrap mx-2>
                <v-flex xs12 md4>
                  <v-text-field
                    v-model="streetNumber"
                    :rules="streetNumberRules"
                    type="number"
                    label="Street number"
                    required
                  ></v-text-field>
                </v-flex>
                <v-flex xs12 md4 lg6>
                  <v-text-field v-model="aptNumber" :rules="suiteRules" label="Apt/Suite (optional)" counter=32 required></v-text-field>
                </v-flex>
                <v-flex xs12 md4>
                  <v-text-field
                    v-model="streetName"
                    :rules="streetNameRules"
                    label="Street name"
                    counter=32
                    required
                  ></v-text-field>
                </v-flex>
                <v-flex xs12 md4>
                  <v-text-field v-model="city" :rules="cityRules" label="City" counter=32 required></v-text-field>
                </v-flex>
                <v-flex xs12 md4>
                  <v-text-field
                    v-model="postalCode"
                    :rules="postalCodeRules"
                    label="Postal Code"
                    required
                  ></v-text-field>
                </v-flex>
                <v-flex xs12 md4>
                  <v-flex class="d-flex" cols="12" sm="6">
                    <v-select :rules="requiredRules" :items="items" v-model="region" label="Region"></v-select>
                  </v-flex>
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
import {mapState} from "vuex";
export default {
  props: ["number"],
  data: () => ({
    items: [
      "Alberni-Clayoquot",
      "Bulkley-Nechako",
      "Capital",
      "Cariboo",
      "Central Coast",
      "Central Kootenay",
      "Central Okanagan",
      "Columnbia Shuswap",
      "Comox Valley",
      "Cowichan Valley",
      "East Kootenay",
      "Fraser Valley",
      "Fraser-Fort George",
      "Islands Trust",
      "Kitimat Stikine",
      "Kootenay Boundary",
      "Metro Vancouver",
      "Mount Waddington",
      "Nanaimo",
      "North Okanagan",
      "North Coast",
      "Okanagan-Similkameen",
      "Peace River",
      "Gathet",
      "Squamish-Lillooet",
      "Strathcona",
      "Sunshine Coast",
      "Thompson-Nicola"
    ],
    valid: false,
    requiredRules: [
      v => !!v || "This field is required"
    ],
    streetNumberRules: [
      v => !!v || "Street number is required",
      v => v >= 0 || "Number cannot be negative",
      v => v <= 2147483647 || "Number must be less than 2147483647"
    ],
    suiteRules: [
      v => v.length <= 32 || "Apt/Suite name must be less than 32 characters"
    ],
    streetNameRules: [
      v => !!v || "Street name is required",
      v => v.length <= 32 || "Street name must be less than 32 characters"
    ],
    cityRules: [
      v => !!v || "City name is required",
      v => v.length <= 32 || "City name must be less than 32 characters"
    ],
    postalCodeRules: [
      v => !!v || "Postal code is required",
      v => /^[ABCEGHJKLMNPRSTVXYabceghjklmnprstvxy]{1}\d{1}[A-Za-z]{1}[ ]{0,1}\d{1}[A-Za-z]{1}\d{1}$/.test(v) || "Postal code must be valid"
    ],
  }),
  methods: {},
  computed: {
    ...mapState({
      operationLocations: state => state.operationLocations
    }),
    streetName: {
      // getter
      get() {
        return this.$store.getters["operationLocations/locations"][this.$props.number].streetName
      },
      // setter
      set(value) {
        this.$store.dispatch("operationLocations/updateLocationProperty", {
          index: this.$props.number,
          property: "streetName",
          value: value,
        });
      }
    },
    aptNumber: {
      // getter
      get() {
        return this.$store.getters["operationLocations/locations"][this.$props.number].aptNumber
      },
      // setter
      set(value) {
        this.$store.dispatch("operationLocations/updateLocationProperty", {
          index: this.$props.number,
          property: "aptNumber",
          value: value,
        });
      }
    },
    streetNumber: {
      // getter
      get() {
        return this.$store.getters["operationLocations/locations"][this.$props.number].streetNumber || ""
      },
      // setter
      set(value) {
        this.$store.dispatch("operationLocations/updateLocationProperty", {
          index: this.$props.number,
          property: "streetNumber",
          value: value,
        });
      }
    },
    city: {
      // getter
      get() {
        return this.$store.getters["operationLocations/locations"][this.$props.number].city
      },
      // setter
      set(value) {
        this.$store.dispatch("operationLocations/updateLocationProperty", {
          index: this.$props.number,
          property: "city",
          value: value,
        });
      }
    },
    postalCode: {
      // getter
      get() {
        return this.$store.getters["operationLocations/locations"][this.$props.number].postalCode
      },
      // setter
      set(value) {
        this.$store.dispatch("operationLocations/updateLocationProperty", {
          index: this.$props.number,
          property: "postalCode",
          value: value,
        });
      }
    },
    region: {
      // getter
      get() {
        return this.$store.getters["operationLocations/locations"][this.$props.number].region;
      }, 
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("operationLocations/updateLocationProperty", {
          index: this.$props.number,
          property: "region",
          value: value,
        });
      }
    }
  }
};
</script>
