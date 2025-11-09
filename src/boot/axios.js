import { boot } from "quasar/wrappers";
import axios from "axios";
import { Cookies } from "quasar";
import { Loading } from "quasar";

const axiosInstance = axios.create({
  baseURL: '/api',
  withCredentials: true,
});

axiosInstance.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    if (error.response.status === 401) {
      Loading.hide();
      // store.dispatch("destroyLoginSession");
      // router.replace("/login");
      return new Promise(() => {});
    } else {
      return Promise.reject(error);
    }
  }
);

axiosInstance.defaults.headers.post["Content-Type"] = "application/json";
axiosInstance.defaults.headers.delete["Content-Type"] = "application/json";

axiosInstance.interceptors.request.use((request) => {
  request.headers["X-CSRFToken"] = Cookies.get("_csrf_token");
  return request;
});

export default boot(({ app }) => {
  // for use inside Vue files (Options API) through this.$axios and this.$api

  app.config.globalProperties.$axios = axiosInstance;

  app.config.globalProperties.$api = axiosInstance;

})

export { axiosInstance }