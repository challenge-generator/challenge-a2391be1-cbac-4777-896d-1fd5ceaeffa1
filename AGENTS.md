# AGENTS.md

Instrucciones para el agente de IA que abra este repositorio (Claude Code, Cursor, Codex, Copilot, Gemini). Se cargan solas: no hay que pegar nada en ningun chat.

## Que es este repositorio

Es el codigo base de un reto de aprendizaje de Pragma: **Diseño y Consulta de Base de Datos NoSQL para Análisis de Datos**.

| | |
|---|---|
| Tema | creación de bases de datos NoSQL |
| Nivel | senior-l2 |
| Chapter | Ciencia de Datos — Ingeniero de IA |
| Especialidad | Ingeniero de IA |
| Stack | Python 3.13 / FastAPI 0.115 |
| Patron arquitectonico | capas estándar con persistencia NoSQL y API de consulta |
| Tiempo estimado | 8 horas |

## Receta del stack

Esqueleto obligatorio:

- `pyproject.toml o requirements.txt en la raiz`
- `app/main.py con la API de inferencia`
- `app/prompts/ con los templates versionados`
- `app/retrieval con la indexacion y la busqueda vectorial`
- `app/chains con la orquestacion (cadena o grafo)`
- `app/eval con el conjunto de evaluacion y las metricas`
- `tests/ con casos deterministas de la cadena`

Dependencias:

- fastapi 0.115.0
- uvicorn 0.30.1
- boto3 1.34.123
- pydantic 2.8.2
- python-dotenv 1.0.1
- pytest 8.2.0
- moto 5.0.0
- pandas 2.2.2
- poetry n/a

## Tu tarea

Dejar este proyecto en estado **verificable**: que el comando de verificacion corra sin errores. Escribi los archivos en disco, en este repositorio. No generes ZIPs ni archivos adjuntos.

En orden:

1. Corre `pip install -r requirements.txt && pytest -q` y mira que falla.
2. Completa lo que falte de la lista de abajo: manifiesto de dependencias, punto de entrada, capa de interfaz y las capas del patron declarado.
3. Arregla SOLO los errores que impiden compilar o arrancar.
4. Volve a correr `pip install -r requirements.txt && pytest -q` hasta que pase.
5. Pará ahí.

## Regla dura: las fases son trabajo del humano

**PROHIBIDO implementar los entregables de las fases.** El valor del reto esta en que la persona los resuelva. Tu trabajo es que tenga un proyecto que arranca; el hueco pedagogico se queda como esta.

No resuelvas nada de esto:

- **Fase 1 — Selección de Clave de Partición**: Documento que describe la clave de partición seleccionada y la justificación.
- **Fase 2 — Implementación de la Base de Datos**: Base de datos NoSQL implementada con datos de prueba.
- **Fase 3 — Consulta de Datos**: Documento con los resultados de las consultas y sugerencias de mejora.

Distincion operativa:

- **Arreglar** (si): import faltante, tipo que no existe, dependencia sin declarar, error de sintaxis, archivo referenciado que no existe.
- **No tocar** (no): logica de negocio incompleta, validaciones ausentes, secretos hardcodeados, APIs deprecadas que funcionan, concurrencia insegura, patrones mejorables. Eso es lo que la persona tiene que encontrar.

## Superficie de practica (NO completes)

Estos archivos SON el ejercicio de la persona. No los implementes; deja stubs. No toques la logica que el reto pide completar.

- [ ] `tests/test_dynamodb_repository.py` — El topic pide TDD/pruebas: este archivo es el ejercicio.
- [ ] `tests/test_sensor_service.py` — El topic pide TDD/pruebas: este archivo es el ejercicio.

## Lo que falta y tenes que completar

### 1. Archivos que la arquitectura declara (3 de 11)

La propuesta arquitectonica del reto los lista y no llegaron al repo. Crealos con implementacion real, respetando la capa en la que viven:

- [ ] `data/sample_data.json`
- [ ] `scripts/setup_dynamodb.py`
- [ ] `README.md`

### 2. Referencias colgando (3)

Salieron de un analisis estatico del codigo que SI esta en el repo. Cada una rompe la compilacion:

- [ ] `app/api/v1/endpoints.py` — `Settings.get`
      Se invoca `get` sobre `Settings`, pero esa clase no declara ese metodo. Agregalo con su implementacion real, o usa uno de los que si declara.
- [ ] `app/api/v1/endpoints.py` — `Settings.post`
      Se invoca `post` sobre `Settings`, pero esa clase no declara ese metodo. Agregalo con su implementacion real, o usa uno de los que si declara.
- [ ] `app/api/v1/endpoints.py` — `Settings.delete`
      Se invoca `delete` sobre `Settings`, pero esa clase no declara ese metodo. Agregalo con su implementacion real, o usa uno de los que si declara.

### Presentes (11)

- `pyproject.toml`
- `app/main.py`
- `app/config/settings.py`
- `app/models/sensor_data.py`
- `app/repositories/dynamodb_repository.py`
- `tests/test_dynamodb_repository.py`
- `app/services/sensor_service.py`
- `app/api/v1/endpoints.py`
- `tests/test_sensor_service.py`
- `docs/clave_particion_justificacion.md`
- `docs/resultados_consultas.md`

### Capas del patron declarado

Cada una tiene que existir como directorio real con al menos un archivo. Codigo plano en la raiz no satisface el patron.

- `app`
- `app/models`
- `app/repositories`
- `app/services`
- `app/api`
- `app/config`
- `tests`
- `data`

## Verificacion

```bash
pip install -r requirements.txt && pytest -q
```

El comando tiene que pasar SIN implementar los archivos de la superficie de practica: solo andamiaje.

Ese comando pasando es la definicion de "terminado" para vos.

## Convenciones que tenes que respetar

- Un solo ecosistema: no declares librerias de otro lenguaje ni mezcles gestores de paquetes.
- Toda libreria que uses tiene que estar declarada en el manifiesto de dependencias.
- Todo import declarado tiene que usarse; todo tipo usado tiene que existir o venir de una dependencia declarada.
- El patron es **capas estándar con persistencia NoSQL y API de consulta**: los contratos (interfaces, puertos) los define la capa interna y los implementa la externa, nunca al revés.
- Los archivos que crees llevan implementacion real, no stubs: sin `TODO`, sin cuerpos vacios, sin `// getters y setters`.

## Contexto del candidato

Sirve para calibrar el nivel del codigo, no para resolver las fases.

- Perfil: Chapter Ciencia de Datos, Especialidad Ingeniero IA, Tecnología NoSQL, Senior
- Brecha que el reto ataca: Selecciona la clave partición adecuada para bases de datos NoSQL y extraer información de ellas. Candidato con experiencia en ciencia de datos e ingeniería de IA.

---

*Generado por Challenge Generator — Pragma. `README.md` tiene el enunciado completo del reto para la persona. `PROMPT_MEJORA.md` es la variante para pegar en un chat, si se prefiere ese flujo.*
