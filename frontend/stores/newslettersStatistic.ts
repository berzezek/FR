import {defineStore} from "pinia";
import {INewsletterStatistic} from "~/types";
import {getCookie} from "~/mixins/cookieOperations";

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
            const router = useRouter();
            try {
                const response = await fetch(`${BASE_API_URL}newsletter-statistic/`, {
                    headers: {
                        "Content-Type": "application/json",
                        "Authorization": "Token " + getCookie("token")
                    }
                });
                if (response.status === 200) {
                    this.newslettersStatistic = await response.json();
                    this.pendingNewslettersStatistic = false;
                } else if (response.status === 401) {
                    alert("Вы не авторизованы");
                    router.push("/login");
                }
            } catch (error) {
                console.log(error);
            }
        },
        searchNewslettersStatisticById(id: Number | String) {
            return this.newslettersStatistic.filter((newsletterStatistic: INewsletterStatistic) => newsletterStatistic.id === id);
        },

    }
});
