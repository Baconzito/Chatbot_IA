import { Usuario } from './Clases/Usuario.js';
import { Sesion } from './Clases/Sesion.js';
import { API_BASE_URL } from './utils.js';

const sesion = new Sesion();

// Referencias al DOM
const elements = {
    chatContainer: document.getElementById('chat-container'),
    promptInput: document.getElementById('prompt'),
    sendButton: document.getElementById('send-button'),
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
    
    elements.chatContainer.scrollTop = elements.chatContainer.scrollHeight;
    return elements.chatContainer.appendChild(mensajeElemento);
}

//#endregion
//#region handlers y eventos

// Manejar envío de mensaje
function MensajeEnvio(mensj) {
    const mensaje = mensj;
    if (!mensaje) return null;

    const mensajeElemento = crearElementoMensaje('Usuario', mensaje, 'user');
    elements.promptInput.value = '';

    return mensajeElemento; 
}

// Evento de logout
if (elements.logoutBtn) {
    elements.logoutBtn.addEventListener('click', () => {
        window.location.href = 'login.html';
    });
}



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


const generarMensajeUsuario = (mensj) => {
    const contenedor = document.createElement("DIV");
    contenedor.classList.add("mensaje", "user");

    const burbuja = document.createElement("DIV");
    burbuja.classList.add("message-text");
    burbuja.textContent = mensj;

    contenedor.appendChild(burbuja);
    return contenedor;
};


function getCookie(name) {
    const match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
    if (match) return match[2];
}

const getToken = () =>{
    const token = getCookie('auth_token');
    if (token) {
        const payload = JSON.parse(atob(token.split('.')[1]));
        document.querySelector(".call-menu").textContent = payload.email;
        return token;
    }
}

getToken();

// Add this after the API_BASE_URL import
const chat_mensaje = document.querySelector(".chat-mensaje");

const llamarChat = async () => {
    try {
        const tk = getToken();
        const response = await fetch(`${API_BASE_URL}/chat/create_chat`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ token: tk })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        console.log('Response data:', data); // Debug log

        if (!data || !data.chat_id) {
            throw new Error('No chat_id in response');
        }

        // Set cookie with the chat_id
        document.cookie = `chat_id=${data.chat_id}; path=/; SameSite=Strict`;
        console.log('Cookie set:', getCookie('chat_id')); // Debug log
        
        return data.chat_id;
    } catch (error) {
        console.error('Error in llamarChat:', error);
        return null;
    }
}



async function getMenuById(menuId = '1'){
    try {
        const idChat = getCookie('chat_id');
        
        const response = await fetch(`${API_BASE_URL}/chat/get_menu`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ id_menu: menuId, id_chat: idChat}),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const menu = await response.json();
        let documentFragment = document.createDocumentFragment();
        
        let menuElement = document.createElement("div");
        menuElement.classList.add("menuElement");

        let mensajeTitulo = document.createElement("p");
        mensajeTitulo.textContent = menu.Mensaje;
        menuElement.appendChild(mensajeTitulo);
        let separador = document.createElement("HR");
        menuElement.appendChild(separador);

        if (Array.isArray(menu.Opciones)) {
        menu.Opciones.forEach(opcion => {
            let divOpcion = document.createElement("div");
            divOpcion.classList.add("menu-option");
            divOpcion.textContent = opcion.Titulo;
            divOpcion.dataset.idMenu = opcion.id_menu;

            divOpcion.addEventListener("click", () => {
                const opcionesDOM = menuElement.querySelectorAll(".menu-option");
                opcionesDOM.forEach( op =>{
                    op.style.pointerEvents = "none";
                    op.classList.add("disabled");
                });
                divOpcion.classList.add("selected");
                chat_mensaje.appendChild(generarMensajeUsuario(divOpcion.textContent));
                getMenuById(divOpcion.dataset.idMenu);
            });
            documentFragment.appendChild(divOpcion);
        });
        } 
        else {
            console.warn("No hay opciones en el menú:", menu);
        }
        menuElement.appendChild(documentFragment);
    
        chat_mensaje.appendChild(menuElement);

        
        return menu;
    } catch (error) {
        console.error('Error fetching menu:', error);
        return null;
    }
}



document.addEventListener('DOMContentLoaded', async () => {

    try {
        llamarChat();
        const menu = await getMenuById();
        
    } catch (error) {
        console.error('Error loading menu:', error);
    }
});

//#endregion