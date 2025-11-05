import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",  # replace with your MySQL password
    database="student_performance"
)

cursor = conn.cursor()
cursor.execute("SELECT subject, ROUND(AVG(marks),2) FROM students GROUP BY subject;")

print("Average Marks by Subject:\n")
for subject, avg_marks in cursor.fetchall():
    print(f"{subject} → {avg_marks}")

cursor.execute("SELECT name, SUM(marks) AS total FROM students GROUP BY name ORDER BY total DESC LIMIT 3;")
print("\nTop 3 Students:")
for name, total in cursor.fetchall():
    print(f"{name} → {total}")

conn.close()
