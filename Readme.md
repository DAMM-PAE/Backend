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
