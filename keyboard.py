from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


def memslots_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🎲 MemDice",
                    url="https://t.me/MemDiceBot"
                )
            ]
        ]
    )


def start_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🎲 Играть",
                    url="https://t.me/lolmanchat"
                )
            ]
        ]
    )


def duel_request_kb(duel_id: str):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="✅ Принять",
                    callback_data=f"duel_accept:{duel_id}"
                ),
                InlineKeyboardButton(
                    text="❌ Отказать",
                    callback_data="duel_decline"
                )
            ]
        ]
    )


def duel_start_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="⚔ Дуэль",
                    url="https://t.me/MemSlotsBot"
                )
            ]
        ]
    )
