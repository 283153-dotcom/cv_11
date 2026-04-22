from sorting import random_numbers

class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):#vrátí počet bodů studenta na zadané pozici
        return self.scores[index]

    def count(self):# vrátí počet studentů (délku seznamu)
        return len(self.scores)


    def get_grade(self, index):
        points=self.get_by_index(index)
        grade=""
        if points>=90:
            grade="A"
        elif points>=80:
            grade="B"
        elif points>=70:
            grade="C"
        elif points>=60:
            grade="D"
        elif points>=50:
            grade="E"
        else:
            grade="F"

        return grade


    def find(self,score):
        positions = []
        searched_list=self.scores

        for i, item in enumerate(searched_list):
            if item == score:
                positions.append(i)

        return positions

    def get_sorted(self):
        my_copy = self.scores.copy()
        n = len(my_copy)
        # swtich=1

        for i in range(n - 1):  # šlo by to taky přes počet výměn, while switch !=0
            for idx in range(n - 1 - i):
                if my_copy[idx] > my_copy[idx + 1]:  # switch +=1
                    my_copy[idx], my_copy[idx + 1] = my_copy[idx + 1], my_copy[idx]

        return my_copy


def main():
    results=StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    print(f"Počet studentů: {results.count()}")
    for student_id in range(results.count()):
        print(f"Student {student_id}: {results.get_by_index(student_id)} points – {results.get_grade(student_id)}")
    print(f"Plný počet bodů měli studenti s ID: {results.find(100)}")
    print(f"Seřazené výsledky: {results.get_sorted()}")

    random_results = StudentsGrades(random_numbers(30, 0, 100))
    print(random_results.count())
    print(random_results.get_sorted())

if __name__ == "__main__":
    main()