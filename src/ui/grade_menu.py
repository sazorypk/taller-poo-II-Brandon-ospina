from ..services.grade_service import GradeService


class GradeMenu:

    def __init__(self, grade_service=None):
        self.service = grade_service or GradeService()

    def show_menu(self):

        print("\n" + "=" * 50)
        print("📝 GESTIÓN DE CALIFICACIONES")
        print("=" * 50)
        print("1. Ver calificaciones")
        print("2. Buscar calificación")
        print("3. Registrar nota")
        print("4. Actualizar nota")
        print("5. Eliminar nota")
        print("6. Estadísticas")
        print("0. Volver")
        print("-" * 50)

    def get_input(self, mensaje, tipo=str):

        while True:

            try:

                valor = input(mensaje)

                if tipo == int:
                    return int(valor)

                if tipo == float:
                    return float(valor)

                return valor

            except ValueError:
                print("❌ Valor inválido")

    def display_grades(self, grades):

        if not grades:
            print("❌ No hay registros")
            return

        print("\n📋 CALIFICACIONES")
        print("📊 Total:", len(grades))
        print("-" * 50)

        for grade in grades:
            print(grade)

    def pause(self):
        print("\n⏸️  Presiona Enter para continuar...")
        input()

    def run(self):

        while True:

            self.show_menu()

            option = input("Seleccione: ")

            if option == "0":
                break

            elif option == "1":

                self.display_grades(
                    self.service.get_all_grades()
                )

            elif option == "2":

                grade_id = self.get_input(
                    "ID: ",
                    int
                )

                print(
                    self.service.get_grade_by_id(
                        grade_id
                    )
                )

            elif option == "3":

                student_id = self.get_input(
                    "ID estudiante: ",
                    int
                )

                subject_id = self.get_input(
                    "ID materia: ",
                    int
                )

                grade = self.get_input(
                    "Nota: ",
                    float
                )

                exam_type = input(
                    "Tipo evaluación: "
                )

                date = input(
                    "Fecha (YYYY-MM-DD): "
                )

                self.service.add_grade(
                    student_id,
                    subject_id,
                    grade,
                    exam_type,
                    date
                )

            elif option == "4":

                grade_id = self.get_input(
                    "ID nota: ",
                    int
                )

                new_grade = self.get_input(
                    "Nueva nota: ",
                    float
                )

                self.service.update_grade(
                    grade_id,
                    new_grade
                )

            elif option == "5":

                grade_id = self.get_input(
                    "ID nota: ",
                    int
                )

                self.service.delete_grade(
                    grade_id
                )

            elif option == "6":

                print(
                    self.service.get_statistics()
                )

            if option != "0":
                self.pause()
