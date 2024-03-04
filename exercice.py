import sys

class Exercice:
    def __init__(self, number, exercise, solution, difficulty):
        self.number = number
        self.exercise = exercise
        self.solution = solution
        self.difficulty = difficulty

    def display_exercice(self):
        print("Exercice" +{self.number}+":"+ {self.exercise})
        print("Solution:" +self.solution)
        print("Niveau d'indice:"+ {self.difficulty})

    @classmethod
    def load_exercises_from_file(cls, filename):
        exercises_list = []
        with open(filename, 'r') as file:
            lines = file.readlines()

        number, exercise, solution, difficulty = None, None, None, None

        for line in lines:
            line = line.strip()
            if line.startswith('='):
                # A new exercise block is starting
                if number is not None:
                    # If this is not the first block, add the previous exercise to the list
                    exercises_list.append(cls(number, exercise, solution, difficulty))

                # Reset variables for the new exercise block
                number, exercise, solution, difficulty = None, None, None, None
            elif line.startswith('Exercice'):
                number = int(line.split(':')[0].split()[1])
                exercise = line.split(':')[1].strip()
            elif line.startswith('Solution'):
                solution = line.split(':')[1].strip()
            elif line.startswith('Niveau d\'indice'):
                difficulty = line.split(':')[1].strip()

        # Add the last exercise to the list
        if number is not None:
            exercises_list.append(cls(number, exercise, solution, difficulty))

        return exercises_list

