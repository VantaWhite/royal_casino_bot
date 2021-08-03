import discord
from discord.ext import commands
from random import randint
import csv

from database import DataBase
from game import Game
from player import Player

from discord_server import CHANNELS


class Bot:
    def __init__(self):
        settings_data = {}

        with open("db/data.csv", "r", newline="") as file:
            raw_settings_data = csv.reader(file)

            for i in raw_settings_data:
                settings_data[i[0]] = i[1]

        self.token = settings_data["token"]
        self.id = int(settings_data["id"])
        self.prefix = settings_data["prefix"]

        self.bot = commands.Bot(command_prefix=self.prefix, intents=discord.Intents.all())

    def initialize_commands(self) -> None:
        bot = self.bot

        @bot.event
        async def on_member_join(member: discord.Member):
            message = discord.Embed(
                title=f"Добро пожаловать {member}!",
                description="Чтобы узнать как играть напиши боту в личные сообщения !help."
            )
            message.set_thumbnail(url=member.avatar_url)

            await bot.get_channel(CHANNELS["welcome"]).send(embed=message)

        @bot.command()
        async def reg(ctx, username: str):
            user_id = ctx.message.author.id

            db = DataBase("db/casino.db")

            if not db.find_user(user_id):
                db.new_user(username, ctx.message.author.id)

                await ctx.send(f"Поздравляем {username}, теперь вы зарегистрированны и можете играть.")
            else:
                await ctx.send("Вы уже зарегистрированы")

            db.end()

        @bot.command()
        async def balance(ctx):
            player = Player(ctx.message.author.id)
            await ctx.send(player.money)

        @bot.command()
        async def num(ctx, number: int, bid: int):
            if Game.check_channel(ctx.channel.id):
                if Game.check_number(number):
                    right_number = randint(0, 36)

                    if number == right_number:
                        price = Game.on_win(bid, "ONE-NUMBER", Player(ctx.message.author.id))
                        await ctx.send(f"Вы выиграли! Сумма вашего выигрыша состовляет {price}$")
                    else:
                        Game.on_lose(bid, Player(ctx.message.author.id))
                        await ctx.send(f"Выпало чисило {right_number}, вы проиграли! "
                                       f"Сумма вашего проигрыша состовляет {bid}$")
                else:
                    await ctx.send("Число должын быть в диапозоне от **0** до **36**")

    def start_bot(self):
        self.bot.run(self.token)


if __name__ == "__main__":
    casino = Bot()
    casino.initialize_commands()
    casino.start_bot()
