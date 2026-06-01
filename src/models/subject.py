from datetime import datetime

class Subject:
    """Modelo de materia"""

    def __init__(self, subject_id, name, teacher_id, credits, description=""):
        self.id = subject_id
        self.name = name
        self.teacher_id = teacher_id
        self.credits = credits
        self.description = description
        self.created_at = datetime.now().isoformat()

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "teacher_id": self.teacher_id,
            "credits": self.credits,
            "description": self.description,
            "created_at": self.created_at
        }

    @classmethod
    def from_dict(cls, data):
        subject = cls(
            data["id"],
            data["name"],
            data["teacher_id"],
            data["credits"],
            data.get("description", "")
        )

        subject.created_at = data.get(
            "created_at",
            datetime.now().isoformat()
        )

        return subject

    def __str__(self):
        return (
            f"ID: {self.id} | "
            f"Materia: {self.name} | "
            f"Profesor ID: {self.teacher_id} | "
            f"Créditos: {self.credits}"
        )