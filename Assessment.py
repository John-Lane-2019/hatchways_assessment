import csv
import json
import sqlite3

connection = sqlite3.connect('c:\\assessment\\assessment.db') #connect to sqlite3 database
cursor = connection.cursor() # create cursor object

def createDB():
    #set file path variables
    marksFilePath = r'C:\\assessment\\marks.csv'
    coursesFilePath = r'C:\\assessment\\courses.csv'
    studentsFilePath = r'C:\\assessment\\students.csv'
    testsFilePath = r'C:\\assessment\\tests.csv'
    
    #create tables that CSV file data will be written to
    cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER NOT NULL UNIQUE PRIMARY KEY, name TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS courses (id INTEGER NOT NULL UNIQUE PRIMARY KEY, name TEXT, teacher TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS tests (id INTEGER NOT NULL UNIQUE PRIMARY KEY, course_id INTEGER, weight INTEGER)")
    cursor.execute("CREATE TABLE IF NOT EXISTS marks (test_id INTEGER NOT NULL UNIQUE PRIMARY KEY, student_id INTEGER, mark INTEGER)")

    #insert CSV file data into database tables
    studentFields = ('id', 'name')
    with open(studentsFilePath) as csvFile:
        scsvReader = csv.reader(csvFile, studentFields)
        for rows in scsvReader:
            if(rows[0].isdigit() and rows[1].isupper()):
                try:
                    cursor.execute('INSERT INTO students (id, name) VALUES (?,?)', (int(rows[0]), rows[1])) 
                    connection.commit()
                except:
                    pass   
    
    courseFields = ('id', 'name', 'teacher')
    with open(coursesFilePath) as csvFile:
        ccsvReader = csv.reader(csvFile, courseFields)
        for rows in ccsvReader:
            if(rows[0].isdigit()):
                try:
                    cursor.execute('INSERT INTO courses (id, name, teacher) VALUES (?, ?, ?)', (int(rows[0]), rows[1], rows[2]))
                    connection.commit()
                except:
                    pass

    testFields = ('id', 'course_id', 'weight')
    with open(testsFilePath) as csvFile:
        tcsvReader = csv.reader(csvFile, testFields)
        for rows in tcsvReader:
            if(rows[0].isdigit() and rows[1].isdigit() and rows[2].isdigit()):
                try:
                    cursor.execute('INSERT INTO tests (id, course_id, weight) VALUES (?, ?, ?)', (int(rows[0]), int(rows[1]), int(rows[2])))
                    connection.commit()
                except:
                    pass
    
    marksFields = ('test_id', 'student_id', 'mark')
    with open(marksFilePath) as csvFile:
        mcsvReader = csv.reader(csvFile, marksFields)
        for rows in mcsvReader:
            if(rows[0].isdigit() and rows[1].isdigit() and rows[2].isdigit()):
                try:
                    cursor.execute('INSERT INTO marks (test_id, student_id, mark) VALUES (?, ?, ?)', (int(rows[0]), int(rows[1]), int(rows[2])))
                    connection.commit()
                except:
                    pass

def produceJSON():
    jsonFilePath = r'C:\\assessment\\assessment.json'
    
    student = {'id': '', 'name': '', 'totalAverage': 0.0, 'courses': []  }
    students = [] #drop the student dictionary objects in here. json object has to be enclosed with {}
    
    #TO DO

createDB()