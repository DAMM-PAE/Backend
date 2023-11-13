# DAMM-PAE BACKEND

## Setup del proyecto

### Crear entorno virtual

#### Windows

```bash
python3.9 -m venv dammvenv
```

#### Linux

```bash
python3.9 -m venv dammvenv
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

### Actualizar pip

```bash
python -m pip install --upgrade pip
```

### Instalar dependencias (mirar cada vez que se modifica el archivo requirements.txt)

ir a la carpeta dammproject donde se encuentra el archivo requirements.txt:

```bash
pip install -r requirements.txt
```

### Crear un usuario administrador

```bash
python manage.py createsuperuser
```

### Migraciones

Esto se hace cada vez que se modifica el modelo de datos

```bash
python manage.py makemigrations predictBeers
```

```bash
python manage.py migrate
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

### ngrok

[Descarga](https://dashboard.ngrok.com/get-started/setup)

Tener en cuenta que el puerto que se utiliza es el 8000 y que hay que ejecutar la aplicación para que funcione.

```bash
ngrok http --domain=manually-pretty-barnacle.ngrok-free.app 8000
```
