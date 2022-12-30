import { defineStore } from "pinia";

export const useNewslettersStatisticStore = defineStore({
    id: "newslettersStatistic",
    state: () => ({
        newslettersStatistic: [],
    }),
    getters: {},
    actions: {
        async fetchNewslettersStatistic() {
            const response = await fetch(`http://localhost:8000/api/v1/newsletter-statistic/`);
            this.newslettersStatistic = await response.json();
        }
    }
});
