from aiogram import Bot, Dispatcher, types

NON_MEMBERS = {
    "start": [
        ("🗂 Divisions", "ex_divisions"),
        ("❔ Seminar", "send_fn_sem"),
        ("🗒 Register", "send_fn_reg"),
        ("📤 Contact", "send_e_feed"),
        ("🪑 Book a seat", "book_seat"),
        ("💳 Donate", "donate"),
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
        ("🏆 Hall of fame", "hof"),
    ],
    "My Divisions": [
        ("👨‍💻 Development", "development_m"),
        ("📊 Comp. Programming", "competitive-programming_m"),
    ],
    "Development": [
        ("🎖 Top Projects", "development_top"),
        ("📈 Statistics", "development_s"),
    ],
    "Competitive-Programming": [
        ("📊 Scoreboard", "competitive-programming_s"),
        ("📋 Schedule", "competitive-programming_sch"),
    ]
    
}


ADMINS = {
    "start": [
        ("📊 Statistics", "statistics"),
        ("🎇 Add Event", "add_event"),
        ("📋 Schedule", "admin_schedule"),
    ]
}