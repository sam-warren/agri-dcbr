<template>
  <div class="hello">
    <h1>Your name is</h1>

    <v-btn>street name: {{ streetName }}</v-btn>
    <br>
    <br>
    <textarea v-model="this.response"/>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "HelloWorld",
  data() {
    return {
      streetName: "",
      input: {
        firstname: "",
        lastname: ""
      },
      response: ""
    };
  },
  mounted() {
    axios({ method: "GET", url: "http://127.0.0.1:8080/api/operators/1" }).then(
      result => {
        this.streetName = result.data.streetName;
      },
      error => {
        console.error(error);
      }
    );
  },
  methods: {
    sendData() {
      axios({
        method: "POST",
        url: "https://httpbin.org/post",
        data: this.input,
        headers: { "content-type": "application/json" }
      }).then(
        result => {
          this.response = result.data;
        },
        error => {
          console.error(error);
        }
      );
    }
  }
};
</script>

