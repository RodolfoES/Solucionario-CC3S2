## 1) HTTP: Fundamentos y herramientas
### Levanta la app con variables de entorno (12-Factor):
### 1. Variables de entorno de app.py: 
```python
##Se instala Flask
pip install flask
```
Se levanta la app Flask indicando el puerto 8080, el mensjae y la version. Esto aplica el principio 12-Factor: configuración por entorno en lugar de "quemar" valores en el código.
```python
##12-Factor:varibles de entorno
PORT=8080 MESSAGE="Hola CC3S2" RELEASE="v1" python app.py
```
La app empieza a escuchar en http://127.0.0.1:8080 y loguea en stdout.  

![](Imagenes/variables_de_entorno.png)

### 2. Inspección con "curl"  
#### Peticion GET:  
"curl -v http://127.0.0.1:8080/" se usa en modo verbose (-v) para ver las cabeceras de la petición y la respuesta.
La app responde con código 200 OK y un JSON que incluye "message" y "release".

![](imagenes/curl-v.png)

#### Peticion POST:  
"curl -i -X POST http://127.0.0.1:8080/" simula  una petición POST a la raíz. Como no existe ruta para POST en Flask,
la respuesta es 405 METHOD NOT ALLOWED. Esto demuestra cómo el servidor valida métodos HTTP.


![](imagenes/curl-i-X.png)

### Pregunta guía: ¿Qué campos de respuesta cambian si actualizas MESSAGE/RELEASE sin reiniciar el proceso? Explica por qué.
Como el proceso ya está en memoria, los cambios en el entorno del sistema no afectan al proceso que ya está corriendo. Para que cambien los valores de message y release en la respuesta JSON, es necesario detener la app y volver a ejecutarla con las nuevas variables.

### 3. Puertos abiertos con ss
Verificamos que puertos se escuchan en el puerto 8080  

![](imagenes/ss-lntp.png)

#### 4. Logs como flujo 
Levantamos algunas peticiones: 

![](imagenes/peticines_curl-s.png)
y nos genera:

![](imagenes/stdout_stderr.png)
