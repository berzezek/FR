export interface ICustomer {
    id: string | number,
    phone_prefix: string,
    phone_number: string,
    tag: string
}

export  interface  INewsletter {
    id: string | number,
    start_launch_date: string,
    end_launch_date: string,
    message: string,
    customer_filter: string,
    is_valid: boolean,
}

export  interface  INewsletterStatistic {
    id: string | number,
    newsletter: string,
    customer: string,
    date_of_creation: string,
}

export  interface  IUser {
    id: string | number,
    username: string,
    email: string,
    password: string,
}