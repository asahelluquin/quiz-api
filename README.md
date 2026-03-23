# Quiz Generator API

API desarrollada con FastAPI que permite generar preguntas tipo quiz a partir de un texto proporcionado por el usuario.

## URL pública de la API

https://quiz-api-50sd.onrender.com/

## Documentación interactiva (Swagger)

https://quiz-api-50sd.onrender.com/docs


---

## Descripción

Esta API recibe un texto como entrada y genera un conjunto de preguntas en formato tipo quiz. La implementación actual utiliza una lógica simplificada para garantizar compatibilidad con entornos de despliegue gratuitos.

---

## Endpoints

### GET /

Verifica que la API esté en funcionamiento.

Respuesta:

```json
{
  "message": "Quiz API funcionando"
}
