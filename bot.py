# (©)Codexbotz
# Recode by @mrismanaziz

import pyromod.listen
import sys

from pyrogram import Client

from config import (
    API_HASH,
    APP_ID,
    CHANNEL_ID,
    FORCE_SUB_CHANNEL1,
    FORCE_SUB_CHANNEL2,
    FORCE_SUB_GROUP1,
    FORCE_SUB_GROUP2,
    LOGGER,
    OWNER,
    TG_BOT_TOKEN,
    TG_BOT_WORKERS,
)


class Bot(Client):
    def __init__(self):
        super().__init__(
            "Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={"root": "plugins"},
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN,
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()

        if FORCE_SUB_CHANNEL1:
            try:
                link = (await self.get_chat(FORCE_SUB_CHANNEL1)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL1)
                    link = (await self.get_chat(FORCE_SUB_CHANNEL1)).invite_link
                self.invitelink = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bot tidak dapat Mengambil link Invite dari Force Sub Channel!"
                )
                self.LOGGER(__name__).warning(
                    f"Silakan periksa kembali var FORCE_SUB_CHANNEL1 dan Pastikan Bot anda Admin di Channel dengan izin link invite Pengguna melalui link undangan, Subs Channel Saat Ini: {FORCE_SUB_CHANNEL1}"
                )
                self.LOGGER(__name__).info(
                    "Bot Berhenti. Tanyakan Ke https://t.me/mrismanaziz untuk Bantuan"
                )
                sys.exit()
        if FORCE_SUB_CHANNEL2:
            try:
                link = (await self.get_chat(FORCE_SUB_CHANNEL2)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL2)
                    link = (await self.get_chat(FORCE_SUB_CHANNEL2)).invite_link
                self.invitelink2 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bot tidak dapat Mengambil link Invite dari Force Sub Channel!"
                )
                self.LOGGER(__name__).warning(
                    f"Silakan periksa kembali var FORCE_SUB_CHANNEL2 dan Pastikan Bot anda Admin di Channel dengan izin link invite Pengguna melalui link undangan, Subs Channel Saat Ini: {FORCE_SUB_CHANNEL2}"
                )
                self.LOGGER(__name__).info(
                    "Bot Berhenti. Tanyakan Ke https://t.me/mrismanaziz untuk Bantuan"
                )
                sys.exit()
        if FORCE_SUB_GROUP1:
            try:
                link = (await self.get_chat(FORCE_SUB_GROUP1)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_GROUP1)
                    link = (await self.get_chat(FORCE_SUB_GROUP1)).invite_link
                self.invitelink3 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bot tidak dapat Mengambil link Invite dari Force Sub Channel!"
                )
                self.LOGGER(__name__).warning(
                    f"Silakan periksa kembali var FORCE_SUB_GROUP1 dan Pastikan Bot anda Admin di Channel dengan izin link invite Pengguna melalui link undangan, Subs Channel Saat Ini: {FORCE_SUB_GROUP1}"
                )
                self.LOGGER(__name__).info(
                    "Bot Berhenti. Tanyakan Ke https://t.me/mrismanaziz untuk Bantuan"
                )
                sys.exit()
        if FORCE_SUB_GROUP2:
            try:
                link = (await self.get_chat(FORCE_SUB_GROUP2)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_GROUP2)
                    link = (await self.get_chat(FORCE_SUB_GROUP2)).invite_link
                self.invitelink4 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bot tidak dapat Mengambil link Invite dari Force Sub Channel!"
                )
                self.LOGGER(__name__).warning(
                    f"Silakan periksa kembali var FORCE_SUB_GROUP2 dan Pastikan Bot anda Admin di Channel dengan izin link invite Pengguna melalui link undangan, Subs Channel Saat Ini: {FORCE_SUB_GROUP2}"
                )
                self.LOGGER(__name__).info(
                    "Bot Berhenti. Tanyakan Ke https://t.me/mrismanaziz untuk Bantuan"
                )
                sys.exit()
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id=db_channel.id, text="Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(
                f"Pastikan Bot adalah Admin di Channel DataBase, dan Periksa kembali CHANNEL_ID, Nilai Saat Ini: {CHANNEL_ID}"
            )
            self.LOGGER(__name__).info(
                "Bot Berhenti. Tanyakan Ke https://t.me/mrismanaziz untuk Bantuan"
            )
            sys.exit()

        self.set_parse_mode("html")
        self.LOGGER(__name__).info(
            f"[🔥 BERHASIL DIAKTIFKAN! 🔥]\n\nBOT Dibuat oleh @{OWNER}"
        )
        self.username = usr_bot_me.username

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot Terhenti.")
