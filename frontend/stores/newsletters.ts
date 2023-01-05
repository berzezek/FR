import {defineStore} from "pinia";

export const useNewslettersStore = defineStore({
    id: "newsletters",
    state: () => ({
        newsletters: [],
    }),
    getters: {},
    actions: {
        async fetchNewsletters() {
            try {
                const response = await fetch(`http://localhost:8000/api/v1/newsletters/`);
                this.newsletters = await response.json();
            }
            catch (error) {
                console.log(error);
            }
        }
    }
});
