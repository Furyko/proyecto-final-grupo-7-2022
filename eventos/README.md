proyecto-final-grupo-7-2022
Proyecto final para el "Informatorio Chaco: Etapa 2" del grupo 7, Comisión 4 del año 2022.

Pasos para ejecutar el proyecto localmente:
- Instalar dependencias:
```
  pip install -r requirements/base.txt
```
- Iniciar la base de datos PostgreSQL.
- Añadir en settings/local.py la información de la base de datos iniciada.
- Ejecutar el proyecto desde la raiz:
```
  python manage.py runserver
```