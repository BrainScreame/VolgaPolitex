student = input().split(",")
if ((student[1] == "муж" and int(student[4]) >= 180 and (student[5] == "спорт" or student[5] == "общая")) or
        (student[1] == "жен" and int(student[4]) >= 175 and (student[5] == "спорт" or student[5] == "общая"))):
    print(student[0] + "," + student[4] + "," + (student[3] if student[3] else "пропуск"))
else:
    print(student[0] + ",не подходит," + (student[3] if student[3] else "пропуск"))
