from django.core.management.base import BaseCommand
from django.conf import settings
from telegram import Bot
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater
from telegram.utils.request import Request


from bot.models import Message
from bot.models import Profile
from bot.views import get_profiles


def list(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text("/list \n /func")


def func(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text("Знайти похідну функції у= 2х﻿²-1")


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(
        "Команда не знайдена. Для відображення списку доступних команд наберіть /list"
    )


class Command(BaseCommand):
    help = "Телеграм-бот"

    def handle(self, *args, **options):
        request = Request(connect_timeout=0.5, read_timeout=1.0)
        bot = Bot(
            request=request,
            token="910669360:AAFv_1cPo-QMfe_Xt_GajxE5V4pex0qaeB8",
            base_url=getattr(settings, "PROXY_URL", None),
        )
        updater = Updater(bot=bot, use_context=True)
        dp = updater.dispatcher
        dp.add_handler(CommandHandler("list", list))
        dp.add_handler(CommandHandler("func", func))
        dp.add_handler(MessageHandler(Filters.text, echo))
        # run endless incoming message processing
        updater.start_polling()
        updater.idle()
