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

![](Imagenes/variables-de-entorno.png)

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

## 2) DNS: nombres, registros y caché
**Meta:** resolver `miapp.local` y observar TTL/caché.
1. **Hosts local:** agrega `127.0.0.1 miapp.local`

    Agrego la entrada en /etc/hosts para que el nombre "miapp.local" resuelva a 127.0.0.1.
Esto simula un dominio en mi máquina local, que sera muy útil para las pruebas de laboratorio.

    ![](imagenes/agregar_mi_app_local.png)

2. **Comprueba resolución:**

   * `dig +short miapp.local` (debe devolver `127.0.0.1`).
   * `getent hosts miapp.local` (muestra la base de resolución del sistema).

     ![](imagenes/gent_hosts_miapplocal.png)

3. **TTL/caché (conceptual):** con `dig example.com A +ttlunits` explica cómo el TTL afecta respuestas repetidas (no cambies DNS público, solo observa).

    Observo el campo TTL (Time To Live) en segundos,  indica cuánto tiempo una respuesta DNS puede guardarse en caché.
|   Si repito la consulta varias veces, mientras no expire el TTL, la respuesta proviene de caché y no del servidor autoritativo.

    ![](imagenes/dig_example.png)

    ![](imagenes/dig_example_2.png)

4. **Pregunta guía:** ¿Qué diferencia hay entre **/etc/hosts** y una zona DNS autoritativa? ¿Por qué el *hosts* sirve para laboratorio? Explica en 3–4 líneas.  

    `/etc/hosts` es un archivo local que fuerza la resolución de nombres a IPs específicas, útil para laboratorios y pruebas.
    Una zona DNS autoritativa, en cambio, se gestiona en servidores DNS y es distribuida a través de Internet, permitiendo escalabilidad y actualización centralizada.
    Para laboratorio usamos /etc/hosts porque no necesitamos montar un servidor DNS completo, basta con mapear el nombre a 127.0.0.1 en local.
