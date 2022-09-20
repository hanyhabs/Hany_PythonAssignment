#dict value avg
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    sumi=0
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for i in student_marks.keys():
        if(query_name==i):
            sumi= sum(student_marks[i])
print("%.2f" % round(sumi/3, 2))