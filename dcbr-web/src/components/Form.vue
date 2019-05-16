 <template>
  <div>
    <v-data-table
      :headers="headers"
      :items="operator"
      :search="search"
      hide-actions
      :pagination.sync="pagination"
      class="elevation-1"
    >
      <template v-slot:items="props">
        <td>{{ firstName}} {{lastName}}</td>
        <td class="text-xs-center">{{ phoneNum }}</td>
        <td class="text-xs-right">{{ streetName}}</td>
        <td class="text-xs-right">{{ city}}</td>
        <td class="text-xs-right">{{ postalCode}}</td>
        <td class="text-xs-right">{{ email }}</td>
      </template>
    </v-data-table>
    <div class="text-xs-center pt-2">
      <v-pagination v-model="pagination.page" :length="pages"></v-pagination>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      streetName: "",
      search: "",
      pagination: {},
      selected: [],
      headers: [
        {
          text: "Full Name",
          align: "centre",
          sortable: false,
          value: "name"
        },
        { text: "Phone#", value: "phone", align: "left" },
        { text: "Address", value: "streetname", align: "centre" },
        { text: "City", value: "city", align: "centre" },
        { text: "Postal Code", value: "postalcode", align: "centre" },
        { text: "Email", value: "email", align: "centre" }
      ],
      operator: [
        {
          name: "Miller Pups Farm",
          phone: "(780) 534-2312",
          streetname: "1239 North Tobruk",
          city: "Kelowna",
          postalcode: "V1P 1A7",
          email: "hello@millerpup.com"
        }
        // {
        //   name: "Hellen Sabe",
        //   phone: "(205) 875-2545",
        //   city: "Victoria",
        //   postalcode: "V8K 2P4",
        //   email: "Helen.Sabe@gmail.com"
        // }
      ]
    };
  },
  mounted() {
    axios({ method: "GET", url: "http://127.0.0.1:8080/api/operators/1" }).then(
      result => {
        this.streetName = result.data.streetName;
        this.email = result.data.email;
        this.firstName = result.data.firstName;
        this.lastName = result.data.lastName;
        this.postalCode = result.data.postalCode;
        this.city = result.data.city;
        this.phoneNum = result.data.phoneNum;
      },
      error => {
        console.error(error);
      }
    );
    // // axios({ method: "GET", url: "http://127.0.0.1:8080/api/operators/" }).then(
    // //   result => {
    // //     this.streetName = result.data.streetName;
    // //     this.email = result.data.email;
    // //     this.firstName = result.data.firstName;
    // //     this.lastName = result.data.lastName;
    // //     this.postalCode = result.data.postalCode;
    // //     this.city = result.data.city;
    // //     this.phoneNum = result.data.phoneNum;
    // //   },
    // //   error => {
    // //     console.error(error);
    // //   }
    // );
  },
  computed: {
    pages() {
      if (
        this.pagination.rowsPerPage == null ||
        this.pagination.totalItems == null
      )
        return 0;

      return Math.ceil(
        this.pagination.totalItems / this.pagination.rowsPerPage
      );
    }
  }
};
</script>