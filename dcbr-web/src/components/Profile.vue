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
                    :rules="nameRules"
                    label="First name"
                    name="firstName"
                    required
                  ></v-text-field>
                </v-flex>
                <v-flex xs12 md4>
                  <v-text-field
                    v-model="middleName"
                    :rules="nameRules"
                    label="Middle name (optional)"
                    name="middleName"
                  ></v-text-field>
                </v-flex>

                <v-flex xs12 md4>
                  <v-text-field
                    v-model="lastName"
                    :rules="nameRules"
                    label="Last name"
                    name="lastName"
                    required
                  ></v-text-field>
                </v-flex>
              </v-layout>

              <!-- Home address section  -->
              <v-layout row mt-5 mx-2>
                <h4>Home Address</h4>
              </v-layout>
              <v-layout row wrap mx-2>
                <v-flex xs12 md4>
                  <v-text-field
                    v-model="streetNumber"
                    :rules="streetNumberRules"
                    label="Street number"
                    name="streetNumber"
                    required
                  ></v-text-field>
                </v-flex>
                <v-flex xs12 md4 lg6>
                  <v-text-field v-model="aptNumber" label="Apt/Suite" name="aptNumber" required></v-text-field>
                </v-flex>

                <v-flex xs12 md4>
                  <v-text-field
                    v-model="streetName"
                    :rules="nameRules"
                    label="Street name"
                    name="streetName"
                    required
                  ></v-text-field>
                </v-flex>
                <v-flex xs12 md4>
                  <v-text-field v-model="city" :rules="nameRules" label="City" name="city" required></v-text-field>
                </v-flex>
                <v-flex xs12 md4>
                  <v-text-field
                    v-model="postalCode"
                    :rules="nameRules"
                    label="Postal Code"
                    name="postalCode"
                    required
                  ></v-text-field>
                </v-flex>
                <v-flex xs12 md4>
                  <v-checkbox
                    v-model="homeAsOperation"
                    :label="`My home address is also my operation address`"
                  ></v-checkbox>
                  <!-- <label for="homeAsOperation">My home address is also my operation address</label> -->
                  <!-- <input type="checkbox" v-model="homeAsOperation" /> -->
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
                  <v-text-field v-model="phone" :mask="mask" label="Phone" name="phone"></v-text-field>
                </v-flex>
              </v-layout>
              <v-layout mx-2 mt-5>
                <subheader>What is the best way to contact you?</subheader>
              </v-layout>
              <v-layout mx-2>
                <v-radio-group v-model="commType" name="commType" row>
                  <v-radio label="E-mail" value="Email"></v-radio>
                  <v-radio label="Mail" value="Mail"></v-radio>
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
export default {
  data: () => ({
    valid: false,
    mask: "",
    nameRules: [
      v => !!v || "Name is required",
      v => v.length <= 50 || "Name must be less than 50 characters"
    ],
    emailRules: [
      v => !!v || "E-mail is required",
      v => /.+@.+/.test(v) || "E-mail must be valid"
    ],
    streetNumberRules: [v => !!v || "Street number is required"]
  }),

  computed: {
    firstName: {
      // getter
      get() {
        return this.$store.getters.firstName;
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("firstName", value);
      }
    },

    middleName: {
      // getter
      get() {
        return this.$store.getters.middleName;
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("middleName", value);
      }
    },
    lastName: {
      // getter
      get() {
        return this.$store.getters.lastName;
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("lastName", value);
      }
    },
    commType: {
      // getter
      get() {
        return this.$store.getters.commType;
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("commType", value);
      }
    },
    phone: {
      // getter
      get() {
        return this.$store.getters.phone;
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("phone", value);
      }
    },
    email: {
      // getter
      get() {
        return this.$store.getters.email;
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("email", value);
      }
    },
    streetNumber: {
      // getter
      get() {
        return this.$store.getters.streetNumber;
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("streetNumber", value);
      }
    },
    aptNumber: {
      // getter
      get() {
        return this.$store.getters.aptNumber;
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("aptNumber", value);
      }
    },
    streetName: {
      // getter
      get() {
        return this.$store.getters.streetName;
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("streetName", value);
      }
    },
    city: {
      // getter
      get() {
        return this.$store.getters.city;
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("city", value);
      }
    },
    postalCode: {
      // getter
      get() {
        return this.$store.getters.postalCode;
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("postalCode", value);
      }
    }
  }
};
</script>
