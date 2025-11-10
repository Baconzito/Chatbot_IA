import { validateEmail, API_BASE_URL, showAlert } from './utils.js';

const imagenUsuario = document.getElementById("user-img");
const mail = document.querySelector('.user-mail');
const cambiarContrasenaBtn = document.querySelector('.change-pass-btn');

const detectarImagen = ()=>{
    if (!imagenUsuario.getAttribute("src")) {
        imagenUsuario.src = "../Imagenes/GenericUserProfile.png";
    }
};

document.addEventListener("DOMContentLoaded", () => {
    detectarImagen();
});


window.onload = function() {
    // document.getElementById('user-img').src = usuario.imagen;
    const userPass = document.getElementById('user-pass');
    const imagenUsuario = document.getElementById('user-img');
    // if (usuario.imagen && usuario.imagen.startsWith('http')) {
    //     imagenUsuario.src = usuario.imagen;
    // } else {
    //     imagenUsuario.src = "../Imagenes/GenericUserProfile.png";
    // }
    
    cambiarContrasenaBtn.addEventListener("click",()=>{
        changePassword(userPass);
    });

    document.querySelector('.back-btn').onclick = function() {
        window.location.href = "index.html";
    };
};

const changePassword = async (pass) => {
    if(pass.value != "" && pass.value.length >= 8){
            const resGet = fetch(`${API_BASE_URL}/users/change_password`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    email: mail.textContent,
                    password: pass 
                })
            });
            pass.value = "";
            showAlert("Contraseña cambiada con éxito.");
        } else {
            alert("La contraseña debe tener al menos 8 caracteres.");
    }
}


const input_IMG = document.querySelector(".input-IMG");
const input_foto = document.querySelector(".input-foto");

input_IMG.addEventListener("click",()=>{
    input_foto.click();
});

input_foto.addEventListener('change', async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    // Validar tipo de archivo
    const allowedTypes = ['image/jpeg', 'image/png', 'image/jpg'];
    if (!allowedTypes.includes(file.type)) {
        showAlert("Solo se permiten imágenes JPG o PNG.");
        e.target.value = ""; // Limpia la selección
        return;
    }

    // Vista previa local
    imagenUsuario.src = URL.createObjectURL(file);

    const formData = new FormData();
    formData.append("email", mail.textContent);
    formData.append("foto", file);

    try {
        const res = await fetch(`${API_BASE_URL}/users/upload_photo`, {
            method: "POST",
            body: formData
        });

        if (res.ok) {
            showAlert("Foto actualizada con éxito.");
        } else {
            showAlert("Error al subir la foto.");
        }
    } catch (err) {
        console.error("Error al subir imagen:", err);
        showAlert("No se pudo conectar con el servidor.");
    }
});



function getCookie(name) {
    const match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
    if (match) return match[2];
}

const getToken = () =>{
    const token = getCookie('auth_token');
    if (token) {
        const payload = JSON.parse(atob(token.split('.')[1]));
        document.querySelector('.user-mail').textContent = payload.email;
        return token;
    }
}

document.addEventListener("DOMContentLoaded",()=>{
    getToken();
});

async function cargarPerfil() {
    const email = mail.textContent;

    try {
        const res = await fetch(`${API_BASE_URL}/users/get_user`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ token: getToken() }),
        });

        if (!res.ok) {
            console.error('Error fetching profile:', res.status, await res.text());
            showAlert("Error al obtener el perfil.");
            return;
        }

        const data = await res.json();

        if (data.foto) {
            imagenUsuario.src = `${API_BASE_URL}/${data.foto}`;
        } else {
            imagenUsuario.src = "../Imagenes/GenericUserProfile.png";
        }
    } catch (err) {
        console.error('Error al cargar perfil:', err);
        showAlert("No se pudo conectar con el servidor.");
    }
}

cargarPerfil();
