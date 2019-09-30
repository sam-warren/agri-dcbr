<template>
  <v-container grid-list-md text-xs-center>
    <v-layout row wrap>
      <v-card-title primary-title>
        <div>
          <h2>Profile</h2>
        </div>
      </v-card-title>
      <v-flex xs12>
        <v-card flat>
          <v-form v-model="valid">
            <v-container>
              <!--Name Section  -->
              <v-layout mx-2 mt-2>
                <h4>Name</h4>
              </v-layout>
              <v-layout row wrap mx-2>
                <v-flex xs12 md4>
                  <v-text-field
                    v-model="firstName"
                    onkeypress="return event.charCode < 48 || event.charCode > 57"
                    :rules="nameRules"
                    label="First name"
                    name="firstName"
                    counter="50"
                    required
                  ></v-text-field>
                </v-flex>
                <v-flex xs12 md4>
                  <v-text-field
                    v-model="middleName"
                    onkeypress="return event.charCode < 48 || event.charCode > 57"
                    :rules="middleNameRules"
                    label="Middle name (optional)"
                    name="middleName"
                    counter="50"
                  ></v-text-field>
                </v-flex>

                <v-flex xs12 md4>
                  <v-text-field
                    v-model="lastName"
                    onkeypress="return event.charCode < 48 || event.charCode > 57"
                    :rules="nameRules"
                    label="Last name"
                    name="lastName"
                    counter="50"
                    required
                  ></v-text-field>
                </v-flex>
              </v-layout>

              <!-- Mailing address section  -->
              <v-layout row mt-5 mx-2>
                <h4>Mailing Address</h4>
              </v-layout>
              <v-layout row wrap mx-2>
                <v-flex xs12 md4>
                  <v-text-field
                    v-model="streetNumber"
                    mask="#########"
                    :rules="streetNumberRules"
                    label="Street number"
                    name="streetNumber"
                    required
                  ></v-text-field>
                </v-flex>
                <v-flex xs12 md4>
                  <v-text-field
                    v-model="streetName"
                    :rules="streetNameRules"
                    label="Street name"
                    name="streetName"
                    counter="32"
                    required
                  ></v-text-field>
                </v-flex>
                <v-flex xs12 md4 lg6>
                  <v-text-field
                    v-model="aptNumber"
                    label="Apt/Suite (optional)"
                    name="aptNumber"
                    counter="32"
                    :rules="suiteRules"
                  ></v-text-field>
                </v-flex>
                <v-flex xs12 md4>
                  <v-text-field
                    v-model="city"
                    onkeypress="return event.charCode < 48 || event.charCode > 57"
                    :rules="cityRules"
                    label="City"
                    name="city"
                    counter="32"
                    required
                  ></v-text-field>
                </v-flex>
                <v-flex xs12 md4>
                  <v-text-field
                    v-model="postalCode"
                    mask="A#A #A#"
                    :rules="postalCodeRules"
                    label="Postal Code"
                    name="postalCode"
                    required
                  ></v-text-field>
                </v-flex>
                <v-flex xs12 md4>
                  <v-text-field
                    v-model="poBox"
                    :rules="poBoxRules"
                    label="P.O. Box"
                    name="poBox"
                    counter="32"
                    required
                  ></v-text-field>
                </v-flex>
                <v-flex xs12 md4>
                  <v-flex class="d-flex" cols="12" sm="6">
                    <v-select
                      :rules="requiredRules"
                      :items="items"
                      v-model="homeRegion"
                      label="Regional District"
                    ></v-select>
                  </v-flex>
                </v-flex>
              </v-layout>
              <v-layout row wrap>
                <v-flex xs12 md4>
                  <v-checkbox
                    v-model="sameAsOperation"
                    label="My primary operation address is the same as my mailing address"
                  ></v-checkbox>
                </v-flex>
              </v-layout>

              <!-- contact info  -->
              <v-layout row mt-5 mx-2>
                <h4>Contact</h4>
              </v-layout>
              <v-layout row mx-2>
                <!-- email -->
                <v-flex xs12 md4 lg6>
                  <v-text-field
                    v-model="email"
                    :rules="emailRules"
                    label="E-mail"
                    name="email"
                    required
                  ></v-text-field>
                </v-flex>
                <!-- phone number -->
                <v-flex xs12 md4 lg6>
                  <v-text-field
                    v-model="phone"
                    type="tel"
                    mask="(###) ### ####"
                    :rules="phoneNumberRules"
                    label="Phone"
                    name="phone"
                  ></v-text-field>
                </v-flex>
              </v-layout>
              <v-layout mx-2 mt-5>
                <v-subheader>What is the best way to contact you?</v-subheader>
              </v-layout>
              <v-layout mx-2>
                <v-radio-group v-model="commType" name="commType" row>
                  <v-radio label="E-mail" value="Email"></v-radio>
                  <v-radio label="Mail" value="Mail"></v-radio>
                  <v-radio label="Phone" value="Phone"></v-radio>
                </v-radio-group>
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
    mask: "",
    requiredRules: [v => !!v || "This field is required"],
    nameRules: [
      v => !!v || "Name is required",
      v => v.length <= 50 || "Name must be less than 50 characters"
    ],
    middleNameRules: [
      v => v.length <= 50 || "Name must be less than 50 characters"
    ],
    emailRules: [
      v => !!v || "E-mail is required",
      v => /.+@.+/.test(v) || "E-mail must be valid",
      v => v.length <= 32 || "Email address must be less than 32 characters"
    ],
    streetNumberRules: [
      v => !!v || "Street number is required",
      v => v >= 0 || "Street number cannot be negative",
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
      v =>
        /^[ABCEGHJKLMNPRSTVXYabceghjklmnprstvxy]{1}\d{1}[A-Za-z]{1}[ ]{0,1}\d{1}[A-Za-z]{1}\d{1}$/.test(
          v
        ) || "Postal code must be valid"
    ],
    phoneNumberRules: [
      v => !!v || "Phone number is required",
      v =>
        /^\D?(\d{3})\D?\D?(\d{3})\D?(\d{4})$/.test(v) ||
        "Phone number must be valid"
    ],
    poBoxRules: [
      v => !!v || "P.O. Box is required",
      v => v.length <= 32 || "P.O. box must be valid"
    ]
  }),

  computed: {
    ...mapState({
      profile: state => state.profile
    }),
    firstName: {
      // getter
      get() {
        return this.$store.getters["profile/firstName"];
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("profile/firstName", value);
      }
    },

    middleName: {
      // getter
      get() {
        return this.$store.getters["profile/middleName"];
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("profile/middleName", value);
      }
    },
    lastName: {
      // getter
      get() {
        return this.$store.getters["profile/lastName"];
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("profile/lastName", value);
      }
    },
    commType: {
      // getter
      get() {
        return this.$store.getters["profile/commType"];
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("profile/commType", value);
      }
    },
    phone: {
      // getter
      get() {
        return this.$store.getters["profile/phone"];
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("profile/phone", value);
      }
    },
    email: {
      // getter
      get() {
        return this.$store.getters["profile/email"];
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("profile/email", value);
      }
    },
    streetNumber: {
      // getter
      get() {
        return this.$store.getters["profile/streetNumber"] || "";
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("profile/streetNumber", value);
      }
    },
    aptNumber: {
      // getter
      get() {
        return this.$store.getters["profile/aptNumber"];
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("profile/aptNumber", value);
      }
    },
    streetName: {
      // getter
      get() {
        return this.$store.getters["profile/streetName"];
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("profile/streetName", value);
      }
    },
    city: {
      // getter
      get() {
        return this.$store.getters["profile/city"];
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("profile/city", value);
      }
    },
    postalCode: {
      // getter
      get() {
        return this.$store.getters["profile/postalCode"];
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("profile/postalCode", value);
      }
    },
    poBox: {
      // getter
      get() {
        return this.$store.getters["profile/poBox"];
      },
      // setter
      set(value) {
        this.$store.dispatch("profile/poBox", value);
      }
    },
    homeRegion: {
      // getter
      get() {
        return this.$store.getters["profile/homeRegion"];
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("profile/homeRegion", value);
      }
    },
    sameAsOperation: {
      get() {
        return this.$store.getters["profile/sameAsOperation"];
      },
      set(value) {
        this.$store.dispatch("profile/sameAsOperation", value);
        if (value === true) {
          // Set operation location properties
          this.$store.dispatch("operationLocations/updateLocationProperty", {
            index: 0,
            property: "streetName",
            value: this.streetName
          });
          this.$store.dispatch("operationLocations/updateLocationProperty", {
            index: 0,
            property: "streetNumber",
            value: this.streetNumber
          });
          this.$store.dispatch("operationLocations/updateLocationProperty", {
            index: 0,
            property: "aptNumber",
            value: this.aptNumber
          });
          this.$store.dispatch("operationLocations/updateLocationProperty", {
            index: 0,
            property: "city",
            value: this.city
          });
          this.$store.dispatch("operationLocations/updateLocationProperty", {
            index: 0,
            property: "postalCode",
            value: this.postalCode
          });
          this.$store.dispatch("operationLocations/updateLocationProperty", {
            index: 0,
            property: "region",
            value: this.homeRegion
          });
        } else {
          // Clear operation location properties
          this.$store.dispatch("operationLocations/updateLocationProperty", {
            index: 0,
            property: "streetName",
            value: ""
          });
          this.$store.dispatch("operationLocations/updateLocationProperty", {
            index: 0,
            property: "streetNumber",
            value: ""
          });
          this.$store.dispatch("operationLocations/updateLocationProperty", {
            index: 0,
            property: "aptNumber",
            value: ""
          });
          this.$store.dispatch("operationLocations/updateLocationProperty", {
            index: 0,
            property: "city",
            value: ""
          });
          this.$store.dispatch("operationLocations/updateLocationProperty", {
            index: 0,
            property: "postalCode",
            value: ""
          });
          this.$store.dispatch("operationLocations/updateLocationProperty", {
            index: 0,
            property: "region",
            value: ""
          });
        }
      }
    }
  }
};
</script>
