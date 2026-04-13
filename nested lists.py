if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # 1. Extract all scores and find unique ones using a set
    # 2. Sort unique scores to find the second lowest (index 1)
    unique_scores = sorted(list(set([s[1] for s in students])))
    second_lowest_score = unique_scores[1]

    # 3. Collect names of all students with that second lowest score
    second_lowest_students = [s[0] for s in students if s[1] == second_lowest_score]

    # 4. Sort student names alphabetically and print each on a new line
    for name in sorted(second_lowest_students):
        print(name)
        