from aiogram import F, Router, types
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from random import randint

import app.keyboards as kb

import euro2024 as eu
from prognosis import matches_formation_predict, final_formation_predict

router = Router()


@router.message(CommandStart())
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
    entities = [entity_mono]
    await message.answer('Расписание игр группового турнира: ', reply_markup=kb.kb_main)
    await message.answer(text=txt, entities=entities)


@router.message(F.text == kb.kb_main_list[1])    # Таблицы
async def tables(message: Message):
    txt = eu.msg_tables
    entity_mono = types.MessageEntity(
        type="code",
        offset=0,
        length=len(txt),
    )
    entities = [entity_mono]
    await message.answer('Таблицы результатов группового турнира.',
                         reply_markup=kb.kb_main_plus_groups)
    await message.answer(text=txt, entities=entities)
    await message.answer('\nДля выбора группы нажмите соответствующую кнопку:')


@router.message(F.text == kb.kb_groups_list[0])  # группа A
async def table_a(message: Message):
    txt = eu.msg_group1
    entity_mono = types.MessageEntity(
        type="code",
        offset=0,
        length=len(txt),
    )
    entities = [entity_mono]
    await message.answer(text=txt, entities=entities)
    await message.answer('\nДля выбора группы нажмите соответствующую кнопку:')


@router.message(F.text == kb.kb_groups_list[1])  # группа B
async def table_b(message: Message):
    txt = eu.msg_group2
    entity_mono = types.MessageEntity(
        type="code",
        offset=0,
        length=len(txt),
    )
    # entity_bold = types.MessageEntity(
    #     type="bold",
    #     offset=5,
    #     length=8,
    # )
    # entity_italic = types.MessageEntity(
    #     type="italic",
    #     offset=16,
    #     length=30,
    # )
    entities = [entity_mono]
    await message.answer(text=txt, entities=entities)
    await message.answer('\nДля выбора группы нажмите соответствующую кнопку:')


@router.message(F.text == kb.kb_groups_list[2])  # группа C
async def table_c(message: Message):
    txt = eu.msg_group3
    entity_mono = types.MessageEntity(
        type="code",
        offset=0,
        length=len(txt),
    )
    entities = [entity_mono]
    await message.answer(text=txt, entities=entities)
    await message.answer('\nДля выбора группы нажмите соответствующую кнопку:')


@router.message(F.text == kb.kb_groups_list[3])  # группа D
async def table_d(message: Message):
    txt = eu.msg_group4
    entity_mono = types.MessageEntity(
        type="code",
        offset=0,
        length=len(txt),
    )
    entities = [entity_mono]
    await message.answer(text=txt, entities=entities)
    await message.answer('\nДля выбора группы нажмите соответствующую кнопку:')


@router.message(F.text == kb.kb_groups_list[4])  # группа E
async def table_e(message: Message):
    txt = eu.msg_group5
    entity_mono = types.MessageEntity(
        type="code",
        offset=0,
        length=len(txt),
    )
    entities = [entity_mono]
    await message.answer(text=txt, entities=entities)
    await message.answer('\nДля выбора группы нажмите соответствующую кнопку:')


@router.message(F.text == kb.kb_groups_list[5])  # группа F
async def table_f(message: Message):
    txt = eu.msg_group6
    entity_mono = types.MessageEntity(
        type="code",
        offset=0,
        length=len(txt),
    )
    entities = [entity_mono]
    await message.answer(text=txt, entities=entities)
    await message.answer('\nДля выбора группы нажмите соответствующую кнопку:')


@router.message(F.text == kb.kb_main_list[2])  # Финал
async def matches_finals(message: Message):
    txt = eu.msg_matches_final
    entity_mono = types.MessageEntity(
        type="code",
        offset=0,
        length=len(txt),
    )
    entities = [entity_mono]
    await message.answer('Расписание игр финального турнира: ', reply_markup=kb.kb_main)
    await message.answer(text=txt, entities=entities)


@router.message(F.text == kb.kb_main_list[3])   # Рейтинги
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
    await message.answer('Рейтинг ФИФА: ', reply_markup=kb.kb_main_plus_rating_uefa)
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
    await message.answer("Рейтинги команд участников ЧЕ2024")


@router.message(F.text == kb.kb_ratings_list[0])     # Рейтинги участников ЧЕ2024
async def table_f(message: Message):
    txt = eu.msg_ratings_euro
    entity_mono = types.MessageEntity(
        type="code",
        offset=0,
        length=len(txt),
    )
    entities = [entity_mono]
    await message.answer(text=txt, entities=entities)
    # await message.answer('\nДля выбора группы нажмите соответствующую кнопку:')


@router.message(F.text == kb.kb_main_list[4])     # Прогноз еще прогноз...
async def predicts(message: Message):
    # формирование прогноза
    teams_predict = eu.teams.copy()
    matches_predict = eu.matches.copy()
    matches_final_predict = eu.matches_final.copy()
    matches_formation_predict(matches_predict)
    # predicts.matches_formation_predict(matches_predict)
    eu.tables_formation(teams_predict, matches_predict)
    msg_matches_predict = eu.matches_to_bot(matches_predict) + eu.separator(33)
    group_itog_predict = eu.tables_sort(teams_predict)
    msg_tables_predict = eu.tables_to_bot(group_itog_predict) + eu.separator(33)
    msg_group1_predict = (eu.matches_group_to_bot(matches_predict, 1) +
                          eu.table_group_to_bot(group_itog_predict, 1) + eu.separator(33))
    msg_group2_predict = (eu.matches_group_to_bot(matches_predict, 2) +
                          eu.table_group_to_bot(group_itog_predict, 2) + eu.separator(33))
    msg_group3_predict = (eu.matches_group_to_bot(matches_predict, 3) +
                          eu.table_group_to_bot(group_itog_predict, 3) + eu.separator(33))
    msg_group4_predict = (eu.matches_group_to_bot(matches_predict, 4) +
                          eu.table_group_to_bot(group_itog_predict, 4) + eu.separator(33))
    msg_group5_predict = (eu.matches_group_to_bot(matches_predict, 5) +
                          eu.table_group_to_bot(group_itog_predict, 5) + eu.separator(33))
    msg_group6_predict = (eu.matches_group_to_bot(matches_predict, 5) +
                          eu.table_group_to_bot(group_itog_predict, 6) + eu.separator(33))
    finalists_predict = eu.finalists_from_group(group_itog_predict)
    # 1/8 финала
    matches_final_predict = eu.final_8_formation(finalists_predict, matches_final_predict)
    matches_final_predict = final_formation_predict(matches_final_predict, '1/8')
    finalists_8_predict = eu.finalists_from_finals(matches_final_predict, '1/8')
    # 1/4 финала
    matches_final_predict = eu.final_4_formation(finalists_8_predict, matches_final_predict)
    matches_final_predict = final_formation_predict(matches_final_predict, '1/4')
    finalists_4_predict = eu.finalists_from_finals(matches_final_predict, '1/4')
    # 1/2 финала
    matches_final_predict = eu.final_2_formation(finalists_4_predict, matches_final_predict)
    matches_final_predict = final_formation_predict(matches_final_predict, '1/2')
    finalists_2_predict = eu.finalists_from_finals(matches_final_predict, '1/2')
    # финал
    matches_final_predict = eu.final_1_formation(finalists_2_predict, matches_final_predict)
    matches_final_predict = final_formation_predict(matches_final_predict, '1/1')
    # итоговая таблица
    itog_table_predict = eu.itog_formation(matches_final_predict)
    msg_final_predict = eu.matches_final_to_bot(matches_final_predict)
    msg_itog_table_predict = eu.itog_table_to_bot(itog_table_predict)


    # return [
    #     msg_matches_predict,
    #     msg_tables_predict,
    #     msg_group1_predict,
    #     msg_group2_predict,
    #     msg_group3_predict,
    #     msg_group4_predict,
    #     msg_group5_predict,
    #     msg_group6_predict,
    #     msg_final_predict,
    #     msg_itog_table_predict
    # ]

    # вывод в бот




    #
    #
    # n = randint(40, 50)
    # # predict(n)
    # predict_to_bot = predict(n)
    txt1 = msg_matches_predict
    txt2 = msg_tables_predict
    txt3 = msg_final_predict
    txt4 = msg_itog_table_predict
    entity_mono1 = types.MessageEntity(type="code", offset=0, length=len(txt1))
    entity_mono2 = types.MessageEntity(type="code", offset=0, length=len(txt2))
    entity_mono3 = types.MessageEntity(type="code", offset=0, length=len(txt3))
    entity_mono4 = types.MessageEntity(type="code", offset=0, length=len(txt4))
    await message.answer('Прогноз: ', reply_markup=kb.kb_main)
    entities = [entity_mono1]
    await message.answer(text=txt1, entities=entities)
    entities = [entity_mono2]
    await message.answer(text=txt2, entities=entities)
    entities = [entity_mono3]
    await message.answer(text=txt3, entities=entities)
    entities = [entity_mono4]
    await message.answer(text=txt4, entities=entities)


'''
@router.callback_query(F.data == "t-shirts")
async def t_shirts(callback: CallbackQuery):
    await callback.answer("You have selected the category", show_alert=True)    # , show_alert=True
    await callback.message.answer("You have selected the t-shirts category")


@router.callback_query(F.data == "sneakers")
async def sneakers(callback: CallbackQuery):
    await callback.answer("You have selected the category", show_alert=True)    # show_alert=True
    await callback.message.answer("You have selected the sneakers category")


@router.callback_query(F.data == "caps")
async def caps(callback: CallbackQuery):
    await callback.answer("You have selected the category", show_alert=True)    # show_alert=True
    await callback.message.answer("You have selected the caps category")
    
    '''




