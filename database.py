import sqlite3 as sqlite


class DataBase:
    def __init__(self, db_name: str):
        self.db = sqlite.connect(db_name)
        self.cursor = self.db.cursor()

    def new_user(self, username: str, user_id: int):
        self.cursor.execute(f"""
        INSERT INTO users VALUES ("{username}", {user_id}, 500);
        """)

        self.db.commit()

    def find_user(self, user_id: int) -> dict:
        """find user from her id"""

        raw_result = self.cursor.execute(f"""
        SELECT username, money FROM users WHERE id = {user_id}
        """).fetchall()[0]

        result = {
            "username": raw_result[0],
            "money": raw_result[1]
        }

        return result

    def edit(self, column: str, value: any, user_id: int):
        """edit some value"""
        self.cursor.execute(f"""
        UPDATE users SET {column} = {value} WHERE id = {user_id};
        """)
        self.db.commit()

    def end(self):
        """close the database when finished"""
        self.db.close()


if __name__ == "__main__":
    db = DataBase("db/casino.db")
    me = db.find_user(655846633212477462)
    print(me)
