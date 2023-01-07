import { defineStore } from "pinia";
import { ICustomer } from "~/types";
const config = useRuntimeConfig()

export const useCustomersStore = defineStore({
    id: "customers",
    state: () => ({
        customers: [],
    }),
    getters: {},
    actions: {
        fetchCustomers: async function () {
            try {
                const response = await fetch(`${config.public.BASE_API_URL}customer/`);
                this.customers = await response.json();
            }
            catch (error) {
                console.log(error);
            }
        },
        addCustomer: async function (customer: ICustomer) {
            try {
                const response = await fetch(`${config.public.BASE_API_URL}customer/`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(customer),
                });
                if (response.status === 201) {
                    this.fetchCustomers();
                }
            }
            catch (error) {
                console.log(error);
            }
        },
        updateCustomer: async function (customer: ICustomer) {
            try {
                const response = await fetch(`${config.public.BASE_API_URL}customer/${customer.id}/`, {
                    method: "PUT",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(customer),
                });
                if (response.status === 200) {
                    this.fetchCustomers();
                }
            }
            catch (error) {
                console.log(error);
            }
        },
        deleteCustomer: async function (id: Number | String) {
            try {
                const response = await fetch(`${config.public.BASE_API_URL}customer/${id}/`, {
                    method: "DELETE",
                });
                if (response.status === 204) {
                    this.fetchCustomers();
                }
            }
            catch (error) {
                console.log(error);
            }
        }
    }
});
