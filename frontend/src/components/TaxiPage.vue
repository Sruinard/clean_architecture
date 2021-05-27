<template>
  <v-container class="mt-5">
    <v-row class="text-center pa-xl">
      <v-col>
        <v-text-field v-model="search" label="Search" required></v-text-field>
        <v-btn color="primary" @click="Fetch">Fetch</v-btn>
        <v-card
          class="mx-auto pa-2 ma-2"
          max-width="344"
          outlined
          v-for="item in all_items"
          :key="item.id"
        >
          <v-list-item three-line>
            <v-list-item-content>
              <div class="overline mb-4">
                {{ item.city }}
              </div>
              <v-list-item-title class="headline mb-1">
                {{ item.is_available }}
              </v-list-item-title>
              <v-list-item-subtitle>
                {{ item.datetime }}
              </v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item> </v-card
        ><v-card></v-card> </v-col
      ><v-col>
        <form>
          <v-text-field v-model="city" label="City" required></v-text-field>
          <v-btn color="primary" @click="submit">Submit</v-btn>
        </form>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "HelloWorld",
  mounted() {
    this.Fetch();
  },
  data: function () {
    return {
      city: "",
      search: "Amsterdam",
      items: [
        {
          city: "Amsterdam",
        },
        {
          city: "Amsterdam",
        },
        {
          city: "Amsterdam",
        },
      ],
    };
  },
  computed: {
    all_items() {
      return this.$store.getters.AvailableCabs;
    },
  },
  methods: {
    Fetch() {
      this.$store.dispatch("getAvailableCabs", { city: this.search });
    },
    submit() {
      this.$store.dispatch("PostCab", { city: this.search });
    },
  },
};
</script>
