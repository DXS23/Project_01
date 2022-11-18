import sqlite3

def get_connection():
  connection = sqlite3.connect('teatchers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()


# connection = get_connection()
# cursor = connection.cursor()
# query = """
# Create table Students
# (Student_id INTEGER not NULL PRIMARY key, Student_name TEXT NOT NULL, School_id INTEGER NOT NULL);
# """
# cursor.execute(query)
# connection.close()
#
# connection = get_connection()
# cursor = connection.cursor()
# query = """
# Insert into Students (Student_id, Student_name, School_id)
# VALUES
# (201, 'Иван', 1),
# (202, 'Петр', 2),
# (203, 'Анастасия', 3),
# (204, 'Игорь', 4);
#  """
#

def get_student_inf(Student_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """
        select Student_id, Student_name, School_id, school_name 
        from Students
        join School using(school_id)
        WHERE Student_id = ?"""
        cursor.execute(select_query, (Student_id,))
        records = cursor.fetchone()
        print ("Данные по студенту")
        for row in records:
          print ("ID студента", row[0])
          print ("Имя студента", row[1])
          print ("ID школы", row[2])
          print("Название школы", row[3])
        close_connection(connection)
    except (Exception, sqlite3.Error) as error:
        print ("Ошибка в получении данных по студенту ", error)

get_student_inf(202)

