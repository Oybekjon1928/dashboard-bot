TEXTS = {
    "ru": {
        # ── language
        "lang_select": "🌐 Выберите язык / Tilni tanlang:",

        # ── welcome / menu
        "welcome": (
            "👋 Xush kelibsiz / Добро пожаловать!\n\n"
            "Biz sizning biznesingiz uchun professional dashboard yaratamiz.\n\n"
            "💵 $10 dan $150 gacha\n"
            "⚡ 1 kundan 8 kungacha\n"
            "✅ 3 ta bepul tuzatish kafolati\n\n"
            "Quyidagi bo'limlardan birini tanlang 👇"
        ),
        "main_menu": "🏠 Главное меню",
        "btn_services":  "📊 Услуги",
        "btn_portfolio": "🖼 Портфолио",
        "btn_calc":      "🧮 Калькулятор цены",
        "btn_faq":       "❓ FAQ",
        "btn_order":     "📝 Оставить заявку",
        "btn_contacts":  "📞 Контакты",
        "btn_back":      "⬅️ Назад",
        "btn_main_menu": "🏠 Главное меню",

        # ── services
        "services_text": (
            "📊 *Xizmatlarimiz*\n\n"

            "📋 *Excel / Google Sheets*\n"
            "✅ Mavjud jadvallaringizni kuchaytiring\n"
            "✅ Avtomatik hisobotlar va grafiklar\n"
            "✅ Formulalar va pivot jadvallar\n"
            "💵 $10–$30 · ⚡ 1–3 kun\n\n"

            "📊 *Business Analytics*\n"
            "✅ Qaysi mahsulot ko'proq sotilishini biling\n"
            "✅ Zarar keltirayotgan xarajatni toping\n"
            "✅ KPI va savdo o'sishini kuzating\n"
            "💵 $20–$50 · ⚡ 3–5 kun\n\n"

            "📈 *Power BI / Tableau*\n"
            "✅ Har qanday manbadan ma'lumot oling\n"
            "✅ Interaktiv filtrlar va grafiklar\n"
            "✅ Avtomatik yangilanish\n"
            "💵 $30–$80 · ⚡ 3–5 kun\n\n"

            "🌐 *Web / SaaS Dashboard*\n"
            "✅ Sayt yoki ilovangizga o'rnatiladi\n"
            "✅ Real vaqt ma'lumotlari\n"
            "✅ Foydalanuvchi ruxsatlari\n"
            "💵 $50–$150 · ⚡ 5–8 kun\n\n"

            "⭐ Barcha xizmatlarda — *3 bepul tuzatish* kafolati\n\n"
            "👇 Hoziroq buyurtma bering:"
        ),

        # ── portfolio
        "portfolio_text":  "🖼 *Портфолио*\n\nНаши работы:",
        "portfolio_empty": "🖼 Портфолио пока не добавлено. Загляните позже!",

        # ── contacts
        "contacts_text": (
            "📞 *Контакты*\n\n"
            "По всем вопросам обращайтесь напрямую:\n"
            "👤 Менеджер: @{admin_username}\n\n"
            "Или оставьте заявку прямо здесь — мы свяжемся с вами!"
        ),

        # ── order flow
        "order_start":   "📝 *Заявка — шаг 1/4*\n\nВведите ваше *имя*:",
        "order_phone":   "📱 *Шаг 2/4*\n\nВведите *номер телефона*:",
        "order_type":    "📊 *Шаг 3/4*\n\nКакой тип дашборда нужен?",
        "order_budget":  "💰 *Шаг 4/4*\n\nУкажите *бюджет и сроки*\n_(например: $50, нужно за 3 дня)_:",
        "order_confirm": (
            "✅ *Проверьте заявку:*\n\n"
            "👤 {name}\n"
            "📱 {phone}\n"
            "📊 {dtype}\n"
            "💰 {budget}\n\n"
            "Всё верно?"
        ),
        "btn_confirm":      "✅ Подтвердить",
        "btn_cancel":       "❌ Отменить",
        "order_sent": (
            "✅ *Заявка принята!*\n\n"
            "Наш менеджер свяжется с вами в течение 15–30 минут.\n"
            "Если не ответили — напишите напрямую: @{admin_username}"
        ),
        "order_cancelled":  "❌ Заявка отменена. Возвращаю в меню.",
        "order_done_user":  "✅ Ваш заказ *#{order_id}* выполнен! Спасибо за доверие. Свяжитесь с нами: @{admin_username}",
        "order_rejected_user": (
            "❌ По заявке *#{order_id}* мы вынуждены отказать.\n"
            "Причина: {reason}\n\n"
            "Если есть вопросы — @{admin_username}"
        ),

        # ── dashboard type labels (shared between order & calculator)
        "type_bi":        "📈 Power BI / Tableau",
        "type_web":       "🌐 Web / SaaS",
        "type_excel":     "📋 Excel / Google Sheets",
        "type_analytics": "📊 Business Analytics",

        # ── admin notification
        "admin_new_order": (
            "🔔 *Новая заявка \\#{order_id}*\n\n"
            "👤 Имя: {name}\n"
            "📱 Телефон: {phone}\n"
            "📊 Тип: {dtype}\n"
            "💰 Бюджет/сроки: {budget}\n"
            "📋 Описание: {desc}\n\n"
            "🆔 Telegram ID: `{user_id}`\n"
            "👤 Username: @{username}\n\n"
            "Ответьте командой:\n"
            "`/done {order_id}` — выполнено\n"
            "`/reject {order_id} причина` — отказ"
        ),

        # ── pricing calculator
        "calc_step1": "🧮 *Калькулятор цены*\n\nШаг 1/3: Выберите тип дашборда:",
        "calc_step2": "📦 Шаг 2/3: Сколько источников данных будет подключено?",
        "calc_step3": "🕐 Шаг 3/3: В какие сроки нужен дашборд?",
        "calc_result": (
            "💰 *Taxminiy narx*\n\n"
            "📊 {dtype}\n"
            "📦 {sources}\n"
            "⚡ {deadline}\n\n"
            "💵 *${min_p} — ${max_p}*\n\n"
            "✅ Aniq narx loyihani ko'rib chiqib belgilanadi\n"
            "🎯 Bugun buyurtma bering — muddatni kafolatlaymiz!\n"
        ),
        "calc_src_1_2": "1–2 источника",
        "calc_src_3_5": "3–5 источников",
        "calc_src_6":   "6+ источников",
        "calc_dl_urgent": "⚡ Срочно (1–2 дня)  +50%",
        "calc_dl_normal": "📅 Стандарт (3–5 дней)",
        "calc_dl_flex":   "🌿 Гибко (6–8 дней)  −10%",
        "btn_calc_order":  "📝 Оформить заявку",
        "btn_recalc":      "🔄 Пересчитать",

        # ── FAQ
        "faq_menu": "❓ *Часто задаваемые вопросы*\n\nВыберите вопрос:",
        "faq_q1": "💰 Сколько стоит дашборд?",
        "faq_q2": "⏱ Сколько времени займёт разработка?",
        "faq_q3": "📂 Какие данные нужны для начала?",
        "faq_q4": "🔧 Можно ли вносить изменения после сдачи?",
        "faq_q5": "📦 В каком формате передаётся готовый дашборд?",
        "faq_a1": (
            "💰 *Narx qancha?*\n\n"
            "📋 Excel / Google Sheets — $10–$30\n"
            "📊 Business Analytics — $20–$50\n"
            "📈 Power BI / Tableau — $30–$80\n"
            "🌐 Web / SaaS — $50–$150\n\n"
            "Narxga manba soni va muddat ta'sir qiladi.\n"
            "🧮 Aniq narxni bilish uchun *Kalkulyator* dan foydalaning!\n\n"
            "👇 Hoziroq buyurtma bering — narxni kelishamiz:"
        ),
        "faq_a2": (
            "⚡ *Muddat qancha?*\n\n"
            "⚡ Shoshilinch — 1–2 ish kuni (+50%)\n"
            "📅 Standart — 3–5 ish kuni\n"
            "🌿 Moslashuvchan — 6–8 ish kuni (−10%)\n\n"
            "✅ Buyurtma berilgan kuni ish boshlanadi.\n\n"
            "👇 Bugun buyurtma bering:"
        ),
        "faq_a3": (
            "📂 *Boshlash uchun nima kerak?*\n\n"
            "📋 *Excel / Sheets uchun:*\n"
            "• Ma'lumot fayli (Excel, CSV, Sheets)\n"
            "• Muhim ko'rsatkichlar ro'yxati\n\n"
            "📈 *Power BI / Tableau uchun:*\n"
            "• Ma'lumot manbai (fayl, baza, 1C, CRM)\n"
            "• Kerakli metrikalar va filtrlar\n\n"
            "🌐 *Web Dashboard uchun:*\n"
            "• Funksional tavsif va grafiklar ro'yxati\n"
            "• Ma'lumot manbai (API yoki baza)\n\n"
            "📊 *Business Analytics uchun:*\n"
            "• Ma'lumotlar yuklamasi\n"
            "• Tahlil maqsadi\n\n"
            "💡 Noaniq bo'lsa — shunchaki yozing, biz o'zimiz yo'llaymiz!\n\n"
            "👇 Hoziroq ariza qoldiring:"
        ),
        "faq_a4": (
            "🔧 *Topshirilgandan keyin o'zgartirish?*\n\n"
            "✅ Ha, albatta!\n\n"
            "• 7 kun ichida *3 ta bepul tuzatish*\n"
            "• Katta o'zgarishlar — alohida kelishuv\n\n"
            "Siz natijadan to'liq mamnun bo'lguningizcha ishlaymiz.\n\n"
            "👇 Buyurtma bering:"
        ),
        "faq_a5": (
            "📦 *Tayyor ish qanday shaklda beriladi?*\n\n"
            "📋 Excel / Sheets — fayl yoki havola\n"
            "📈 Power BI / Tableau — fayl + yo'riqnoma\n"
            "🌐 Web — hosting havolasi yoki kod\n\n"
            "✅ Har birida qisqa foydalanish yo'riqnomasi bepul!\n\n"
            "👇 Hoziroq buyurtma bering:"
        ),
        "btn_back_faq": "⬅️ К списку вопросов",

        # ── admin order notification
        "admin_order_notify": (
            "🔔 *Yangi buyurtma #{order_id}!*\n\n"
            "👤 {name}\n"
            "📱 {phone}\n"
            "📊 {dtype}\n"
            "💰 {budget}\n"
            "📋 {desc}\n\n"
            "🆔 ID: `{user_id}` | @{username}\n\n"
            "✅ Qabul qilish: `/accept {order_id}`\n"
            "❌ Rad etish: `/reject {order_id} sabab`"
        ),
        "admin_order_remind": (
            "⏰ *15 daqiqa o'tdi! #{order_id} buyurtmaga javob berilmadi!*\n\n"
            "👤 {name} | 📱 {phone}\n"
            "📊 {dtype} | 💰 {budget}\n\n"
            "✅ Qabul: `/accept {order_id}`\n"
            "❌ Rad: `/reject {order_id} sabab`"
        ),
        "admin_consult_notify": (
            "📅 *Yangi konsultatsiya #{consult_id}!*\n\n"
            "👤 {name} (@{username})\n"
            "📱 {phone}\n"
            "📅 {day} | 🕐 {time}\n\n"
            "🆔 ID: `{user_id}`\n\n"
            "✅ Qabul: `/acceptc {consult_id}`"
        ),
        "admin_consult_remind": (
            "⏰ *15 daqiqa o'tdi! #{consult_id} konsultatsiyaga javob berilmadi!*\n\n"
            "👤 {name} | 📱 {phone}\n"
            "📅 {day} | 🕐 {time}\n\n"
            "✅ Qabul: `/acceptc {consult_id}`"
        ),
        "admin_accepted":   "✅ #{id} qabul qilindi. Mijoz bilan bog'laning!",
        "admin_accept_404": "❌ #{id} topilmadi.",

        # ── portfolio (user)
        "portfolio_select_cat":  "🖼 *Портфолио*\n\nВыберите категорию:",
        "portfolio_empty_cat":   "📭 В этой категории пока нет работ.",
        "portfolio_item": (
            "*{title}*\n\n"
            "{desc}\n"
        ),
        "portfolio_demo":  "\n🔗 Демо: {url}",
        "portfolio_video": "\n🎬 Видео: {url}",
        "portfolio_nav_btn":  "{cur}/{total}",
        "btn_port_prev":      "⬅️",
        "btn_port_next":      "➡️",
        "btn_port_cats":      "🗂 Категории",
        "btn_port_order":     "📝 Заказать такой же",

        # ── portfolio (admin)
        "adm_port_step_cat":   "📂 Выберите категорию:",
        "adm_port_step_photo": "🖼 Отправьте скриншот (фото)\nили нажмите *Пропустить*:",
        "adm_port_step_title": "✏️ Введите *название* работы:",
        "adm_port_step_desc":  "📝 Введите *описание* (или Пропустить):",
        "adm_port_step_link":  "🔗 Введите *ссылку на демо* (или Пропустить):",
        "adm_port_step_video": "🎬 Введите *YouTube/Vimeo ссылку* (или Пропустить):",
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
        "adm_port_saved":      "✅ Работа добавлена в портфолио!",
        "adm_port_cancelled":  "❌ Отменено.",
        "adm_port_list_title": "🗂 *Все работы в портфолио:*\n",
        "adm_port_list_row":   "#{id} [{cat}] {title}\n",
        "adm_port_empty":      "📭 Портфолио пустое.",
        "adm_port_del_confirm":"🗑 Удалить *#{id} — {title}*?",
        "adm_port_deleted":    "✅ Работа #{id} удалена.",
        "btn_skip":            "⏭ Пропустить",
        "btn_save":            "✅ Сохранить",
        "btn_delete":          "🗑 Удалить",
        "btn_del_yes":         "✅ Да, удалить",
        "btn_del_no":          "❌ Отмена",

        # ── channel
        "btn_channel": "📢 Наш канал",

        # ── my orders button
        "btn_myorders": "📋 Мои заявки",

        # ── language switch
        "btn_switch_lang": "🌐 O'zbekcha",
        "lang_switched": "Язык изменён на русский.",

        # ── my orders
        "myorders_empty": "📭 У вас пока нет заявок. Оставьте первую заявку!",
        "myorders_header": "📋 *Ваши заявки:*\n",
        "myorders_row": "{status} *#{id}* — {dtype}\n💰 {budget} | 🕐 {date}\n",
        "status_pending":  "⏳ В обработке",
        "status_done":     "✅ Выполнено",
        "status_rejected": "❌ Отклонено",

        # ── reminder
        "reminder_text": (
            "⏰ Вы начали оформлять заявку, но не завершили.\n\n"
            "Хотите продолжить или отменить?"
        ),
        "btn_reminder_continue": "▶️ Продолжить",
        "btn_reminder_cancel":   "❌ Отменить заявку",
        "reminder_cancelled": "Заявка отменена. Возвращаю в меню.",

        # ── free consultation
        "btn_consult":      "📅 Бесплатная консультация",
        "consult_step1":    "📅 *Бесплатная консультация*\n\nВыберите удобный день:",
        "consult_step2":    "🕐 Выберите удобное время:",
        "consult_step3":    "📱 Введите ваш *номер телефона* для подтверждения:",
        "consult_confirm": (
            "✅ *Консультация забронирована!*\n\n"
            "📅 День: {day}\n"
            "🕐 Время: {time}\n\n"
            "Мы свяжемся с вами по номеру {phone} для подтверждения.\n"
            "По вопросам: @{admin_username}"
        ),
        "admin_consult": (
            "📅 *Запрос на консультацию!*\n\n"
            "👤 {name} (@{username})\n"
            "📱 Телефон: {phone}\n"
            "📅 День: {day}\n"
            "🕐 Время: {time}\n\n"
            "🆔 ID: `{user_id}`"
        ),
        "consult_day_0": "Bugun",
        "consult_day_1": "Ertaga",
        "consult_day_2": "Indiniga",
        "booked_slot_alert": "❌ Bu vaqt allaqachon band! Boshqa vaqtni tanlang.",
        "all_slots_booked": "😔 Bu kunda barcha vaqtlar band.\nIltimos, boshqa kun tanlang.",
        "consult_t_9":  "09:00",
        "consult_t_11": "11:00",
        "consult_t_13": "13:00",
        "consult_t_15": "15:00",
        "consult_t_17": "17:00",
    },

    "uz": {
        # ── language
        "lang_select": "🌐 Выберите язык / Tilni tanlang:",

        # ── welcome / menu
        "welcome": (
            "👋 Xush kelibsiz!\n\n"
            "Biz sizning biznesingiz uchun professional dashboard yaratamiz.\n\n"
            "💵 $10 dan $150 gacha\n"
            "⚡ 1 kundan 8 kungacha\n"
            "✅ 3 ta bepul tuzatish kafolati\n\n"
            "Quyidagi bo'limlardan birini tanlang 👇"
        ),
        "main_menu": "🏠 Asosiy menyu",
        "btn_services":  "📊 Xizmatlar",
        "btn_portfolio": "🖼 Portfolio",
        "btn_calc":      "🧮 Narx kalkulyatori",
        "btn_faq":       "❓ FAQ",
        "btn_order":     "📝 Ariza qoldirish",
        "btn_contacts":  "📞 Aloqa",
        "btn_back":      "⬅️ Orqaga",
        "btn_main_menu": "🏠 Asosiy menyu",

        # ── services
        "services_text": (
            "📊 *Xizmatlarimiz*\n\n"

            "📋 *Excel / Google Sheets*\n"
            "✅ Mavjud jadvallaringizni kuchaytiring\n"
            "✅ Avtomatik hisobotlar va grafiklar\n"
            "✅ Formulalar va pivot jadvallar\n"
            "💵 $10–$30 · ⚡ 1–3 kun\n\n"

            "📊 *Business Analytics*\n"
            "✅ Qaysi mahsulot ko'proq sotilishini biling\n"
            "✅ Zarar keltirayotgan xarajatni toping\n"
            "✅ KPI va savdo o'sishini kuzating\n"
            "💵 $20–$50 · ⚡ 3–5 kun\n\n"

            "📈 *Power BI / Tableau*\n"
            "✅ Har qanday manbadan ma'lumot oling\n"
            "✅ Interaktiv filtrlar va grafiklar\n"
            "✅ Avtomatik yangilanish\n"
            "💵 $30–$80 · ⚡ 3–5 kun\n\n"

            "🌐 *Web / SaaS Dashboard*\n"
            "✅ Sayt yoki ilovangizga o'rnatiladi\n"
            "✅ Real vaqt ma'lumotlari\n"
            "✅ Foydalanuvchi ruxsatlari\n"
            "💵 $50–$150 · ⚡ 5–8 kun\n\n"

            "⭐ Barcha xizmatlarda — *3 bepul tuzatish* kafolati\n\n"
            "👇 Hoziroq buyurtma bering:"
        ),

        # ── portfolio
        "portfolio_text":  "🖼 *Portfolio*\n\nIshlarimiz:",
        "portfolio_empty": "🖼 Portfolio hali qo'shilmagan. Keyinroq qarang!",

        # ── contacts
        "contacts_text": (
            "📞 *Aloqa*\n\n"
            "Barcha savollar bo'yicha to'g'ridan-to'g'ri murojaat qiling:\n"
            "👤 Menejer: @{admin_username}\n\n"
            "Yoki bu yerda ariza qoldiring — siz bilan bog'lanamiz!"
        ),

        # ── order flow
        "order_start":   "📝 *Ariza — 1/4-qadam*\n\n*Ismingizni* kiriting:",
        "order_phone":   "📱 *2/4-qadam*\n\n*Telefon raqamingizni* kiriting:",
        "order_type":    "📊 *3/4-qadam*\n\nQaysi turdagi dashboard kerak?",
        "order_budget":  "💰 *4/4-qadam*\n\n*Byudjet va muddatni* kiriting\n_(masalan: $50, 3 kun ichida kerak)_:",
        "order_confirm": (
            "✅ *Arizangizni tekshiring:*\n\n"
            "👤 {name}\n"
            "📱 {phone}\n"
            "📊 {dtype}\n"
            "💰 {budget}\n\n"
            "Hammasi to'g'rimi?"
        ),
        "btn_confirm":      "✅ Tasdiqlash",
        "btn_cancel":       "❌ Bekor qilish",
        "order_sent": (
            "✅ *Ariza qabul qilindi!*\n\n"
            "Menejerimiz 15–30 daqiqa ichida siz bilan bog'lanadi.\n"
            "Javob bo'lmasa — to'g'ridan-to'g'ri yozing: @{admin_username}"
        ),
        "order_cancelled":  "❌ Ariza bekor qilindi. Menyuga qaytaraman.",
        "order_done_user":  "✅ *#{order_id}* raqamli buyurtmangiz bajarildi! Ishonch uchun rahmat. Bog'lanish: @{admin_username}",
        "order_rejected_user": (
            "❌ *#{order_id}* raqamli ariza bo'yicha rad etishga majburmiz.\n"
            "Sabab: {reason}\n\n"
            "Savollar bo'lsa — @{admin_username}"
        ),

        # ── dashboard type labels
        "type_bi":        "📈 Power BI / Tableau",
        "type_web":       "🌐 Web / SaaS",
        "type_excel":     "📋 Excel / Google Sheets",
        "type_analytics": "📊 Business Analytics",

        # ── admin notification
        "admin_new_order": (
            "🔔 *Yangi ariza \\#{order_id}*\n\n"
            "👤 Ism: {name}\n"
            "📱 Telefon: {phone}\n"
            "📊 Tur: {dtype}\n"
            "💰 Byudjet/muddat: {budget}\n"
            "📋 Tavsif: {desc}\n\n"
            "🆔 Telegram ID: `{user_id}`\n"
            "👤 Username: @{username}\n\n"
            "Komanda bilan javob bering:\n"
            "`/done {order_id}` — bajarildi\n"
            "`/reject {order_id} sabab` — rad etish"
        ),

        # ── pricing calculator
        "calc_step1": "🧮 *Narx kalkulyatori*\n\n1/3-qadam: Dashboard turini tanlang:",
        "calc_step2": "📦 2/3-qadam: Nechta ma'lumot manbai ulanadi?",
        "calc_step3": "🕐 3/3-qadam: Qanday muddatda dashboard kerak?",
        "calc_result": (
            "💰 *Taxminiy narx*\n\n"
            "📊 {dtype}\n"
            "📦 {sources}\n"
            "⚡ {deadline}\n\n"
            "💵 *${min_p} — ${max_p}*\n\n"
            "✅ Aniq narx loyihani ko'rib chiqib belgilanadi\n"
            "🎯 Bugun buyurtma bering — muddatni kafolatlaymiz!\n"
        ),
        "calc_src_1_2": "1–2 manba",
        "calc_src_3_5": "3–5 manba",
        "calc_src_6":   "6+ manba",
        "calc_dl_urgent": "⚡ Shoshilinch (1–2 kun)  +50%",
        "calc_dl_normal": "📅 Standart (3–5 kun)",
        "calc_dl_flex":   "🌿 Moslashuvchan (6–8 kun)  −10%",
        "btn_calc_order":  "📝 Ariza qoldirish",
        "btn_recalc":      "🔄 Qayta hisoblash",

        # ── FAQ
        "faq_menu": "❓ *Ko'p so'raladigan savollar*\n\nSavolni tanlang:",
        "faq_q1": "💰 Dashboard narxi qancha?",
        "faq_q2": "⏱ Ishlab chiqish qancha vaqt oladi?",
        "faq_q3": "📂 Boshlash uchun qanday ma'lumotlar kerak?",
        "faq_q4": "🔧 Topshirilgandan keyin o'zgartirish mumkinmi?",
        "faq_q5": "📦 Tayyor dashboard qanday shaklda beriladi?",
        "faq_a1": (
            "💰 *Narx qancha?*\n\n"
            "📋 Excel / Google Sheets — $10–$30\n"
            "📊 Business Analytics — $20–$50\n"
            "📈 Power BI / Tableau — $30–$80\n"
            "🌐 Web / SaaS — $50–$150\n\n"
            "Narxga manba soni va muddat ta'sir qiladi.\n"
            "🧮 Aniq narxni bilish uchun *Kalkulyator* dan foydalaning!\n\n"
            "👇 Hoziroq buyurtma bering — narxni kelishamiz:"
        ),
        "faq_a2": (
            "⚡ *Muddat qancha?*\n\n"
            "⚡ Shoshilinch — 1–2 ish kuni (+50%)\n"
            "📅 Standart — 3–5 ish kuni\n"
            "🌿 Moslashuvchan — 6–8 ish kuni (−10%)\n\n"
            "✅ Buyurtma berilgan kuni ish boshlanadi.\n\n"
            "👇 Bugun buyurtma bering:"
        ),
        "faq_a3": (
            "📂 *Boshlash uchun nima kerak?*\n\n"
            "📋 *Excel / Sheets uchun:*\n"
            "• Ma'lumot fayli (Excel, CSV, Sheets)\n"
            "• Muhim ko'rsatkichlar ro'yxati\n\n"
            "📈 *Power BI / Tableau uchun:*\n"
            "• Ma'lumot manbai (fayl, baza, 1C, CRM)\n"
            "• Kerakli metrikalar va filtrlar\n\n"
            "🌐 *Web Dashboard uchun:*\n"
            "• Funksional tavsif va grafiklar ro'yxati\n"
            "• Ma'lumot manbai (API yoki baza)\n\n"
            "📊 *Business Analytics uchun:*\n"
            "• Ma'lumotlar yuklamasi\n"
            "• Tahlil maqsadi\n\n"
            "💡 Noaniq bo'lsa — shunchaki yozing, biz yo'llaymiz!\n\n"
            "👇 Hoziroq ariza qoldiring:"
        ),
        "faq_a4": (
            "🔧 *Topshirilgandan keyin o'zgartirish?*\n\n"
            "✅ Ha, albatta!\n\n"
            "• 7 kun ichida *3 ta bepul tuzatish*\n"
            "• Katta o'zgarishlar — alohida kelishuv\n\n"
            "Siz natijadan to'liq mamnun bo'lguningizcha ishlaymiz.\n\n"
            "👇 Buyurtma bering:"
        ),
        "faq_a5": (
            "📦 *Tayyor ish qanday shaklda beriladi?*\n\n"
            "📋 Excel / Sheets — fayl yoki havola\n"
            "📈 Power BI / Tableau — fayl + yo'riqnoma\n"
            "🌐 Web — hosting havolasi yoki kod\n\n"
            "✅ Har birida qisqa foydalanish yo'riqnomasi bepul!\n\n"
            "👇 Hoziroq buyurtma bering:"
        ),
        "btn_back_faq": "⬅️ Savollarga qaytish",

        # ── admin order/consult notifications
        "admin_order_notify": (
            "🔔 *Yangi buyurtma #{order_id}!*\n\n"
            "👤 {name}\n"
            "📱 {phone}\n"
            "📊 {dtype}\n"
            "💰 {budget}\n"
            "📋 {desc}\n\n"
            "🆔 ID: `{user_id}` | @{username}\n\n"
            "✅ Qabul qilish: `/accept {order_id}`\n"
            "❌ Rad etish: `/reject {order_id} sabab`"
        ),
        "admin_order_remind": (
            "⏰ *15 daqiqa o'tdi! #{order_id} buyurtmaga javob berilmadi!*\n\n"
            "👤 {name} | 📱 {phone}\n"
            "📊 {dtype} | 💰 {budget}\n\n"
            "✅ Qabul: `/accept {order_id}`\n"
            "❌ Rad: `/reject {order_id} sabab`"
        ),
        "admin_consult_notify": (
            "📅 *Yangi konsultatsiya #{consult_id}!*\n\n"
            "👤 {name} (@{username})\n"
            "📱 {phone}\n"
            "📅 {day} | 🕐 {time}\n\n"
            "🆔 ID: `{user_id}`\n\n"
            "✅ Qabul: `/acceptc {consult_id}`"
        ),
        "admin_consult_remind": (
            "⏰ *15 daqiqa o'tdi! #{consult_id} konsultatsiyaga javob berilmadi!*\n\n"
            "👤 {name} | 📱 {phone}\n"
            "📅 {day} | 🕐 {time}\n\n"
            "✅ Qabul: `/acceptc {consult_id}`"
        ),
        "admin_accepted":   "✅ #{id} qabul qilindi. Mijoz bilan bog'laning!",
        "admin_accept_404": "❌ #{id} topilmadi.",

        # ── portfolio (user)
        "portfolio_select_cat":  "🖼 *Portfolio*\n\nKategoriyani tanlang:",
        "portfolio_empty_cat":   "📭 Bu kategoriyada hali ishlar yo'q.",
        "portfolio_item": (
            "*{title}*\n\n"
            "{desc}\n"
        ),
        "portfolio_demo":  "\n🔗 Demo: {url}",
        "portfolio_video": "\n🎬 Video: {url}",
        "portfolio_nav_btn":  "{cur}/{total}",
        "btn_port_prev":      "⬅️",
        "btn_port_next":      "➡️",
        "btn_port_cats":      "🗂 Kategoriyalar",
        "btn_port_order":     "📝 Shunday buyurtma berish",

        # ── portfolio (admin)
        "adm_port_step_cat":   "📂 Kategoriyani tanlang:",
        "adm_port_step_photo": "🖼 Skrinshot (rasm) yuboring\nyoki *O'tkazib yuborish* tugmasini bosing:",
        "adm_port_step_title": "✏️ Ish *sarlavhasini* yozing:",
        "adm_port_step_desc":  "📝 *Tavsif* yozing (yoki O'tkazib yuborish):",
        "adm_port_step_link":  "🔗 *Demo havolasini* yozing (yoki O'tkazib yuborish):",
        "adm_port_step_video": "🎬 *YouTube/Vimeo havolasini* yozing (yoki O'tkazib yuborish):",
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
        "adm_port_saved":      "✅ Ish portfolio'ga qo'shildi!",
        "adm_port_cancelled":  "❌ Bekor qilindi.",
        "adm_port_list_title": "🗂 *Portfolio'dagi barcha ishlar:*\n",
        "adm_port_list_row":   "#{id} [{cat}] {title}\n",
        "adm_port_empty":      "📭 Portfolio bo'sh.",
        "adm_port_del_confirm":"🗑 *#{id} — {title}* ni o'chirishni tasdiqlaysizmi?",
        "adm_port_deleted":    "✅ #{id} raqamli ish o'chirildi.",
        "btn_skip":            "⏭ O'tkazib yuborish",
        "btn_save":            "✅ Saqlash",
        "btn_delete":          "🗑 O'chirish",
        "btn_del_yes":         "✅ Ha, o'chirish",
        "btn_del_no":          "❌ Bekor",

        # ── channel
        "btn_channel": "📢 Bizning kanal",

        # ── my orders button
        "btn_myorders": "📋 Mening buyurtmalarim",

        # ── language switch
        "btn_switch_lang": "🌐 Русский",
        "lang_switched": "Til o'zbekchaga o'zgartirildi.",

        # ── my orders
        "myorders_empty": "📭 Sizda hali arizalar yo'q. Birinchi arizani qoldiring!",
        "myorders_header": "📋 *Sizning arizalaringiz:*\n",
        "myorders_row": "{status} *#{id}* — {dtype}\n💰 {budget} | 🕐 {date}\n",
        "status_pending":  "⏳ Ko'rib chiqilmoqda",
        "status_done":     "✅ Bajarildi",
        "status_rejected": "❌ Rad etildi",

        # ── reminder
        "reminder_text": (
            "⏰ Siz ariza to'ldirishni boshladingiz, lekin tugatmadingiz.\n\n"
            "Davom etmoqchimisiz yoki bekor qilmoqchimisiz?"
        ),
        "btn_reminder_continue": "▶️ Davom etish",
        "btn_reminder_cancel":   "❌ Arizani bekor qilish",
        "reminder_cancelled": "Ariza bekor qilindi. Menyuga qaytaraman.",

        # ── free consultation
        "btn_consult":      "📅 Bepul konsultatsiya",
        "consult_step1":    "📅 *Bepul konsultatsiya*\n\nQulay kunni tanlang:",
        "consult_step2":    "🕐 Qulay vaqtni tanlang:",
        "consult_step3":    "📱 Tasdiqlash uchun *telefon raqamingizni* kiriting:",
        "consult_confirm": (
            "✅ *Konsultatsiya band qilindi!*\n\n"
            "📅 Kun: {day}\n"
            "🕐 Vaqt: {time}\n\n"
            "Siz bilan {phone} raqami orqali bog'lanamiz.\n"
            "Savollar uchun: @{admin_username}"
        ),
        "admin_consult": (
            "📅 *Konsultatsiya so'rovi!*\n\n"
            "👤 {name} (@{username})\n"
            "📱 Telefon: {phone}\n"
            "📅 Kun: {day}\n"
            "🕐 Vaqt: {time}\n\n"
            "🆔 ID: `{user_id}`"
        ),
        "consult_day_0": "Bugun",
        "consult_day_1": "Ertaga",
        "consult_day_2": "Indiniga",
        "booked_slot_alert": "❌ Bu vaqt allaqachon band! Boshqa vaqtni tanlang.",
        "all_slots_booked": "😔 Bu kunda barcha vaqtlar band.\nIltimos, boshqa kun tanlang.",
        "consult_t_9":  "09:00",
        "consult_t_11": "11:00",
        "consult_t_13": "13:00",
        "consult_t_15": "15:00",
        "consult_t_17": "17:00",
    },
}
