from pyrogram import Client, filters
from pyrogram.errors import BadRequest
from AnonXMusic import app


board = [[" " for _ in range(3)] for _ in range(3)]
bot_turn = False


@app.on_message(filters.command("اكس او"))
async def start_game(_, message):
    global board, bot_turn
    board = [[" " for _ in range(3)] for _ in range(3)]
    bot_turn = False
    await message.reply("لعبة XO جاهزة! ابدأ بإرسال الإحداثيات (1-9).")


@app.on_message(filters.text)
async def play(_, message):
    global board, bot_turn
    try:
        if not bot_turn:
            coords = int(message.text.strip())
            row = (coords - 1) // 3
            col = (coords - 1) % 3
            if board[row][col] != " ":
                await message.reply("هذا المربع مشغول، جرب مربعًا آخرًا!")
                return
            board[row][col] = "X"
            if check_winner("X"):
                await message.reply("أحسنت! فازت اللاعب X.")
                return
            bot_turn = True
            bot_coords = get_bot_coords()
            board[bot_coords[0]][bot_coords[1]] = "O"
            if check_winner("O"):
                await message.reply("أحسنت! فاز البوت O.")
                return
            bot_turn = False
            await message.reply(game_to_string())
        else:
            await message.reply("ليست دورك الآن!")
    except BadRequest:
        await message.reply("اختر رقمًا بين 1 و 9 فقط!")


def check_winner(player):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False


def get_bot_coords():
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                return row, col


def game_to_string():
    lines = []
    for row in range(3):
        line = " ".join(board[row])
        lines.append(line)
    return "\n".join(lines)
