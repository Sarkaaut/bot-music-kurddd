# Copyright (C) 2022 By Shadow

from driver.queues import QUEUE
from pyrogram import Client, filters
from program.utils.inline import menu_markup
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    BOT_PHOTO,
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.answer("ماڵپەڕی سەرەکی")
    await query.edit_message_text(
        f"""👋 **سڵاو ئازیزم »「 [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) 」!**\n
**᥀︙ من بۆتێکم کە دەتوانم لە پەیوەندی دەنگیدا گۆرانی و مۆسیقا لێبدەم!

᥀︙ بۆ زانینی فەرمانەکانی ئەم بۆتە، کلیک لەسەر ‹فەرمانە بنەڕەتییەکان›!

᥀︙ بۆ زانینی چۆنیەتی کارپێکردنی ئەم بۆتە، کلیک لەسەر شێوازی ‹کارپێکردنی بکە›!
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("", callback_data="cbhowtouse")
                    ],
                [
                    InlineKeyboardButton("‹ کارپێکردن › ", callback_data="cbcmds"),
                    InlineKeyboardButton("خاوه ن بۆت", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "‹ گرووپ پشتگیری ›", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "‹ که ناڵی بۆت ›", url=f"https://t.me/EITHON1"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "بۆتەکە زیاد بکە بۆ گروپەکەت",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.answer("شیوازی به کارهێنان")
    await query.edit_message_text(
        f""" ڕێنمایی بنەڕەتی بۆ بەکارهێنانی ئەم بۆتە:

 سەرەتا من زیاد بکە بۆ گروپەکەت
 دواتر وەک ئەدمین بەرزم بکەرەوە و هەموو دەسەڵاتەکانت پێ بدە جگە لە دۆخی دزێو
 دوای بەرزکردنەوەی من /reload گرووپ بنووسە بۆ نوێکردنەوەی داتای ئەدمینەکان
 زیاد @{ASSISTANT_NAME} بکە بۆ گروپەکەت یان بانگهێشتی ئەژمێری یارمەتیدەر بنووسە
 قم بتشغيل المكالمة  أولاً قبل البدء في تشغيل الفيديو / الموسيقى
 هەندێک جار دووبارە بارکردنەوەی بۆتەکە بە فرمانی /reload دەتوانێت یارمەتیت بدات بۆ چارەسەرکردنی هەندێک کێشە
 ئەگەر بۆتەکە بەشداری پەیوەندییەکە نەکرد، دڵنیابە پەیوەندییەکە پێشتر چالاکە، یان /userbotleave بنووسە و پاشان دووبارە /userbotjoin بنووسە

💡 ئەگەر پرسیارتان هەیە دەربارەی ئەم بۆتە ئەتوانن لە ڕێگەی گروپی پشتگیری منەوە لێرە پێمان بڵێن ↤ @{GROUP_SUPPORT

""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 گه رانه وه", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.answer("لیستی فه رمانه کان")
    await query.edit_message_text(
        f"""» **کلیک لەسەر ئەو دوگمەیە بکە کە دەتەوێت داواکارییەکانی هەر پۆلێکیان ببینیت !**

 """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷🏻 فەرمانەکانی ئادمین", callback_data="cbadmin"),
                    InlineKeyboardButton("🧙🏻 فەرمانەکانی گەشەپێدەر", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("📚 فەرمانە بنەڕەتییەکان", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙 گه رانه وه", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.answer("فەرمانە بنەڕەتییەکان")
    await query.edit_message_text(
        f"""🏮 فەرمانە بنەڕەتییەکان:

» /play +「ناوی گۆرانی/لینک」بۆ لێدانی گۆرانییەک لە چاتی دەنگیدا
» /vplay +「ناوی ڤیدیۆ / بەستەر」 بۆ پەخشکردنی ڤیدیۆکە لەناو پەیوەندییەکەدا
» /vstream 「لینك」 ڤیدیۆیەکی ڕاستەوخۆ لە یوتیوبەوە پەخش بکە
» /playlist 「پلەی لیست دەردەکەوێت」
» /end「بۆ تەواوکردنی مۆسیقا/ڤیدیۆ لە کۆلاج」
» /song +「ناو داگرتنی دەنگ لە youtube」
» /vsong +「ناو ڤیدیۆ لە youtube دابەزێنە」
» /skip「بۆ پەڕینەوە بۆ گۆرانی دواتر」
» /ping 「دۆخی بۆت پیشان بدە」
» /uptime 「بۆ پیشاندانی کاتی کارکردنی بۆتەکە」
» /alive「زانیارییەکانی بۆت پیشان بدە (لە گروپەکەدا)」
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 گه رانه وه", callback_data="cbcmds")]]
        ),
    )



@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.answer("فەرمانەکانی ئادەمین")
    await query.edit_message_text(
        f"""🏮 لێرەدا فەرمانەکانی ئەدمین دەخەینەڕوو:

» /pause 「وەستاندنی پەخشکردن」
» /resume 「دەستپێکردنەوەی پەخشکردن」
» /stop 「بۆ کوژانەوە」
» /vmute 「بۆ بێدەنکردنی بۆتەکە」
» /vunmute 「بۆ لابردنی بێدەنگی بۆتەکە」
» /volume 「رێکخستنی قه باره ی ده نگ」
» /reload 「بۆ نوێکردنەوەی بۆتەکە و لیستی ئەدمینەکان」
» /userbotjoin 「بۆ بانگهێشتکردنی ئاکاونتی یارمەتیدەر」
» /userbotleave 「بۆ دەرکردنی ئەکاونتی یارمەتیدەر」
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 گه رانه وه", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.answer("فەرمانەکانی گەشەپێدەر")
    await query.edit_message_text(
        f"""🏮 لێرەدا فەرمانەکانی گەشەپێدەر دەخەینەڕوو:

» /rmw「بۆ سڕینەوەی هەموو فایلەکان」
» /rmd「هەموو فایلە دابەزێنراوەکان بسڕەوە」
» /sysinfo「بۆ زانیاری سێرڤەر」
» /update「نوێکردنەوە ي بۆتت بۆ ئاخر نسخ」
» /restart「بۆتەکە دووبارە بوت بکەرەوە」
» /leaveall「ده رچۆنی ئاکاونتی یارمه تیده ر له هه مو گروپه کانه وه」
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 گه رانه وه", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 تەنها ئەو بەڕێوەبەرەی کە مۆڵەتی بەڕێوەبردنی چاتی دەنگی هەیە دەتوانێت کرتە لەم دوگمەیە بکات !", show_alert=True)
    chat_id = query.message.chat.id
    user_id = query.message.from_user.id
    buttons = menu_markup(user_id)
    chat = query.message.chat.title
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ : {query.message.chat.title}\n\n⏸ : وەستاندنی پەخشکردن\n▶️ : دەستپێکردنەوەی پەخشکردن\n🔇 : بێدەنگ\n🔊 : بێدەنگ نەکردن\n⏹ : پەخشکردن ڕابگرە",
              reply_markup=InlineKeyboardMarkup(buttons),
          )
    else:
        await query.answer("❌ پلەی لیست بەتاڵە", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 تەنها ئەو بەڕێوەبەرەی کە مۆڵەتی بەڕێوەبردنی چاتی دەنگی هەیە دەتوانێت کرتە لەم دوگمەیە بکات !", show_alert=True)
    await query.message.delete()
