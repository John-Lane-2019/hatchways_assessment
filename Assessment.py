import csv
import json
import sqlite3

connection = sqlite3.connect('c:\\assessment\\assessment.db') #connect to sqlite3 database
cursor = connection.cursor() # create cursor object

def createDB():
    #set file path variables, YOU MAY HAVE TO CUSTOMIZE THE FILE PATHS IF YOU DON'T DROP THE "assessment" FOLDER ON YOUR C DRIVE.
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
    bio = {'id': '', 'name': '', 'teacher': '', 'courseAverage': 0.0}
    hist = {'id': '', 'name': '', 'teacher': '', 'courseAverage': 0.0}
    math = {'id': '', 'name': '', 'teacher': '', 'courseAverage': 0.0}
    students = [] #drop the student dictionary objects in here. json object has to be enclosed with {}

    #query student A's id
    cursor.execute('SELECT id FROM students WHERE id = 1')
    s_id = cursor.fetchone()[0]
    student['id'] = s_id
    #query student A's name
    cursor.execute('SELECT name FROM students WHERE id = 1')
    name = cursor.fetchone()[0]
    student['name'] = name
    #query student A's overall average
    cursor.execute('SELECT ROUND(AVG(mark)) FROM marks WHERE student_id = 1')
    totalAverage = cursor.fetchone()[0]
    student['totalAverage'] = totalAverage
    
    #query student A's biology average
    cursor.execute('SELECT ROUND(AVG(mark)) FROM marks WHERE student_id = 1 AND test_id = 1 OR test_id = 2 OR test_id = 3' )
    courseAverage = cursor.fetchone()[0]
    bio['courseAverage'] = courseAverage
    
    #query bio course info
    cursor.execute('SELECT * FROM courses WHERE id = 1')
    bio_info = cursor.fetchone()
    bio['id'] = bio_info[0]
    bio['name'] = bio_info[1]
    bio['teacher'] = bio_info[2]
    #drop course object into student dictionary
    student['courses'].append(bio)

    #query student A's history average
    cursor.execute('SELECT ROUND(AVG(mark)) FROM marks WHERE student_id = 1 AND test_id = 4 OR test_id = 5' )
    courseAverage = cursor.fetchone()[0]
    hist['courseAverage'] = courseAverage

    #query history course info
    cursor.execute('SELECT * FROM courses WHERE id = 2')
    history_info = cursor.fetchone()
    hist['id'] = history_info[0]
    hist['name'] = history_info[1]
    hist['teacher'] = history_info[2]
    #drop course object into student dictionary
    student['courses'].append(hist)

    #query student A's math average
    cursor.execute('SELECT ROUND(AVG(mark)) FROM marks WHERE student_id = 1 AND test_id = 6 OR test_id = 7' )
    courseAverage = cursor.fetchone()[0]
    math['courseAverage'] = courseAverage

    #query math course info
    cursor.execute('SELECT * FROM courses WHERE id = 3')
    course_info = cursor.fetchone()
    math['id'] = course_info[0]
    math['name'] = course_info[1]
    math['teacher'] = course_info[2]
    student['courses'].append(math)
    
    #drop course object into student dictionary

    students.append(student)

    jsonObject = json.dumps(students, indent=4)# convert list to JSON object

    print(jsonObject) #output to the console

    with open(jsonFilePath, 'w') as outfile:
        json.dump(students, outfile, indent=4) # write to file







    
    
    

    
    


createDB()
produceJSON()