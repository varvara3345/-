import asyncio

import re
from datetime import date

from conf import TOKEN
from KeyBoard import main_kb, date_kb, test_kb, question1, question2, question3

from bd import Database

from aiogram import F
from aiogram import Bot, Dispatcher, types

dp = Dispatcher()
bd = Database()

t = []

t1 = '''
Понедельник:
1. Кардио 30-40 мин.
2. Жим лежа 3х12.
3. Разведение гантелей лежа 3х15.
4. Французкий жим 3х10.
5. Подъем туловища 3х20.
6. Свободная ходьба 20 мин.

Среда:
1. Кардио 30-40 мин.
2. Верхняя тяга 3х10.
3. Тяга нижнего блока 3х12.
4. Молотки 3х10.
5. Разведение гантелей в стороны 3х8.
6. Подъем туловища 3х20.
7. Свободная ходьба 20 мин.

Пятница:
1. Кардио 30-40 мин.
2. Приседание со штангой 3х12.
3. Разгибание ног 3х12.
4. Жим ногами 3х15.
5. Икры 3х15.
6. Подъем туловища 3х20.
7. Свободная ходьба 20 мин.
'''
t2 = '''
Понедельник:
1. Разминка.
2. Жим лежа 3х12-15.
3. Жим гантелей под углом 3х12-15.
4. Отжимания на брусьях с весом 3х12-15.
5. Жим гантелей сидя 3х12-15.
6. Французкий жим 3х12.
7. Растяжка.

Среда:
1. Разминка.
2. Приседание со штангой 3х12-15.
3. Жим ногами 3х12-15.
4. Разгибание ног 3х12-15.
5. Пресс 3х15.
6. Икры 3х15-20.
7. Растяжка.


Пятница:
1. Разминка.
2. Тяга штанги в наклоне 3х12-15.
3. Подтягивание широким хватом 3х10.
4. Тяга в вертикальном блоке 3х12.
5. Молотки 3х12.
6. Шраги 3х15.
7. Растяжка.
'''
t3 = '''
Понедельник:
1. Кардио 30-40 мин.
2. Приседания 3х10.
3. Ягодичный мостик 3х12.
4. Сгибание ног 3х10.
5. Разгибание ног 3х12.
6. Планца 3х45сек.
7. Свободная ходьба 20 мин.

Среда:
1. Кардио 30-40 мин.
2. Жим лежа 3х6.
3. Тяга в наклоне 3х8.
4. Сгибание рук на бицепс 3х6.
5. Бабочка 3х10.
6. Подъем туловища 3х15.
7. Свободная ходьба 20 мин.

Пятница:
1. Кардио 30-40 мин.
2. Выпады 3х12.
3. Жим над головой 3х8.
4. Жим ногами 3х12.
5. Икры 3х12.
6. Французкий жим 3х10.
7. Свободная ходьба 20 мин.
'''
t4 = '''
Понедельник:
1. Разминка.
2. Становая тяга 3х10.
3. Жим гантелей лежа 3х12.
4. Французкий жим 3х12.
5. Бабочка 3х12.
7. Растяжка.

Среда:
1. Разминка.
2. Приседание со штангой 3х12-15.
3. Жим ногами 3х12-15.
4. Выпады 3х12-15.
5. Пресс 3х15.
6. Сгибание ног 3х15.
7. Растяжка.


Пятница:
1. Разминка.
2. Подъем штанги на бицепс 3х12.
3. Верхний жим 3х10.
4. Тяга штанги к подборотку 3х12.
5. Разводка гантелей стоя 3х10.
6. Шраги 3х12.
7. Растяжка.
'''

start_mes = '''
Привет, я бот, который будет делать записи в твой электронный дневник!
Так же я предоставлю тебе список дат, при помощи которых ты сможешь обращаться ко мне.
Тем самым я буду отправлять тебе твои записи в этот день)
Каждое твоё отправленное сообщение будет записываться в дневник.
'''

@dp.message(F.text == '/start')
async def cmd_start(message: types.Message) -> None:
    bd.add_user(message.from_user.id)
    await message.answer(start_mes,reply_markup=test_kb)

@dp.message(F.text == 'Список дат')
async def write_the_date(message: types.Message) -> None:
    s = bd.get_key(message.from_user.id)
    if s is None:
        await message.answer('У вас нет записей. Чтобы добавить запись напишите боту, то что вы бы хотели добавить в дневник.')
    else:
        await message.answer('Ваши дни записи.',reply_markup=date_kb(s))

@dp.message(F.text == 'Тест')
async def t1_menu(message: types.Message) -> None:
    await message.answer('Какая у вас цель похода в зал?',reply_markup=question1)

@dp.message(F.text == 'Похудеть')
async def q1_menu(message: types.Message) -> None:
    await message.answer('Выберите диапазон веса',reply_markup=question2)
    t.append(1)

@dp.message(F.text == 'Накачаться')
async def q2_menu(message: types.Message) -> None:
    await message.answer('Выберите диапазон веса',reply_markup=question2)
    t.append(2)

@dp.message(F.text == '49кг и менее')
async def q3_menu(message: types.Message) -> None:
    await message.answer('Выберите пол',reply_markup=question3)
    t.append(1)

@dp.message(F.text == '50-74кг')
async def q4_menu(message: types.Message) -> None:
    await message.answer('Выберите пол',reply_markup=question3)
    t.append(2)

@dp.message(F.text == '75-99кг')
async def q5_menu(message: types.Message) -> None:
    await message.answer('Выберите пол',reply_markup=question3)
    t.append(3)

@dp.message(F.text == '100кг и более')
async def q6_menu(message: types.Message) -> None:
    await message.answer('Выберите пол',reply_markup=question3)
    t.append(4)

@dp.message(F.text == 'Мужской')
async def q6_menu(message: types.Message) -> None:
    t.append(1)
    if t[0] == 1 and t[2] == 1:
        await message.answer("Для похудения вам следует соблюдать питание: есть 1.5г белка на килограмм весатела и максимум 3г углеводов на килограмм тела.")
        await message.answer(t1,reply_markup=main_kb)
    elif t[0] == 2 and t[2] == 1:
        await message.answer("Для набора вам следует соблюдать питание: есть 1.5-2г белка на килограмм весатела и 5-6г углеводов на килограмм тела.")
        await message.answer(t2, reply_markup=main_kb)


@dp.message(F.text == 'Женский')
async def q5_menu(message: types.Message) -> None:
    t.append(2)
    if t[0] == 1 and t[2] == 2:
        await message.answer(
            "Для похудения вам следует соблюдать питание: есть 1г белка на килограмм весатела и максимум 2-3г углеводов на килограмм тела.")
        await message.answer(t3, reply_markup=main_kb)
    elif t[0] == 2 and t[2] == 2:
        await message.answer(
            "Для набора вам следует соблюдать питание: есть 1.5г белка на килограмм весатела и 4-5г углеводов на килограмм тела.")
        await message.answer(t4, reply_markup=main_kb)

@dp.message(F.text == 'Меню')
async def main_menu(message: types.Message) -> None:
    await message.answer('Вы перешли в главное меню.',reply_markup=main_kb)

@dp.message(F.text)
async def write_the_record(message: types.Message) -> None:
    if bool(re.match(r'[1-9][0-9]{3}-[0-1][1-9]-[0-3][0-9]',message.text)):
        s = bd.ret_record(re.match(r'[1-9][0-9]{3}-[0-1][1-9]-[0-3][0-9]',message.text).group(),message.from_user.id)
        if not s:
            await message.answer('Такой даты не существует')
        else:
            await message.answer(s)
    else:
        bd.add_record(message.from_user.id,{str(date.today()):message.text})
        await message.answer('Запись добавлена!',reply_markup=main_kb)


async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
