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
    loginForm.addEventListener('submit', function (e) {
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

        const usuario = new Usuario(email, password);
        const loginExitoso = sesion.iniciarSesion(usuario);
        
        
        if (loginExitoso != 1) {
            document.cookie = 
            window.location.href = 'index.html';

        } else {
            showAlert('Correo o contraseña incorrectos');
        }
    });
}

// Evento para ir a la página de registro
if (registerBtn) {
    registerBtn.addEventListener('click', function () {
        window.location.href = 'register.html';
    });
}