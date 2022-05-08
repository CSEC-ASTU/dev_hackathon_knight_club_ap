from aiogram import Bot, Dispatcher, types

NON_MEMBERS = {
    "start": [
        ("🗂 Divisions", "d"),
        ("❔ Seminar", "send_fn_sem"),
        ("🗒 Register", "send_fn_reg"),
        ("📤 Contact", "send_e_feed"),
    ],
    "divisions": [
        ("👨‍💻 Development", "dev"),
        ("📊 Comp. Programming", "cp"),
        ("✍️ Cap. Building", "cb"),
        ("🛡 Security", "sec"),
        ("⬅️ Back", "/start"),
    ],
    "development": [
        ("📈 Statistics", "d_s"),
        ("📋 Schedule", "d_sch"),
        ("⬅️ Back", "d"),
    ],
    "competitive programming": [
        ("📈 Statistics", "cp_s"),
        ("📋 Schedule", "cp_sch"),
        ("⬅️ Back", "d"),
    ],
    "capacity building": [
        ("Seminar", "cb_s"),
        ("Tutorial", "cb_t"),
        ("⬅️ Back", "d"),
    ],
}
