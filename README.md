# conference-rekognition-app

## Instalar dependencias
```
sudo apt install python3-pip
sudo apt install python3-flask
sudo apt install python3-waitress
```

En el directorio *server*, instalar los paquetes:
```
pip3 install -r requirements.txt
```

## Ejecutar aplicación modo desarrollo
En el directorio *raíz* (Linux y Mac):
```
export FLASK_APP=server
export FLASK_ENV=development
flask run
```

## Ejecutar aplicación modo producción
En el directorio *raíz*:
```
waitress-serve --call 'server:create_app'
```