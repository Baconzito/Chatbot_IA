import { validateEmail, showAlert, API_BASE_URL } from './utils.js';

// DOM Elements
const loginForm = document.getElementById('login-form');
const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');
const registerBtn = document.getElementById('register-btn');

async function handleLogin(email, password) {
    try {
        const response = await fetch(`${API_BASE_URL}/users/login`, {
            method: 'POST',
            headers: { 
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password })
        });

        const data = await response.json();

        if (response.ok) {
            // Store token/session data if received
            if (data.token) {
                document.cookie = `auth_token=${data.token}; path=/`;
            }
            window.location.href = 'index.html';
        } else {
            showAlert(data.message || 'Error en el inicio de sesión');
        }
    } catch (error) {
        console.error('Error:', error);
        showAlert('Error al conectar con el servidor');
    }
}

// Form submission
if (loginForm) {
    loginForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const email = emailInput.value.trim();
        const password = passwordInput.value.trim();

        // Validation
        if (!email || !password) {
            showAlert('Por favor, completa todos los campos.');
            return;
        }

        if (!validateEmail(email)) {
            showAlert('Correo electrónico no válido');
            return;
        }

        await handleLogin(email, password);
    });
}

// Register button
if (registerBtn) {
    registerBtn.addEventListener('click', () => {
        window.location.href = 'register.html';
    });
}