import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='proyectofinal',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)



try:
    with connection.cursor() as cursor:
        # Create a new record
        #sql = "INSERT INTO `asteroides` (`idnasa`,`name`,`diameter_min`, `diameter_max`, `hazardous`) VALUES (%s, %s, %s, %s, %s)"
        sql = "SELECT * FROM `asteroides`"
        cursor.execute(sql, )
        row = cursor.fetchone()
        while row is not None:
            print(type(row))
            #print(row['idnasa'])
            print(row)
            row = cursor.fetchone()
        


    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()
finally:
    connection.close()