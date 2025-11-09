
import { defineStore } from "pinia";
export const authStore = defineStore("auth", {
  state: () => ({
    session: {
      is_logged_in: false,
      email: "",
      password: "",
      username: "",
      
    },
  }),
  getters: {},

  actions: {
    setLoginSession(data) {
      this.session.is_logged_in = true;
      this.session.email = data.email;
      this.password = data.password;
      this.session.username = data.username;
    
    },
    destroyLoginSession() {
      this.session.is_logged_in = false;
      this.session.email = "";
      this.session.password = "";
      this.session.username = "";

    },
  },
  strict: process.env.DEBUGGING,
});
