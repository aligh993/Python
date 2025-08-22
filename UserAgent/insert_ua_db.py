# @author: ALI GHANBARI 
# @email: alighanbari446@gmail.com

import sqlite3
from user_agents import parse

conn = sqlite3.connect('ua_db.db')
cr = conn.cursor()

with open("common2.txt", encoding='utf-8') as f:
    for ua_string in f:
        user_agent = parse(ua_string)
        if user_agent.is_mobile or user_agent.is_tablet:
            b_type = "Mobile Browser"
        elif user_agent.is_pc:
            b_type = "Browser"
        elif user_agent.is_bot:
            b_type = "Bot"
        else:
            b_type = "Other"

        cr.execute('INSERT OR IGNORE into ua_table values (?, ?)',  (ua_string, b_type))

conn.commit()
conn.close()
