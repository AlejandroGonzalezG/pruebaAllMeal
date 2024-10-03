# Prueba Simplilatam

Este README esta confeccionado para probar el repositorio creado para la prueba técnica de Simplilatam, explicaremos como corres el repositorio paso a paso partiendo por el backend.

## Backend

para comenzar, por simplicidad de la prueba, se mantuvo el frontend y el backend en el mismo repositorio (lo cual se separaría en repositorios distintos de ser una app no de prueba). En ese sentido debemos primero ingresar al backend para comenzar a ejecutar, debemos primero

```cd pruebaAllMeal/backend/prueba_all_meal```

Luego, debemos tomar el .env.example como ejemplo para crear nuestro propio .env, el cual nos servirá para guardar datos sensibles y que no sean de fácil acceso para un tercero.

Estando dentro de la carpeta activaremos el entorno virtual:

```source prueba_all_meal_env/bin/activate```

Con el entorno activado, podemos levantar los contenedores (las acciones del MakeFile no me funcionaban, por lo que, debemos usar docker como comandos para comenzar:

```docker-compose build```
```docker-compose up -d```

Para revisar los contenedores que se crearon podemos hacer:

```docker container ls -a```

Ahora, con nuestros contenedores corriendo en el backend, debemos crear un super usuario para acceder al Administrador de Django, para podemos hacer:

```docker-compose exec web python manage.py createsuperuser```

Seguimos las instrucciones y, teniendo creado nuestro super usuario podremos acceder a nuestro Administrador de Django en 'http://127.0.0.1:8000/admin/' con las credenciales creadas.
En el Administrador, dentro de lo que podemos hacer es crear Entradas, Platos Principales, Postres, Menús y Órdenes. Para crear un Menú, debemos tener creado al menos 1 Entrada, 1 Plato Principal y 1 Postre, ya que necesita de los 3 datos para crearse un menú.

Con esto, tendríamos corriendo nuestros 5 contenedores para el backend.

## Frontend

Para el frontend, debemos ingresar a la carpeta correspondiente así:

```cd pruebaAllMeal/frontend/AllMeal```

Una vez adentro, debemos instalar las dependencias:

```npm install```

Con nuestras dependencias instaladas podemos correr el frontend con:

```npm run dev```

Con esto, tanto el frontend como nuestro backend se encuentran ejecutandosé correctamente!.
