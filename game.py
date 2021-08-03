from player import Player
from discord_server import CHANNELS

EVEN = lambda x: x % 2 == 0
ODD = lambda x: x % 2 != 0
RED = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
BLACK = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
ZERO = 0
COLUMN = [
    [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34],
    [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35],
    [3, 6, 9, 12, 15, 18, 21, 24, 27, 20, 22, 26]
]
DOZEN = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
]


class Game:
    def __init__(self):
        pass

    @classmethod
    def get_сoef(cls, bid_type: str) -> int:
        if bid_type == "ONE-NUMBER":
            return 35

    @staticmethod
    def on_win(bid_count: int, bid_type: str, player: Player) -> bool:
        try:
            count = bid_count * Game.get_сoef(bid_type)
            player.edit_money(count + player.money)
            return count
        except:
            return False

    @staticmethod
    def on_lose(bid_count: int, player: Player) -> bool:
        try:
            player.edit_money(player.money - bid_count)
            return True
        except:
            return False

    @staticmethod
    def check_channel(channel_id: int) -> bool:
        if channel_id == CHANNELS["roulette"] == channel_id:
            return True
        else:
            return False

    @staticmethod
    def check_number(number: int) -> bool:
        if 0 <= number <= 36:
            return True
        else:
            return False


if __name__ == "__main__":
    pass
