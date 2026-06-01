from ..models.grade import Grade
from ..storage.json_storage import JSONStorage


class GradeService:

    def __init__(self, storage=None):

        self.storage = storage or JSONStorage(
            "data/grades.json"
        )

        self.grades = self.storage.load_entities(Grade, "calificaciones")

    def _save_changes(self):
        return self.storage.save_entities(self.grades, "calificaciones")

    def get_next_id(self):

        if not self.grades:
            return 1

        return max(g.id for g in self.grades) + 1

    # CREATE

    def add_grade(
        self,
        student_id,
        subject_id,
        grade,
        exam_type,
        date
    ):

        if grade < 0 or grade > 5:
            print("❌ La nota debe estar entre 0 y 5")
            return False

        new_grade = Grade(
            self.get_next_id(),
            student_id,
            subject_id,
            grade,
            exam_type,
            date
        )

        self.grades.append(new_grade)

        if self._save_changes():
            return new_grade.id

        self.grades.remove(new_grade)

        return False

    # READ

    def get_all_grades(self):
        return self.grades.copy()

    def get_grade_by_id(self, grade_id):

        for grade in self.grades:
            if grade.id == grade_id:
                return grade

        return None

    # UPDATE

    def update_grade(
        self,
        grade_id,
        new_grade=None
    ):

        grade = self.get_grade_by_id(grade_id)

        if not grade:
            return False

        if new_grade is not None:

            if 0 <= new_grade <= 5:
                grade.grade = new_grade
            else:
                return False

        return self._save_changes()

    # DELETE

    def delete_grade(self, grade_id):

        grade = self.get_grade_by_id(grade_id)

        if not grade:
            return False

        self.grades.remove(grade)

        return self._save_changes()

    # SEARCH

    def get_student_grades(
        self,
        student_id
    ):

        return [
            grade
            for grade in self.grades
            if grade.student_id == student_id
        ]

    # STATISTICS

    def get_statistics(self):

        if not self.grades:
            return {"total": 0}

        average = sum(
            grade.grade
            for grade in self.grades
        ) / len(self.grades)

        return {
            "total": len(self.grades),
            "average": average
        }
