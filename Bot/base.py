import sqlite3


try:
    sqlite_connection = sqlite3.connect('Askar_database.db', check_same_thread=False)
    cursor = sqlite_connection.cursor()
    print("База данных создана и успешно подключена к SQLite")

    sqlite_select_query = "select sqlite_version();"
    cursor.execute(sqlite_select_query)
    record = cursor.fetchall()
    print("Версия базы данных SQLite: ", record)

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)

cursor.execute("""CREATE TABLE IF NOT EXISTS requests(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id INTEGER NOT NULL,
                            username_sender TEXT NOT NULL,
                            username TEXT,
                            user_message TEXT
);""")
sqlite_connection.commit()


def db_add(user_id, username_sender, username, user_message):
    cursor.execute("""INSERT INTO requests(user_id , username_sender , username , user_message) VALUES (? , ? , ?, ?)""", (user_id, username_sender , username, user_message))
    sqlite_connection.commit()


