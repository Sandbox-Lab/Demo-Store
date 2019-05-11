# Demo Store

>Práctica Demo Fullstack con __Django__, __Vue__ y __MySQL__

## Requerimientos
### Back-end
- python >= 3.7.3
- virtualenv >= 16.4.3

### Front-end
- node >= 8.9.1
- npm >= 5.5.1
- Vue-CLI >= 2.9.6

Si no tienes instaladas ninguna, aquí te digo como:

#### Python
Para instalar __python__ solo tienes que ir a la página [python.org/downloads](https://www.python.org/downloads/) y descargar la version exacta del proyecto o superior para tu sistema operativo. Aquí tienes la [última versiónn](https://www.python.org)

#### Virtualenv

Instala __virtualev__ desde __pip__, que es un sistema de gestión de paquetes para Python. Viene incluido por defecto desde Python 2.7.9 en adelante.

```sh
# Mira si ya tienes instalado pip y cuál version tienes
pip -V

# Descarga la última versión de virtualenv
pip install virtualenv

# Descarga la versión exacta de virtualenv
pip install virtualenv==16.4.3
```

#### Node
Para instalar __node.js__ solo tienes que ir a la página [nodejs.org/en/download](https://nodejs.org/en/download/) y descargar la version exacta de este proyecto o superior para tu sistema operativo. Aquí tienes la [última versión](https://nodejs.org).

#### NPM
Es el manejador de paquetes de __Node__.
```sh
# Ya viene instalado con node.js. Mira la version que tienes
npm --version
# o
npm -v
```

#### Vue CLI
Instalalo de manera global con __npm__.
```sh
$ npm install -g vue-cli

# Cuando ya se haya instalado, revisa la versión que tienes
vue --version
#o
vue -V
```


## Instalación

Ya hemos visto todos los requerimientos de este proyecto y como instalarlos. Ahora veremos cómo levantar el proyecto.

Clona el repositorio con __git__
```sh
git clone https://github.com/Sandbox-Lab/Demo-Store.git
```

o descargalo directamente.

Dentro del repositorio hay dos directorios principales `backend` y `frontend`. Comenzaremos por levantar el backend primero.

### Levantando el Backend

### Creando un Entorno

Para crear crear un entorno debes estar situando en el directorio `backend/`, depués ejecutas el siguiente comando:

```sh
virtualenv <directorio_del_entorno>
```

Por convencion le podemos llamar al directorio del entorno __env__. Quedaría así:

```sh
virtualenv env
```

### Activar y Desactivar Entorno Virtualenv

#### Windows

Para activar el entorno virtual en __Windows__ después de haberlo instalado, te situas en el directorio `backend/env/Scripts` y ejecutas el comando:

```sh
activate
```

Para desactivarlo:

```sh
deactivate
```

#### Mac o Linux

Para activar el entorno virtual en __Mac__ o __Linux__ te situas en el directorio `backend/env` y después ejecutas el siguiente comando:

```sh
source bin/activate
```

Para desactivarlo:

```sh
source bin/deactivate
```

#### Requerimientos

Situado en el directorio `backend/` se encuentra el archivo `requirements.txt` el cual contiene las dependencias a instalar.

```sh
# Ejecuta este comando para ver los requerimientos
cat requirements.txt
```

Instalaremos todos los requerimientos con __pip__ de la siguiente manera:

```sh
pip install -r requirements.txt
```

### Configurando la Base de Datos

Este proyecto ya tiene una configuración para la conexión de base de datos hecha. La puedes encontrar en el archivo `backend/src/demo_store/settings.py`.

```py
...
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'demo_store',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3307 ',
    }
}
...
```

Por defecto se está usando el motor de base de datos para MySQL pero puedes cambiarla por cualquier motor que soporte __Django__. [Ver la documentación](https://docs.djangoproject.com/en/2.2/ref/databases/#connection-management).

Esta es la configuración de la base de datos por defecto en el archivo `settings.py` que tiene un proyecto de __Django__ caundo se instala desde cero.

```sh
...
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
...
```

Cambia la configuración de la base de datos si así lo necesitas.

```py
...
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.base_de_datos_que_uso',
        'NAME': 'mi_base_de_datos',
        'USER': 'mi_usuario_de_base_de_datos',
        'PASSWORD': 'mi_contraseña_de_la_base_de_datos',
        'HOST': 'localhost',
        'PORT': 'mi_puerto',
    }
}
...
```

Más información para la configuración de la base de datos en la [documentación](https://docs.djangoproject.com/en/2.2/ref/databases/#connecting-to-the-database).

### Migraciones del Proyecto

Situado en el dirctorio `backend/src/` realiza las migraciones con el siguiente comando:

```sh
python manage.py migrate
```

### Correr el Servidor

Situado en el dirctorio `backend/src/` ejecuta el siguiente comando para levantar el servidor:

```sh
# Corre el servidor de desarrollo en localhost:8000
python manage.py runserver
```

Bien, ya has levantado el backend. Es hora de levantar el frontend.

## Levantando el Fontend

Estos es mucho más sencillos. Situados en el directorio `frontend/gui` ejecuta los siguientes comandos:

```sh
# Instala las dependecias
npm install

# Corre el servidor de desarrollo en localhost:8080
npm run dev
```

Listo, ya puedes probar este Demo.
