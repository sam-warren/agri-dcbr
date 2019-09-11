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
                  <v-checkbox v-model="hasAgreed" name="hasAgreed" required>
                    <template v-slot:label>
                      <div>
                        I have read and agree to the
                        <v-tooltip bottom>
                          <template v-slot:activator="{ on }">
                            <a
                              target="_blank"
                              href="https://www2.gov.bc.ca/gov/content/governments/organizational-structure/ministries-organizations/ministries/agriculture"
                              @click.stop
                              v-on="on"
                            >terms</a>
                          </template>
                          Opens in new window
                        </v-tooltip> and
                        <v-tooltip bottom>
                          <template v-slot:activator="{ on }">
                            <a
                              target="_blank"
                              href="https://www2.gov.bc.ca/gov/content/governments/organizational-structure/ministries-organizations/ministries/agriculture"
                              @click.stop
                              v-on="on"
                            >conditions</a>
                          </template>
                          Opens in new window
                        </v-tooltip>
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
  computed: {
    ...mapState({
      termsAndConditions: state => state.termsAndConditions
    }),
    hasAgreed: {
      get() {
        return this.$store.getters["termsAndConditions/hasAgreed"];
      },
      set(value) {
        this.$store.dispatch("termsAndConditions/hasAgreed", value);
      }
    }
  }
};
</script>
