import sqlite3 as sql

conn = sql.connect(r'db\users.db', check_same_thread=False)
cur = conn.cursor()


def add_new_data(user_id: int, user_lname: str, user_fname: str, username: str):
    conn.execute("""CREATE TABLE IF NOT EXISTS users_info(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
            user_id INT NOT NULL UNIQUE,
            user_fname TEXT NOT NULL,
            user_lname TEXT,
            username STRING);
            """)
    try:
        cur.execute('''INSERT INTO users_info (user_id, user_lname, user_fname, username) 
                        VALUES (?, ?, ?, ?)''', (user_id, user_lname, user_fname, username))
    except (sql.IntegrityError, sql.DatabaseError) as exc:
        print(f'{exc}')
    finally:
        conn.commit()
