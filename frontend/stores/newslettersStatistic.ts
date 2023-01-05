import { defineStore } from "pinia";

export const useNewslettersStatisticStore = defineStore({
    id: "newslettersStatistic",
    state: () => ({
        newslettersStatistic: [],
    }),
    getters: {},
    actions: {
        async fetchNewslettersStatistic() {
            try {
                const response = await fetch(`http://localhost:8000/api/v1/newsletter-statistic/`);
                this.newslettersStatistic = await response.json();
            }
            catch (error) {
                console.log(error);
            }
        },
        searchNewslettersStatisticById(id: Number | String) {
            return this.newslettersStatistic.filter((newsletterStatistic: any) => newsletterStatistic.id === id);
        }
    }
});
