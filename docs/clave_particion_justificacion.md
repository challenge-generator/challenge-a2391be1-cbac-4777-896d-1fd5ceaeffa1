# Justificación de Clave de Partición para DynamoDB

## Análisis del Patrón de Acceso

El sistema de monitoreo de infraestructura genera datos de sensores con un patrón de acceso específico que debe guiar el diseño de la clave de partición. Los datos provienen de múltiples sensores que registran mediciones de temperatura, humedad y vibración de forma continua. Cada registro incluye un identificador único del sensor, un timestamp preciso y los valores de las tres mediciones. La naturaleza de las consultas frecuentes determina directamente qué estrategia de partición maximiza el rendimiento.

Las consultas principales que el sistema debe soportar son dos: primera, la recuperación de todos los datos de un sensor específico dentro de un rango temporal, que representa el caso de uso más común cuando un analista necesita evaluar el comportamiento de un sensor particular durante un período de tiempo definido; segunda, la consulta de datos de múltiples sensores en un momento específico, que permite comparar las mediciones de diferentes sensores en un instante dado para detectar anomalías o correlaciones.

## Evaluación de Estrategias de Partición

### Opción 1: Solo sensor_id como clave de partición

Utilizar exclusivamente el identificador del sensor como clave de partición organizaría todos los registros de un mismo sensor en una única partición física de DynamoDB. Esta estrategia garantiza que las consultas por sensor sean extremadamente eficientes, ya que todos los datos relevantes residen en la misma partición y DynamoDB puede realizar operaciones de lectura secuencial. Sin embargo, esta aproximación presenta un problema crítico cuando un sensor genera datos con alta frecuencia: la partición correspondiente recibiría un volumen masivo de escrituras, creando un hotspot que degradaría el rendimiento y podría superar los límites de capacidad de esa partición específica. Además, las consultas que requieren datos de múltiples sensores en un rango de tiempo específico necesitarían realizar operaciones de escaneo paralelo o múltiples consultas a diferentes particiones, aumentando la latencia y el costo.

### Opción 2: Solo timestamp como clave de partición

Invertir la estrategia y utilizar únicamente el timestamp como clave de partición agruparía todos los registros generados en el mismo instante temporal en una partición. Esta aproximación favorece las consultas de instantáneas multiples sensores, permitiendo recuperar todos los registros de un momento dado con una sola operación de lectura. El problema fundamental es que los datos de un sensor específico quedarían dispersos a través de múltiples particiones, obligando a realizar consultas que abarcan muchas particiones diferentes para reconstruir el historial de un sensor. Esta dispersión elimina prácticamente cualquier beneficio de rendimiento para el caso de uso más frecuente del sistema.

### Opción 3: Clave de partición compuesta sensor_id más timestamp truncado

La tercera opción, y la seleccionada para este sistema, combina ambas dimensiones en una clave de partición compuesta. El identificador del sensor se utiliza como primer componente de la clave de partición, mientras que el timestamp se trunca a una granularidad específica (por ejemplo, a nivel de hora o día) y se utiliza como segundo componente. Esta estrategia híbrida ofrece un equilibrio óptimo entre los dos patrones de consulta principales: todos los datos de un sensor en un período truncado específico residen en la misma partición, permitiendo consultas eficientes por sensor y rango temporal; la dispersión de datos a través de múltiples particiones previene la formación de热点; y las consultas de instantáneas múltiples sensores pueden realizarse leyendo las particiones correspondientes a ese momento temporal.

## Distribución de Datos y Consideraciones de Escalabilidad

La clave de partición composta seleccionada debe evaluarse contra la distribución esperada de datos. El sistema de monitoreo contempla un número finito de sensores, típicamente entre decenas y cientos según el tamaño de la infraestructura. Cada sensor genera mediciones a intervalos regulares, probablemente cada pocos minutos o segundos dependiendo del tipo de medición. Con esta distribución, la clave de partición por sensor más timestamp horario garantiza que cada partición contenga un volumen manejable de datos mientras evita la concentración excesiva en una sola partición.

El truncamiento del timestamp a nivel de hora significa que cada partición contendrá las lecturas de un sensor específico durante una hora completa. Para un sensor que genera datos cada minuto, esto representa aproximadamente 60 registros por partición, un volumen perfectamente manejable para DynamoDB. Si la frecuencia de muestreo aumenta a cada segundo, la partición contendría 3600 registros, todavía dentro de rangos operativos normales. La granularidad del truncamiento puede ajustarse según la frecuencia real de muestreo: mayor granularidad (menos preciso) para muestreos muy frecuentes, menor granularidad (más preciso) para muestreos esporádicos.

## Índices Secundarios para Consultas Alternativas

Aunque la clave de partición compuesta optimiza los patrones de consulta principales, el sistema puede necesitar consultas adicionales que no se benefician de esta estructura. Un índice secundario global inverso, que invierta el orden de los componentes de la clave, permitiría consultas eficientes por rango temporal de todos los sensores sin especificar un identificador particular. Este índice representa una opción futura si los patrones de consulta evolucionan para incluir este caso de uso.