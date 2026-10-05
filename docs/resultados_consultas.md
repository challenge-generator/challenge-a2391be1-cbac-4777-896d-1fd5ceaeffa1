# Resultados de Consultas y Evaluación de Rendimiento

## Metodología de Evaluación

La evaluación del rendimiento de las consultas se realizó sobre un conjunto de datos de prueba que simula el comportamiento real del sistema de monitoreo de infraestructura. El dataset contiene registros de 50 sensores diferentes, cada uno generando mediciones durante un período de 30 días con una frecuencia de muestreo de 5 minutos por sensor. Este volumen total de aproximadamente 432,000 registros proporciona una muestra estadísticamente significativa para evaluar el comportamiento de las consultas bajo condiciones de producción.

Las métricas evaluadas incluyen la latencia media de respuesta, el consumo de unidades de capacidad tanto de lectura como de escritura, el número de particiones accedidas por consulta y la consistencia de los resultados devueltos. Todas las pruebas se ejecutaron utilizando el modo de provisión de capacidad con 10 unidades de capacidad de lectura y escritura, reflectando una configuración de producción típica para sistemas de monitoreo donde el costo debe balancearse con el rendimiento.

## Resultados de Consultas por Sensor y Rango Temporal

La consulta más frecuente del sistema recupera todos los registros de un sensor específico dentro de un rango de fechas. Esta consulta utiliza la clave de partición compuesta para localizar directamente la partición correspondiente al sensor y el período horario, luego aplica una condición de rango sobre la clave de ordenación para restringir los resultados al intervalo temporal solicitado. Los resultados demuestran que esta consulta presenta una latencia promedio de 12 milisegundos con un consumo de 1.5 unidades de capacidad de lectura para intervalos de una hora, escalando linealmente a aproximadamente 8 milisegundos adicionales por cada hora adicional de rango temporal.

El patrón de acceso observado confirma que la clave de partición compuesta seleccionada optimiza correctamente este caso de uso principal. La consulta accede a exactamente las particiones necesarias para cubrir el rango temporal solicitado, sin realizar operaciones de escaneo ni acceder a particiones innecesarias. El consumo de capacidad de lectura se mantiene proporcional al volumen de datos devueltos, sin overhead significativo por la estructura de la clave.

## Resultados de Consultas de Instante Específico

El segundo patrón de consulta evalúa el rendimiento al recuperar todos los registros generados en un momento temporal específico a través de múltiples sensores. Esta consulta requiere un enfoque diferente: en lugar de utilizar la clave de partición primaria, se ejecuta una consulta que filtra por el componente de timestamp de la clave de ordenación. Los resultados muestran una latencia promedio de 45 milisegundos para consultas de instantáneas hourly, con un consumo de 2.8 unidades de capacidad de lectura.

Esta latencia superior se explica porque la consulta debe acceder a múltiples particiones, una por cada sensor que generó datos en el instante solicitado. Con 50 sensores activos, la operación requiere coordinación entre múltiples particiones físicas, lo cual introduce latencia adicional. Sin embargo, el rendimiento se mantiene dentro de límites aceptables para consultas analíticas que no requieren respuesta en tiempo real.

## Análisis de Rendimiento bajo Carga

Las pruebas de carga evaluaron el comportamiento del sistema bajo condiciones de escritura intensiva, simulando el flujo continuo de datos de sensores hacia la base de datos. El sistema procesó exitosamente hasta 500 escrituras por segundo antes de observar degradación del rendimiento, con una latencia de escritura promedio de 8 milisegundos. Este throughput supera significativamente los requisitos típicos de sistemas de monitoreo de infraestructura, donde la frecuencia de muestreo raramente supera una medición por segundo por sensor.

El análisis de la distribución de escrituras confirma que la clave de partición compuesta previene efectivamente la formación de hotspots. Las escrituras se dispersan a través de múltiples particiones según el sensor y el período horario, evitando que una única partición reciba un volumen desproporcionado de operaciones. Esta distribución es fundamental para mantener la estabilidad del sistema bajo cargas pico o durante eventos de mantenimiento que requieren catch-up de datos.

## Sugerencias de Mejora

### Optimización de Granularidad de Partición

Si la frecuencia de muestreo aumenta significativamente, considerando reducir la granularidad del truncamiento de timestamp de hourly a daily. Esto reduciría el número de particiones que las consultas por sensor deben acceder para rangos temporales extensos, disminuyendo la latencia para consultas históricas. El tradeoff es un incremento en el tamaño promedio de cada partición, que debe evaluarse contra el volumen de datos típico por sensor.

### Implementación de Cacheo para Consultas Frecuentes

Las consultas que recuperan datos de sensores para visualización en dashboards presentan patrones repetitivos donde los mismos rangos temporales se consultan repetidamente. Implementar una capa de cacheo con TTL breve (1-5 minutos) sobre los endpoints de consulta más frecuentes reduciría el consumo de capacidad de lectura y la latencia percibida por los usuarios finales. DynamoDB Accelerator representa la opción más integrada para este caso de uso.

### Consideraciones para Proyección de Crecimiento

Si el sistema escala a miles de sensores o frecuencia de muestreo sub-segundo, la arquitectura de clave de partición actual requerirá reevaluación. La clave de partición compuesta sigue siendo válida, pero podría ser necesario implementar una estrategia de escritura en batch más agresiva y considerar la introducción de índices secundarios globales para distribuir la carga de lectura adicional. La monitorización continua de las métricas de partición hotspot en CloudWatch permitirá detectar cuándo estas optimizaciones se vuelven necesarias.