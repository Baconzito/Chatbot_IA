export const validateEmail = (email) => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(String(email).toLowerCase());
};

export const API_BASE_URL = 'http://127.0.0.1:5000';

export const showAlert = (message) => {
    alert(message); // Could be replaced with a better UI notification system
};