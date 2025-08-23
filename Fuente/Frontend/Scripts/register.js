import { validateEmail, API_BASE_URL, showAlert } from './utils.js';

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('registration-form');
    if (!form) return;

    form.addEventListener('submit', async (event) => {
        event.preventDefault();

        const emailInput = document.getElementById('email');
        const passwordInput = document.getElementById('password');
        const email = emailInput ? emailInput.value.trim() : '';
        const password = passwordInput ? passwordInput.value.trim() : '';

        // Validaciones
        if (!validateEmail(email)) {
            showAlert('Por favor, introduce un correo electrónico válido.');
            return;
        }

        if (password.length < 6) {
            showAlert('La contraseña debe tener al menos 6 caracteres.');
            return;
        }

        try {
            const response = await fetch(`${API_BASE_URL}/users/register`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email, password })
            });

            const data = await response.json();

            if (response.ok) {
                showAlert('Registro exitoso. Redirigiendo a la página de inicio de sesión...');
                setTimeout(() => {
                    window.location.href = 'login.html';
                }, 1500);
            } else {
                showAlert(data.message || 'Error en el registro. Inténtalo de nuevo.');
            }
        } catch (error) {
            console.error('Error al conectar con el servidor:', error);
            showAlert('Error al conectar con el servidor. Inténtalo de nuevo más tarde.');
        }
    });
});