import {defineStore} from "pinia";
import {INewsletterStatistic} from "~/types";
const BASE_API_URL = 'http://localhost:8000/api/v1/';

export const useNewslettersStatisticStore = defineStore({
    id: "newslettersStatistic",
    state: () => ({
        newslettersStatistic: [] as INewsletterStatistic[],
        pendingNewslettersStatistic: true,
    }),
    getters: {},
    actions: {
        async fetchNewslettersStatistic() {
            try {
                const response = await fetch(`${BASE_API_URL}newsletter-statistic/`);
                this.pendingNewslettersStatistic = false;
                this.newslettersStatistic = await response.json();
            } catch (error) {
                console.log(error);
            }
        },
        searchNewslettersStatisticById(id: Number | String) {
            return this.newslettersStatistic.filter((newsletterStatistic: INewsletterStatistic) => newsletterStatistic.id === id);
        },

    }
});
