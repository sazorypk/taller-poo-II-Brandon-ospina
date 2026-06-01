from datetime import datetime

class Grade:
    """Modelo de calificación"""

    def __init__(
        self,
        grade_id,
        student_id,
        subject_id,
        grade,
        exam_type,
        date
    ):
        self.id = grade_id
        self.student_id = student_id
        self.subject_id = subject_id
        self.grade = grade
        self.exam_type = exam_type
        self.date = date
        self.created_at = datetime.now().isoformat()

    def to_dict(self):
        return {
            "id": self.id,
            "student_id": self.student_id,
            "subject_id": self.subject_id,
            "grade": self.grade,
            "exam_type": self.exam_type,
            "date": self.date,
            "created_at": self.created_at
        }

    @classmethod
    def from_dict(cls, data):
        grade = cls(
            data["id"],
            data["student_id"],
            data["subject_id"],
            data["grade"],
            data["exam_type"],
            data["date"]
        )

        grade.created_at = data.get(
            "created_at",
            datetime.now().isoformat()
        )

        return grade

    def is_passing(self):
        return self.grade >= 3.0

    def __str__(self):
        return (
            f"ID: {self.id} | "
            f"Estudiante: {self.student_id} | "
            f"Materia: {self.subject_id} | "
            f"Nota: {self.grade}"
        )