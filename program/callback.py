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

 1 ↤ أولاً ، أضفني إلى مجموعتك
 2 ↤ بعد ذلك ، قم بترقيتي كمشرف ومنح جميع الصلاحيات باستثناء الوضع الخفي
 3 ↤ بعد ترقيتي ، اكتب /reload مجموعة لتحديث بيانات المشرفين
 4 ↤ أضف @{ASSISTANT_NAME} إلى مجموعتك أو اكتب انضم لدعوة حساب المساعد
 5 ↤ قم بتشغيل المكالمة  أولاً قبل البدء في تشغيل الفيديو / الموسيقى
 6 ↤ في بعض الأحيان ، يمكن أن تساعدك إعادة تحميل البوت باستخدام الأمر /reload في إصلاح بعض المشكلات
 📌 إذا لم ينضم البوت إلى المكالمة ، فتأكد من تشغيل المكالمة  بالفعل ، أو اكتب /userbotleave ثم اكتب /userbotjoin مرة أخرى

 💡 إذا كانت لديك أسئلة  حول هذا البوت ، فيمكنك إخبارنا منن خلال قروب الدعم الخاصة بي هنا ↤ @{GROUP_SUPPORT}

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

» /play +「اسم الأغنية / رابط」لتشغيل اغنيه في المحادثه الصوتيه
» /vplay +「اسم الفيديو / رابط 」 لتشغيل الفيديو داخل المكالمة
» /vstream 「رابط」 تشغيل فيديو مباشر من اليوتيوب
» /playlist 「تظهر لك قائمة التشغيل」
» /end「لإنهاء الموسيقى / الفيديو في الكول」
» /song + 「الاسم تنزيل صوت من youtube」
»/vsong + 「الاسم  تنزيل فيديو من youtube」
» /skip「للتخطي إلى التالي」
» /ping 「إظهار حالة البوت بينغ」
» /uptime 「لعرض مده التشغيل للبوت」
» /alive「اظهار معلومات البوت(في المجموعه)」
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
» /stop「بۆ کوژانەوە」
» /vmute 「بۆ بێدەنکردنی بۆتەکە」
» /vunmute 「بۆ لابردنی بێدەنگی بۆتەکە」
» /volume 「رێکخستنی قه باره ی ده نگ」
» /reload「بۆ نوێکردنەوەی بۆتەکە و لیستی ئەدمینەکان」
» /userbotjoin「بۆ بانگهێشتکردنی ئاکاونتی یارمەتیدەر」
» /userbotleave「بۆ دەرکردنی ئەکاونتی یارمەتیدەر」
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
              f"⚙️ **رێکخستنه کان** {query.message.chat.title}\n\n⏸ : ايقاف التشغيل موقتآ\n▶️ : استئناف التشغيل\n🔇 : كتم الصوت\n🔊 : الغاء كتم الصوت\n⏹ : ايقاف التشغيل",
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
