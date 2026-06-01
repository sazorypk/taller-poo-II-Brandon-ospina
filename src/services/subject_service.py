from ..models.subject import Subject
from ..storage.json_storage import JSONStorage


class SubjectService:
    """CRUD de materias"""

    def __init__(self, storage=None):
        self.storage = storage or JSONStorage("data/subjects.json")
        self.subjects = self.storage.load_entities(Subject, "materias")

    def _save_changes(self):
        return self.storage.save_entities(self.subjects, "materias")

    def get_next_id(self):
        if not self.subjects:
            return 1

        return max(subject.id for subject in self.subjects) + 1

    # CREATE

    def add_subject(
        self,
        name,
        teacher_id,
        credits,
        description=""
    ):

        if not name.strip():
            print("❌ Nombre inválido")
            return False

        if credits <= 0:
            print("❌ Los créditos deben ser mayores a cero")
            return False

        new_subject = Subject(
            self.get_next_id(),
            name.strip(),
            teacher_id,
            credits,
            description.strip()
        )

        self.subjects.append(new_subject)

        if self._save_changes():
            print("✅ Materia agregada")
            return new_subject.id

        self.subjects.remove(new_subject)
        return False

    # READ

    def get_all_subjects(self):
        return self.subjects.copy()

    def get_subject_by_id(self, subject_id):

        for subject in self.subjects:
            if subject.id == subject_id:
                return subject

        return None

    # UPDATE

    def update_subject(
        self,
        subject_id,
        name=None,
        teacher_id=None,
        credits=None,
        description=None
    ):

        subject = self.get_subject_by_id(subject_id)

        if not subject:
            print("❌ Materia no encontrada")
            return False

        if name:
            subject.name = name

        if teacher_id:
            subject.teacher_id = teacher_id

        if credits:
            subject.credits = credits

        if description:
            subject.description = description

        return self._save_changes()

    # DELETE

    def delete_subject(self, subject_id):

        subject = self.get_subject_by_id(subject_id)

        if not subject:
            return False

        self.subjects.remove(subject)

        return self._save_changes()

    # SEARCH

    def search_subjects(self, term):

        term = term.lower()

        return [
            subject
            for subject in self.subjects
            if term in subject.name.lower()
        ]

    # STATISTICS

    def get_statistics(self):

        if not self.subjects:
            return {"total": 0}

        total_credits = sum(
            subject.credits
            for subject in self.subjects
        )

        return {
            "total": len(self.subjects),
            "credits": total_credits
        }
