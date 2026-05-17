TEXTS = {
    "ru": {
        # ── language
        "lang_select": "🌐 Выберите язык / Tilni tanlang:",

        # ── welcome / menu
        "welcome": (
            "👋 Добро пожаловать в *Markenti*!\n\n"
            "Мы помогаем бизнесу расти через SMM\n"
            "и стратегии брендинга.\n\n"
            "📱 Instagram · Telegram · Facebook · YouTube\n"
            "🧠 Брендинг · Стратегия · Аналитика аудитории\n\n"
            "Выберите раздел 👇"
        ),
        "main_menu": "🏠 Главное меню",
        "btn_services":  "📊 Услуги",
        "btn_portfolio": "🖼 Портфолио",
        "btn_faq":       "❓ FAQ",
        "btn_order":     "📝 Оставить заявку",
        "btn_contacts":  "📞 Контакты",
        "btn_back":      "⬅️ Назад",
        "btn_main_menu": "🏠 Главное меню",

        # ── services
        "services_text": (
            "🚀 *Услуги Markenti*\n\n"

            "📱 *SMM — Управление соцсетями*\n"
            "✅ Ведение Instagram, Telegram, Facebook, YouTube\n"
            "✅ Контент-план и создание публикаций\n"
            "✅ Работа с аудиторией (комментарии, DM)\n"
            "✅ Ежемесячный отчёт и аналитика\n"
            "💰 Цена — по договорённости\n"
            "⚡ Старт проекта — за 1–3 дня\n\n"

            "🧠 *Поведение потребителей & Бренд-стратегия*\n"
            "✅ Анализ целевой аудитории и конкурентов\n"
            "✅ Позиционирование бренда\n"
            "✅ Голос, тон и визуальный стиль\n"
            "✅ Готовая маркетинговая стратегия\n"
            "💰 Цена — зависит от объёма задачи\n"
            "⚡ Длительность — 2–4 недели\n\n"

            "🎯 Начнём с *бесплатной консультации*!\n\n"
            "👇 Оставьте заявку прямо сейчас:"
        ),

        # ── portfolio
        "portfolio_text":  "🖼 *Портфолио*\n\nНаши работы:",
        "portfolio_empty": "🖼 Портфолио пока не добавлено. Загляните позже!",

        # ── contacts
        "contacts_text": (
            "📞 *Контакты*\n\n"
            "По всем вопросам обращайтесь напрямую:\n"
            "👤 Менеджер: @{admin_username}\n\n"
            "Или оставьте заявку — мы свяжемся с вами!"
        ),

        # ── order flow
        "order_start":   "📝 *Заявка — шаг 1/6*\n\nВведите ваше *имя*:",
        "order_phone":   "📱 *Шаг 2/6*\n\nВведите *номер телефона*:",
        "order_service": "🎯 *Шаг 3/6*\n\nКакая услуга вас интересует?",
        "order_niche":   "🏢 *Шаг 4/6*\n\nОпишите ваш *бизнес / нишу*\n_(например: интернет-магазин, кафе, фитнес)_:",
        "order_goal":    "📊 *Шаг 5/6*\n\nКакова ваша главная *цель*?",
        "order_budget":  (
            "💰 *Шаг 6/6*\n\nУкажите ваш *бюджет*\n"
            "_(например: $200/мес или $500 разово)_\n\n"
            "Есть ли уже аккаунты в соцсетях? Напишите кратко:"
        ),
        "order_confirm": (
            "✅ *Проверьте заявку:*\n\n"
            "👤 {name}\n"
            "📱 {phone}\n"
            "🎯 {dtype}\n"
            "🏢 {niche}\n"
            "📊 {goal}\n"
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

        # ── service type labels
        "type_smm":      "📱 SMM (соцсети)",
        "type_branding": "🧠 Брендинг & Стратегия",
        "type_both":     "🚀 Оба направления",

        # ── goal labels
        "goal_followers": "👥 Больше подписчиков",
        "goal_sales":     "💸 Увеличить продажи",
        "goal_awareness": "📢 Узнаваемость бренда",

        # ── admin notifications
        "admin_order_notify": (
            "🔔 *Yangi buyurtma #{order_id}!*\n\n"
            "👤 {name}\n"
            "📱 {phone}\n"
            "🎯 Xizmat: {dtype}\n"
            "🏢 Soha: {niche}\n"
            "📊 Maqsad: {goal}\n"
            "💰 Byudjet: {budget}\n\n"
            "🆔 ID: `{user_id}` | @{username}\n\n"
            "✅ Qabul qilish: `/accept {order_id}`\n"
            "❌ Rad etish: `/reject {order_id} sabab`"
        ),
        "admin_order_remind": (
            "⏰ *15 daqiqa o'tdi! #{order_id} buyurtmaga javob berilmadi!*\n\n"
            "👤 {name} | 📱 {phone}\n"
            "🎯 {dtype} | 💰 {budget}\n\n"
            "✅ Qabul: `/accept {order_id}`\n"
            "❌ Rad: `/reject {order_id} sabab`"
        ),
        "admin_accepted":   "✅ #{id} qabul qilindi. Mijoz bilan bog'laning!",
        "admin_accept_404": "❌ #{id} topilmadi.",

        # ── FAQ
        "faq_menu": "❓ *Часто задаваемые вопросы*\n\nВыберите вопрос:",
        "faq_q1": "💰 Сколько стоят услуги?",
        "faq_q2": "⏱ Когда появятся результаты?",
        "faq_q3": "📱 С какими платформами работаете?",
        "faq_q4": "🤝 Как строится сотрудничество?",
        "faq_q5": "📊 Как отслеживаем результаты?",
        "faq_a1": (
            "💰 *Xizmat narxi qancha?*\n\n"
            "Narx loyiha hajmi va murakkabligiga qarab belgilanadi:\n\n"
            "📱 *SMM xizmati:*\n"
            "• Kichik biznes — arzon paketlar\n"
            "• O'rta va katta biznes — kengaytirilgan paket\n\n"
            "🧠 *Brend strategiyasi:*\n"
            "• Bir martalik loyiha — muzokaraga asosan\n\n"
            "🎯 Aniq narxni bilish uchun *bepul maslahat* oling!\n\n"
            "👇 Hoziroq ariza qoldiring:"
        ),
        "faq_a2": (
            "⏱ *Natijalar qachon ko'rinadi?*\n\n"
            "📱 *SMM:*\n"
            "• 1-oy: Kontent sifati va doimiylik\n"
            "• 2–3-oy: Organik o'sish sezilarli\n"
            "• 3–6-oy: Sotuv natijalariga ta'sir\n\n"
            "🧠 *Brend strategiyasi:*\n"
            "• 2–4 hafta: Tayyor strategiya\n\n"
            "✅ Har oyda hisobot va tahlil taqdim etamiz.\n\n"
            "👇 Boshlaylik:"
        ),
        "faq_a3": (
            "📱 *Qaysi platformalarda ishlaymiz?*\n\n"
            "✅ *Instagram* — rasm, reels, stories\n"
            "✅ *Telegram* — kanal va guruh boshqaruvi\n"
            "✅ *Facebook* — korporativ sahifa\n"
            "✅ *YouTube* — video kontent strategiyasi\n\n"
            "💡 Bir nechta platformani birgalikda boshqarish ham mumkin!\n\n"
            "👇 Ariza qoldiring:"
        ),
        "faq_a4": (
            "🤝 *Hamkorlik qanday ishlaydi?*\n\n"
            "1️⃣ Bepul maslahat — biznesni tushunib olamiz\n"
            "2️⃣ Tahlil — raqobatchilar va auditoriyangiz\n"
            "3️⃣ Strategiya — kontent rejasi va maqsadlar\n"
            "4️⃣ Ijro — postlar, hikoyalar, videolar\n"
            "5️⃣ Hisobot — har oyda natijalar tahlili\n\n"
            "✅ Siz faqat natijaga e'tibor qilasiz!\n\n"
            "👇 Boshlaylik:"
        ),
        "faq_a5": (
            "📊 *Natijalarni qanday kuzatamiz?*\n\n"
            "✅ Har oyda batafsil hisobot:\n"
            "• Auditoriya o'sishi\n"
            "• Qamrov va ko'rishlar soni\n"
            "• Engagement (like, izoh, ulashish)\n"
            "• Sayt yoki do'konga o'tishlar\n\n"
            "📊 Ko'rsatkichlar asosida strategiyani moslashtiramiz.\n\n"
            "👇 Hoziroq boshlaymiz:"
        ),
        "btn_back_faq": "⬅️ К списку вопросов",

        # ── portfolio (user)
        "portfolio_select_cat": "🖼 *Портфолио*\n\nВыберите категорию:",
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
        "btn_port_order":     "📝 Заказать такое же",

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
        "adm_port_saved":       "✅ Работа добавлена в портфолио!",
        "adm_port_cancelled":   "❌ Отменено.",
        "adm_port_list_title":  "🗂 *Все работы в портфолио:*\n",
        "adm_port_list_row":    "#{id} [{cat}] {title}\n",
        "adm_port_empty":       "📭 Портфолио пустое.",
        "adm_port_del_confirm": "🗑 Удалить *#{id} — {title}*?",
        "adm_port_deleted":     "✅ Работа #{id} удалена.",
        "btn_skip":             "⏭ Пропустить",
        "btn_save":             "✅ Сохранить",
        "btn_delete":           "🗑 Удалить",
        "btn_del_yes":          "✅ Да, удалить",
        "btn_del_no":           "❌ Отмена",

        # ── channel
        "btn_channel": "📢 Наш канал",

        # ── my orders button
        "btn_myorders": "📋 Мои заявки",

        # ── language switch
        "btn_switch_lang": "🌐 O'zbekcha",
        "lang_switched": "Язык изменён на русский.",

        # ── my orders
        "myorders_empty":  "📭 У вас пока нет заявок. Оставьте первую заявку!",
        "myorders_header": "📋 *Ваши заявки:*\n",
        "myorders_row":    "{status} *#{id}* — {dtype}\n💰 {budget} | 🕐 {date}\n",
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
        "reminder_cancelled":    "Заявка отменена. Возвращаю в меню.",
    },

    "uz": {
        # ── language
        "lang_select": "🌐 Выберите язык / Tilni tanlang:",

        # ── welcome / menu
        "welcome": (
            "👋 *Markenti*ga xush kelibsiz!\n\n"
            "Biz biznesingizni SMM va brend strategiyasi\n"
            "orqali o'sishiga yordam beramiz.\n\n"
            "📱 Instagram · Telegram · Facebook · YouTube\n"
            "🧠 Brending · Strategiya · Auditoriya tahlili\n\n"
            "Bo'limlardan birini tanlang 👇"
        ),
        "main_menu": "🏠 Asosiy menyu",
        "btn_services":  "📊 Xizmatlar",
        "btn_portfolio": "🖼 Portfolio",
        "btn_faq":       "❓ FAQ",
        "btn_order":     "📝 Ariza qoldirish",
        "btn_contacts":  "📞 Aloqa",
        "btn_back":      "⬅️ Orqaga",
        "btn_main_menu": "🏠 Asosiy menyu",

        # ── services
        "services_text": (
            "🚀 *Markenti xizmatlari*\n\n"

            "📱 *SMM — Ijtimoiy tarmoqlar boshqaruvi*\n"
            "✅ Instagram, Telegram, Facebook, YouTube\n"
            "✅ Kontent rejasi va post yaratish\n"
            "✅ Auditoriya bilan ishlash (izohlar, DM)\n"
            "✅ Har oyda hisobot va tahlil\n"
            "💰 Narx — muzokaraga asosan\n"
            "⚡ Loyiha boshlanishi — 1–3 kun ichida\n\n"

            "🧠 *Iste'molchi xulqi & Brend strategiyasi*\n"
            "✅ Maqsadli auditoriya va raqobatchilar tahlili\n"
            "✅ Brend pozitsioneri\n"
            "✅ Ovoz, ton va vizual uslub\n"
            "✅ Tayyor marketing strategiyasi\n"
            "💰 Narx — vazifa hajmiga qarab\n"
            "⚡ Davomiyligi — 2–4 hafta\n\n"

            "🎯 *Bepul maslahat* bilan boshlaymiz!\n\n"
            "👇 Hoziroq ariza qoldiring:"
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
        "order_start":   "📝 *Ariza — 1/6-qadam*\n\n*Ismingizni* kiriting:",
        "order_phone":   "📱 *2/6-qadam*\n\n*Telefon raqamingizni* kiriting:",
        "order_service": "🎯 *3/6-qadam*\n\nQaysi xizmat qiziqtiradi?",
        "order_niche":   "🏢 *4/6-qadam*\n\n*Biznesingiz / sohangizni* tasvirlab bering\n_(masalan: kiyim do'koni, restoran, fitnes)_:",
        "order_goal":    "📊 *5/6-qadam*\n\nAsosiy *maqsadingiz* nima?",
        "order_budget":  (
            "💰 *6/6-qadam*\n\n*Byudjetingizni* kiriting\n"
            "_(masalan: $200/oy yoki $500 bir marta)_\n\n"
            "Hozirda ijtimoiy tarmoqlarda akkauntlaringiz bormi? Qisqacha yozing:"
        ),
        "order_confirm": (
            "✅ *Arizangizni tekshiring:*\n\n"
            "👤 {name}\n"
            "📱 {phone}\n"
            "🎯 {dtype}\n"
            "🏢 {niche}\n"
            "📊 {goal}\n"
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

        # ── service type labels
        "type_smm":      "📱 SMM (ijtimoiy tarmoqlar)",
        "type_branding": "🧠 Brending & Strategiya",
        "type_both":     "🚀 Ikkalasi ham",

        # ── goal labels
        "goal_followers": "👥 Ko'proq obunachilar",
        "goal_sales":     "💸 Savdolarni oshirish",
        "goal_awareness": "📢 Brend taniqliligini oshirish",

        # ── admin notifications
        "admin_order_notify": (
            "🔔 *Yangi buyurtma #{order_id}!*\n\n"
            "👤 {name}\n"
            "📱 {phone}\n"
            "🎯 Xizmat: {dtype}\n"
            "🏢 Soha: {niche}\n"
            "📊 Maqsad: {goal}\n"
            "💰 Byudjet: {budget}\n\n"
            "🆔 ID: `{user_id}` | @{username}\n\n"
            "✅ Qabul qilish: `/accept {order_id}`\n"
            "❌ Rad etish: `/reject {order_id} sabab`"
        ),
        "admin_order_remind": (
            "⏰ *15 daqiqa o'tdi! #{order_id} buyurtmaga javob berilmadi!*\n\n"
            "👤 {name} | 📱 {phone}\n"
            "🎯 {dtype} | 💰 {budget}\n\n"
            "✅ Qabul: `/accept {order_id}`\n"
            "❌ Rad: `/reject {order_id} sabab`"
        ),
        "admin_accepted":   "✅ #{id} qabul qilindi. Mijoz bilan bog'laning!",
        "admin_accept_404": "❌ #{id} topilmadi.",

        # ── FAQ
        "faq_menu": "❓ *Ko'p so'raladigan savollar*\n\nSavolni tanlang:",
        "faq_q1": "💰 Xizmat narxi qancha?",
        "faq_q2": "⏱ Natijalar qachon ko'rinadi?",
        "faq_q3": "📱 Qaysi platformalarda ishlaysiz?",
        "faq_q4": "🤝 Hamkorlik jarayoni qanday?",
        "faq_q5": "📊 Natijalarni qanday kuzatamiz?",
        "faq_a1": (
            "💰 *Xizmat narxi qancha?*\n\n"
            "Narx loyiha hajmi va murakkabligiga qarab belgilanadi:\n\n"
            "📱 *SMM xizmati:*\n"
            "• Kichik biznes — arzon paketlar\n"
            "• O'rta va katta biznes — kengaytirilgan paket\n\n"
            "🧠 *Brend strategiyasi:*\n"
            "• Bir martalik loyiha — muzokaraga asosan\n\n"
            "🎯 Aniq narxni bilish uchun *bepul maslahat* oling!\n\n"
            "👇 Hoziroq ariza qoldiring:"
        ),
        "faq_a2": (
            "⏱ *Natijalar qachon ko'rinadi?*\n\n"
            "📱 *SMM:*\n"
            "• 1-oy: Kontent sifati va doimiylik\n"
            "• 2–3-oy: Organik o'sish sezilarli\n"
            "• 3–6-oy: Sotuv natijalariga ta'sir\n\n"
            "🧠 *Brend strategiyasi:*\n"
            "• 2–4 hafta: Tayyor strategiya\n\n"
            "✅ Har oyda hisobot va tahlil taqdim etamiz.\n\n"
            "👇 Boshlaylik:"
        ),
        "faq_a3": (
            "📱 *Qaysi platformalarda ishlaymiz?*\n\n"
            "✅ *Instagram* — rasm, reels, stories\n"
            "✅ *Telegram* — kanal va guruh boshqaruvi\n"
            "✅ *Facebook* — korporativ sahifa\n"
            "✅ *YouTube* — video kontent strategiyasi\n\n"
            "💡 Bir nechta platformani birgalikda boshqarish ham mumkin!\n\n"
            "👇 Ariza qoldiring:"
        ),
        "faq_a4": (
            "🤝 *Hamkorlik qanday ishlaydi?*\n\n"
            "1️⃣ Bepul maslahat — biznesni tushunib olamiz\n"
            "2️⃣ Tahlil — raqobatchilar va auditoriyangiz\n"
            "3️⃣ Strategiya — kontent rejasi va maqsadlar\n"
            "4️⃣ Ijro — postlar, hikoyalar, videolar\n"
            "5️⃣ Hisobot — har oyda natijalar tahlili\n\n"
            "✅ Siz faqat natijaga e'tibor qilasiz!\n\n"
            "👇 Boshlaylik:"
        ),
        "faq_a5": (
            "📊 *Natijalarni qanday kuzatamiz?*\n\n"
            "✅ Har oyda batafsil hisobot:\n"
            "• Auditoriya o'sishi\n"
            "• Qamrov va ko'rishlar soni\n"
            "• Engagement (like, izoh, ulashish)\n"
            "• Sayt yoki do'konga o'tishlar\n\n"
            "📊 Ko'rsatkichlar asosida strategiyani moslashtiramiz.\n\n"
            "👇 Hoziroq boshlaymiz:"
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
        "btn_port_order":     "📝 Shundan buyurtma berish",

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
        "adm_port_saved":       "✅ Ish portfolio'ga qo'shildi!",
        "adm_port_cancelled":   "❌ Bekor qilindi.",
        "adm_port_list_title":  "🗂 *Portfolio'dagi barcha ishlar:*\n",
        "adm_port_list_row":    "#{id} [{cat}] {title}\n",
        "adm_port_empty":       "📭 Portfolio bo'sh.",
        "adm_port_del_confirm": "🗑 *#{id} — {title}* ni o'chirishni tasdiqlaysizmi?",
        "adm_port_deleted":     "✅ #{id} raqamli ish o'chirildi.",
        "btn_skip":             "⏭ O'tkazib yuborish",
        "btn_save":             "✅ Saqlash",
        "btn_delete":           "🗑 O'chirish",
        "btn_del_yes":          "✅ Ha, o'chirish",
        "btn_del_no":           "❌ Bekor",

        # ── channel
        "btn_channel": "📢 Bizning kanal",

        # ── my orders button
        "btn_myorders": "📋 Mening buyurtmalarim",

        # ── language switch
        "btn_switch_lang": "🌐 Русский",
        "lang_switched":   "Til o'zbekchaga o'zgartirildi.",

        # ── my orders
        "myorders_empty":  "📭 Sizda hali arizalar yo'q. Birinchi arizani qoldiring!",
        "myorders_header": "📋 *Sizning arizalaringiz:*\n",
        "myorders_row":    "{status} *#{id}* — {dtype}\n💰 {budget} | 🕐 {date}\n",
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
        "reminder_cancelled":    "Ariza bekor qilindi. Menyuga qaytaraman.",
    },
}
