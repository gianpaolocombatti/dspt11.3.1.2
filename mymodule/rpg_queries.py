import sqlite3

conn = sqlite3.connect('/Users/gianpaolocombatti/dspt11.3.1.2/rpg_db.sqlite3')

curs = conn.cursor()

TOTAL_CHARACTERS = """select count(*) from charactercreator_character"""

TOTAL_CHARACTERS_RESULTS = curs.execute(TOTAL_CHARACTERS).fetchall()

TOTAL_SUBCLASS = """select count(*) from charactercreator_necromancer"""

TOTAL_ITEMS = """select count(*) from armory_item"""

WEAPONS = """select count(*) from armory_item left join armory_weapon aw on armory_item.item_id = aw.item_ptr_id where aw.item_ptr_id is not null"""

NON_WEAPONS = """select count(*) from armory_item left join armory_weapon aw on armory_item.item_id = aw.item_ptr_id where aw.item_ptr_id is null"""

CHARACTER_ITEMS = """select character_id, count(item_id) from charactercreator_character_inventory group by character_id"""

CHARACTER_WEAPONS = """select character_id, count(item_id) from charactercreator_character_inventory where item_id in (select item_ptr_id from armory_weapon) group by character_id"""

AVG_CHARACTER_ITEMS = """select avg(c) from (select count(item_id) as c from charactercreator_character_inventory group by character_id)"""

AVG_CHARACTER_WEAPONS = """select avg(c) from (select count(item_id) as c from charactercreator_character_inventory where item_id in (select item_ptr_id from armory_weapon) group by character_id)"""

conn.close()