class Node:
    def __init__(self, content, yes_branch=None, no_branch=None):
        self.content = content
        self.yes_branch = yes_branch
        self.no_branch = no_branch

class QuestionTree:
    def __init__(self):
        self.root = self.build_question_tree()

    def build_question_tree(self):
        # Preguntas relacionadas con síntomas
        cough = Node("Tos")
        fever = Node("Fiebre")
        breathlessness = Node("Dificultad para respirar")
        chest_pain = Node("Dolor en el pecho")

        # Construcción del árbol
        node1 = Node("¿Tiene tos?", yes_branch=cough, no_branch=fever)
        node2 = Node("¿Tiene dificultad para respirar?", yes_branch=breathlessness, no_branch=chest_pain)

        root = Node("¿Tiene fiebre?", yes_branch=node1, no_branch=node2)

        return root

    def ask_questions(self, node=None, symptoms=None):
        if node is None:
            node = self.root
        if symptoms is None:
            symptoms = []

        if node.yes_branch is None and node.no_branch is None:
            symptoms.append(node.content)
            return symptoms

        answer = input(f"{node.content} (sí/no): ").strip().lower()
        if answer == 's':
            symptoms.append(node.content)
            return self.ask_questions(node.yes_branch, symptoms)
        elif answer == 'n':
            return self.ask_questions(node.no_branch, symptoms)
        else:
            print("Por favor, responda con 's' o 'n'.")
            return self.ask_questions(node, symptoms)

class DiagnosisTree:
    def __init__(self):
        self.root = self.build_diagnosis_tree()

    def build_diagnosis_tree(self):
        # Diagnósticos
        asthma = Node("Asma")
        bronchitis = Node("Bronquitis")
        pneumonia = Node("Neumonía")
        common_cold = Node("Resfriado común")

        # Construcción del árbol de diagnóstico
        node1 = Node("¿Tiene tos?", yes_branch=bronchitis, no_branch=common_cold)
        node2 = Node("¿Tiene dificultad para respirar?", yes_branch=asthma, no_branch=node1)

        root = Node("¿Tiene fiebre?", yes_branch=pneumonia, no_branch=node2)

        return root

    def diagnose(self, symptoms, node=None):
        if node is None:
            node = self.root

        if node.yes_branch is None and node.no_branch is None:
            print(f"Diagnóstico: {node.content}")
            return

        if node.content in symptoms:
            self.diagnose(symptoms, node.yes_branch)
        else:
            self.diagnose(symptoms, node.no_branch)

if __name__ == "__main__":
    print("Bienvenido al sistema de diagnóstico de enfermedades respiratorias.")

    question_tree = QuestionTree()
    symptoms = question_tree.ask_questions()

    print("\nBasado en sus respuestas, se procederá al diagnóstico...\n")

    diagnosis_tree = DiagnosisTree()
    diagnosis_tree.diagnose(symptoms)
