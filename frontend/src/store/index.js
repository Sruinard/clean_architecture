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
    },
  },
  actions: {
    async getAvailableCabs(context, city) {
      const { data } = await axios.get(
        `https://sruinardwebapp.azurewebsites.net/api/cabs?city=${city}`
      );
      context.commit("setAvailableCabs", data);
    },
    async PostCab(context, city) {
      const res = await axios.post(
        "https://sruinardwebapp.azurewebsites.net/api/cabs",
        { city: city }
      );
      context.commit("SetAvailableCabs", res);
    },
  },
  getters: {
    AvailableCabs(state) {
      return state.available_cabs;
    },
  },
  modules: {},
});
