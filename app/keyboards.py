from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           # InlineKeyboardMarkup, InlineKeyboardButton,
    )


kb_main_list = ("Расписание", "Таблицы", "Финал", "Рейтинги", "Прогноз еще прогноз...")
kb_groups_list = ("A", "B", "C", "D", "E", "F")
kb_ratings_list = ("Рейтинги участников ЧЕ2024", )

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

kb_main_plus_rating_uefa = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=kb_main_list[0]),
                                        KeyboardButton(text=kb_main_list[1]),
                                        KeyboardButton(text=kb_main_list[2]),
                                        KeyboardButton(text=kb_main_list[3]),
                                        KeyboardButton(text=kb_main_list[4])],
                                        [KeyboardButton(text=kb_ratings_list[0])]],
                              resize_keyboard=True,
                              input_field_placeholder="Выберите кнопку")


# kb_ratings_uefa = InlineKeyboardMarkup(inline_keyboard=[
#         {InlineKeyboardButton(text="Рейтинги участников ЧЕ", callback_data="ratings_euro")}])

