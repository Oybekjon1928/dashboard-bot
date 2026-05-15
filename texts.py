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
            "Срок выполнения: от 1 до 8 дней\n"
            "Стоимость: от $10 до $150 — зависит от сложности\n\n"
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
            "💰 *Сколько стоит дашборд?*\n\n"
            "Стоимость зависит от типа и сложности:\n"
            "• Excel / Google Sheets — от $10 до $30\n"
            "• Business Analytics — от $20 до $50\n"
            "• Power BI / Tableau — от $30 до $80\n"
            "• Web / SaaS дашборд — от $50 до $150\n\n"
            "На цену влияют количество источников данных и сроки.\n"
            "Воспользуйтесь 🧮 *Калькулятором* для быстрой оценки!"
        ),
        "faq_a2": (
            "⏱ *Сколько времени займёт разработка?*\n\n"
            "• Срочно — 1–2 рабочих дня (надбавка +50%)\n"
            "• Стандарт — 3–5 рабочих дней\n"
            "• Гибко — 6–8 рабочих дней (скидка 10%)\n\n"
            "Сроки обсуждаются при оформлении заявки."
        ),
        "faq_a3": (
            "📂 *Какие данные нужны для начала?*\n\n"
            "В зависимости от задачи нам могут понадобиться:\n\n"
            "*Для Excel / Google Sheets:*\n"
            "• Ваши исходные данные в любом формате (Excel, CSV, Google Sheets)\n"
            "• Описание: какие показатели важны (продажи, расходы, остатки и т.д.)\n"
            "• Пример или скриншот желаемого результата (если есть)\n\n"
            "*Для Power BI / Tableau:*\n"
            "• Источники данных: файлы, база данных, 1C, CRM или API\n"
            "• Логины/доступы к системам (передаются безопасно)\n"
            "• Список метрик и фильтров для отчёта\n\n"
            "*Для Web / SaaS дашборда:*\n"
            "• Описание функционала и нужных графиков\n"
            "• Дизайн-референс или примеры (необязательно)\n"
            "• Источник данных: API, база данных или ручной ввод\n\n"
            "*Для Business Analytics:*\n"
            "• Выгрузка данных за нужный период\n"
            "• Описание бизнес-процесса (что анализируем)\n"
            "• Цель анализа: рост продаж, оптимизация, отчётность\n\n"
            "Не знаете с чего начать? Просто напишите — мы сами разберёмся вместе!"
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
        "consult_day_0": "Сегодня",
        "consult_day_1": "Завтра",
        "consult_day_2": "Послезавтра",
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
            "Men sizga professional dashboard buyurtma qilishda yordam beraman.\n"
            "Biz yaratamiz:\n"
            "• 📊 Business / Analytics dashboardlar\n"
            "• 📈 Power BI va Tableau hisobotlar\n"
            "• 🌐 Web / SaaS dashboardlar\n"
            "• 📋 Excel / Google Sheets yechimlar\n\n"
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
            "*Business / Analytics dashboardlar*\n"
            "KPI, savdo, voronka va biznesingizning asosiy ko'rsatkichlarini vizualizatsiya.\n\n"
            "*Power BI / Tableau*\n"
            "Har qanday ma'lumot manbasiga ulanuvchi interaktiv hisobotlar.\n\n"
            "*Web / SaaS dashboardlar*\n"
            "Mahsulotingiz yoki saytingizga o'rnatilgan maxsus veb-dashboardlar.\n\n"
            "*Excel / Google Sheets*\n"
            "Grafiklar, pivot va formulalar bilan avtomatlashtirilgan jadvallar.\n\n"
            "Bajarish muddati: 1 kundan 8 kungacha\n"
            "Narxi: $10 dan $150 gacha — murakkabligiga qarab\n\n"
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
            "💰 *Dashboard narxi qancha?*\n\n"
            "Narx tur va murakkabligiga qarab:\n"
            "• Excel / Google Sheets — $10 dan $30 gacha\n"
            "• Business Analytics — $20 dan $50 gacha\n"
            "• Power BI / Tableau — $30 dan $80 gacha\n"
            "• Web / SaaS dashboard — $50 dan $150 gacha\n\n"
            "Narxga ma'lumot manbalari soni va muddat ta'sir qiladi.\n"
            "Tezkor baholash uchun 🧮 *Kalkulyator* dan foydalaning!"
        ),
        "faq_a2": (
            "⏱ *Ishlab chiqish qancha vaqt oladi?*\n\n"
            "• Shoshilinch — 1–2 ish kuni (+50% qo'shimcha)\n"
            "• Standart — 3–5 ish kuni\n"
            "• Moslashuvchan — 6–8 ish kuni (10% chegirma)\n\n"
            "Muddat ariza topshirishda kelishiladi."
        ),
        "faq_a3": (
            "📂 *Boshlash uchun qanday ma'lumotlar kerak?*\n\n"
            "Vazifaga qarab quyidagilar kerak bo'lishi mumkin:\n\n"
            "*Excel / Google Sheets uchun:*\n"
            "• Istalgan formatdagi dastlabki ma'lumotlar (Excel, CSV, Google Sheets)\n"
            "• Tavsif: qaysi ko'rsatkichlar muhim (savdo, xarajat, qoldiq va h.k.)\n"
            "• Kerakli natijaning namunasi yoki skrinshoti (bo'lsa)\n\n"
            "*Power BI / Tableau uchun:*\n"
            "• Ma'lumot manbalari: fayllar, baza, 1C, CRM yoki API\n"
            "• Tizimga kirish ma'lumotlari (xavfsiz tarzda uzatiladi)\n"
            "• Hisobot uchun metrikalar va filtrlar ro'yxati\n\n"
            "*Web / SaaS dashboard uchun:*\n"
            "• Funktsional va kerakli grafiklar tavsifi\n"
            "• Dizayn namunasi yoki misollar (shart emas)\n"
            "• Ma'lumot manbai: API, baza yoki qo'lda kiritish\n\n"
            "*Business Analytics uchun:*\n"
            "• Kerakli davr uchun ma'lumotlar yuklamasi\n"
            "• Biznes jarayonining tavsifi (nimani tahlil qilamiz)\n"
            "• Tahlil maqsadi: savdoni oshirish, optimallashtirish, hisobot\n\n"
            "Qayerdan boshlashni bilmaysizmi? Yozing — biz birgalikda aniqlaymiz!"
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
        "consult_t_9":  "09:00",
        "consult_t_11": "11:00",
        "consult_t_13": "13:00",
        "consult_t_15": "15:00",
        "consult_t_17": "17:00",
    },
}
