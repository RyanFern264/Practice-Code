with open("file1.txt") as file:
    numbers1 = file.readlines()
with open("file2.txt") as file:
    numbers2 = file.readlines()
# list comprehension to get union of list 1 and list 2
result = [int(n.strip()) for n in numbers1 if n in numbers2]

print(result)

# dictionary comprehension to create then filter down a dictionary
import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {student:random.randint(1,100) for student in names}
print(student_scores)
passing_students = {student:student_scores[student] for student in student_scores if student_scores[student] >= 60}
#Or you can do this:
passing_students = {student:score for (student, score) in student_scores.items() if score >=60}
print(passing_students)

# Dict comprehension to create a dict called result that takes each word in the given sentence and calculates the number of letters in each word
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words = sentence.split()
result = {word:len(word) for word in words}
print(result)

# Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day:(temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)