
import { authStore } from "../stores/authStore.js";
import  { axiosInstance } from "./axios.js";

export const sessionGuard = (to, from, next) => {
  const store = authStore();
  let publicPages = ["/login", "/access-denied"];
  if (publicPages.includes(to.path)) {
    if(to.path=="/access-denied") {
      next();
    }
    else {
      axiosInstance
        .get("/get_authenticated_user_information/", { withCredentials: true })
        .then((response) => {
          if (response.data.ok) {
            store.setLoginSession(response.data.data);
            next("/");
          } else {
            next();
          }
        });
    }
  } else {
    axiosInstance
      .get("/get_authenticated_user_information/", { withCredentials: true })
      .then((response) => {
        if (response.data.ok) {
          store.setLoginSession(response.data.data);
          next();
        } else {
          next("/login");
        }
      });
  }
};





// function check_user_group(to, store, next) {
//   if (to.meta) {
//     if (to.meta.user_access && store.session.user_group) {
//       if (to.meta.user_access.includes(store.session.user_group)) {
//         // console.log(redirect)
//         if(to.fullPath.split("/")[1]=='sales' && (!store.session.sales_flag)){
//           next("/access-denied");
//         }
//         if(to.fullPath.split("/")[1]=='marketing' && (!store.session.marketing_flag)){
//           next("/access-denied");
//         }
//         if(to.fullPath.split("/")[1]=='communications' && (!store.session.communications_flag)){
//           next("/access-denied");
//         }
//         if(to.fullPath.split("/")[1]=='executive' && (!store.session.executive_flag)){
//           next("/access-denied");
//         }
//         if(to.fullPath.split("/")[1]=='marketaccess' && (!store.session.market_access_flag)){
//           next("/access-denied");
//         }
//         if(to.fullPath.split("/")[1]=='operations' && (!store.session.ops_ui_flag)){
//           next("/access-denied");
//         }
//         if(to.fullPath.split("/")[1]=='executive' && to.fullPath.split("/")[2]=='launch_performance_tracking' && (!store.session.executive_lpt_flag)){
//           next("/access-denied");
//         }
//         if(to.fullPath.split("/")[1]=='executive' && to.fullPath.split("/")[2]=='ojemda_performance' && (!store.session.executive_ojemda_perf_flag)){
//           next("/access-denied");
//         }
//         if(to.fullPath.split("/")[1]=='log' && (!store.session.log_utility_flag)){
//           next("/access-denied");
//         }
//         if(to.fullPath.split("/")[1]=='executive' && to.fullPath.split("/")[2]=='elt_summary_2' && (!store.session.elt_summary_2_flag)){
//           next("/access-denied");
//         }
//         next();
//       } else {
//         next("/access-denied");
//       }
//     } else {
//       next("/access-denied");
//     }
//   } else {
//     next("/access-denied");
//   }
// }