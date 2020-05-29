
# Metrobus CDMX Datapipeline

_Consume información de los datos abiertos de la CDMX correspondientes a la ubicación de unidades de metrobus, con base en la información geográfica (latitud y longitud) obtiene por medio de georversing de google información especifica de ubicación y ofrece un endpoint en GraphQL para el consumo de datos_

## Comenzando 

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._


### Pre-requisitos 📋

```
docker-compose
```

### Instalación usando docker-compose
_1. Clonar repositorio_
```bash
# Clonar repositorio
$ git clone https://github.com/sachiel/mb-pipeline.git
# Cambiar directorio de trabajo
$ cd mb-pipeline/
```
_2. Configuración de variables de entorno para proyecto_
```bash
# Crear archivo con variables de entorno necesarias
$ touch .env.dev
```
El archivo .env.dev debe contener la siguiente información
```bash
# Quitar los comentarios en el .env.dev final
DEBUG=1 # 1 is True, 0 is False
SECRET_KEY=^9q5ih7pf=hc8_&*x%-@ywl^mju$*y6sj$mfjf6j!75go=r77+  # random string
DJANGO_ALLOWED_HOSTS=*  # Todos los hosts permitidos
GOOGLE_APIKEY=AIzadhusSds_DMenaEdYPKDnjhpddd95xnvuw # apikey de google
CDMX_ROWS=207 # por defecto la respuesta máxima del API de CDMX/metrobus es de 207 registros

```
_3. Inicialización de proyecto con docker-compose_
```bash
# Configurar permisos de scripts de instalación y configuración
$ chmod +x bin/docker_build.sh # script que inicializa configuración de docker
$ chmod +x bin/fetch_data.sh # script que configura e introduce data inicial
# Inicializar configuración de docker
$ sudo bin/docker_build.sh # sudo es opcional, depende la configuracion de docker
# Configuración de base de datos y carga inicial de data
$ sudo bin/fetch_data.sh # sudo es opcional, depende la configuracion de docker
```
_4. Acceder desde navegador web a localhost:8000_

Al inicializar docker se activa un cronjob que descarga nueva información del API de CDMX cada 10 minutos.
## GraphQL Endpoint

_El endpoint de graphql es:_
```
http://localhost:8000/graphql
```
_Ejemplos de request a Graphql_
```bash
# Obtener listado de alcaldías disponibles
query {
  allCities{
    name
  }
}
```
```bash
# Obtener listado de unidades disponibles
query {
  allVehiclesAvailables{
    id
    label,
  }
}
```
```bash
# Consultar historial de ubicaciones/fechas de una unidad por su id
query {
  allVehicles(vehicleId: "1148"){
    edges {
      node {
        id,
        vehicleId,
        vehicleLabel,
        address,
        county,
        zipcode,
        city,
        dateUpdated
      }
    }
  }
}
```
```bash
# Consultar unidades que hayan estado en una alcaldía
query {
  allVehicles(city: "Gustavo A. Madero"){
    edges {
      node {
        id,
        vehicleId,
        vehicleLabel,
        address,
        county,
        zipcode,
        city,
        dateUpdated
      }
    }
  }
}
```

## Construido con 🛠️

* [Django](https://www.djangoproject.com/) - Framework web
* [Graphene](https://docs.graphene-python.org/projects/django/en/latest/) - GraphQL
* [Docker](https://docs.docker.com/) - Contenedor

## Autores ✒️

* **Rich O.** -  [sachiel](https://github.com/sachiel)

## Licencia

Este proyecto está bajo Licencia GPL3 [https://www.gnu.org/licenses/gpl-3.0.html](https://www.gnu.org/licenses/gpl-3.0.html)

---
⌨️ con ❤️ por [Rich. O](https://github.com/sachiel) :D
