import {defineStore} from "pinia";
import {IUser} from "~/types";
import {setCookie, getCookie} from "~/mixins/cookieOperations";

const BASE_API_URL = 'http://localhost:8000/auth/';

export const useUserStore = defineStore({
    id: "users",
    state: () => ({
        pendingUser: true,
        data_token: {auth_token: ''},
        data_user: {id: 0, username: '', email: ''}
    }),
    getters: {},
    actions: {
        loginUser: async function (user: IUser) {
            try {
                const response = await fetch(`${BASE_API_URL}token/login/`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(user),
                })
                const data_token = await response.json();
                if (response.ok) {
                    alert('Login successful');
                    setCookie('token', data_token.auth_token, 1);
                    this.pendingUser = false;
                }
            } catch (error) {
                console.log(error);
            }
        },
        async fetchUser() {
            console.log(getCookie('token'));
            try {
                const response = await fetch(`${BASE_API_URL}users/me/`, {
                    method: "GET",
                    headers: {
                        "Content-Type": "application/json",
                        "Authorization": `Token ${getCookie('token')}`
                    }
                })
                const data_user = await response.json();
                if (response.ok) {
                    this.pendingUser = false;
                    return data_user;
                }
            } catch (error) {
                console.log(error);
            }
        }
    }
});