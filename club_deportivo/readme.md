**Instalación**
- **Requisitos**: Python 3.10+ y Git instalados.
- Clona el repositorio (si no lo hiciste):

```powershell
cd C:\Users\Alejo\Documents\Proyectos_DJango
git clone <URL_DEL_REPO>
cd django-club\club_deportivo
```

- Crea y activa un entorno virtual (PowerShell):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

- Instala dependencias (si existe `requirements.txt`):

```powershell
pip install -r requirements.txt
# Si no existe requirements.txt instala Django
pip install django
```

- Crea y aplica migraciones:

```powershell
python manage.py makemigrations
python manage.py migrate
```

- Crea un superusuario para acceder al admin:

```powershell
python manage.py createsuperuser
```

- Ejecuta el servidor de desarrollo:

```powershell
python manage.py runserver
```

Abre `http://127.0.0.1:8000/` en tu navegador y `http://127.0.0.1:8000/admin` para el panel de administración.

**Descripción**
- Este proyecto es una aplicación sencilla para gestionar un club deportivo. Permite organizar deportes, deportistas y socios en aplicaciones separadas, ofrece vistas públicas para listar recursos y una interfaz de administración para gestionar datos.

**Características implementadas**
- **Apps**: `gestion_deportes`, `gestion_deportistas`, `gestion_socios`.
- **Modelos básicos**: entidades para `Deporte` y `Deportista` (revisa `gestion_deportes/models.py` y `gestion_deportistas/models.py`).
- **Vistas y plantillas**: plantillas en `templates/` (por ejemplo `templates/gestion_deportes/lista_deportes.html`) y plantilla base en `templates/base.html`.
- **Estilos**: tema oscuro deportivo en `static/css/base.css` y carga desde `templates/base.html`.
- **Admin**: interfaz de administración de Django disponible en `/admin` (registra modelos en `admin.py` para que aparezcan).

**Atajos y notas útiles**
- Si no ves tus modelos en el admin, añade en cada app el archivo `admin.py` con, por ejemplo:

```python
from django.contrib import admin
from .models import Deporte  # o Deportista

admin.site.register(Deporte)
```

- Crear datos de ejemplo rápidamente desde el shell:

```powershell
python manage.py shell

# Dentro del shell (Python):
from gestion_deportes.models import Deporte
from gestion_deportistas.models import Deportista

d = Deporte.objects.create(nombre='Fútbol')
p = Deportista.objects.create(nombre='Ana', edad=25)
# Si existe relación many-to-many: d.deportistas.add(p)
```

**Estructura importante**
- `manage.py` : script de administración.
- `club_deportivo/settings.py` : configuración del proyecto (apps instaladas, base de datos, staticfiles).
- `templates/` : plantillas base y específicas.
- `static/css/base.css` : estilos del tema oscuro.

¿Quieres que:
- registre automáticamente los modelos en `admin.py` (puedo añadir los archivos)?
- genere un fixture JSON con datos de ejemplo para cargar con `python manage.py loaddata <fixture>`?
- añada un `requirements.txt` con la versión de Django utilizada en desarrollo?

