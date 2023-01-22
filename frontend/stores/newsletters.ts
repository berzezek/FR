import {defineStore} from "pinia";
import {ICustomer, INewsletter} from "~/types";
const BASE_API_URL = 'http://localhost:8000/api/v1/';

export const useNewslettersStore = defineStore({
    id: "newsletters",
    state: () => ({
        newsletters: [],
        pendingNewsletters: true,
    }),
    getters: {},
    actions: {
        async fetchNewsletters() {
            try {
                const response = await fetch(`${BASE_API_URL}newsletter/`);
                this.newsletters = await response.json();
                this.pendingNewsletters = false;
            }
            catch (error) {
                console.log(error);
            }
        },
        async addNewsletter(newsletter: INewsletter) {
            try {
                const response = await fetch(`${BASE_API_URL}newsletter/`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(newsletter),
                });
                if (response.status === 201) {
                    alert("Рассылка добавлена");
                    this.fetchNewsletters();
                }
            }
            catch (error) {
                console.log(error);
            }
        },
        async updateNewsletter(newsletter: INewsletter, id: Number | String) {
            try {
                const response = await fetch(`${BASE_API_URL}newsletter/${newsletter.id}/`, {
                    method: "PUT",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(newsletter),
                });
                if (response.status === 200) {
                    alert("Рассылка обновлена");
                    this.fetchNewsletters();
                }
            }
            catch (error) {
                console.log(error);
            }
        },
        async deleteNewsletter(id: Number | String) {
            try {
                const response = await fetch(`${BASE_API_URL}newsletter/${id}/`, {
                    method: "DELETE",
                });
                if (response.status === 204) {
                    alert("Рассылка удалена");
                    this.fetchNewsletters();
                }
            }
            catch (error) {
                console.log(error);
            }
        },
        async launchNewsletter(id: Number | String, customersFiltered: ICustomer[], message: String) {
            alert("Рассылка запущена");
            await useFetch(`${BASE_API_URL}newsletter-statistic/`, {
                method: 'POST',
                body: {
                    newsletter: id,
                    customers: customersFiltered,
                    message: message
                }
            })

        }
    }
});
