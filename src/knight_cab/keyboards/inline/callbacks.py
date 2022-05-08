from aiogram import Bot, Dispatcher, types

NON_MEMBERS = {
    "start": [
        ("🗂 Divisions", "ex_divisions"),
        ("❔ Seminar", "send_fn_sem"),
        ("🗒 Register", "send_fn_reg"),
        ("📤 Contact", "send_e_feed"),
    ],
    "divisions": [
        ("👨‍💻 Development", "ex_development"),
        ("📊 Comp. Programming", "ex_competitive-programming"),
        ("✍️ Cap. Building", "ex_capacity-building"),
        ("🛡 Security", "ex_security"),
        ("⬅️ Back", "start"),
    ],
    "development": [
        ("📈 Statistics", "d_s"),
        ("📋 Schedule", "d_sch"),
        ("⬅️ Back", "ex_divisions"),
    ],
    "competitive-programming": [
        ("📈 Statistics", "cp_s"),
        ("📋 Schedule", "cp_sch"),
        ("⬅️ Back", "ex_divisions"),
    ],
    "capacity-building": [
        ("Seminar", "cb_s"),
        ("Tutorial", "cb_t"),
        ("⬅️ Back", "ex_divisions"),
    ],
    "security": [
        ("Seminar", "cb_s"),
        ("Tutorial", "cb_t"),
        ("⬅️ Back", "ex_divisions"),
    ],
}


MEMBERS = {
    "start": [
        ("🗂 My Divisions", "my_divisions"),
        ("❔ Seminar", "send_fn_sem"),
        ("🗒 Register", "send_fn_reg"),
        ("📤 Contact", "send_e_feed"),
    ],
    "My Divisions": [
        ("👨‍💻 Development", "my_development"),
        ("📊 Comp. Programming", "my_competitive-programming"),
    ],
    
}