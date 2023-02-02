export const basicAuthenticateUser = (username: string, password: string) => {
    return 'Basic ' + btoa(username + ':' + password);
}