<template>
  <v-app class="hello">
    <h1>Your name is {{ name }}</h1>
    <input type="text" v-model="input.firstname" placeholder="First Name">
    <input type="text" v-model="input.lastname" placeholder="Last Name">
    <br>
    <br>
    <v-btn v-on:click="sendData()">Register</v-btn>
  </v-app>
</template>

<script>
import axios from "axios";

export default {
  name: "HelloWorld",
  data() {
    return {
      name: "",
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
        this.name = result.data.name;
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
        mounted() {
            axios({ method: "GET", "url": "http://127.0.0.1:8080/api/operators/5" }).then(result => {
                this.name = result.data.firstName;
            }, error => {
                console.error(error);
            });
        },
       methods: {
            sendData() {
                axios({ method: "POST", "url": "https://httpbin.org/post", "data": this.input, "headers": { "content-type": "application/json" } }).then(result => {
                    this.response = result.data;
                }, error => {
                    console.error(error);
                });
            }
        }
      );
    }
  }
};
</script>

<style scoped>
h1,
h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}

textarea {
  width: 600px;
  height: 200px;
}
</style>
