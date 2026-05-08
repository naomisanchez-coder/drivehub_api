# 🚗 DriveHub API

API REST desarrollada con Django y Django REST Framework para administrar vehículos y sus dueños.

---

## 🛠️ Tecnologías usadas

- Python 3.x
- Django
- Django REST Framework (DRF)

---

## ⚙️ Instrucciones para ejecutar el servidor

### 1. Clona el repositorio
```bash
git clone https://github.com/naomisanchez-coder/drivehub_api.git
cd drivehub_api
```

### 2. Crea y activa el entorno virtual
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instala las dependencias
```bash
pip install django djangorestframework
```

### 4. Aplica las migraciones
```bash
python manage.py migrate
```

### 5. Ejecuta el servidor
```bash
python manage.py runserver
```

---

## 📌 Endpoints disponibles

### 👤 Owners (Dueños)

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | /api/owners/ | Lista todos los dueños |
| POST | /api/owners/ | Crea un nuevo dueño |
| PUT | /api/owners/{id}/ | Actualiza un dueño |
| DELETE | /api/owners/{id}/ | Elimina un dueño |
| GET | /api/owners/?search= | Busca dueños por nombre o licencia |

### 🚗 Vehicles (Vehículos)

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | /api/vehicles/ | Lista todos los vehículos |
| POST | /api/vehicles/ | Crea un nuevo vehículo |
| PUT | /api/vehicles/{id}/ | Actualiza un vehículo |
| DELETE | /api/vehicles/{id}/ | Elimina un vehículo |
| GET | /api/vehicles/?search= | Busca vehículos por marca o modelo |

---

## 📋 Ejemplos de uso

### Crear un dueño
```json
POST /api/owners/
{
    "name": "Carlos Pérez",
    "license_number": "LIC-001"
}
```

### Crear un vehículo
```json
POST /api/vehicles/
{
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2020,
    "owner": 1
}
```

### Respuesta con relación
```json
{
    "id": 1,
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2020,
    "owner": 1,
    "owner_name": "Carlos Pérez"
}
```
---

## ✅ Endpoints probados

Todos los endpoints fueron probados con **Postman**:

- ✅ GET /api/owners/ — Lista de dueños
- ✅ POST /api/owners/ — Crear dueño
- ✅ PUT /api/owners/{id}/ — Editar dueño
- ✅ DELETE /api/owners/{id}/ — Eliminar dueño
- ✅ GET /api/owners/?search= — Buscar dueño
- ✅ GET /api/vehicles/ — Lista de vehículos
- ✅ POST /api/vehicles/ — Crear vehículo
- ✅ PUT /api/vehicles/{id}/ — Editar vehículo
- ✅ DELETE /api/vehicles/{id}/ — Eliminar vehículo
- ✅ GET /api/vehicles/?search= — Buscar vehículo

