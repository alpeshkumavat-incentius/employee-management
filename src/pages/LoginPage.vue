<template>
    <div class="flex flex-center fixed-center">

        <q-card class="my-card">
            <q-card-section class="bg-teal text-white" align="center">
                <div class="text-h6">Welcome to Login Page</div>
            </q-card-section>

            <q-card-section align="center">

                <q-input v-model="authStore.email" label="Enter your email" />
                <q-input v-model="authStore.password" label="Make Strong Password" />
            </q-card-section>


            <q-card-actions vertical align="center">
                <q-btn color="secondary" @click="onLogin()" label="Login" />

            </q-card-actions>
        </q-card>

    </div>
</template>

<script>

import axios from 'axios';
import { useRouter } from 'vue-router';

import { authStore } from 'src/stores/authStore';

export default {
    setup() {

        return {
            // info: ref({
            //     email: '',
            //     password: ''
            // }),

            router: useRouter(),

            authStore : authStore()
        }
    },
    methods: {

        async onLogin() {
            try {
                const res = await axios({
                    method: 'post',
                    url: 'http://127.0.0.1:5000/login',
                    data: {
                        email: this.authStore.email,
                        password: this.authStore.password
                    }
                })
                if (res.data['msg']) {
                    this.router.push('home')
                    alert("Login Successfully !!!")
                }
                else {
                    alert("Enter valid Credentials !!")
                    this.router.push('login')

                }
            }
            catch (error) {
                console.error(error)
            }

        }
    }
}
</script>