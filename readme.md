# Club Deportivo - Sistema de Gestión

**Materia:** Programación 2  
**Carrera:** Tecnicatura Universitaria en Programación – UTN FRLP  
**Año:** 2025  

## 1. Descripción del Proyecto

Este proyecto es una aplicación web desarrollada en **Django** para la gestión integral de un club deportivo. Su objetivo es centralizar la administración de las entidades principales de la institución, permitiendo un control eficiente de:

*   **Deportes:** Altas, bajas y modificaciones de las disciplinas ofrecidas.
*   **Deportistas:** Gestión de atletas y su asignación a diferentes deportes.
*   **Socios:** Registro y control de los miembros del club.

El sistema implementa una arquitectura **MVT (Modelo-Vista-Template)** modular, asegurando escalabilidad y mantenimiento sencillo. Cuenta con un frontend responsivo y un panel de administración seguro.

## 2. Características Principales

*   **CRUD Completo:** Funcionalidad de Crear, Leer, Actualizar y Eliminar para todas las entidades (Deportes, Deportistas, Socios).
*   **Seguridad:** Vistas protegidas que requieren autenticación de 'staff' para operaciones de modificación (decorador `@staff_member_required`).
*   **Diseño Modular:** Separación lógica en tres aplicaciones independientes (`gestion_deportes`, `gestion_deportistas`, `gestion_socios`).
*   **Interfaz de Usuario:** Plantillas HTML5/CSS3 con herencia (`extends`), diseño limpio y navegación intuitiva.
*   **Testing:** Pruebas unitarias integradas para asegurar la calidad del código.

## 3. Instalación y Ejecución

Sigue estos pasos para levantar el proyecto en tu entorno local.

### Requisitos Previos
*   Python 3.10 o superior
*   Git

### Pasos

1.  **Clonar el repositorio:**
    ```powershell
    git clone https://github.com/AlejoGBazzana/django-club.git
    cd django-club
    ```

2.  **Crear y activar el entorno virtual:**
    ```powershell
    python -m venv venv
    .\venv\Scripts\Activate
    ```

3.  **Instalar dependencias:**
    ```powershell
    pip install -r requirements.txt
    ```

4.  **Aplicar migraciones:**
    ```powershell
    cd club_deportivo
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Crear un superusuario (Administrador):**
    ```powershell
    python manage.py createsuperuser
    ```

6.  **Ejecutar el servidor:**
    ```powershell
    python manage.py runserver
    ```

7.  **Acceso:**
    *   Sitio público: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
    *   Panel de Administración: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

## 4. Estructura del Proyecto

El proyecto sigue la convención estándar de Django:

*   `club_deportivo/` (Carpeta raíz del proyecto)
    *   `gestion_deportes/`: App para la lógica de disciplinas deportivas.
    *   `gestion_deportistas/`: App para la gestión de atletas.
    *   `gestion_socios/`: App para la administración de la masa societaria.
    *   `templates/`: Plantillas HTML globales y específicas por app.
    *   `static/`: Archivos CSS, imágenes y JS.

## 5. Roles del Equipo

| Integrante | Rol Principal | Responsabilidades |
| :--- | :--- | :--- |
| **Pedro** | Backend Developer | Desarrollo de modelos, vistas y lógica de negocio. |
| **Alejo** | Frontend / DevOps | Diseño de templates, estilos CSS y configuración del entorno. |
| **Colaborador** | QA / Testing | Pruebas unitarias y control de calidad. |

*(Nota: Roles asignados para propósitos de la entrega académica)*

---
&copy; 2025 Club Deportivo. Todos los derechos reservados.