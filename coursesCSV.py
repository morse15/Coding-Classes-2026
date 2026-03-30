import csv

courses = []

with open("courses.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        course = {
            "name": row["courseName"],
            "score": int(row["score"]),
            "unit": int(row["numUnit"])
        }
        courses.append(course)
