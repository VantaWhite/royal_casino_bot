from database import DataBase


class Player:
    def __init__(self, user_id: int):
        self.db = DataBase("db/casino.db")

        user_data = self.db.find_user(user_id)
        self.user_id = user_id
        self.money = user_data["money"]
        self.username = user_data["username"]

    def __str__(self):
        return f"<id={self.user_id};username={self.username};money={self.money}>"

    def edit_money(self, count: int):
        self.db.edit("money", count, self.user_id)


if __name__ == "__main__":
    x = Player(655846633212477462)
    print(x)
