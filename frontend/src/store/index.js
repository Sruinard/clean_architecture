import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    available_cabs: [],
  },
  mutations: {
    setAvailableCabs(state, data) {
      state.available_cabs = data;
      console.log(data);
    },
  },
  actions: {
    async getAvailableCabs(context, city) {
      let url = `https://sruinardwebapp.azurewebsites.net/api/cabs?city=${city.city}`;
      console.log(url);
      const { data } = await axios.get(url);
      context.commit("setAvailableCabs", data);
    },
    async PostCab(context, city) {
      const { data } = await axios.post(
        "https://sruinardwebapp.azurewebsites.net/api/cabs",
        { city: city.city, is_available: true }
      );
      context.commit("setAvailableCabs", [data]);
    },
  },
  getters: {
    AvailableCabs(state) {
      return state.available_cabs;
    },
  },
  modules: {},
});
