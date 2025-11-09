import { Sesion } from './Clases/Sesion.js';
import { Usuario } from './Clases/Usuario.js';
import { validateEmail, showAlert } from './utils.js';

const sesion = new Sesion();

// Referencias al DOM
const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');
const loginForm = document.getElementById('login-form');
const errorMessage = document.getElementById('error-message');
const registerBtn = document.getElementById('register-btn');

// Función para mostrar mensajes de error
function mostrarError(mensaje) {
    if (errorMessage) {
        errorMessage.textContent = mensaje;
        errorMessage.style.display = 'block';
    }
}

// Función para limpiar mensajes de error
function limpiarError() {
    if (errorMessage) {
        errorMessage.textContent = '';
        errorMessage.style.display = 'none';
    }
}

// Evento de envío del formulario
if (loginForm) {
    loginForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        limpiarError();

        const email = emailInput.value.trim();
        const password = passwordInput.value.trim();

        if (!email || !password) {
            mostrarError('Por favor, completa todos los campos.');
            return;
        }

        if (!validateEmail(email)) {
            showAlert('Correo electrónico no válido');
            return;
        }

        window.location.href = './index.html';

        // try {
        //     const response = await fetch(`${API_BASE_URL}/users/login`, {
        //         method: 'POST',
        //         headers: { 'Content-Type': 'application/json' },
        //         body: JSON.stringify({
        //             email: email,      
        //             password: password
        //         }),
        //     });

            
        //     const data = await response.json();
        //     console.log('Respuesta del servidor:', data);

        //     if (!response.ok) {
        //         showAlert(data.message || 'Credenciales inválidas');
        //         return;
        //     }

        //     if (data.success) {
        //         document.cookie = `token=${data.token}; path=/; max-age=3600;`;
        //         window.location.href = '../index.html';
        //     } else {
        //         showAlert(data.mensaje || 'Error al iniciar sesión');
        //     }

        // } catch (err) {
        //     console.error('Error al conectar con el servidor:', err);
        //     showAlert('Error al conectar con el servidor.');
        // }
    });
}

// Evento para ir a la página de registro
if (registerBtn) {
    registerBtn.addEventListener('click', function () {
        window.location.href = 'register.html';
    });
}



