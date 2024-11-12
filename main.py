import aiogram
import logging
import sqlite3
import random, time, asyncio
from aiogram import Bot, Dispatcher, executor, types
from time import gmtime, strptime, strftime
import config as cfg
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import Message
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.utils.exceptions import Throttled
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.storage import FSMContext
from datetime import datetime, timedelta
from PIL import Image, ImageDraw, ImageFont

logging.basicConfig(level=logging.INFO)

bot = Bot(token=cfg.token, parse_mode='html')

storage = MemoryStorage()

dp = Dispatcher(bot=bot, storage=storage)

dp.middleware.setup(LoggingMiddleware())

print("""\033[1;32m
|-----------------------|
|Developer: geyklub.      |
|-----------------------|\033[0m""")


connect = sqlite3.connect("db.db")
cursor = connect.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    user_id INT,
    user_name STRING,
    balance INT,
    ethereum INT,
    scam INT,
    blago INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS chance(
    chance INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promoco(
user_id INT, 
promoco_name TEXT, 
reward BIGINT, 
max_users INT, 
users INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promiki(
user_id INT, 
promo_name TEXT, 
reward BIGINT, 
max_users INT, 
users INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promiki(
user_id INT, 
promo_name TEXT, 
reward BIGINT, 
max_users INT, 
users INT
)
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS promo(
user_id INT, 
activation INT, 
promo_name TEXT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo1(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo2(
    user_id INT,
    members INT,
    ob_members INT
)
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS promo3(
    user_id INT,
    members INT,
    ob_members INT
)
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS promo4(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo5(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo6(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo7(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo8(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo9(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo10(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo11(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo12(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo13(
    user_id INT,
    members INT,
    ob_members INT
)
""")

async def anti_flood(*args, **kwargs):
	return

class reg(StatesGroup):
	st = State()
	ref = State()

@dp.message_handler(commands=['reset'])
async def start_cmd(message):
    msg = message
    user_id = msg.from_user.id
    user_name = cursor.execute(
        "SELECT user_name from users where user_id = ?", (message.from_user.id,)).fetchone()
    user_name = str(user_name[0])

    if user_id == cfg.admin:
        await bot.send_message(message.chat.id, f"🤴 |Владелец бота: <a href='tg://user?id={user_id}'>{user_name}</a>\n🌏 |Действие: Масовое обнуление\n💈 | операция по обнулению: успешно✅️\n👨 | Всем игрокам", parse_mode='html')
        cursor.execute(f'UPDATE users SET balance = {0}')
        cursor.execute(f'UPDATE users SET blago = {0}')
        cursor.execute(f'UPDATE users SET level = {0}')
        cursor.execute(f'UPDATE users SET work = {0}')
        cursor.execute(f'UPDATE users SET user_name = "гражданин GBX"')
        cursor.execute(f'UPDATE users SET bank = {500}')                
        cursor.execute(f'UPDATE users SET rating = {0}')                
        cursor.execute('DELETE from businesses')      
        cursor.execute(f'UPDATE farm SET linen = {0}')
        cursor.execute(f'UPDATE farm SET cotton = {0}')
        cursor.execute(f'UPDATE house SET house = {0}')        
        cursor.execute(f'UPDATE house SET basement = {0}')
        cursor.execute(f'UPDATE cars SET cars = {0}')   
        cursor.execute(f'UPDATE airplanes SET airplanes = {0}')        
        cursor.execute(f'UPDATE bot_time SET stavka_games = {0} ')
        cursor.execute(f'UPDATE bot_time SET stavka_bank = {0} ')
        cursor.execute(f'UPDATE bot_time SET stavka_bonus = {0} ')
        cursor.execute(f'UPDATE bot_time SET stavka_depozit = {0} ')
        cursor.execute(f'UPDATE bot_time SET time_pick = {0} ')
        cursor.execute(f'UPDATE bot_time SET time_rake = {0} ')
        cursor.execute(f'UPDATE bot_time SET time_craft = {0} ')
        cursor.execute(f'UPDATE bot_time SET time_kit = {0} ')

        connect.commit()
        full_name = msg.from_user.full_name
        print(f'{full_name} сделал масовое обнуление')
        return
    else:
        await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a> , данная функция доступна только с категории администратора \"Owner\"", parse_mode='html')
            								    								
@dp.message_handler(commands=['users_bal'])
@dp.throttled(anti_flood, rate=0.5)
async def sbal(message):
	user_id = message.from_user.id
	chat_id = message.chat.id
	try:
		id = int(message.text.split()[1])
		su = message.text.split()[2]
		su2 = (su).replace('к', '000')
		su3 = (su2).replace('м', '000000')
		su4 = (su3).replace('.', '')
		sum = int(su4)
		summ = '{:,}'.format(sum).replace(",", ".")
	except:
		await message.answer(f'Не верный ввод команды!\nПример » <code>/users_bal</code> (telegram id) (сумма)')
	name = cursor.execute(f'SELECT user_name from users where user_id = {id}').fetchone()
	name = str(name[0])
	balance = cursor.execute(f'SELECT balance from users where user_id = {id}').fetchone()
	balance = int(balance[0])
	if user_id == cfg.owner.gay.adminestrator:
		await message.answer(f'Вы изменили баланс <b>{name}</b> на <b>{summ}$</b>')
		cursor.execute(f'UPDATE users SET balance = {sum} WHERE user_id = {id}')
		connect.commit()
	else:
		return

@dp.message_handler(commands=['users'])
@dp.throttled(anti_flood, rate=0.5)
async def sbal(message):
	user_id = message.from_user.id
	chat_id = message.chat.id
	try:
		id = int(message.text.split()[1])
		su = message.text.split()[2]
		su2 = (su).replace('к', '000')
		su3 = (su2).replace('м', '000000')
		su4 = (su3).replace('.', '')
		sum = int(su4)
		summ = '{:,}'.format(sum).replace(",", ".")
	except:
		await message.answer(f'Не верный ввод команды!\nПример » <code>/users_bal</code> (telegram id) (сумма)')
	name = cursor.execute(f'SELECT user_name from users where user_id = {id}').fetchone()
	name = str(name[0])
	balance = cursor.execute(f'SELECT balance from users where user_id = {id}').fetchone()
	balance = int(balance[0])
	if user_id == cfg.admin:
		await message.answer(f'Вы изменили баланс <b>{name}</b> на <b>{summ}$</b>')
		cursor.execute(f'UPDATE users SET balance = {sum} WHERE user_id = {id}')
		connect.commit()
	else:
		return
		
@dp.message_handler(text=['помощь', 'Помощь'])
@dp.throttled(anti_flood, rate=1)
async def help(message):
	await message.answer(f'''Список команд, которые доступны в лс с ботом:
💸/pay (telegram id) сумма - передать денег
💵/top - топ 5 самых богатых игроков
😄/me - выход в главное меню баланса
💸/скам
🔴/rul
🎰/coin''')

@dp.message_handler(text=['я', 'Я', '/me'])
@dp.throttled(anti_flood, rate=0.5)
async def balance(message):
	user_id = message.from_user.id
	photo = open('start.jpg', 'rb')
	user_name = cursor.execute(f'SELECT user_name from users where user_id = {user_id}').fetchone()
	user_name = str(user_name[0])
	balance = cursor.execute(f'SELECT balance from users where user_id = {user_id}').fetchone()
	balance = int(balance[0])
	b = '{:,}'.format(balance).replace(",", ".")
	await bot.send_photo(chat_id = message.chat.id, photo=photo, caption=f'Привет, <b>{user_name}</b>, сейчас ты находишься в городе <b>Лас Вегас</b> на руках у тебя <b>{b}$</b>')

@dp.message_handler(commands=['start'])
@dp.throttled(anti_flood, rate=0.5)
async def start(message):
	msg = message
	user_id = message.from_user.id
	user_name = message.from_user.full_name
	photo = open('start.jpg', 'rb')
	referrer_id = None
	cursor.execute(f'SELECT user_id from users where user_id = {user_id}')
	if cursor.fetchone() is None:
		start_command = message.text
		referrer_id = str(start_command[7:])
		if str(referrer_id) != '' and referrer_id.isdigit():
			if str(referrer_id) != str(msg.from_user.id):
				global referrer_id2
				referrer_id2=referrer_id
				await bot.send_photo(chat_id = message.chat.id, photo=photo, caption='✅ <b>Придумай имя своему персонажу</b>')
				await reg.ref.set()
			else:
				await message.answer('Гениально, но нет.')
		else:
			await bot.send_photo(chat_id = message.chat.id, photo=photo, caption='✅ <b>Придумай имя своему персонажу</b>')
			await reg.st.set()
	else:
		if message.chat.id == user_id:
			kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
			b1 = InlineKeyboardButton('Я')
			b2 = InlineKeyboardButton('Помощь')
			b2 = InlineKeyboardButton('Бизнес')
			kb.row(b1, b2,b3)
			await message.answer(f'🎛 <b>Меню бота</b>', reply_markup=kb)

@dp.message_handler(content_types=types.ContentType.ANY, state=reg.st)
async def regs(message, state: FSMContext):
	user_id = message.from_user.id
	name = message.from_user.full_name
	user_name = message.text
	if message.chat.id == user_id:
		kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
		b1 = InlineKeyboardButton('Я')
		b2 = InlineKeyboardButton('Помощь')
		kb.row(b1, b2)
	await message.answer(f'''✈ <b>{user_name}, ты завершил регистрацию</b>

<b>бот миллионер - это бот где ты можешь:</b>
<i>зарабатывать деньги: покупать машины, одежду; строить бизнес; вступить в опг или создать свой и многое другое...</i>''', reply_markup=kb)
	cursor.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?);", (user_id, user_name, 200, 0, 0))
	connect.commit()
	await state.finish()

@dp.message_handler(content_types=types.ContentType.ANY, state=reg.ref)
async def regs(message, state: FSMContext):
	user_id = message.from_user.id
	name = message.from_user.full_name
	user_name = message.text
	if message.chat.id == user_id:
		kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
		b1 = InlineKeyboardButton('Я')
		b2 = InlineKeyboardButton('Помощь')
		kb.row(b1, b2)
	await message.answer(f'''✈ <b>{user_name}, ты завершил регистрацию</b>

<b>бот миллионер - это бот где ты можешь:</b>
<i>зарабатывать деньги: покупать машины, одежду; строить бизнес; вступить в опг или создать свой и многое другое...</i>''', reply_markup=kb)
	cursor.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?);", (user_id, user_name, 200, 0, 0))
	connect.commit()
	await state.finish()
	balance = cursor.execute(f'SELECT balance from users where user_id = {referrer_id2}').fetchone()
	balance = int(balance[0])
	scam = cursor.execute(f'SELECT scam from users where user_id = {referrer_id2}').fetchone()
	scam = int(scam[0])
	cursor.execute(f'UPDATE users SET balance = {balance+400000000} WHERE user_id = {referrer_id2}')
	cursor.execute(f'UPDATE users SET scam = {scam+400000000} WHERE user_id = {referrer_id2}')
	await bot.send_message(referrer_id2, f'''🦣 <b>Есть профит!</b>
	<i>- Вам удалось заскамить {name}. Вы получили » 400.000 000$</i>''')
	connect.commit()

	
	c = int(message.text.split()[1])
	
	if user_id == cfg.admin:
		if c in range(0, 5):
			await message.answer(f'Шанс в /coin /рулетке изменен на {c}/4')
			cursor.execute(f'UPDATE chance SET chance = {c}')
			connect.commit()
		else:
			await message.answer('Шанс может быть установлен в диапазоне 0-4')
	
@dp.message_handler(commands=['coin'])
@dp.throttled(anti_flood, rate=0.5)
async def blago(message: types.Message):
    user_id = message.from_user.id
    
    # Проверка наличия аргумента в команде
    if len(message.text.split()) < 2:
        await message.answer('Не верный ввод команды!\nПример » /coin сумма')
        return
    
    # Обработка суммы
    try:
        su = message.text.split()[1]
        su2 = su.replace('к', '000').replace('м', '000000').replace('.', '')
        sum_amount = int(su2)
        formatted_sum = '{:,}'.format(sum_amount).replace(",", ".")
    except ValueError:
        await message.answer('Не верный ввод суммы! Используйте числа.')
        return

    # Получение имени пользователя и баланса
    user_name = cursor.execute('SELECT user_name FROM users WHERE user_id = ?', (user_id,)).fetchone()
    balance = cursor.execute('SELECT balance FROM users WHERE user_id = ?', (user_id,)).fetchone()
    chance = cursor.execute('SELECT chance FROM chance').fetchone()

    if user_name is None or balance is None or chance is None:
        await message.answer('Пользователь не найден в базе данных.')
        return

    user_name = str(user_name[0])
    balance = int(balance[0])
    chance = int(chance[0])

    win_chance = 100 if chance == 0 else chance * 25 if 0 < chance < 4 else 0

    r = random.randint(1, 100)
    rand = random.randint(1, 50)

    c = 2 if rand >= 20 else 3

    if sum_amount <= balance:
        if sum_amount >= 1:
            if win_chance < r <= 100:
                wn = sum_amount * c
                w = '{:,}'.format(wn).replace(",", ".")
                n = '{:,}'.format(balance + wn).replace(",", ".")
                await message.answer(f'🥳 <b>{user_name}</b>, вы выиграли <b>{w}$</b> (x{c})\nТеперь твой баланс: {n}')
                cursor.execute('UPDATE users SET balance = ? WHERE user_id = ?', (balance + wn, user_id))
            else:
                g = '{:,}'.format(balance - sum_amount).replace(",", ".")
                await message.answer(f'😢 <b>{user_name}</b>, к сожалению, вы проиграли <b>{formatted_sum}</b>\nТеперь ваш баланс: {g}$ (x0)')
                cursor.execute('UPDATE users SET balance = ? WHERE user_id = ?', (balance - sum_amount, user_id))
            connect.commit()
        else:
            await message.answer('Ставка не может быть отрицательной')
    else:
        await message.answer('У вас недостаточно средств')







	
@dp.message_handler(commands=['blago'])
@dp.throttled(anti_flood, rate=0.5)
async def blago(message):
	user_id = message.from_user.id
	try:
		su = message.text.split()[1]
		su2 = (su).replace('к', '000')
		su3 = (su2).replace('м', '000000')
		su4 = (su3).replace('.', '')
		sum = int(su4)
		summ = '{:,}'.format(sum).replace(",", ".")
	except:
		await message.answer(f'''Не верный ввод команды!
Пример » /blago сумма''')
	user_name = cursor.execute(f'SELECT user_name from users where user_id = {user_id}').fetchone()
	user_name = str(user_name[0])
	balance = cursor.execute(f'SELECT balance from users where user_id = {user_id}').fetchone()
	balance = int(balance[0])
	blago = cursor.execute(f'SELECT blago from users where user_id = {user_id}').fetchone()
	blago = int(blago[0])
	
	if balance >= sum:
		if sum >= 1:
			await message.answer(f'Вы пожертвовали {summ}$')
			cursor.execute(f'UPDATE users SET balance = {balance-sum} WHERE user_id = {user_id}')
			cursor.execute(f'UPDATE users SET blago = {blago+sum} WHERE user_id = {user_id}')
			connect.commit()
		else:
			await message.answer(f'Нельзя пожертовать отрицательное число')
	else:
		await message.answer(f'Недостаточно средств')

@dp.callback_query_handler(text_contains='top_')
@dp.throttled(anti_flood, rate=0.5)
async def top(callback):
	user_id = callback.from_user.id
	chat_id = callback.message.chat.id
	message_id = callback.message.message_id
	cd = callback.data[4:]
	if cd == 'blago':
		list = cursor.execute(f"SELECT * FROM users ORDER BY blago DESC")
		list = cursor.fetchmany(1000)
		top_list = []
		my_list = []
		top_list2 = []
		num = 1
		b = InlineKeyboardButton(text='Топ богатых', callback_data='top_many')
		kb = InlineKeyboardMarkup()
		kb.row(b)
		for user in list:
			bal = user[4]
			balance = '{:,}'.format(bal).replace(',', '.')
			if user[0]==user_id:
				for x in str(num):
					my_list.append(int(x))
					if len(my_list)==1:
						first = my_list[0]
						count=first
					elif len(my_list)==2:
						first = my_list[0]
						second = my_list[1]
						count = first + second
					elif len(my_list)==3:
						first = my_list[0]
						second = my_list[1]
						third=my_list[2]
						count=first+second+third
					else:
						count="0"
				top_list2.append(f'''<b>(Ты на {count} месте)</b>\n\n''')
			if num <= 5:
				top_list.append(f'''<b>{num}. <a href='tg://openmessage?user_id={user[0]}'>{user[1]}</a> - {balance}$</b>''')
				num += 1
		top2 = "\n".join(top_list2)
		top = "\n".join(top_list)
		text = f'''💰 <b>Топ 5 благотворителей</b>\n'''+ top2 + top
		await bot.edit_message_caption(chat_id=chat_id, message_id=message_id, caption=text, reply_markup=kb)
	else:
		list = cursor.execute(f"SELECT * FROM users ORDER BY balance DESC")
		list = cursor.fetchmany(1000)
		top_list = []
		top_list2 = []
		my_list = []
		num = 1
		b = InlineKeyboardButton(text='Топ благотворителей', callback_data='top_blago')
		kb = InlineKeyboardMarkup()
		kb.row(b)
		for user in list:
			bal = user[2]
			balance = '{:,}'.format(bal).replace(',', '.')
			if user[0]==user_id:
				for x in str(num):
					my_list.append(int(x))
					if len(my_list)==1:
						first = my_list[0]
						count=first
					elif len(my_list)==2:
						first = my_list[0]
						second = my_list[1]
						count = first + second
					elif len(my_list)==3:
						first = my_list[0]
						second = my_list[1]
						third=my_list[2]
						count=first+second+third
					else:
						count="0"
				top_list2.append(f'''<b>(Ты на {count} месте)</b>\n\n''')
			if num <= 5:
				top_list.append(f'''<b>{num}. <a href='tg://openmessage?user_id={user[0]}'>{user[1]}</a> - {balance}$</b>''')
				num += 1
		top = "\n".join(top_list)
		top2 = "\n".join(top_list2)
		text = f'''💰 <b>Топ 5 самых богатых игроков</b>\n'''+ top2 + top
		await bot.edit_message_caption(chat_id=chat_id, message_id=message_id, caption=text, reply_markup=kb)

@dp.message_handler(commands=["CheckId"], commands_prefix='!./')
async def id(message):
	user_id = message.reply_to_message.from_user.id
	if message.reply_to_message:
		await message.reply(f"Айди пользователя: {user_id}", parse_mode='html')	
	if not message.reply_to_message:
		await message.reply(f"Эта команда должна быть ответом на сообщение!", parse_mode='html')
		
@dp.message_handler(text=['топ', 'Топ', '/top'])
@dp.throttled(anti_flood, rate=0.5)
async def top(message):
	user_id = message.from_user.id
	list = cursor.execute(f"SELECT * FROM users ORDER BY balance DESC")
	list = cursor.fetchmany(5)
	top_list = []
	my_list = []
	top_list2 = []
	num = 1
	photo = open('top.jpg', 'rb')
	b = InlineKeyboardButton(text='Топ благотворителей', callback_data='top_blago')
	kb = InlineKeyboardMarkup()
	kb.row(b)
	for user in list:
		bal = user[2]
		balance = '{:,}'.format(bal).replace(',', '.')
		if user[0]==user_id:
			for x in str(num):
				my_list.append(int(x))
				if len(my_list)==1:
					first = my_list[0]
					count=first
				elif len(my_list)==2:
					first = my_list[0]
					second = my_list[1]
					count = first + second
				elif len(my_list)==3:
					first = my_list[0]
					second = my_list[1]
					third=my_list[2]
					count=first+second+third
				else:
					count="0"
			top_list2.append(f'''<b>(Ты на {count} месте)</b>\n\n''')
		if num <= 5:
			top_list.append(f'''<b>{num}. <a href='tg://openmessage?user_id={user[0]}'>{user[1]}</a> - {balance}$</b>''')
			num += 1
	top = "\n".join(top_list)
	top2 = "\n".join(top_list2)
	text = f'''💰 <b>Топ 5 самых богатых игроков\n</b>'''+ top2 + top
	await bot.send_photo(chat_id = message.chat.id, photo=photo, caption=text, reply_markup=kb)

@dp.message_handler(text=['скам', 'Скам', '/scam'])
@dp.throttled(anti_flood, rate=0.5)
async def scam(message):
	user_id = message.from_user.id
	name = cursor.execute(f'SELECT user_name from users where user_id = {user_id}').fetchone()
	name = str(name[0])
	scam = cursor.execute(f'SELECT scam from users where user_id = {user_id}').fetchone()
	scam = int(scam[0])
	
	if scam == 0:
		s = '---'
	else:
		sc = '{:,}'.format(scam).replace(",", ".")
		s = f'{sc}$'
	
	photo = open('scam.jpg', 'rb')
	
	await bot.send_photo(chat_id = message.chat.id, photo=photo, caption=f'''<b>{name}, ты находишься на работе "скам"

🦣 Всего заработано:</b>
<i>{s}</i>

💵 <b>Оплата за мамонта:</b>
<i>400.000.000$</i>

🔗 <b>Твоя скам-ссылка:</b>
<code>https://t.me/{cfg.bot_name}?start={user_id}</code>''')

@dp.message_handler(commands=['users_bal'])
@dp.throttled(anti_flood, rate=0.5)
async def sbal(message):
	user_id = message.from_user.id
	chat_id = message.chat.id
	try:
		id = int(message.text.split()[1])
		su = message.text.split()[2]
		su2 = (su).replace('к', '000')
		su3 = (su2).replace('м', '000000')
		su4 = (su3).replace('.', '')
		sum = int(su4)
		summ = '{:,}'.format(sum).replace(",", ".")
	except:
		await message.answer(f'Не верный ввод команды!\nПример » <code>/users_bal</code> (telegram id) (сумма)')
	name = cursor.execute(f'SELECT user_name from users where user_id = {id}').fetchone()
	name = str(name[0])
	balance = cursor.execute(f'SELECT balance from users where user_id = {id}').fetchone()
	balance = int(balance[0])
	if user_id == cfg.admin:
		await message.answer(f'Вы изменили баланс <b>{name}</b> на <b>{summ}$</b>')
		cursor.execute(f'UPDATE users SET balance = {sum} WHERE user_id = {id}')
		connect.commit()
	else:
		return



@dp.message_handler(commands=['рул'])
async def chance(message: types.Message):
    user_id = message.from_user.id
    try:
        col = message.text.split()[1]
        su = message.text.split()[2]
        su2 = su.replace('к', '000')
        su3 = su2.replace('м', '000000')
        su4 = su3.replace('.', '')
        sum_bet = int(su4)
        summ = '{:,}'.format(sum_bet).replace(",", ".")
        color = str(col).replace("кра", "красный").replace('чер', 'черный')
    except (IndexError, ValueError):
        await message.answer(f'''Не верный ввод команды!
Пример » /рул кра/чер сумма''')
        return

    user_name = cursor.execute(f'SELECT user_name FROM users WHERE user_id = ?', (user_id,)).fetchone()
    if user_name is None:
        await message.answer('Пользователь не найден.')
        return

    user_name = str(user_name[0])
    balance = cursor.execute(f'SELECT balance FROM users WHERE user_id = ?', (user_id,)).fetchone()
    
    if balance is None:
        await message.answer('Баланс не найден.')
        return

    balance = int(balance[0])

    if col not in ['кра', 'чер']:
        await message.answer(f'''Не верный ввод команды!
Пример » /рул кра/чер сумма''')
        return

    l = ['красный', 'черный']
    r = random.choice(l)
    ran = random.randint(1, 5)

    c = 2 if ran <= 15 else 3

    photo_path = 'red.jpg' if r == 'красный' else 'black.jpg'

    if balance >= sum_bet:
        if sum_bet >= 1:
            if color == r:
                nb = sum_bet * c
                n = '{:,}'.format(nb).replace(",", ".")
                new_balance = balance + nb
                b = '{:,}'.format(new_balance).replace(",", ".")
                await bot.send_photo(chat_id=message.chat.id, photo=open(photo_path, 'rb'), 
                                     caption=f'''🎉 <b>{user_name}</b>, поздравляю, ты выиграл <b>{n}$</b><i>(x{c})</i>

Теперь твой баланс: {b}''')
                cursor.execute(f'UPDATE users SET balance = ? WHERE user_id = ?', (new_balance, user_id))
                connect.commit()
            else:
                new_balance = balance - sum_bet
                u = '{:,}'.format(new_balance).replace(",", ".") 
                await bot.send_photo(chat_id=message.chat.id, photo=open(photo_path, 'rb'), 
                                     caption=f'''😢 <b>{user_name}</b>, к сожалению ты проиграл <b>{summ}$</b> (x0)

Теперь твой баланс: {u}''')
                cursor.execute(f'UPDATE users SET balance = ? WHERE user_id = ?', (new_balance, user_id))
                connect.commit()
        else:
            await message.answer(f'Нельзя ставить отрицательное число')
    else:
        await message.answer(f'У вас недостаточно средств.')




@dp.message_handler(text=['Статистика', 'статистика', 'стата', 'стат', 'Стата', 'Стат'])
async def stats(message):
    user_name = cursor.execute(
        "SELECT user_name from users where user_id = ?", (message.from_user.id,)).fetchone()
    user_name = str(user_name[0])

    sqlite_select_query = """SELECT * from users"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()

    await bot.send_message(message.chat.id, f"{user_name}, успешно была открыта статистика бота TITAN-BOT📗\n👥️️ | Игроков зарегестрированно в боте: {len(records)}", parse_mode='html')


@dp.message_handler(commands=['users'])
@dp.throttled(anti_flood, rate=0.5)
async def sbal(message):
	user_id = message.from_user.id
	chat_id = message.chat.id
	try:
		id = int(message.text.split()[1])
		su = message.text.split()[2]
		su2 = (su).replace('к', '000')
		su3 = (su2).replace('м', '000000')
		su4 = (su3).replace('.', '')
		sum = int(su4)
		summ = '{:,}'.format(sum).replace(",", ".")
	except:
		await message.answer(f'Не верный ввод команды!\nПример » <code>/users_bal</code> (telegram id) (сумма)')
	name = cursor.execute(f'SELECT user_name from users where user_id = {id}').fetchone()
	name = str(name[0])
	balance = cursor.execute(f'SELECT balance from users where user_id = {id}').fetchone()
	balance = int(balance[0])
	if user_id == cfg.owner:
		await message.answer(f'Вы изменили баланс <b>{name}</b> на <b>{summ}$</b>')
		cursor.execute(f'UPDATE users SET balance = {sum} WHERE user_id = {id}')
		connect.commit()
	else:
		return
		
@dp.message_handler(commands=['pay'])
@dp.throttled(anti_flood, rate=0.5)
async def pay(message):
	user_id = message.from_user.id
	chat_id = message.chat.id
	try:
		id = int(message.text.split()[1])
		su = message.text.split()[2]
		su2 = (su).replace('к', '000')
		su3 = (su2).replace('м', '000000')
		su4 = (su3).replace('.', '')
		sum = int(su4)
		summ = '{:,}'.format(sum).replace(",", ".")
	except:
		await message.answer(f'''✅ <b>Используй:</b>
/pay (telegram id) сумма

📋 <b>Примеры:</b>
/pay (telegram id) 1к
/pay (telegram id) 1000''')
	name = cursor.execute(f'SELECT user_name from users where user_id = {id}').fetchone()
	name = str(name[0])
	user_name = cursor.execute(f'SELECT user_name from users where user_id = {user_id}').fetchone()
	user_name = str(user_name[0])
	balance = cursor.execute(f'SELECT balance from users where user_id = {id}').fetchone()
	balance = int(balance[0])
	bal = cursor.execute(f'SELECT balance from users where user_id = {user_id}').fetchone()
	bal = int(bal[0])
	if id != user_id:
		if bal >= sum:
			if sum >= 1:
				await message.answer(f'<b>{user_name}</b>, вы перевели <b>{summ}$</b> <b>{name}</b>')
				cursor.execute(f'UPDATE users SET balance = {balance+sum} WHERE user_id = {id}')
				cursor.execute(f'UPDATE users SET balance = {bal-sum} WHERE user_id = {user_id}')
				connect.commit()
			else:
				await message.answer(f'Нельзя перевести отрицательное число')
		else:
			await message.answer(f'У тебя недостаточно средств')
	else:
		await message.answer(f'Невозможно перевести деньги самому себе')




async def on_startup(_):
    await bot.send_message(chat_id=cfg.admin,text=f"""<b>✅ гэй</b>
<code>{datetime.now().strftime("%d.%m.%y %H:%M:%S")}</code>""")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
