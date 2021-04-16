import pyodbc
import mysql.connector

class databaseQuery:
  def getCatalog(self,names,ids, links):

    # for driver in pyodbc.drivers():
    #     print(driver)
    # server ='DESKTOP-MG8TJIG'
    server = 'DESKTOP-E8VFGUU'
    database ='stock_database'
    username = 'root'
    password = 'Louis_Josh_SQL'

    try:
        conn = mysql.connector.connect(user='root', password = 'Louis_Josh_SQL', host='127.0.0.1', database='stock_database')

    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
      else:
        print(err)


    cursor = conn.cursor()

    # class_name = 'Calculus I for the Mathematical and Physical Sciences'
    #cursor.execute('INSERT INTO sample VALUES (1,2)')
    #cursor.execute('SELECT courseid FROM math_courses WHERE course_name=\'' + class_name + '\';')
    #cursor.execute('SELECT courseid FROM math_courses WHERE course_name=\'Calculus I for the Mathematical and Physical Sciences\';')
    cursor.execute('SELECT * FROM math_courses')

    coursenames = []
    courseids = []
    courselinks = []
    for row in cursor:
        coursename,courseid,link = row
        coursenames.append(coursename)
        courseids.append(courseid)
        courselinks.append(link)
        # print(coursename)
        # print(courseid)


    names = coursenames
    ids = courseids
    links = courselinks
    conn.commit()
    cursor.close()
    conn.close()
    return names,ids,links
