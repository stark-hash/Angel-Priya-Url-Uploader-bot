#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram.types.bots_and_keyboards import InlineKeyboardButton, InlineKeyboardMarkup


@pyrogram.Client.on_message(pyrogram.filters.command(["help"]))
async def help_user(bot, update):
    if update.from_user.id in Config.AUTH_USERS:
        # logger.info(update)
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.HELP_USER,
            parse_mode="html",
            disable_web_page_preview=True,
            reply_to_message_id=update.message_id
        )


@pyrogram.Client.on_message(pyrogram.filters.command(["start"]))
async def start(bot, update):
    if update.from_user.id in (Config.AUTH_USERS & Config.LAZY_DEVELOPER):
        # logger.info(update)
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.LAZY_DEVELOPER_TEXT.format(update.from_user.first_name),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⚡️𝔖𝔲𝔭𝔭𝔬𝔯𝔱", url="https://t.me/StarkBotSupport"),
                        InlineKeyboardButton("⭑💢 𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁 💢⭑", url="https://t.me/AnAutoFilterBot"),
                        InlineKeyboardButton("⚡️ U𝖕𝖉𝖆𝖙e", url="https://t.me/StarkBotUpdates"),
                    ],
                    [InlineKeyboardButton("⭑💢 𝙵𝙸𝙻𝙴 𝚂𝚃𝙾𝚁𝙴 💢⭑", url="https://t.me/FDFileStoreBot")],
                    [InlineKeyboardButton("🦋 ⭑┗━━┫⦀⦙ O W N E R ⦙⦀┣━━┛⭑ 🦋", url="https://t.me/TalismanBro")],
                ]
            ),
            reply_to_message_id=update.message_id
        )
    elif update.from_user.id in Config.AUTH_USERS:
        # logger.info(update)
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.START_TEXT.format(update.from_user.first_name),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⚡️𝔖𝔲𝔭𝔭𝔬𝔯𝔱", url="https://t.me/LazyPrincessSupport"),
                        InlineKeyboardButton("⭑💢 𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁 💢⭑", url="https://t.me/AnAutoFilterBot"),
                        InlineKeyboardButton("⚡️ U𝖕𝖉𝖆𝖙e", url="https://t.me/StarkBotUpdates"),
                    ],
                    [InlineKeyboardButton("⭑💢 𝙵𝙸𝙻𝙴 𝚂𝚃𝙾𝚁𝙴 💢⭑", url="https://t.me/FDFileStoreBot")],
                    [InlineKeyboardButton("🦋 ⭑┗━━┫⦀⦙ O W N E R ⦙⦀┣━━┛⭑ 🦋", url="https://t.me/TalismanBro")],
                ]
            ),
            reply_to_message_id=update.message_id
        )
    else:
        # logger.info(update) ==         
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.LAZY_START_TEXT.format(update.from_user.first_name),
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("🦋 ⭑┗━━┫⦀⦙ O W N E R ⦙⦀┣━━┛⭑ 🦋", url="https://t.me/TalismanBro")],
                    [
                        InlineKeyboardButton("▍║▍▏║ UPDATE ║▍▏║▍", url="https://t.me/StarkBotUpdates"),
                    ],
                    [InlineKeyboardButton("⭑💢 𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁 💢⭑", url="https://t.me/AnAutoFilterBot")],
                ]
            ),
            reply_to_message_id=update.message_id
        )
         
