import sqlite3
import os
import pandas as pd



conn = sqlite3.connect('/Users/gianpaolocombatti/dspt11.3.1.2/rpg_db.sqlite3')

print(conn)

curs = conn.cursor()

select_weapon_query = """select * from armory_weapon left join armory_item ai on armory_weapon.item_ptr_id = ai.item_id"""

weapon_results = curs.execute(select_weapon_query).fetchall()

weapon_df = pd.DataFrame(weapon_results)

conn.close()

print(weapon_results)

