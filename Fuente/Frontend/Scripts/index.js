import { Usuario } from './Clases/Usuario.js';
import { Sesion } from './Clases/Sesion.js';
import { API_BASE_URL } from './utils.js';

const sesion = new Sesion();

// Referencias al DOM
const elements = {
    chatContainer: document.getElementById('chat-container'),
    promptInput: document.getElementById('prompt'),
    sendButton: document.getElementById('send-button'),
    menuButton: document.getElementById('menu-button'),
    menuDropdown: document.getElementById('menu-dropdown'),
    mainContent: document.getElementById('main-content'),
    logoutBtn: document.getElementById('logout-btn'),
};
//#region funciones
// Crear elemento de mensaje
function crearElementoMensaje(nombre, mensaje, tipo) {
    const template = `
        <div class="mensaje ${tipo}">
            <div class="message-header">
                <div class="avatar-container">
                    <div class="avatar"></div>
                    <div class="message-name">${nombre}</div>
                </div>
            </div>
            <div class="message-content">
                <div class="message-text">${mensaje}</div>
            </div>
        </div>
    `;
    const wrapper = document.createElement('div');
    wrapper.innerHTML = template;
    return wrapper.firstElementChild;
}

// Agregar mensaje al chat
function agregarMensaje(nombre, mensaje, tipo) {
    const mensajeElemento = crearElementoMensaje(nombre, mensaje, tipo);
    elements.chatContainer.appendChild(mensajeElemento);
    elements.chatContainer.scrollTop = elements.chatContainer.scrollHeight;
}

//#endregion
//#region handlers y eventos
// Manejar envío de mensaje
function handleMensajeEnvio() {
    const mensaje = elements.promptInput.value.trim();
    if (!mensaje) return;

    agregarMensaje('Usuario', mensaje, 'user');
    elements.promptInput.value = '';

    // Mock response
    setTimeout(() => {
        agregarMensaje('Ai-chan', 'Esta es una respuesta de prueba', 'ai-chan');
    }, 500);
}

// Eventos del menú lateral
// elements.menuButton.addEventListener('click', function (e) {
//     e.stopPropagation();
//     elements.menuDropdown.classList.toggle('show');
//     elements.mainContent.classList.toggle('menu-open');
// });

document.addEventListener('click', function (event) {
    if (
        !elements.menuDropdown.contains(event.target) &&
        !elements.menuButton.contains(event.target)
    ) {
        elements.menuDropdown.classList.remove('show');
        elements.mainContent.classList.remove('menu-open');
    }
});

// Evento de logout
if (elements.logoutBtn) {
    elements.logoutBtn.addEventListener('click', () => {
        window.location.href = 'login.html';
    });
}

// Eventos de envío de mensaje
elements.sendButton.addEventListener('click', handleMensajeEnvio);
elements.promptInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
        e.preventDefault();
        handleMensajeEnvio();
    }
});

document.addEventListener('DOMContentLoaded', () => {
    const profileMock = document.querySelector('.div-profile');
    if (profileMock) {
        profileMock.style.cursor = "pointer";
        profileMock.addEventListener('click', () => {
            window.location.href = "profile.html";
        });
    }
});

const call_menu = document.querySelectorAll(".call-menu");
const dropDown = document.querySelector(".menuDropDown");

call_menu.forEach(element => {
    element.addEventListener("click", (e) => {
        e.stopPropagation();
        dropDown.classList.toggle("dropDownAction");
    });
});

document.addEventListener("click", (e) => {
    if (!dropDown.contains(e.target) && !e.target.classList.contains("call-menu")) {
        dropDown.classList.remove("dropDownAction");
    }
});

// Add this after the API_BASE_URL import
async function getMenuById(menuId = "1") {
    try {
        const response = await fetch(`${API_BASE_URL}/chat/get_menu/${menuId}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const menu = await response.json();
        
        // Detailed console logging
        console.group('Menu Data Retrieved:');
        console.log('Complete menu object:', menu);
        console.log('Menu structure:', JSON.stringify(menu, null, 2));
        if (menu.items) {
            console.log('Menu items:', menu.items);
        }
        console.groupEnd();
        
        return menu;
    } catch (error) {
        console.error('Error fetching menu:', error);
        return null;
    }
}

// Test in DOMContentLoaded
document.addEventListener('DOMContentLoaded', async () => {
    // ...existing DOMContentLoaded code...

    console.log('Fetching menu data...');
    try {
        const menu = await getMenuById();
        if (menu) {
            console.log('------- Menu Data -------');
            console.log('Raw menu data:', menu);
            console.table(menu); // Shows data in table format if possible
            console.log('------------------------');
        } else {
            console.warn('No menu data received');
        }
    } catch (error) {
        console.error('Error loading menu:', error);
    }
});

//#endregion