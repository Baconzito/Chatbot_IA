import { Usuario } from './Usuario.js';

export class Sesion {
    static instancia = null;
    usuario = null;

    // Método para obtener la instancia de la sesión
    static obtenerInstancia() {
        if (!Sesion.instancia) {
            Sesion.instancia = new Sesion();
        }
        return Sesion.instancia;
    }

    // Método para iniciar sesión
    iniciarSesion(usr) {
        if (this.usuario === null) {
            this.usuario = usr;
            return true;
        }
        return false;
    }

    // Método para cerrar sesión
    cerrarSesion() {
        this.usuario = null;
    }

    // Verificar si está logueado
    estaLogeado() {
        return this.usuario !== null;
    }

    // Obtener el usuario logueado
    obtenerUsuario() {
        return this.usuario;
    }
}
