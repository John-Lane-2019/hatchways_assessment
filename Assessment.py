import csv
import json
import sqlite3

def createJSON():
    #set file path variables
    marksFilePath = r'C:\\assessment\\marks.csv'
    coursesFilePath = r'C:\\assessment\\courses.csv'
    studentsFilePath = r'C:\\assessment\\students.csv'
    testsFilePath = r'C:\\assessment\\tests.csv'
    jsonFilePath = r'C:\\assessment\\assessment.json'

    student = {'id': '', 'name': '', 'totalAverage': 0.0, 'courses': []  }
    students = [] #drop the student dictionary objects in here. json object has to be enclosed with {}
   
    connection = sqlite3.connect('c:\\assessment\\assessment.db')

    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER, name TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS courses (id INTEGER, name TEXT, teacher TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS tests (id INTEGER, course_id INTEGER, weight INTEGER)")
    cursor.execute("CREATE TABLE IF NOT EXISTS marks (test_id INTEGER, student_id INTEGER, mark INTEGER)")
    print(connection.total_changes)
   

   
    
    #todo





createJSON()