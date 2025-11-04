<template>
    <div class="flex flex-center fixed-center">

        <q-card class="my-card">
            <q-card-section class="bg-teal text-white" align="center">
                <div class="text-h6">Welcome to Login Page</div>
            </q-card-section>

            <q-card-section align="center">

                <q-input v-model="info.email" label="Enter your email" />
                <q-input v-model="info.password" label="Make Strong Password" />
            </q-card-section>


            <q-card-actions vertical align="center">
                <q-btn color="secondary" @click="onLogin()" label="Login" />

            </q-card-actions>
        </q-card>

    </div>
</template>

<script>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

export default {
    setup() {

        return {
            info: ref({
                email: '',
                password: ''
            }),

            router: useRouter()

        }
    },
    methods: {

        async onLogin() {
            try {
                const res = await axios({
                    method: 'post',
                    url: 'http://127.0.0.1:5000/login',
                    data: {
                        email: this.info.email,
                        password: this.info.password
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