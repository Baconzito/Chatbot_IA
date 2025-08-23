import { validateEmail, API_BASE_URL, showAlert } from './utils.js';

document.getElementById('registration-form').addEventListener('submit', async (event) => {
    event.preventDefault();

    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value.trim();

    if (!validateEmail(email)) {
        showAlert('Por favor, introduce un correo electrónico válido.');
        return;
    }

    if (password.length < 6) {
        showAlert('La contraseña debe tener al menos 6 caracteres.');
        return;
    }

    try {
        const response = await fetch(`${API_BASE_URL}/register`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password })
        });

        const data = await response.json();

        if (response.ok) {
            showAlert('Registro exitoso. Redirigiendo a la página de inicio de sesión...');
            window.location.href = '/login.html';
        } else {
            showAlert(data.message || 'Error en el registro. Inténtalo de nuevo.');
        }
    } catch (error) {
        console.error('Error al conectar con el servidor:', error);
        showAlert('Error al conectar con el servidor. Inténtalo de nuevo más tarde.');
    }
});