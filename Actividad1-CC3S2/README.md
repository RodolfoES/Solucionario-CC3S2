# Titulo : "Actividad 1: introducción devops, devsecops"
Nombre: José Rodolfo Estacio Sánchez  
**Fecha:** 05/09/2025   
**Tiempo invertido:** 4h   
## Contexto de entorno usado  
Winodows 11, Visual Studio Code como editor de texto principal y el   repositorio de las actividadaes se encuentra en GitHub. 
## 4.1 DevOps vs. cascada tradicional 
## Imagen de comparación : 
![](/Actividad1-CC3S2/Imagenes/comparativo.png)
## Por qué DevOps acelera y reduce riesgos en software para la nube frente a la cascada ? 
- **FeedBack**: Monitoreo muy continuo que sirve de retroalimentacion para el equipo, lo que garantiza una observabilidad casi en tiempo real.
- **Pequeños Cambios**: Esto hace que se eviten grandes cambios y se pueda hacer mas facil un rollback.
- **Automatizacion**: se eliminan poco a poco los errores que pueden ser causados por el hombre.
## Pregunta retadora: señala un contexto real donde un enfoque cercano a cascada sigue siendo razonable
- **Caso Real : Sistema Bancario**  
Los bancos usan sistema core, eso hace referencia a transferencias bancarias, emision de tarjetas, etc. Se trata de la columna vertebral del sistema bancario donde es usada ususalmente la cascada.
- **Criterios verificables**:
1. **Cumplimiento regulatorio estricto**  
   - Normativas como **PCI DSS** (para transacciones con tarjetas) o las exigencias de los bancos centrales.  
   - Requieren documentación exhaustiva, aprobación de auditores y pruebas de conformidad antes de desplegar cambios en producción.

2. **Impacto directo en la estabilidad financiera**  
   - Una falla puede generar pérdidas millonarias en minutos o afectar la confianza del mercado.  
   - Por eso se priorizan ciclos largos de prueba y certificación antes de liberar software.

**Trade-offs:**

- **Se gana:**  
  - Conformidad legal y regulatoria (evitar sanciones).  
  - Seguridad y confianza para clientes y auditores.  

- **Se pierde:**  
  - Velocidad de entrega (un release puede tardar semanas o meses).  
  - Menor flexibilidad para adaptarse rápidamente a nuevas funcionalidades o UX modernas.  

## 4.2 Ciclo tradicional de dos pasos y silos (limitaciones y anti-patrones)

![](/Actividad1-CC3S2/Imagenes/silos-equipos.png)

**Limitaciones del ciclo "construcción → operación" sin integración continua:**

1. **Grandes lotes de cambios**  
   - El código se acumula durante semanas o meses antes de ser liberado.  
   - Esto provoca que los defectos aparezcan en masa al final, aumentando el costo de corrección.

2. **Colas de defectos y tiempos de entrega largos**  
   - Los problemas reportados en el área producción tardan en llegar a los equipos de desarrollo.  
   - La falta de integración continua genera asimetrías de información y esto genera retrasos en la solución.

---

**Pregunta retadora: Anti-patrones y su impacto**

1. **Throw over the wall**  
   - Los equipos de desarrollo entregan el software a operaciones sin compartir contexto de sus cambios ejecutados .  
   - **Impacto:**  
     - Incidentes tardan más en resolverse ( El MTTR sube, este es el tiempo medio de reparación).  
     - Se repiten los mismos errores porque Ops no tiene trazabilidad ni criterios claros.

2. **Seguridad como auditoría tardía**  
   - La seguridad se revisa solo al final del ciclo, como una lista de chequeo antes del despliegue.  
   - **Impacto:**  
     - Vulnerabilidades críticas se detectan demasiado tarde, generando retrabajos costosos y tardios.  
     - Los parches apresurados o relaizados a ultimahora pueden traer consigo nuevas degradaciones, repitiendo incidentes en cada release.
## 4.3 Principios y beneficios de DevOps (CI/CD, automatización, colaboración)

**CI y CD en la práctica:**  
- **Integración continua (CI):** se busca integrar los cambios de código en lotes pequeños, verificando con pruebas automáticas cerca del repositorio. Esto reduce los conflictos y permite detectar errores justo después de que se introducen.  
- **Entrega continua (CD):** prepara estos cambios para ser desplegados de forma rápida y confiable en distintos entornos. El punto fuerte de la entrega continua está en que las actualizaciones pasen por pruebas y validaciones antes de llegar a el área de producción.  

**Automatización y colaboración:**  
- La automatización (builds, tests, despliegues) evita tareas repetitivas y asegura mejores resultados.  
- La colaboración se refuerza porque desarrollo y operaciones comparten métricas, logs y decisiones de despliegue en tiempo real.  

**Práctica Agile como precursora:**  
- Una reunión diaria ayuda a decidir qué cambios están listos para integrarse y cuáles deben esperar.  
- Una retrospectiva posterior permite ajustar las reglas del pipeline (por ejemplo, reforzar pruebas en áreas donde hubo fallos).  

**Indicador observable propuesto:**  
- Tiempo promedio desde que un "Pull Request" queda listo hasta que se despliega en un entorno de pruebas.  
- Cómo recolectarlo sin pagar herramientas: registrar las marcas de tiempo en los PR (GitHub/GitLab) y compararlas con los logs de despliegue almacenados en el sistema de integración. Con simples bitácoras y registros de commits se obtiene el dato sin depender de plataformas comerciales.

## 4.4 Evolución a DevSecOps (seguridad desde el inicio: SAST/DAST; cambio cultural)

**SAST vs. DAST:**  
- **SAST (Static Application Security Testing):** análisis estático que se ejecuta temprano, donde se revisa el código fuente y dependencias antes de compilar.  
- **DAST (Dynamic Application Security Testing):** pruebas dinámicas sobre la aplicación en ejecución, buscando vulnerabilidades mientras responde a peticiones.  
- Ubicación en pipeline: SAST se ejecuta durante la fase de build/CI, mientras que DAST se aplica en entornos de pruebas o preproducción dentro de CD.  

**Gate mínimo de seguridad con umbrales cuantitativos:**  
- **Umbral 1:** ningún hallazgo crítico o de severidad alta (CVSS ≥ 7.0) detectado por SAST puede pasar a producción.  
- **Umbral 2:** al menos un 80% de cobertura de rutas críticas de la aplicación debe ser evaluado en pruebas dinámicas (DAST).  

**Política de excepción:**  
- En caso de vulnerabilidad crítica no resuelta: se permite una excepción de 7 días, asignada a un **responsable específico** (ej. líder técnico).  
- Debe incluir un plan de corrección o mitigación temporal (por ejemplo, reglas en un WAF).  
- Pasado el plazo, la excepción caduca y el hallazgo bloquea el pipeline.  

**Pregunta retadora: Como evitar el “teatro de seguridad”?:**  
Cumplir listas de chequeo no garantiza reducción de riesgo. Dos señales de eficacia que pueden medirse son:  
1. **Disminución de hallazgos repetidos en escaneos sucesivos** → indica que el equipo corrige de raíz y no solo parchea.  
   - *Medición:* comparar informes de SAST/DAST de despliegues consecutivos.  
2. **Reducción del tiempo de remediación en vulnerabilidades críticas** → evidencia de respuesta ágil.  
   - *Medición:* registrar la fecha de detección en pipeline y la fecha del commit que corrige el fallo; el objetivo puede ser ≤ 48 h.

## 4.5 CI/CD y estrategias de despliegue

![Pipeline canary](/Actividad1-CC3S2/Imagenes/pipeline_canary.png)
**Escoge una estrategia para un microservicio**   
Para el microservicio de autenticación se aplica un **canary release**. Esta estrategia es la más usada porque:  
- Reduce el riesgo, esto queire decir que solo un porcentaje de usuarios prueba la nueva versión al inicio.  
- Permite observar métricas reales en producción sin exponer a todos los clientes.  
- Facilita el rollback inmediato si se detectan fallos.

---

**Tabla de Riesgos vs Mitigaciones**

| Riesgo | Mitigación |
|--------|------------|
| Regresión funcional (fallos en endpoints de autenticación) | Validación de contratos de API antes de promover. |
| Costo operativo del doble despliegue | Definir un límite de convivencia (ej. máximo 48 h de canary). |
| Manejo de sesiones activas| Usar “draining” de sesiones y esquemas compatibles para evitar cortes. |
--- 

**KPI primario de promoción/abortado:**  
- **Tasa de errores HTTP 5xx ≤ 0.1%** en una **ventana de observación de 1 hora** tras activar el canary.  

**Pregunta retadora – Métricas de negocio y técnicas deben coexistir:**  
Aunque el KPI técnico (5xx) se mantenga dentro de lo esperado, una caída en métricas de producto como la **tasa de conversión de login** indica que algo en la experiencia del usuario no funciona bien (ej. fallos de usabilidad o cambios en el flujo de autenticación).  
Por ello, los **gates deben considerar tanto métricas técnicas como de negocio**, ya que ambas influyen directamente en la calidad del servicio entregado.

## 4.6 Fundamentos prácticos sin comandos (evidencia mínima) 
### 1. HTTP – contrato observable
![](/Actividad1-CC3S2/Imagenes/http-evidencia.png)
**Hallazgos:**  
- Método: GET  
- Código de estado: 200   

### 2. DNS - nombres y TTL
![](/Actividad1-CC3S2/Imagenes/dns-ttl.png)
### 3.TLS - seguridad en tránsito
![](/Actividad1-CC3S2/Imagenes/tls-cert.png)
### 4. Puertos - estado de runtime
![](/Actividad1-CC3S2/Imagenes/puertos.png)

### 5. 12-Factor - port binding, configuración, logs
**Port binding:**  
El servicio no debe depender de un puerto fijo en el código. En su lugar, el puerto se parametriza mediante una **variable de entorno** (`PORT=8080`) o un archivo de configuración externo. Esto permite desplegar la misma aplicación en distintos entornos (desarrollo, pruebas, producción) sin modificar el código fuente.

**Configuración externa:**  
Las credenciales y endpoints no deben quedar incrustados en el repositorio. Deben manejarse mediante variables de entorno o sistemas de configuración centralizados. De esta forma, se facilita la rotación de claves y la reproducibilidad de despliegues.

**Logs:**  
Los logs se envían como **flujo estándar (stdout/stderr)** en tiempo de ejecución. Así, cualquier entorno (Docker, Kubernetes, sistema operativo) puede recolectarlos y almacenarlos en un agregador central. Esto evita depender de archivos locales rotados manualmente, los cuales dificultan la observabilidad y la recuperación post-incidente.

**Anti-patrón a evitar:**  
Guardar **credenciales en el código fuente**. Esto rompe la portabilidad, dificulta la rotación de secretos y expone la aplicación a filtraciones si el repositorio es compartido. Externalizar la configuración asegura mayor seguridad y consistencia.

### 6. Checklist de diagnóstico – incidente de intermitencia

1. **Contrato HTTP**  
   - *Objetivo:* comprobar método, código y cabeceras.  
   - *Evidencia esperada:* respuestas 200 con cabeceras de caché/traza.  
   - *Acción:* si hay 4xx/5xx inesperado, revisar despliegue reciente y considerar rollback.

2. **Resolución DNS**  
   - *Objetivo:* validar registros (A/CNAME) y TTL.  
   - *Evidencia esperada:* todas las consultas responden la misma IP o destino.  
   - *Acción:* si hay mezcla de respuestas por TTL alto, extender ventana de coexistencia o ajustar propagación.

3. **Certificado TLS**  
   - *Objetivo:* verificar CN/SAN, fechas y emisora.  
   - *Evidencia esperada:* cert válido, no caducado, CN/SAN coinciden con dominio.  
   - *Acción:* si falla, renovar el certificado antes de promover.

4. **Puertos en escucha**  
   - *Objetivo:* confirmar que el servicio escucha en el puerto esperado.  
   - *Evidencia esperada:* puerto 443/HTTP activo en el proceso correcto.  
   - *Acción:* si no está en escucha o hay conflicto, liberar y reconfigurar el binding.

5. **Correlación de trazas**  
   - *Objetivo:* seguir un `X-Request-ID` desde la entrada hasta logs backend.  
   - *Evidencia esperada:* mismo ID visible en todas las capas.  
   - *Acción:* si se pierde, habilitar propagación de trazas en el gateway o servicio intermedio.

6. **Evaluación de gates**  
   - *Objetivo:* revisar KPIs técnicos y de producto en ventana de observación.  
   - *Evidencia esperada:* errores 5xx ≤ 0.1% y conversión ≥ 95% baseline en 1 h.  
   - *Acción:* si algún KPI cae fuera de umbral, abortar despliegue y revertir.
### 4.7 Desafíos de DevOps y mitigaciones
     