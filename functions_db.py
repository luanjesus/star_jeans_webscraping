import os
import sqlite3

from sqlite3 import Error

def database_conetion(db_name, sub_dir):
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..' + sub_dir + '/' + db_name + '.db'))
    con=None

    try:
        con=sqlite3.connect(path)
        print(f"Connection done on {db_name} ")
        return con
    except Error as ex:
        print(f"Error to connect on {db_name} | Path: {path} >>>>>>> Error: {ex} ")
    return None
    
def get_data(connection, query):
    c = connection.cursor()
   
    c.execute( query )        
    res = c.fetchall()

    print('Select Done')
    return res
    
def insert_data(data, table_name, connection, insert_type ):   
    try: 
        data.to_sql( 'showcase_hm', con=connection, if_exists=insert_type, index=False )
    except Error as ex:
        print(f'Error to insert data. Error >>>>  {ex}')
    finally:
        print('Data inserted successfully')
    
def delete_data(connection, query):
    c = connection.cursor()
    try: 
        c.execute( query)
        connection.commit()
    except Error as ex:
        print(f'Error to delete data. Error >>>>  {ex}')
    finally:
        print('Data deleted successfully')


def create_table(connection, query):
    c = connection.cursor()
    try: 
        c.execute( query)
    except Error as ex:
        print(f'Error to create table. Error >>>>  {ex}')
    finally:        
        print('Table created successfully')