import {defineStore} from "pinia";
import {ICustomer} from "~/types";

const BASE_API_URL = 'http://localhost:8000/api/v1/';

export const useCustomersStore = defineStore({
    id: "customers",
    state: () => ({
        customers: [],
        pendingCustomers: true,
    }),
    getters: {},
    actions: {
        fetchCustomers: async function () {
            try {
                const response = await fetch(`${BASE_API_URL}customer/`)
                if (response.ok) {
                    this.customers = await response.json();
                    this.pendingCustomers = false;
                }
            } catch (error) {
                console.log(error);
            }
        },
        addCustomer: async function (customer: ICustomer) {
            try {
                const response = await fetch(`${BASE_API_URL}customer/`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(customer),
                });
                if (response.status === 201) {
                    alert("Клиент добавлен")
                    this.fetchCustomers();
                }
            } catch (error) {
                console.log(error);
            }
        },
        updateCustomer: async function (customer: ICustomer) {
            try {
                const response = await fetch(`${BASE_API_URL}customer/${customer.id}/`, {
                    method: "PUT",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(customer),
                });
                if (response.status === 200) {
                    alert("Клиент обновлен");
                    this.fetchCustomers()
                }
            } catch (error) {
                console.log(error);
            }
        },
        deleteCustomer: async function (id: Number | String) {
            try {
                const response = await fetch(`${BASE_API_URL}customer/${id}/`, {
                    method: "DELETE",
                });
                if (response.status === 204) {
                    alert(`Клиент удален`);
                    this.fetchCustomers()
                }
            } catch (error) {
                console.log(error);
            }
        }
    }
});
