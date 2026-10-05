# Diseño y Consulta de Base de Datos NoSQL para Análisis de Datos

En un entorno de ciencia de datos e ingeniería de IA, se requiere almacenar y extraer información de una base de datos NoSQL. El objetivo es seleccionar la clave de partición adecuada para optimizar el rendimiento y facilitar la consulta de datos. Los datos a almacenar provienen de sensores de un sistema de monitoreo de infraestructura, incluyendo mediciones de temperatura, humedad y vibración. Cada registro incluye un timestamp, el identificador del sensor, y los valores de las mediciones. La base de datos debe permitir consultas eficientes por rango de tiempo y por identificador de sensor.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | creación de bases de datos NoSQL |
| **Nivel** | senior-l2 |
| **Tipo** | practical |
| **Tiempo estimado** | 8 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Un IDE o editor de código.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Verifica que el proyecto arranca sin errores.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Selección de Clave de Partición

**Objetivo:** Identificar y justificar la clave de partición óptima para la base de datos NoSQL.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Analiza los datos de entrada y las consultas más comunes.
- Evalúa las opciones de clave de partición y selecciona la más adecuada.
- Justifica tu elección considerando el rendimiento y la escalabilidad.

**Entregable:** Documento que describe la clave de partición seleccionada y la justificación.

<details>
<summary>Pistas de conocimiento</summary>

- Considera la distribución de los datos y las consultas frecuentes.
- Piensa en cómo la elección de la clave de partición afecta el rendimiento y la capacidad de consulta.

</details>

### Fase 2: Implementación de la Base de Datos

**Objetivo:** Implementar la base de datos NoSQL con la clave de partición seleccionada.

**Tiempo estimado:** 3 horas

**Instrucciones:**

- Crea la estructura de la base de datos utilizando la clave de partición elegida.
- Inserta un conjunto de datos de prueba.
- Verifica que la estructura y los datos se hayan almacenado correctamente.

**Entregable:** Base de datos NoSQL implementada con datos de prueba.

<details>
<summary>Pistas de conocimiento</summary>

- Asegúrate de que la estructura de la base de datos refleje la clave de partición seleccionada.
- Verifica la inserción y almacenamiento de los datos.

</details>

### Fase 3: Consulta de Datos

**Objetivo:** Realizar consultas eficientes en la base de datos NoSQL.

**Tiempo estimado:** 3 horas

**Instrucciones:**

- Realiza consultas por rango de tiempo y por identificador de sensor.
- Evalúa el rendimiento de las consultas.
- Documenta tus hallazgos y sugiere mejoras si es necesario.

**Entregable:** Documento con los resultados de las consultas y sugerencias de mejora.

<details>
<summary>Pistas de conocimiento</summary>

- Considera el tiempo de respuesta y la consistencia de los resultados.
- Piensa en posibles optimizaciones para mejorar el rendimiento.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es una clave de partición en una base de datos NoSQL y por qué es importante?
- **paraQueSirve**: ¿Para qué sirve la clave de partición en el contexto de nuestra base de datos NoSQL?
- **comoSeUsa**: ¿Cómo se usa la clave de partición en la implementación de la base de datos NoSQL?
- **erroresComunes**: ¿Qué errores comunes pueden ocurrir al seleccionar y usar una clave de partición inadecuada?
- **queDecisionesImplica**: ¿Qué decisiones implica la selección de la clave de partición en términos de rendimiento y escalabilidad?

## Criterios de Evaluacion

- Selección justificada de la clave de partición.
- Implementación correcta de la base de datos NoSQL.
- Realización de consultas eficientes y documentación de los resultados.

## Como trabajar con un asistente de IA

Hay dos caminos, elegi uno:

- **AGENTS.md** (recomendado) — instrucciones nativas del repo. Abri esta carpeta con tu agente local (Claude Code, Cursor, Codex, Copilot, Gemini) y las carga solo. Sabe que archivos faltan y con que comando se verifica, y completa el scaffold escribiendo en disco.
- **PROMPT_MEJORA.md** — para copiar y pegar en un chat (claude.ai, ChatGPT). Devuelve un ZIP con el proyecto. Sirve si no tenes un agente en el IDE.

Ninguno de los dos resuelve las fases del reto: eso es tu trabajo.

## Verificacion

El proyecto esta listo para trabajar cuando este comando corre sin errores:

```bash
pip install -r requirements.txt && pytest -q
```

---

*Reto generado automaticamente por Challenge Generator - Pragma*
