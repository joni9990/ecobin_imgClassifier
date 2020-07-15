import mysql.connector
from mysql.connector import Error
id = 2

connection = mysql.connector.connect(host='localhost',
                                     database='ecobin-db',
                                     user='root',
                                     password='rootroot')

def update_reciclable():
    try:
        sql_select_Query = "select reciclable from tipo"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        for row in records:
            reciclable = row[0]
           # print("Esta en: ",reciclable)

        #Update single record now
        sql_update_query = "Update tipo set reciclable = %s where id = %s"
        reciclable += 1
        val = (reciclable,id)
        cursor.execute(sql_update_query,val)
        connection.commit()
        cursor.execute(sql_select_Query)
        record = cursor.fetchone()
       # print("Pasa a: ",reciclable)

    except Error as e:
        print(e)
    finally:
            print("MySQL connection is closed reciclable")


def update_basura():
    try:

        sql_select_Query = "select basura from tipo"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        rows = cursor.rowcount
        for row in records:
            basura = row[0]
            #print("Esta en: ",basura)

        #Update single record now
        sql_update_query = "Update tipo set basura= %s where id = %s"
        basura += 1
        val = (basura,id)
        cursor.execute(sql_update_query,val)
        connection.commit()
        cursor.execute(sql_select_Query)
        record = cursor.fetchone()
        #print("Pasa a: ",basura)

    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
            print("MySQL connection is closed basura")


def update_vidrio():
    try:
        sql_select_Query = "select vidrio from material"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        rows = cursor.rowcount
        for row in records:
            vidrio = row[0]
            #print(vidrio)

        #Update single record now
        sql_update_query = "Update material set vidrio = %s where id = %s"
        vidrio += 1
        val = (vidrio,1)
        cursor.execute(sql_update_query,val)
        connection.commit()
        cursor.execute(sql_select_Query)
        record = cursor.fetchone()
        #print(vidrio)

    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
            print("Vidrio updated")


def update_metal():
    try:
        sql_select_Query = "select metal from material"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        rows = cursor.rowcount
        for row in records:

            metal = row[0]
            #print(metal)

        #Update single record now
        sql_update_query = "Update material set metal = %s where id = %s"
        metal += 1
        val = (metal,1)
        cursor.execute(sql_update_query,val)
        connection.commit()
        cursor.execute(sql_select_Query)
        record = cursor.fetchone()
        #print(metal)

    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
            print("Metal updated")


def update_plastico():
    try:
        sql_select_Query = "select plastico from material"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        rows = cursor.rowcount
        for row in records:
            plastico = row[0]
            #print(plastico)

        #Update single record now
        sql_update_query = "Update material set plastico = %s where id = %s"
        plastico += 1
        val = (plastico,1)
        cursor.execute(sql_update_query,val)
        connection.commit()
        cursor.execute(sql_select_Query)
        record = cursor.fetchone()
        #print(plastico)

    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
            print("Plastico updated")


def update_papel():
    try:
        sql_select_Query = "select papel from material"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        rows = cursor.rowcount
        for row in records:
            papel = row[0]
            #print(papel)

        #Update single record now
        sql_update_query = "Update material set papel = %s where id = %s"
        papel += 1
        val = (papel,1)
        cursor.execute(sql_update_query,val)
        connection.commit()
        cursor.execute(sql_select_Query)
        record = cursor.fetchone()
        #print(papel)

    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
            print("Papel updated")


def update_carton():
    try:
        sql_select_Query = "select carton from material"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        rows = cursor.rowcount
        for row in records:
            carton = row[0]
           # print(carton)

        #Update single record now
        sql_update_query = "Update material set carton = %s where id = %s"
        carton += 1
        val = (carton,1)
        cursor.execute(sql_update_query,val)
        connection.commit()
        cursor.execute(sql_select_Query)
        record = cursor.fetchone()
        #print(carton)

    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
            print("Carton updated")
