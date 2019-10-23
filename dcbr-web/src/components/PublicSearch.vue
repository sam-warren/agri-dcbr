<template>
  <div class="grey lighten-4">
    <v-content class="mx-4 mb-4">
      <v-container fluid>
        <v-layout row wrap>
          <v-flex>
            <h1>Public Search</h1>
          </v-flex>
          <v-flex>
            <v-text-field prepend-icon="search" label="Search for a breeder/seller" />
          </v-flex>
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
              <td class="text-xs-left">{{ props.item.firstName }}</td>
              <td class="text-xs-left">{{ props.item.lastName }}</td>
              <td class="text-xs-left">{{ props.item.registrationNumber }}</td>
            </template>
          </v-data-table>
        </v-layout>
      </v-container>
    </v-content>
  </div>
</template>
<script>
export default {
  data() {
    return {
      headers: [
        {
          text: "First Name",
          sortable: false,
          value: "firstName"
        },
        { text: "Last Name", sortable: false, value: "lastName" },
        { text: "Registration Number", sortable: false, value: "registrationNumber" },
      ],
      results: [
        {
          firstName: "Sam",
          lastName: "Warren",
          registrationNumber: "BC-DCBR-000001",
        },
        {
          firstName: "Kevin",
          lastName: "Sage",
          registrationNumber: "BC-DCBR-000002",
        },
        {
          firstName: "Dean",
          lastName: "Colpman",
          registrationNumber: "BC-DCBR-000003",
        },
      ]
    };
  }
};
</script>