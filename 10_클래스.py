students = [
    {"name":"윤인성", "Korean":87, "math":98, "english":88, "science":95},
    {"name":"윤인성", "Korean":87, "math":98, "english":88, "science":95},
    {"name":"윤인성", "Korean":87, "math":98, "english":88, "science":95},
    {"name":"윤인성", "Korean":87, "math":98, "english":88, "science":95},
    {"name":"윤인성", "Korean":87, "math":98, "english":88, "science":95},
    {"name":"윤인성", "Korean":87, "math":98, "english":88, "science":95}
]

print("이름", "총점", "평균", sep="\t")

for student in students:
    #점수의 총합과 평균을 구합니다.
    score_sum = student["Korean"] + student["math"] + student["english"] + student["science"]
    score_average = score_sum / 4
    #출력합니다.
    print(student["name"], score_sum, score_average, sep="\t")