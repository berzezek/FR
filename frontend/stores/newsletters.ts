import {defineStore} from "pinia";

export const useNewslettersStore = defineStore({
    id: "newsletters",
    state: () => ({
        newsletters: [],
    }),
    getters: {},
    actions: {
        async fetchNewsletters() {
            const response = await fetch(`http://localhost:8000/api/v1/newsletter/`);
            this.newsletters = await response.json();
        }
    }
});
