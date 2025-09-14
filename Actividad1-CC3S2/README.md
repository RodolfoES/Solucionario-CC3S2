# Titulo : "Actividad 1: introducción devops, devsecops"
Nombre: José Rodolfo Estacio Sánchez  
**Fecha:** 05/09/2025   
**Tiempo invertido:** 2h   
## Contexto de entorno usado  
Winodows 11, Visual Studio Code como editor de texto principal y el   repositorio de las actividadaes se encuentra en GitHub. 
## 4.1 DevOps vs. cascada tradicional 
## Imagen de comparación : 
![](imagenes/devops-vs-cascada.png)
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

![](imagenes/silos-equipos.png)

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
     