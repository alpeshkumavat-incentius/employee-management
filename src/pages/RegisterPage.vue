<template>
    <div class="flex flex-center fixed-center">

        <q-card class="my-card">
            <q-card-section class="bg-teal text-white" align="center">
                <div class="text-h6">Welcome to Register Page</div>
            </q-card-section>

            <q-card-section align="center">
                <q-input v-model="credentials.username" label="Enter your Name" />
                <q-input v-model="credentials.email" label="Enter your email" />
                <q-input v-model="credentials.password" label="Make Strong Password" />
            </q-card-section>


            <q-card-actions vertical align="center">
                <q-btn color="secondary" @click="onSubmit()" label="Submit" />
                <div>
                    <q-btn color="purple" @click="goToLogin()" flat>Already Account ?</q-btn>
                    <q-btn color="purple" @click="goToLogin()" flat>Login</q-btn>
                </div>
            </q-card-actions>
        </q-card>

    </div>
</template>



<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';



export default {

    setup() {

        return {

            credentials: ref(
                {
                    username: '',
                    email: '',
                    password: ''
                }
            ),
            router: useRouter(),


        }
    },


    methods: {

        async onSubmit() {
            console.log(this.store.username);
            try {
                const res = await axios({
                    method: 'post',
                    url: 'http://127.0.0.1:5000/register',
                    data: {
                        username: this.credentials.username,
                        email: this.credentials.email,
                        password: this.credentials.password
                    }
                })

                if (res.data['ok']) {
                    this.router.push('login')
                    alert("Register Successufully !!")
                }
                else {
                    this.router.push('register')
                }
            }
            catch (error) {
                console.error(error)
            }

        },
        goToLogin() {
            this.router.push('login')
        }
    }
}

</script>