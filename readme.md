# Student-Edu

## Presentación del proyecto

**Nombre completo:** Brandon ospina vargas

Este proyecto es un sistema académico en consola que permite gestionar estudiantes, profesores, materias y calificaciones. La información se organiza mediante menús interactivos y se guarda en archivos JSON para conservar los datos entre ejecuciones.

## Instrucciones de ejecución

1. Abre una terminal en la carpeta del proyecto.
2. Como `requirements.txt` está vacío, no necesitas instalar dependencias externas.
3. Ejecuta el proyecto principal:

```bash
python main.py
```

## Estructura de carpetas

```text
Student-Edu/
├── main.py
├── README.md
├── requirements.txt
├── data/
│   ├── grades.json
│   ├── students.json
│   ├── subjects.json
│   └── teachers.json
└── src/
	├── __init__.py
	├── models/
	│   ├── __init__.py
	│   ├── grade.py
	│   ├── student.py
	│   ├── subject.py
	│   └── teacher.py
	├── services/
	│   ├── __init__.py
	│   ├── grade_service.py
	│   ├── student_service.py
	│   ├── subject_service.py
	│   └── teacher_service.py
	├── storage/
	│   ├── __init__.py
	│   └── json_storage.py
	└── ui/
		├── __init__.py
		├── grade_menu.py
		├── menu.py
		├── subject_menu.py
		└── teacher_menu.py
```
