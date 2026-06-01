import json
import os
from ..models.student import Student
from ..models.teacher import Teacher
from ..models.subject import Subject
from ..models.grade import Grade


class JSONStorage:
    """Maneja la persistencia de datos en archivos JSON"""

    def __init__(self, file_path="data/students.json"):
        self.file_path = file_path
        # Crear directorio data si no existe
        self._ensure_data_directory()

    def _ensure_data_directory(self):
        """Crea el directorio data si no existe"""
        data_dir = os.path.dirname(self.file_path)
        if data_dir and not os.path.exists(data_dir):
            os.makedirs(data_dir)
            print(f"📂 Directorio {data_dir} creado")

    def _get_default_entity_class(self):
        """Retorna la clase por defecto según el archivo actual"""
        file_name = os.path.basename(self.file_path).lower()

        if "teacher" in file_name:
            return Teacher
        if "subject" in file_name:
            return Subject
        if "grade" in file_name:
            return Grade
        return Student

    def load_entities(self, entity_cls=None, entity_label="registros"):
        """Carga entidades desde el archivo JSON"""
        entity_cls = entity_cls or self._get_default_entity_class()

        if not os.path.exists(self.file_path):
            print(
                f"📂 Archivo {self.file_path} no existe, creando uno nuevo...")
            return []

        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                items = [entity_cls.from_dict(item_data) for item_data in data]
                print(
                    f"📂 Cargados {len(items)} {entity_label} desde {self.file_path}")
                return items
        except json.JSONDecodeError:
            print(
                f"❌ Error al leer {self.file_path}, archivo JSON corrupto. Creando archivo nuevo...")

            # Hacer backup del archivo corrupto
            backup_file = f"{self.file_path}.backup"
            try:
                os.rename(self.file_path, backup_file)
                print(f"💾 Archivo corrupto guardado como {backup_file}")
            except:
                pass
            return []
        except Exception as e:
            print(f"❌ Error inesperado al cargar {entity_label}: {e}")
            return []

    def save_entities(self, items, entity_label="registros"):
        """Guarda lista de entidades en el archivo JSON"""
        try:
            # Asegurar que el directorio existe
            self._ensure_data_directory()

            # Convertir entidades a diccionarios
            data = [item.to_dict() for item in items]

            # Guardar en JSON con formato bonito
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)

            print(f"💾 {len(items)} {entity_label} guardados en {self.file_path}")
            return True
        except Exception as e:
            print(f"❌ Error al guardar {entity_label}: {e}")
            return False

    def load_students(self):
        """Compatibilidad: carga estudiantes desde el archivo JSON"""
        return self.load_entities(Student, "estudiantes")

    def save_students(self, students):
        """Compatibilidad: guarda estudiantes en el archivo JSON"""
        return self.save_entities(students, "estudiantes")

    def file_exists(self):
        """Verifica si el archivo JSON existe"""
        return os.path.exists(self.file_path)

    def get_file_info(self):
        """Retorna información sobre el archivo JSON"""
        if not self.file_exists():
            return {"exists": False}

        try:
            stat = os.stat(self.file_path)
            return {
                "exists": True,
                "size": stat.st_size,
                "modified": stat.st_mtime,
                "path": self.file_path
            }
        except Exception as e:
            return {"exists": True, "error": str(e)}
