import logging
from aiogram import Router, Bot, F
from aiogram.filters import StateFilter, Command

from aiogram.fsm.context import FSMContext
from aiogram.types import (
    Message,
    CallbackQuery,
)

from keyboards.inline_buttons import home_menu
from main import crete_seo, random_query, improve_seo, mark_answer_create

logger = logging.getLogger(__name__)
router = Router()


@router.message(Command("start"))
async def start_bot_command(message: Message, state: FSMContext, bot: Bot):
    await message.answer(
        "<b>👋 Привет, это демо бот <code>Просто Доставка</code></b>",
        reply_markup=home_menu()
    )


@router.callback_query(F.data.startswith("mark_answer"))
async def mark_answer_call(call: CallbackQuery, state: FSMContext):
    await call.message.answer(
        "<b>🟡 Пришли мне текст отзыва, который оставил покупатель\n\nДля более развернутого ответа, "
        "можете дополнить отзыв характеристиками товара</b>"
    )
    await state.set_state('mark_answer_state')


@router.message(StateFilter('mark_answer_state'))
async def improve_seo_state(message: Message, state: FSMContext):
    try:
        await message.answer('<b>⏳ создаю ответ...</b>')
        await state.clear()
        result = mark_answer_create(message.text)
        await message.reply(
            f"<b>✅ Ответ сгенерирован.</b>\n\n<code>{result}</code>",
            reply_markup=home_menu()
        )
    except Exception as ex:
        await state.clear()
        print(ex, "mark_answer_state")
        await message.answer(
            '<b>❌Неизвестная ошибка</b>',
            reply_markup=home_menu()
        )


@router.callback_query(F.data.startswith("improve_seo"))
async def improve_seo_call(call: CallbackQuery, state: FSMContext):
    await call.message.answer(
        "<b>👍 Прекрасно, пришли мне текущее описание своего товара, а нейросеть его улучшит.</b>"
    )
    await state.set_state('improve_seo_state')


@router.message(StateFilter('improve_seo_state'))
async def improve_seo_state(message: Message, state: FSMContext):
    try:
        await message.answer('<b>⏳ улучшаем описание...</b>')
        await state.clear()
        result = improve_seo(message.text)
        await message.reply(
            f"<b>✅ Редактирование описания завершено.</b>\n\n<code>{result}</code>",
            reply_markup=home_menu()
        )
    except Exception as ex:
        await state.clear()
        print(ex, "improve_seo_state")
        await message.answer(
            '<b>❌Неизвестная ошибка</b>',
            reply_markup=home_menu()
        )


@router.callback_query(F.data.startswith("question_ii"))
async def random_query_ii_call(call: CallbackQuery, state: FSMContext):
    await call.message.answer(
        "<b>👍 Окей, ты можешь задать любой вопрос нейросети и она даст ответ.</b>"
    )
    await state.set_state('random_quest_ii')


@router.message(StateFilter('random_quest_ii'))
async def random_quest_state(message: Message, state: FSMContext):
    try:
        await message.answer('<b>⏳ генерирую ответ нейросети...</b>')
        await state.clear()
        result = random_query(message.text)
        await message.reply(
            f"<b>✅ Ответ успешно сгенерировано.</b>\n\n<code>{result}</code>",
            reply_markup=home_menu()
        )
    except Exception as ex:
        await state.clear()
        print(ex, "random_quest_ii")
        await message.answer(
            '<b>❌Неизвестная ошибка</b>',
            reply_markup=home_menu()
        )


@router.callback_query(F.data.startswith("seo_cart"))
async def create_new_seo_call(call: CallbackQuery, state: FSMContext):
    await call.message.answer(
        "<b>👍Хорошо, напиши мне данные для создания описания карточки в таком формате:</b>\n\n"
        "1. Название товара\n"
        "2. Ключевые слова\n\n"
        "<i>Пример:\n1. Салфетница\n2. привлекательная, удобная, эстетичная.</i>"
    )
    await state.set_state('set_seo_prompt')


@router.message(StateFilter('set_seo_prompt'))
async def seo_prompt_state(message: Message, state: FSMContext):
    try:
        name = message.text.split('1.')[1].split('\n')[0].strip()
        words = message.text.split('2.')[1].split('\n')[0].strip()
        await message.answer('<b>⏳ генерирую описание для карточки...</b>')
        await state.clear()
        result = crete_seo(name, words)
        await message.answer(
            f"<b>✅ Описание успешно сгенерировано.</b>\n\n<code>{result}</code>",
            reply_markup=home_menu()
        )
    except Exception as ex:
        await state.clear()
        print(ex, "seo_prompt_state")
        await message.answer(
            '<b>❌Вы указали данные не по шаблону!\n\nПопробуйте снова</b>',
            reply_markup=home_menu()
        )