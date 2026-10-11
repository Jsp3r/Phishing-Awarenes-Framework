import csv
import random

num_users: int = 50

def generate_data(num_users):
    records = []

    for i in range(num_users):
        user_id = f"user-{i + 1}"
        email = f"employee.{i + 1}@example.test"

        opened = random.random() < 0.75

        if opened:
            clicked = random.random() < 0.25
            reported = not clicked and random.random() < 0.30
        else:
            clicked = False
            reported = random.random() < 0.05

        records.append([
            user_id,
            email,
            int(opened),
            int(clicked),
            int(reported),
        ])

    return records


headers = [
    "User_ID",
    "Email",
    "Opened",
    "Clicked",
    "Reported",
]

with open(
        "phishing_metrics.csv",
        "w",
        newline="",
        encoding="utf-8"
) as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(generate_data(num_users))

print("Synthetic phishing dataset created successfully.")
print("File:phishing_metrics.csv")
