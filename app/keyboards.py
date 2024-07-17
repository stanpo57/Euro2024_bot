from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           # InlineKeyboardMarkup, InlineKeyboardButton,
    )


kb_main_list = ("Расписание", "Таблицы", "Финал", "Рейтинги", "Прогнозы")
kb_groups_list = ("A", "B", "C", "D", "E", "F")
kb_ratings_list = ("Рейтинг ФИФА", "Рейтинг УЕФА")
kb_itog_list = ("Итоговая таблица", )

kb_main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=kb_main_list[0]),
                                        KeyboardButton(text=kb_main_list[1]),
                                        KeyboardButton(text=kb_main_list[2]),
                                        KeyboardButton(text=kb_main_list[3]),
                                        KeyboardButton(text=kb_main_list[4])]],
                              resize_keyboard=True,
                              input_field_placeholder="Выберите кнопку")

kb_main_plus_groups = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=kb_main_list[0]),
                                        KeyboardButton(text=kb_main_list[1]),
                                        KeyboardButton(text=kb_main_list[2]),
                                        KeyboardButton(text=kb_main_list[3]),
                                        KeyboardButton(text=kb_main_list[4])],
                                        [KeyboardButton(text=kb_groups_list[0]),
                                        KeyboardButton(text=kb_groups_list[1]),
                                        KeyboardButton(text=kb_groups_list[2]),
                                        KeyboardButton(text=kb_groups_list[3]),
                                        KeyboardButton(text=kb_groups_list[4]),
                                        KeyboardButton(text=kb_groups_list[5])]],
                                resize_keyboard=True,
                                input_field_placeholder="Выберите кнопку")

kb_main_plus_itog = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=kb_main_list[0]),
                                        KeyboardButton(text=kb_main_list[1]),
                                        KeyboardButton(text=kb_main_list[2]),
                                        KeyboardButton(text=kb_main_list[3]),
                                        KeyboardButton(text=kb_main_list[4])],
                                        [KeyboardButton(text=kb_itog_list[0]),
                                         # KeyboardButton(text=kb_ratings_list[1])
                                         ]
                                                   ],
                              resize_keyboard=True,
                              input_field_placeholder="Выберите кнопку")




kb_main_plus_rating_uefa = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=kb_main_list[0]),
                                        KeyboardButton(text=kb_main_list[1]),
                                        KeyboardButton(text=kb_main_list[2]),
                                        KeyboardButton(text=kb_main_list[3]),
                                        KeyboardButton(text=kb_main_list[4])],
                                        [KeyboardButton(text=kb_ratings_list[0]),
                                         KeyboardButton(text=kb_ratings_list[1])]],
                              resize_keyboard=True,
                              input_field_placeholder="Выберите кнопку")
