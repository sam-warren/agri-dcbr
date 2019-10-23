<template>
  <div class="grey lighten-4">
    <v-content class="mx-4 mb-4">
      <v-container>
        <v-layout row wrap>
          <v-flex mt-2>
            <h1>Public Search</h1>
          </v-flex>
          <v-flex>
            <v-text-field
              v-model="searchQuery"
              label="Registration Number"
              v-mask="'BC-DCBR-######'"
            />
          </v-flex>
          <v-flex mt-2>
            <v-btn text icon @click="search()">
              <v-icon color="primary">search</v-icon>
            </v-btn>
          </v-flex>
        </v-layout>
        <v-layout mb-4>
          <div>Enter a valid registration number in the searchbar to see their details.</div>
        </v-layout>
        <v-layout>
          <v-data-table :headers="headers" :items="results" class="elevation-1">
            <template slot="headerCell" slot-scope="props">
              <v-tooltip bottom>
                <template v-slot:activator="{ on }">
                  <span v-on="on">{{ props.header.text }}</span>
                </template>
                <span>{{ props.header.text }}</span>
              </v-tooltip>
            </template>
            <template v-slot:items="props">
              <td class="text-xs-left">{{ props.item.first_name }}</td>
              <td class="text-xs-left">{{ props.item.last_name }}</td>
              <td class="text-xs-left">{{ props.item.registration_number }}</td>
            </template>
          </v-data-table>
        </v-layout>
      </v-container>
    </v-content>
  </div>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      searchQuery: "",
      headers: [
        {
          text: "First Name",
          sortable: false,
          value: "first_name"
        },
        { text: "Last Name", sortable: false, value: "last_name" },
        {
          text: "Registration Number",
          sortable: false,
          value: "registration_number"
        }
      ],
      results: []
    };
  },
  methods: {
    search() {
      axios
        .get("/api/search", {
          params: {
            string: this.searchQuery
          }
        })
        .then(res => {
          this.results = res.data.results;
        });
    }
  }
};
</script>