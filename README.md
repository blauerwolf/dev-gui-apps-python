# Desarrollo de Aplicaciones de escritorio con python

## Creación de la Base de Datos
```
python3
from src import app
app.create()
quit()
```

## Creación de usuarios de prueba
```
python3
from src import app
app.seed_db()
quit()
```

## Instalación de dependencias
>Desde la carpeta del proyecto
```
pip3 install -r requirements.txt
```