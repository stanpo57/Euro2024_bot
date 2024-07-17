from aiogram import F, Router, types
from aiogram.types import Message      # CallbackQuery
from aiogram.filters import CommandStart, Command
# from random import randint

import app.keyboards as kb

import app.euro2024 as eu
# from prognosis import matches_formation_predict, final_formation_predict

router = Router()


@router.message(CommandStart())
@router.message(Command('s'))
async def cmd_start(message: Message):
    await message.answer('Привет! Я бот Euro2024.', reply_markup=kb.kb_main)


@router.message(F.text == kb.kb_main_list[0])     # Расписание
async def matches_groups(message: Message):
    txt = eu.msg_matches
    entity_mono = types.MessageEntity(
        type="code",
        offset=0,
        length=len(txt),
    )
    entity_bold = types.MessageEntity(
        type="bold",
        offset=0,
        length=34,
    )
    entity_bold2 = types.MessageEntity(
        type="bold",
        offset=0,
        length=52,
    )
    entity_underline = types.MessageEntity(
        type="underline",
        offset=0,
        length=34,
    )
    entity_italic = types.MessageEntity(
        type="italic",
        offset=0,
        length=50,
    )
    entities1 = [entity_bold, entity_underline]
    entities2 = [entity_italic, entity_bold2]
    entities = [entity_mono]

    await message.answer('Расписание игр группового турнира: ', entities=entities1, reply_markup=kb.kb_main)
    await message.answer(text=txt, entities=entities)
    await message.answer('\nДля просмотра информации о матче введите его номер: ', entities=entities2)


@router.message(F.text == kb.kb_main_list[1])    # Таблицы
async def tables(message: Message):
    txt = eu.msg_tables
    entity_mono = types.MessageEntity(
        type="code",
        offset=0,
        length=len(txt),
    )
    entity_bold = types.MessageEntity(
        type="bold",
        offset=0,
        length=40,
    )
    entity_bold2 = types.MessageEntity(
        type="bold",
        offset=0,
        length=50,
    )
    entity_underline = types.MessageEntity(
        type="underline",
        offset=0,
        length=40,
    )
    entity_italic = types.MessageEntity(
        type="italic",
        offset=0,
        length=50,
    )
    entities1 = [entity_bold, entity_underline]
    entities2 = [entity_italic, entity_bold2]
    entities = [entity_mono]

    await message.answer(
        'Таблицы результатов группового турнира:  ',
         entities=entities1,
         reply_markup=kb.kb_main_plus_groups
    )
    await message.answer(text=txt, entities=entities)
    await message.answer('\nДля выбора группы нажмите соответствующую кнопку:  ', entities=entities2)


@router.message(F.text == kb.kb_groups_list[0])  # группа A
async def table_a(message: Message):
    txt = eu.msg_group1
    entity_mono = types.MessageEntity(
        type="code",
        offset=0,
        length=len(txt),
    )
    entity_italic1 = types.MessageEntity(
        type="italic",
        offset=0,
        length=52,
    )
    entity_bold1 = types.MessageEntity(
        type="bold",
        offset=0,
        length=52,
    )
    entities1 = [entity_italic1, entity_bold1]
    entities = [entity_mono]
    await message.answer(text=txt, entities=entities)
    await message.answer('\nДля выбора группы нажмите соответствующую кнопку:   ', entities=entities1)
    await message.answer('\nДля просмотра информации о матче введите его номер: ', entities=entities1)


@router.message(F.text == kb.kb_groups_list[1])  # группа B
async def table_b(message: Message):
    txt = eu.msg_group2
    entity_mono = types.MessageEntity(
        type="code",
        offset=0,
        length=len(txt),
    )
    entity_italic1 = types.MessageEntity(
        type="italic",
        offset=0,
        length=52,
    )
    entity_bold1 = types.MessageEntity(
        type="bold",
        offset=0,
        length=52,
    )
    entities1 = [entity_italic1, entity_bold1]
    entities = [entity_mono]
    await message.answer(text=txt, entities=entities)
    await message.answer('\nДля выбора группы нажмите соответствующую кнопку:   ', entities=entities1)
    await message.answer('\nДля просмотра информации о матче введите его номер: ', entities=entities1)


@router.message(F.text == kb.kb_groups_list[2])  # группа C
async def table_c(message: Message):
    txt = eu.msg_group3
    entity_mono = types.MessageEntity(
        type="code",
        offset=0,
        length=len(txt),
    )
    entity_italic1 = types.MessageEntity(
        type="italic",
        offset=0,
        length=52,
    )
    entity_bold1 = types.MessageEntity(
        type="bold",
        offset=0,
        length=52,
    )
    entities1 = [entity_italic1, entity_bold1]
    entities = [entity_mono]
    await message.answer(text=txt, entities=entities)
    await message.answer('\nДля выбора группы нажмите соответствующую кнопку:   ', entities=entities1)
    await message.answer('\nДля просмотра информации о матче введите его номер: ', entities=entities1)


@router.message(F.text == kb.kb_groups_list[3])  # группа D
async def table_d(message: Message):
    txt = eu.msg_group4
    entity_mono = types.MessageEntity(
        type="code",
        offset=0,
        length=len(txt),
    )
    entity_italic1 = types.MessageEntity(
        type="italic",
        offset=0,
        length=52,
    )
    entity_bold1 = types.MessageEntity(
        type="bold",
        offset=0,
        length=52,
    )
    entities1 = [entity_italic1, entity_bold1]
    entities = [entity_mono]
    await message.answer(text=txt, entities=entities)
    await message.answer('\nДля выбора группы нажмите соответствующую кнопку:   ', entities=entities1)
    await message.answer('\nДля просмотра информации о матче введите его номер: ', entities=entities1)


@router.message(F.text == kb.kb_groups_list[4])  # группа E
async def table_e(message: Message):
    txt = eu.msg_group5
    entity_mono = types.MessageEntity(
        type="code",
        offset=0,
        length=len(txt),
    )
    entity_italic1 = types.MessageEntity(
        type="italic",
        offset=0,
        length=52,
    )
    entity_bold1 = types.MessageEntity(
        type="bold",
        offset=0,
        length=52,
    )
    entities1 = [entity_italic1, entity_bold1]
    entities = [entity_mono]
    await message.answer(text=txt, entities=entities)
    await message.answer('\nДля выбора группы нажмите соответствующую кнопку:   ', entities=entities1)
    await message.answer('\nДля просмотра информации о матче введите его номер: ', entities=entities1)


@router.message(F.text == kb.kb_groups_list[5])  # группа F
async def table_f(message: Message):
    txt = eu.msg_group6
    entity_mono = types.MessageEntity(
        type="code",
        offset=0,
        length=len(txt),
    )
    entity_italic1 = types.MessageEntity(
        type="italic",
        offset=0,
        length=52,
    )
    entity_bold1 = types.MessageEntity(
        type="bold",
        offset=0,
        length=52,
    )
    entities1 = [entity_italic1, entity_bold1]
    entities = [entity_mono]
    await message.answer(text=txt, entities=entities)
    await message.answer('\nДля выбора группы нажмите соответствующую кнопку:   ', entities=entities1)
    await message.answer('\nДля просмотра информации о матче введите его номер: ', entities=entities1)


@router.message(F.text == kb.kb_main_list[2])  # Финал
async def matches_finals(message: Message):
    txt = eu.msg_matches_final
    entity_mono = types.MessageEntity(
        type="code",
        offset=0,
        length=len(txt),
    )
    entity_bold = types.MessageEntity(
        type="bold",
        offset=0,
        length=34,
    )
    entity_underline = types.MessageEntity(
        type="underline",
        offset=0,
        length=34,
    )
    entity_italic2 = types.MessageEntity(
        type="italic",
        offset=0,
        length=62,
    )
    entity_bold2 = types.MessageEntity(
        type="bold",
        offset=0,
        length=62,
    )
    entities = [entity_mono]
    entities1 = [entity_bold, entity_underline]
    entities2 = [entity_italic2, entity_bold2]

    await message.answer(
        'Расписание игр финального турнира: ',
        entities=entities1,
        reply_markup=kb.kb_main_plus_itog
    )
    await message.answer(text=txt, entities=entities)
    await message.answer('\nДля просмотра итоговой таблицы нажмите соответствующую кнопку: ', entities=entities2)
    await message.answer('\nДля просмотра информации о матче введите его номер:            ', entities=entities2)



@router.message(F.text == kb.kb_itog_list[0])  # Итог
async def table_itog(message: Message):
    txt = eu.msg_itog_table
    entity_mono = types.MessageEntity(
        type="code",
        offset=0,
        length=len(txt),
    )
    entity_bold1 = types.MessageEntity(
        type="bold",
        offset=0,
        length=24,
    )
    entity_underline1 = types.MessageEntity(
        type="underline",
        offset=0,
        length=24,
    )
    entities = [entity_mono]
    entities1 = [entity_bold1, entity_underline1]
    await message.answer('Итоговая таблица ЧЕ2024  ', entities=entities1)
    await message.answer(text=txt, entities=entities)
    # await message.answer('\nДля выбора группы нажмите соответствующую кнопку:')


@router.message(F.text == kb.kb_main_list[3])   # Рейтинги участников ЧЕ2024
async def table_fifa(message: Message):
    txt = eu.msg_ratings_euro
    entity_mono = types.MessageEntity(
        type="code",
        offset=0,
        length=len(txt),
    )
    entity_bold1 = types.MessageEntity(
        type="bold",
        offset=0,
        length=26,
    )
    entity_underline1 = types.MessageEntity(
        type="underline",
        offset=0,
        length=26,
    )
    entity_italic2 = types.MessageEntity(
        type="italic",
        offset=0,
        length=68,
    )
    entity_bold2 = types.MessageEntity(
        type="bold",
        offset=0,
        length=68,
    )
    entities1 = [entity_bold1, entity_underline1]
    entities2 = [entity_bold2, entity_italic2]
    entities = [entity_mono]
    await message.answer("Рейтинг участников ЧЕ2024: ", entities=entities1)
    await message.answer(text=txt, entities=entities, reply_markup=kb.kb_main_plus_rating_uefa)
    await message.answer("Для просмотра рейтингов ФИФА и УЕФА нажмите соответствующую кнопку:  ",
                         entities=entities2)


@router.message(F.text == kb.kb_ratings_list[0])     # Рейтинг ФИФА
async def ratings(message: Message):
    txt1 = eu.msg1_ratings
    txt2 = eu.msg2_ratings
    txt3 = eu.msg3_ratings
    txt4 = eu.msg4_ratings
    txt5 = eu.msg5_ratings
    entity_mono1 = types.MessageEntity(type="code", offset=0, length=len(txt1))
    entity_mono2 = types.MessageEntity(type="code", offset=0, length=len(txt2))
    entity_mono3 = types.MessageEntity(type="code", offset=0, length=len(txt3))
    entity_mono4 = types.MessageEntity(type="code", offset=0, length=len(txt4))
    entity_mono5 = types.MessageEntity(type="code", offset=0, length=len(txt5))

    entity_bold1 = types.MessageEntity(
        type="bold",
        offset=0,
        length=14,
    )
    entity_underline1 = types.MessageEntity(
        type="underline",
        offset=0,
        length=14,
    )
    entities1 = [entity_bold1, entity_underline1]
    await message.answer('Рейтинг ФИФА:  ', entities=entities1, reply_markup=kb.kb_main_plus_rating_uefa)
    entities = [entity_mono1]
    await message.answer(text=txt1, entities=entities)
    entities = [entity_mono2]
    await message.answer(text=txt2, entities=entities)
    entities = [entity_mono3]
    await message.answer(text=txt3, entities=entities)
    entities = [entity_mono4]
    await message.answer(text=txt4, entities=entities)
    entities = [entity_mono5]
    await message.answer(text=txt5, entities=entities)


@router.message(F.text == kb.kb_ratings_list[1])  # Рейтинг УЕФА
async def ratings_uefa(message: Message):
    txt1 = eu.msg1_ratings_uefa
    txt2 = eu.msg2_ratings_uefa

    entity_mono1 = types.MessageEntity(type="code", offset=0, length=len(txt1))
    entity_mono2 = types.MessageEntity(type="code", offset=0, length=len(txt2))

    entity_bold1 = types.MessageEntity(
        type="bold",
        offset=0,
        length=14,
    )
    entity_underline1 = types.MessageEntity(
        type="underline",
        offset=0,
        length=14,
    )
    entities1 = [entity_bold1, entity_underline1]
    await message.answer('Рейтинг УЕФА: ', entities=entities1, reply_markup=kb.kb_main_plus_rating_uefa)
    entities = [entity_mono1]
    await message.answer(text=txt1, entities=entities)
    entities = [entity_mono2]
    await message.answer(text=txt2, entities=entities)



@router.message(F.text == kb.kb_main_list[4])     # Прогнозы
async def predicts(message: Message):
    if eu.itog_table[0].strip() != "-":
        await message.answer("Чемпионат закончен, прогнозы не требуются!")



@router.message()   # Вывод информации о матче по его номеру
async def match_info(message: Message):
    matches_groups_in = eu.matches
    matches_finals_in = eu.matches_final

    try:
       match_num = int(message.text)
    except ValueError:
        await message.answer(
            text="Введите номер матча:",
            reply_markup=kb.kb_main
        )
        return

    match_info_out = eu.match_info_to_bot(matches_groups_in, matches_finals_in, match_num)

    if match_info_out:
        txt = match_info_out
    else:
        txt = "                    \nМатч с таким номером отсутствует!  "

    entity_bold = types.MessageEntity(      # Жирный
        type="bold",
        offset=0,
        length=55,
    )
    entity_italic = types.MessageEntity(    # Курсив
        type="italic",
        offset=0,
        length=20,
    )
    entity_underline = types.MessageEntity(  # Подчеркивание
        type="underline",
        offset=0,
        length=20,
    )
    entities = [
        entity_bold,
        entity_italic,
        entity_underline,
    ]
    await message.answer(
        text=txt,
        entities=entities,
        reply_markup=kb.kb_main
    )
