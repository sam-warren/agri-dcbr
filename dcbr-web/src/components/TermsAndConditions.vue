<template>
  <v-container grid-list-md text-xs-center>
    <v-layout row wrap>
      <v-flex xs12>
        <v-card flat>
          <v-form>
            <v-container>
              <!--Name Section  -->
              <v-layout row wrap mx-2>
                <v-flex>
                  <v-checkbox
                    :disabled="!this.hasClicked"
                    v-model="hasAgreed"
                    name="hasAgreed"
                    required
                  >
                    <template v-slot:label>
                      <div>
                        I have read and agree to the
                      </div>
                    </template>
                  </v-checkbox>
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
  valid: false,
  mask: "",
  computed: {
    ...mapState({
      termsAndConditions: state => state.termsAndConditions
    }),
    hasAgreed: {
      get() {
        return this.$store.getters["termsAndConditions/hasAgreed"];
      },
      set(value) {
        console.log(value);
        this.$store.dispatch("termsAndConditions/hasAgreed", value);
      }
    },
    hasClicked: {
      get() {
        return true;
      }
    }
  }
};
</script>
