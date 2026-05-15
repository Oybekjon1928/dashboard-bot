TEXTS = {
    "ru": {
        # ── language
        "lang_select": "🌐 Выберите язык / Tilni tanlang:",

        # ── welcome / menu
        "welcome": (
            "👋 Добро пожаловать!\n\n"
            "Я помогу вам заказать профессиональный дашборд под ваши нужды.\n"
            "Мы создаём:\n"
            "• 📊 Business / Analytics дашборды\n"
            "• 📈 Power BI и Tableau отчёты\n"
            "• 🌐 Web / SaaS дашборды\n"
            "• 📋 Excel / Google Sheets решения\n\n"
            "Выберите раздел ниже 👇"
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
            "📊 *Наши услуги*\n\n"
            "*Business / Analytics дашборды*\n"
            "Визуализация KPI, продаж, воронок и ключевых метрик вашего бизнеса.\n\n"
            "*Power BI / Tableau*\n"
            "Интерактивные отчёты с подключением к любым источникам данных.\n\n"
            "*Web / SaaS дашборды*\n"
            "Кастомные веб-дашборды, встроенные в ваш продукт или сайт.\n\n"
            "*Excel / Google Sheets*\n"
            "Автоматизированные таблицы с графиками, сводными и формулами.\n\n"
            "Срок выполнения: от 3 до 14 дней\n"
            "Стоимость: от $50 — зависит от сложности\n\n"
            "Готовы обсудить ваш проект? Оставьте заявку! 👇"
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
        "order_start":   "📝 Оформление заявки\n\nШаг 1 из 5\n\nВведите ваше *имя*:",
        "order_phone":   "📱 Шаг 2 из 5\n\nВведите ваш *номер телефона*:",
        "order_type":    "📊 Шаг 3 из 5\n\nКакой тип дашборда вам нужен?",
        "order_budget":  "💰 Шаг 4 из 5\n\nУкажите ваш *бюджет и сроки*\n_(например: $100, нужно за 5 дней)_:",
        "order_desc":    "📋 Шаг 5 из 5\n\nОпишите *задачу подробнее*\n_(что нужно отслеживать, откуда данные, какой результат ожидаете)_:",
        "order_confirm": (
            "✅ *Проверьте заявку:*\n\n"
            "👤 Имя: {name}\n"
            "📱 Телефон: {phone}\n"
            "📊 Тип: {dtype}\n"
            "💰 Бюджет/сроки: {budget}\n"
            "📋 Описание: {desc}\n\n"
            "Всё верно?"
        ),
        "btn_confirm":      "✅ Подтвердить",
        "btn_cancel":       "❌ Отменить",
        "order_sent":       "🎉 Заявка отправлена! Мы свяжемся с вами в ближайшее время.",
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
            "💰 *Примерная стоимость*\n\n"
            "📊 Тип: {dtype}\n"
            "📦 Источников данных: {sources}\n"
            "🕐 Сроки: {deadline}\n\n"
            "💵 *Стоимость: ${min_p} — ${max_p}*\n\n"
            "_Точная цена согласовывается индивидуально после обсуждения задачи._"
        ),
        "calc_src_1_2": "1–2 источника",
        "calc_src_3_5": "3–5 источников",
        "calc_src_6":   "6+ источников",
        "calc_dl_urgent": "⚡ Срочно (1–3 дня)  +50%",
        "calc_dl_normal": "📅 Стандарт (4–7 дней)",
        "calc_dl_flex":   "🌿 Гибко (8+ дней)  −10%",
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
            "💰 *Сколько стоит дашборд?*\n\n"
            "Стоимость зависит от типа и сложности:\n"
            "• Excel / Google Sheets — от $50\n"
            "• Business Analytics — от $80\n"
            "• Power BI / Tableau — от $100\n"
            "• Web / SaaS дашборд — от $150\n\n"
            "На цену влияют количество источников данных и сроки.\n"
            "Воспользуйтесь 🧮 *Калькулятором* для быстрой оценки!"
        ),
        "faq_a2": (
            "⏱ *Сколько времени займёт разработка?*\n\n"
            "• Срочно — 1–3 рабочих дня (надбавка +50%)\n"
            "• Стандарт — 4–7 рабочих дней\n"
            "• Гибко — 8–14 рабочих дней (скидка 10%)\n\n"
            "Сроки обсуждаются при оформлении заявки."
        ),
        "faq_a3": (
            "📂 *Какие данные нужны для начала?*\n\n"
            "В зависимости от задачи нам могут понадобиться:\n"
            "• Образец данных (Excel, CSV, Google Sheets)\n"
            "• Доступ к базе данных или API\n"
            "• Скриншоты/описание того, что хотите видеть\n\n"
            "Мы сами поможем разобраться — просто оставьте заявку."
        ),
        "faq_a4": (
            "🔧 *Можно ли вносить изменения после сдачи?*\n\n"
            "Да! Мы предоставляем:\n"
            "• 3 бесплатные правки в течение 7 дней после сдачи\n"
            "• Платные доработки — по договорённости\n\n"
            "Серьёзные изменения в логике или структуре обсуждаются отдельно."
        ),
        "faq_a5": (
            "📦 *В каком формате передаётся готовый дашборд?*\n\n"
            "• Excel / Google Sheets — файл или ссылка на таблицу\n"
            "• Power BI / Tableau — файл отчёта + инструкция\n"
            "• Web дашборд — ссылка на хостинг или исходный код\n\n"
            "Всё сопровождается краткой инструкцией по использованию."
        ),
        "btn_back_faq": "⬅️ К списку вопросов",
    },

    "uz": {
        # ── language
        "lang_select": "🌐 Выберите язык / Tilni tanlang:",

        # ── welcome / menu
        "welcome": (
            "👋 Xush kelibsiz!\n\n"
            "Men sizga professional dashboard buyurtma qilishda yordam beraman.\n"
            "Biz yaratamiz:\n"
            "• 📊 Business / Analytics dashboardlar\n"
            "• 📈 Power BI va Tableau hisobotlar\n"
            "• 🌐 Web / SaaS dashboardlar\n"
            "• 📋 Excel / Google Sheets yechimlar\n\n"
            "Quyidagi bo'limni tanlang 👇"
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
            "*Business / Analytics dashboardlar*\n"
            "KPI, savdo, voronka va biznesingizning asosiy ko'rsatkichlarini vizualizatsiya.\n\n"
            "*Power BI / Tableau*\n"
            "Har qanday ma'lumot manbasiga ulanuvchi interaktiv hisobotlar.\n\n"
            "*Web / SaaS dashboardlar*\n"
            "Mahsulotingiz yoki saytingizga o'rnatilgan maxsus veb-dashboardlar.\n\n"
            "*Excel / Google Sheets*\n"
            "Grafiklar, pivot va formulalar bilan avtomatlashtirilgan jadvallar.\n\n"
            "Bajarish muddati: 3 dan 14 kungacha\n"
            "Narxi: $50 dan — murakkabligiga qarab\n\n"
            "Loyihangizni muhokama qilishga tayyormisiz? Ariza qoldiring! 👇"
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
        "order_start":   "📝 Ariza rasmiylashtirilmoqda\n\n1/5-qadam\n\n*Ismingizni* kiriting:",
        "order_phone":   "📱 2/5-qadam\n\n*Telefon raqamingizni* kiriting:",
        "order_type":    "📊 3/5-qadam\n\nQaysi turdagi dashboard kerak?",
        "order_budget":  "💰 4/5-qadam\n\n*Byudjet va muddatni* kiriting\n_(masalan: $100, 5 kun ichida kerak)_:",
        "order_desc":    "📋 5/5-qadam\n\n*Vazifani batafsil tasvirlab bering*\n_(nima kuzatish kerak, ma'lumotlar qayerdan, qanday natija kutilmoqda)_:",
        "order_confirm": (
            "✅ *Arizangizni tekshiring:*\n\n"
            "👤 Ism: {name}\n"
            "📱 Telefon: {phone}\n"
            "📊 Tur: {dtype}\n"
            "💰 Byudjet/muddat: {budget}\n"
            "📋 Tavsif: {desc}\n\n"
            "Hammasi to'g'rimi?"
        ),
        "btn_confirm":      "✅ Tasdiqlash",
        "btn_cancel":       "❌ Bekor qilish",
        "order_sent":       "🎉 Ariza yuborildi! Tez orada siz bilan bog'lanamiz.",
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
            "📊 Tur: {dtype}\n"
            "📦 Ma'lumot manbalari: {sources}\n"
            "🕐 Muddat: {deadline}\n\n"
            "💵 *Narx: ${min_p} — ${max_p}*\n\n"
            "_Aniq narx vazifani muhokama qilgandan so'ng belgilanadi._"
        ),
        "calc_src_1_2": "1–2 manba",
        "calc_src_3_5": "3–5 manba",
        "calc_src_6":   "6+ manba",
        "calc_dl_urgent": "⚡ Shoshilinch (1–3 kun)  +50%",
        "calc_dl_normal": "📅 Standart (4–7 kun)",
        "calc_dl_flex":   "🌿 Moslashuvchan (8+ kun)  −10%",
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
            "💰 *Dashboard narxi qancha?*\n\n"
            "Narx tur va murakkabligiga qarab:\n"
            "• Excel / Google Sheets — $50 dan\n"
            "• Business Analytics — $80 dan\n"
            "• Power BI / Tableau — $100 dan\n"
            "• Web / SaaS dashboard — $150 dan\n\n"
            "Narxga ma'lumot manbalari soni va muddat ta'sir qiladi.\n"
            "Tezkor baholash uchun 🧮 *Kalkulyator* dan foydalaning!"
        ),
        "faq_a2": (
            "⏱ *Ishlab chiqish qancha vaqt oladi?*\n\n"
            "• Shoshilinch — 1–3 ish kuni (+50% qo'shimcha)\n"
            "• Standart — 4–7 ish kuni\n"
            "• Moslashuvchan — 8–14 ish kuni (10% chegirma)\n\n"
            "Muddat ariza topshirishda kelishiladi."
        ),
        "faq_a3": (
            "📂 *Boshlash uchun qanday ma'lumotlar kerak?*\n\n"
            "Vazifaga qarab quyidagilar kerak bo'lishi mumkin:\n"
            "• Ma'lumot namunasi (Excel, CSV, Google Sheets)\n"
            "• Ma'lumotlar bazasi yoki API ga kirish\n"
            "• Ko'rmoqchi bo'lgan narsaning tasviri/skrinshotlari\n\n"
            "Biz o'zimiz yordam beramiz — shunchaki ariza qoldiring."
        ),
        "faq_a4": (
            "🔧 *Topshirilgandan keyin o'zgartirish mumkinmi?*\n\n"
            "Ha! Biz taqdim etamiz:\n"
            "• Topshirilgandan keyin 7 kun ichida 3 ta bepul tuzatish\n"
            "• Pullik qo'shimcha o'zgartirishlar — kelishuv asosida\n\n"
            "Mantiq yoki tuzilmadagi katta o'zgartirishlar alohida muhokama qilinadi."
        ),
        "faq_a5": (
            "📦 *Tayyor dashboard qanday shaklda beriladi?*\n\n"
            "• Excel / Google Sheets — fayl yoki jadval havolasi\n"
            "• Power BI / Tableau — hisobot fayli + yo'riqnoma\n"
            "• Web dashboard — hosting havolasi yoki manba kodi\n\n"
            "Hamma narsa qisqa foydalanish yo'riqnomasi bilan birga beriladi."
        ),
        "btn_back_faq": "⬅️ Savollarga qaytish",
    },
}
