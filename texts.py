TEXTS = {
    "ru": {
        # ── language
        "lang_select": "🌐 Выберите язык / Tilni tanlang:",

        # ── welcome
        "welcome": (
            "👋 Добро пожаловать!\n\n"
            "Я — специалист по поведению потребителей и бренд-стратегии.\n\n"
            "Здесь вы найдёте моё портфолио, исследовательские опросы\n"
            "и возможность связаться со мной.\n\n"
            "Выберите раздел 👇"
        ),

        # ── menu buttons
        "btn_portfolio":   "🖼 Портфолио",
        "btn_surveys":     "📋 Опросы",
        "btn_about":       "🙋 Обо мне",
        "btn_contact":     "📩 Связаться",
        "btn_channel":     "📢 Канал",
        "btn_switch_lang": "🌐 O'zbekcha",
        "btn_main_menu":   "🏠 Главное меню",

        # ── about me
        "about_text": (
            "🙋 *Обо мне*\n\n"
            "Специалист по поведению потребителей и бренд-стратегии.\n\n"
            "Помогаю брендам понять свою аудиторию и выстроить стратегии, "
            "которые конвертируют. Открыт к фриланс-проектам и постоянному сотрудничеству.\n\n"
            "📊 *Специализация:*\n"
            "• Анализ поведения потребителей\n"
            "• Позиционирование и бренд-стратегия\n"
            "• SMM и управление контентом\n\n"
            "📩 Напишите мне — обсудим ваш проект!"
        ),

        # ── contact
        "contact_prompt": (
            "📩 *Связаться со мной*\n\n"
            "Напишите ваше сообщение — я отвечу как можно скорее."
        ),
        "contact_sent": (
            "✅ Сообщение отправлено!\n\n"
            "Я свяжусь с вами в ближайшее время."
        ),
        "admin_contact_notify": (
            "📨 *Новое сообщение!*\n\n"
            "👤 {name} (@{username})\n"
            "🆔 ID: `{user_id}`\n\n"
            "💬 {message}"
        ),

        # ── surveys (user)
        "surveys_title":   "📋 *Опросы*\n\nВыберите опрос:",
        "surveys_empty":   "📭 Сейчас нет активных опросов. Загляните позже!",
        "survey_intro": (
            "📋 *{title}*\n\n"
            "Добро пожаловать в опрос! Отвечайте честно — "
            "результаты используются в исследовательских целях.\n\n"
            "Всего вопросов: *{total}*\n\n"
            "Нажмите *Начать*, чтобы приступить."
        ),
        "btn_survey_start": "▶️ Начать опрос",
        "survey_question":  "❓ *Вопрос {n}/{total}:*\n\n{text}",
        "survey_done": (
            "✅ *Опрос завершён!*\n\n"
            "Спасибо за участие 🙏\n"
            "Ваши ответы помогают в исследовании."
        ),
        "admin_survey_notify": (
            "📋 *Новый ответ на опрос!*\n\n"
            "📝 Опрос: {title}\n"
            "👤 {name} (@{username})\n"
            "🆔 ID: `{user_id}`\n"
            "🕐 {time}"
        ),

        # ── portfolio
        "portfolio_select_cat": "🖼 *Портфолио*\n\nВыберите категорию:",
        "portfolio_empty_cat":  "📭 В этой категории пока нет работ.",
        "portfolio_item":       "*{title}*\n\n{desc}\n",
        "portfolio_demo":       "\n🔗 Демо: {url}",
        "portfolio_video":      "\n🎬 Видео: {url}",
        "portfolio_nav_btn":    "{cur}/{total}",
        "btn_port_prev":        "⬅️",
        "btn_port_next":        "➡️",
        "btn_port_cats":        "🗂 Категории",

        # ── portfolio category labels
        "type_brand_strategy": "🎯 Brand Strategy",
        "type_consumer_beh":   "🧠 Consumer Behaviour",
        "type_smm_content":    "📱 SMM / Content",

        # ── portfolio (admin)
        "adm_port_step_cat":    "📂 Выберите категорию:",
        "adm_port_step_photo":  "🖼 Отправьте скриншот (фото)\nили нажмите *Пропустить*:",
        "adm_port_step_title":  "✏️ Введите *название* работы:",
        "adm_port_step_desc":   "📝 Введите *описание* (или Пропустить):",
        "adm_port_step_link":   "🔗 Введите *ссылку на демо* (или Пропустить):",
        "adm_port_step_video":  "🎬 Введите *YouTube/Vimeo ссылку* (или Пропустить):",
        "adm_port_preview": (
            "👁 *Предпросмотр:*\n\n"
            "📂 Категория: {cat}\n"
            "📌 Название: {title}\n"
            "📝 Описание: {desc}\n"
            "🔗 Демо: {demo}\n"
            "🎬 Видео: {video}\n"
            "🖼 Фото: {photo}\n\n"
            "Сохранить?"
        ),
        "adm_port_saved":       "✅ Работа добавлена в портфолио!",
        "adm_port_cancelled":   "❌ Отменено.",
        "adm_port_list_title":  "🗂 *Все работы:*\n",
        "adm_port_list_row":    "#{id} [{cat}] {title}\n",
        "adm_port_empty":       "📭 Портфолио пустое.",
        "adm_port_del_confirm": "🗑 Удалить *#{id} — {title}*?",
        "adm_port_deleted":     "✅ Работа #{id} удалена.",
        "btn_skip":             "⏭ Пропустить",
        "btn_save":             "✅ Сохранить",
        "btn_del_yes":          "✅ Да, удалить",
        "btn_del_no":           "❌ Отмена",
    },

    "uz": {
        # ── language
        "lang_select": "🌐 Выберите язык / Tilni tanlang:",

        # ── welcome
        "welcome": (
            "👋 Xush kelibsiz!\n\n"
            "Men — Consumer Behaviour va Brand Strategy mutaxassisi.\n\n"
            "Bu yerda mening portfoliom, tadqiqot so'rovlari\n"
            "va men bilan bog'lanish imkoniyati mavjud.\n\n"
            "Bo'limni tanlang 👇"
        ),

        # ── menu buttons
        "btn_portfolio":   "🖼 Portfolio",
        "btn_surveys":     "📋 So'rovlar",
        "btn_about":       "🙋 Men haqimda",
        "btn_contact":     "📩 Bog'lanish",
        "btn_channel":     "📢 Kanal",
        "btn_switch_lang": "🌐 Русский",
        "btn_main_menu":   "🏠 Asosiy menyu",

        # ── about me
        "about_text": (
            "🙋 *Men haqimda*\n\n"
            "Consumer Behaviour va Brand Strategy mutaxassisi.\n\n"
            "Brendlarga o'z auditoriyasini tushunishga va konversiyaga aylantiruvchi "
            "strategiyalar yaratishga yordam beraman. Frilanser loyihalar va doimiy "
            "hamkorlikka tayyorman.\n\n"
            "📊 *Mutaxassisligim:*\n"
            "• Consumer Behaviour\n"
            "• Brand Strategy\n"
            "• SMM Manager\n\n"
            "📩 Yozing — loyihangizni muhokama qilamiz!"
        ),

        # ── contact
        "contact_prompt": (
            "📩 *Men bilan bog'lanish*\n\n"
            "Xabaringizni yozing — imkon qadar tez javob beraman."
        ),
        "contact_sent": (
            "✅ Xabar yuborildi!\n\n"
            "Yaqin orada siz bilan bog'lanaman."
        ),
        "admin_contact_notify": (
            "📨 *Yangi xabar!*\n\n"
            "👤 {name} (@{username})\n"
            "🆔 ID: `{user_id}`\n\n"
            "💬 {message}"
        ),

        # ── surveys (user)
        "surveys_title":   "📋 *So'rovlar*\n\nSo'rovni tanlang:",
        "surveys_empty":   "📭 Hozirda faol so'rovlar yo'q. Keyinroq qarang!",
        "survey_intro": (
            "📋 *{title}*\n\n"
            "So'rovga xush kelibsiz! Halol javob bering — "
            "natijalar tadqiqot maqsadida ishlatiladi.\n\n"
            "Jami savollar: *{total}*\n\n"
            "Boshlash uchun *Start* tugmasini bosing."
        ),
        "btn_survey_start": "▶️ Boshlash",
        "survey_question":  "❓ *Savol {n}/{total}:*\n\n{text}",
        "survey_done": (
            "✅ *So'rov tugadi!*\n\n"
            "Ishtirok etganingiz uchun rahmat 🙏\n"
            "Javoblaringiz tadqiqotga yordam beradi."
        ),
        "admin_survey_notify": (
            "📋 *Yangi so'rov javobi!*\n\n"
            "📝 So'rov: {title}\n"
            "👤 {name} (@{username})\n"
            "🆔 ID: `{user_id}`\n"
            "🕐 {time}"
        ),

        # ── portfolio
        "portfolio_select_cat": "🖼 *Portfolio*\n\nKategoriyani tanlang:",
        "portfolio_empty_cat":  "📭 Bu kategoriyada hali ishlar yo'q.",
        "portfolio_item":       "*{title}*\n\n{desc}\n",
        "portfolio_demo":       "\n🔗 Demo: {url}",
        "portfolio_video":      "\n🎬 Video: {url}",
        "portfolio_nav_btn":    "{cur}/{total}",
        "btn_port_prev":        "⬅️",
        "btn_port_next":        "➡️",
        "btn_port_cats":        "🗂 Kategoriyalar",

        # ── portfolio category labels
        "type_brand_strategy": "🎯 Brand Strategy",
        "type_consumer_beh":   "🧠 Consumer Behaviour",
        "type_smm_content":    "📱 SMM / Content",

        # ── portfolio (admin)
        "adm_port_step_cat":    "📂 Kategoriyani tanlang:",
        "adm_port_step_photo":  "🖼 Skrinshot yuboring\nyoki *O'tkazib yuborish* tugmasini bosing:",
        "adm_port_step_title":  "✏️ Ish *sarlavhasini* yozing:",
        "adm_port_step_desc":   "📝 *Tavsif* yozing (yoki O'tkazib yuborish):",
        "adm_port_step_link":   "🔗 *Demo havolasini* yozing (yoki O'tkazib yuborish):",
        "adm_port_step_video":  "🎬 *YouTube/Vimeo havolasini* yozing (yoki O'tkazib yuborish):",
        "adm_port_preview": (
            "👁 *Ko'rinishi:*\n\n"
            "📂 Kategoriya: {cat}\n"
            "📌 Sarlavha: {title}\n"
            "📝 Tavsif: {desc}\n"
            "🔗 Demo: {demo}\n"
            "🎬 Video: {video}\n"
            "🖼 Rasm: {photo}\n\n"
            "Saqlashni tasdiqlaysizmi?"
        ),
        "adm_port_saved":       "✅ Ish portfolio'ga qo'shildi!",
        "adm_port_cancelled":   "❌ Bekor qilindi.",
        "adm_port_list_title":  "🗂 *Barcha ishlar:*\n",
        "adm_port_list_row":    "#{id} [{cat}] {title}\n",
        "adm_port_empty":       "📭 Portfolio bo'sh.",
        "adm_port_del_confirm": "🗑 *#{id} — {title}* ni o'chirishni tasdiqlaysizmi?",
        "adm_port_deleted":     "✅ #{id} raqamli ish o'chirildi.",
        "btn_skip":             "⏭ O'tkazib yuborish",
        "btn_save":             "✅ Saqlash",
        "btn_del_yes":          "✅ Ha, o'chirish",
        "btn_del_no":           "❌ Bekor",
    },
}
