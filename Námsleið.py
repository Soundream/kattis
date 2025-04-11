import sys
inputs = sys.stdin.read().split("\n")

# Solution:
# build the adjacency list
# then use a BFS to find the number of layers


from collections import deque

number_of_courses = int(inputs[0])

semester = [1] * (number_of_courses)
in_degree = [0] * (number_of_courses)
adjacency_list = [[] for _ in range(number_of_courses)]

# build adjacency list
for r in range(0, number_of_courses):
    course_prerequisites = list(map(int, inputs[r+1].split()))
    in_degree[r] = course_prerequisites[0]
    for course in course_prerequisites[1:]:
        adjacency_list[course-1].append(r+1)

# then use a BFS to find the number of layers
def BFS(semester, in_degree, adjacency_list):
    queue = deque()
    max = 1
    count = 0
    for i in range(len(in_degree)):
        if in_degree[i] == 0:
            queue.append(i)

    # if initially no course can be taken
    if not queue:
        return 0

    while queue:
        current = queue.popleft()
        count += 1
        for neighbor in adjacency_list[current]:
            related_course = neighbor-1
            in_degree[related_course] -= 1
            if in_degree[related_course] == 0:
                queue.append(related_course)
                max = semester[current] + 1
                semester[related_course] = max
    
    # cycle check
    if count < len(semester):
        return 0
    return max
    

max_semester = BFS(semester, in_degree, adjacency_list)

if max_semester == 0:
    print("Omogulegt!")
else:
    print("Mogulegt!")
    max_semester = max(semester)
    print(max_semester)
    semester_courses = [[] for _ in range(max_semester+1)]
    for course, sem in enumerate(semester):
        semester_courses[sem].append(course+1)

    for sem in range(1, max_semester+1):
        print(" ".join(map(str, [len(semester_courses[sem])]+semester_courses[sem])))