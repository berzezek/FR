import { defineStore } from "pinia";

export const useCustomersStore = defineStore({
    id: "customers",
    state: () => ({
        customers: [],
    }),
    getters: {},
    actions: {
        fetchCustomers: async function () {
            try {
                const response = await fetch(`http://localhost:8000/api/v1/customers/`);
                this.customers = await response.json();
            }
            catch (error) {
                console.log(error);
            }
        }
    }
});
