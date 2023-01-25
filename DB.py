# ☣️ Developer (KittyHack)

import sqlite3


def GetUsers():
    try:
        query = """SELECT * FROM Users"""
        cursor.execute(query)
        info = cursor.fetchall()
        return info

    except sqlite3.Error as error:
        print("!! Error GetChats():", error)


def GetChats():
    try:
        query = """SELECT * FROM Chats"""
        cursor.execute(query)
        info = cursor.fetchall()
        return info

    except sqlite3.Error as error:
        print("!! Error GetChats():", error)


def InsertUsers(name, user_id, from_chat):
    query = f"""
        INSERT OR REPLACE INTO Users
        (name, user_id, from_chat)  VALUES  ('{name}', '{user_id}', '{from_chat}')
    """
    # print(">> ", query)
    cursor.execute(query)
    sqlite_connection.commit()


def InsertChats(name, channel_id):
    query = f"""
        INSERT OR REPLACE INTO Chats
        (name, channel_id)  VALUES  ('{name}', '{channel_id}')
    """
    # print(">> ", query)
    cursor.execute(query)
    sqlite_connection.commit()


query_Users = '''
    CREATE TABLE IF NOT EXISTS Users (  
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    user_id TEXT NOT NULL UNIQUE,
    from_chat TEXT,
    FOREIGN KEY (from_chat) REFERENCES Chats (channel_id) ON DELETE SET NULL
    );
'''
query_Chats = '''
    CREATE TABLE IF NOT EXISTS Chats (  
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    channel_id text NOT NULL UNIQUE
    );
'''


def CreateTable(query):
    try:
        cursor.execute(query)
        sqlite_connection.commit()
        print(">> Table SQLite was created")
    except sqlite3.Error as error:
        print("!! Table creation error:", error)


def Close():
    print(">> Close DataBase")
    cursor.close()
    if sqlite_connection:
        sqlite_connection.close()


def Main():
    try:
        global cursor, sqlite_connection

        sqlite_connection = sqlite3.connect('telegram_users_data.db')

        cursor = sqlite_connection.cursor()
        print(">> Database created and successfully connected to SQLite")  # preparation completed

        sqlite_select_query = "select sqlite_version();"
        cursor.execute(sqlite_select_query)  # request to DB
        record = cursor.fetchall()
        print(">> SQLite database version: ", record)

        CreateTable(query_Chats)
        CreateTable(query_Users)

    except sqlite3.Error as error:
        print("!! Error connecting sqlite:", error)


Main()
