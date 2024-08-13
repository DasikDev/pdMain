import logging

import math
import random
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

logger = logging.getLogger(__name__)


def home_menu() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="📋 Создать описание карточки", callback_data="seo_cart")
    keyboard.button(text="❔ Задать вопрос нейросети", callback_data="question_ii")
    keyboard.button(text="🌟 Ответ на отзыв", callback_data="mark_answer")
    keyboard.adjust(1, 1, 1)
    return keyboard.as_markup()