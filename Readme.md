# DAMM-PAE BACKEND

## Setup del proyecto

### Crear entorno virtual

#### Windows

```bash
py -m venv dammvenv
````

#### Linux

```bash
python -m venv dammvenv
```

### Activar entorno virtual (mirar cada vez que se abre una nueva terminal)

Windows:

```bash
.\dammvenv\Scripts\activate
```

Linux:

```bash
source dammvenv/bin/activate
```

### Instalar dependencias (mirar cada vez que se modifica el archivo requirements.txt)

```bash
pip install -r requirements.txt
```

### Arrancar el servidor

En la carpeta dammproject donde se encuentra el archivo manage.py:

```bash
python manage.py runserver
```

### Nuevas dependencias

```bash
pip freeze > requirements.txt
```

### Crear un usuario administrador

```bash
python manage.py createsuperuser
```

### Migraciones

Esto se hace cada vez que se modifica el modelo de datos

```bash
python manage.py makemigrations <nombre_app>
```

```bash
python manage.py migrate
```

### Carpeta dammproject/utils

En esta carpeta se encuentran un script para limpiar la base de datos(TODOS LOS DATOS) y otro para inicializar la base de datos con datos de prueba.


### Cargar datos de prueba

```bash
http://127.0.0.1:8000/inicializarBaseDatos/
```

De esta manera se cargan los datos de prueba en la base de datos.

### Admin

```bash
http://127.0.0.1:8000/admin/
```

para acceder al panel de administración de django.
