from ..services.subject_service import SubjectService


class SubjectMenu:

    def __init__(self, subject_service=None):
        self.service = subject_service or SubjectService()

    def show_menu(self):
        print("\n" + "=" * 50)
        print("📚 GESTIÓN DE MATERIAS")
        print("=" * 50)
        print("1. Ver materias")
        print("2. Buscar materia por ID")
        print("3. Agregar materia")
        print("4. Actualizar materia")
        print("5. Eliminar materia")
        print("6. Buscar materia")
        print("7. Estadísticas")
        print("0. Volver")
        print("-" * 50)

    def get_input(self, mensaje, tipo=str):

        while True:

            try:

                valor = input(mensaje)

                if tipo == int:
                    return int(valor)

                return valor

            except ValueError:
                print("❌ Valor inválido")

    def display_subjects(self, subjects):

        if not subjects:
            print("❌ No hay materias")
            return

        print("\n📋 MATERIAS")
        print("📊 Total:", len(subjects))
        print("-" * 50)

        for subject in subjects:
            print(subject)

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

                self.display_subjects(
                    self.service.get_all_subjects()
                )

            elif option == "2":

                subject_id = self.get_input(
                    "ID: ",
                    int
                )

                print(
                    self.service.get_subject_by_id(subject_id)
                )

            elif option == "3":

                name = input("Nombre: ")

                teacher_id = self.get_input(
                    "ID profesor: ",
                    int
                )

                credits = self.get_input(
                    "Créditos: ",
                    int
                )

                description = input(
                    "Descripción: "
                )

                self.service.add_subject(
                    name,
                    teacher_id,
                    credits,
                    description
                )

            elif option == "4":

                subject_id = self.get_input(
                    "ID materia: ",
                    int
                )

                name = input("Nuevo nombre: ")

                self.service.update_subject(
                    subject_id,
                    name=name
                )

            elif option == "5":

                subject_id = self.get_input(
                    "ID materia: ",
                    int
                )

                self.service.delete_subject(
                    subject_id
                )

            elif option == "6":

                term = input("Buscar: ")

                self.display_subjects(
                    self.service.search_subjects(term)
                )

            elif option == "7":

                print(
                    self.service.get_statistics()
                )

            if option != "0":
                self.pause()
