import { defineStore } from "pinia";

export const useCustomersStore = defineStore({
    id: "customers",
    state: () => ({
        customers: [],
    }),
    getters: {},
    actions: {
        async fetchCustomers() {
            const response = await fetch(`http://localhost:8000/api/v1/customer/`);
            this.customers = await response.json();
        }
    }
});
