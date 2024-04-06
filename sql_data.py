import pyodbc
from extract_data import agg_transaction,agg_user, map_transaction,map_user,top_user,top_transaction
import pandas as pd
def sql_schemadef():
    """
    This function is to create database and tables (channel,playlist, video, comment)
    :return: None
    """
    # creating data base
    server = r'Purna\SQLEXPRESS'
    database = 'master'
    username = 'sa'
    password = 'sqlserver'
    driver = '{SQL Server}'
    conn = pyodbc.connect(
        'DRIVER=' + driver + ';SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password,
        autocommit=True)
    cursor = conn.cursor()
    new_database_name = 'phonepe'
    cursor.execute('CREATE DATABASE ' + new_database_name)

    cursor.execute('USE phonepe')

    # creating tables
    sql_create_Agg_Transaction_table = '''
    CREATE TABLE Agg_Transaction (
        State VARCHAR(255),
        Year INT,
        Quarter INT,
        Transaction_Type VARCHAR(255),       
        Transaction_Count INT,
        Transaction_Amount FLOAT       
    )
    '''
    cursor.execute(sql_create_Agg_Transaction_table)

    sql_create_Agg_User_table = '''
       CREATE TABLE Agg_User (
           State VARCHAR(255),
           Year INT,
           Quarter INT,
           Registered_Users BIGINT,       
           App_Opens BIGINT
                  
       )
       '''
    cursor.execute(sql_create_Agg_User_table)

    sql_create_Map_Transaction_table = '''
       CREATE TABLE Map_Transaction (
           State VARCHAR(255),
           Year INT,
           Quarter INT,
           District VARCHAR(255),       
           Count INT,
           Amount FLOAT       
       )
       '''
    cursor.execute(sql_create_Map_Transaction_table)

    sql_create_Map_User_table = '''
       CREATE TABLE Map_User (
           State VARCHAR(255),
           Year INT,
           Quarter INT,
           District VARCHAR(255),       
           App_Opens INT,
           Registered_User INT       
       )
       '''
    cursor.execute(sql_create_Map_User_table)

    sql_create_Top_Transaction_District_table = '''
       CREATE TABLE Top_Transaction_District (
           State VARCHAR(255),
           Year INT,
           Quarter INT,
           District VARCHAR(255),       
           Amount FLOAT,
           Count INT       
       )
       '''
    cursor.execute(sql_create_Top_Transaction_District_table)

    sql_create_Top_Transaction_Pincode_table = '''
       CREATE TABLE Top_Transaction_Pincode (
           State VARCHAR(255),
           Year INT,
           Quarter INT,
           Pincode VARCHAR(255),       
           Amount FLOAT,
           Count INT       
       )
       '''
    cursor.execute(sql_create_Top_Transaction_Pincode_table)

    sql_create_Top_User_District_table = '''
       CREATE TABLE Top_User_District (
           State VARCHAR(255),
           Year INT,
           Quarter INT,
           District VARCHAR(255),       
           Registered_Users INT      
       )
       '''
    cursor.execute(sql_create_Top_User_District_table)

    sql_create_Top_User_Pincode_table = '''
       CREATE TABLE Top_User_Pincode (
           State VARCHAR(255),
           Year INT,
           Quarter INT,
           Pincode VARCHAR(255),       
           Registered_User INT     
       )
       '''
    cursor.execute(sql_create_Top_User_Pincode_table)


def sql_data_insert():
    server = r'Purna\SQLEXPRESS'  # Server name or IP address
    database = 'master'  # Default database (system database)
    username = 'sa'  # Username
    password = 'sqlserver'  # Password
    driver = '{SQL Server}'
    conn = pyodbc.connect(
        'DRIVER=' + driver + ';SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password,
        autocommit=True)
    cursor = conn.cursor()

    # SQL query to check if the database exists
    sql_query = "SELECT name FROM sys.databases WHERE name = ?"
    cursor.execute(sql_query, 'phonepe')
    row = cursor.fetchone()
    if row is None:
        sql_schemadef()
    cursor.execute('USE phonepe')
    df = pd.DataFrame(agg_transaction())
    sql_insert = """
                    INSERT INTO Agg_Transaction ( 
                    State, Year, Quarter, Transaction_Type, Transaction_Count, Transaction_Amount
                    )
                  VALUES (?, ?, ?, ?, ?, ?)
                """

    # Insert data into SQL table from DataFrame
    for index, row in df.iterrows():
        cursor.execute(sql_insert, tuple(row))

    df = pd.DataFrame(agg_user())
    sql_insert = """
                        INSERT INTO Agg_User ( 
                        State, Year, Quarter, Registered_Users, App_Opens
                        )
                      VALUES (?, ?, ?, ?, ?)
                    """

    # Insert data into SQL table from DataFrame
    for index, row in df.iterrows():
        cursor.execute(sql_insert, tuple(row))

    df = pd.DataFrame(map_transaction())
    sql_insert = """
                            INSERT INTO Map_Transaction ( 
                            State, Year, Quarter, District, Count, Amount
                            )
                          VALUES (?, ?, ?, ?, ?, ?)
                        """

    # Insert data into SQL table from DataFrame
    for index, row in df.iterrows():
        cursor.execute(sql_insert, tuple(row))

    df = pd.DataFrame(map_user())
    sql_insert = """
                            INSERT INTO Map_User ( 
                            State, Year, Quarter, District, App_Opens, Registered_user
                            )
                          VALUES (?, ?, ?, ?, ?, ?)
                        """

    # Insert data into SQL table from DataFrame
    for index, row in df.iterrows():
        cursor.execute(sql_insert, tuple(row))

    x, y = top_transaction()
    df = pd.DataFrame(x)
    sql_insert = """
                            INSERT INTO Top_Transaction_District ( 
                            State, Year, Quarter, District, Amount, Count
                            )
                          VALUES (?, ?, ?, ?, ?, ?)
                        """

    # Insert data into SQL table from DataFrame
    for index, row in df.iterrows():
        cursor.execute(sql_insert, tuple(row))

    df = pd.DataFrame(y)
    sql_insert = """
                                INSERT INTO Top_Transaction_Pincode ( 
                                State, Year, Quarter, Pincode, Amount, Count
                                )
                              VALUES (?, ?, ?, ?, ?, ?)
                            """

    # Insert data into SQL table from DataFrame
    for index, row in df.iterrows():
        cursor.execute(sql_insert, tuple(row))

    m, n = top_user()
    df = pd.DataFrame(m)
    sql_insert = """
                                INSERT INTO Top_User_District ( 
                                State, Year, Quarter, District, Registered_Users
                                )
                              VALUES (?, ?, ?, ?, ?)
                            """

    # Insert data into SQL table from DataFrame
    for index, row in df.iterrows():
        cursor.execute(sql_insert, tuple(row))

    df = pd.DataFrame(n)
    sql_insert = """
                                INSERT INTO Top_User_Pincode ( 
                                State, Year, Quarter, Pincode, Registered_User
                                )
                              VALUES (?, ?, ?, ?, ?)
                            """

    # Insert data into SQL table from DataFrame
    for index, row in df.iterrows():
        cursor.execute(sql_insert, tuple(row))

    conn.close()

sql_data_insert()


