import {defineStore} from "pinia";
import {IUser} from "~/types";
import {getCookie, setCookie, eraseCookie} from "~/mixins/cookieOperations";
import {basicAuthenticateUser} from "~/mixins/basicAuthenticatedUser";
import {BASE_AUTH_URL, BASE_OAUTH_URL, CLIENT_ID, CLIENT_SECRET} from "~/utils/constants";


export const useUserStore = defineStore({
    id: "users",
    state: () => ({
        pendingUser: false,
        data_token: {auth_token: ''},
        data_user: {email: '', id: 0, username: ''},
    }),
    getters: {
        isAuthenticated: (state) => {
            return state.data_token.auth_token !== '';
        },
        isOauthAuthenticated: (state) => {
            return getCookie('oauth_token') !== '';
        },
        clearDataUser: (state) => {
            state.data_user = {email: '', id: 0, username: ''};
        }
    },
    actions: {
        signUser: async function (user: IUser) {
            this.pendingUser = true;
            try {
                const response = await fetch(`${BASE_AUTH_URL}users/`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(user),
                })
                const data = await response.json();
                if (response.ok) {
                    console.log(data)
                    alert('Вы успешно зарегистрировались');
                } else {
                    alert('Ошибка регистрации');
                }
            } catch (error) {
                console.log(error);
            }
            this.pendingUser = false;
        },
        loginUser: async function (user: IUser) {
            eraseCookie('token');
            this.pendingUser = true;
            try {
                const response = await fetch(`${BASE_AUTH_URL}token/login/`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(user),
                })
                const data_token = await response.json();
                if (response.ok) {
                    alert('Вы успешно авторизовались');
                    setCookie('token', data_token.auth_token, 1);
                } else {
                    alert('Ошибка авторизации');
                }
            } catch (error) {
                console.log(error);
            }
            this.pendingUser = false;
        },
        async fetchUser() {
            try {
                const response = await fetch(`${BASE_AUTH_URL}users/me/`, {
                    method: "GET",
                    headers: {
                        "Content-Type": "application/json",
                        "Authorization": `Token ${getCookie('token')}`
                    }
                })
                if (response.ok) {
                    this.data_user = await response.json();
                }
            } catch (error) {
                console.log(error);
            }
        },
        async logoutUser() {
            this.pendingUser = true;
            try {
                const response = await fetch(`${BASE_AUTH_URL}token/logout/`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "Authorization": `Token ${getCookie('token')}`
                    }
                })
                if (response.ok) {
                    alert('Вы успешно вышли из аккаунта');
                } else {
                    alert('Произошла ошибка');
                }
            } catch (error) {
                console.log(error);
            }
            this.pendingUser = false;
        },
        loginOauth: async function (user: IUser) {
            this.pendingUser = true;
            try {
                const {data: post, error, refresh, execute, pending} = await useFetch(`${BASE_OAUTH_URL}token/`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Authorization': basicAuthenticateUser(CLIENT_ID, CLIENT_SECRET),
                        'Accept': 'application/json',
                    },
                    body: `grant_type=password&username=${user.username}&password=${user.password}`,
                });
                if (!error.value) {
                    alert('Login successful');
                    // @ts-ignore
                    setCookie('oauth_token', post.value.access_token, 30);
                } else {
                    alert('Login failed');
                }
            } catch (error) {
                console.log(error);
            }

            this.pendingUser = false;


        }
    }
});