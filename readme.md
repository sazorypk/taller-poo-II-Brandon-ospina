# Student-Edu

**Autor:** Brandon Ospina Vargas

**Programa:** Programación de Software

**Jornada:** Noche

**Docente:** James Mosquera Rentería

## Descripción

Student-Edu es un sistema académico de consola para gestionar estudiantes, profesores, materias y calificaciones. Permite realizar operaciones básicas de consulta, creación, actualización y eliminación, además de mostrar estadísticas e información general del sistema. El proyecto está organizado por capas para separar modelos, servicios, almacenamiento e interfaz de usuario.

## Ejecución local

1. Instala Python 3.13 o superior.
2. Abre una terminal en la carpeta del proyecto.
3. El archivo `requirements.txt` no instala paquetes externos porque el proyecto usa solo la biblioteca estándar de Python.
4. Si deseas mantener el paso de instalación, puedes ejecutar:

```bash
pip install -r requirements.txt
```

5. Ejecuta el proyecto:

```bash
python main.py
```

## Estructura de carpetas

```text
Student-Edu/
├── main.py
├── readme.md
├── requirements.txt
├── data/
│   ├── students.json
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
