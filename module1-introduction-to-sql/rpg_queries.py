import sqlite3


def connect_to_db(db_name="rpg_db.sqlite3"):
    return sqlite3.connect(db_name)


def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()


total_chars = """
    SELECT count (*) 
    FROM charactercreator_character;
    """

num_thief = """
    SELECT count (*)
    FROM charactercreator_thief;
    """

num_fighter = """
    SELECT count (*)
    FROM charactercreator_fighter;
    """

num_mage = """
    SELECT count (*)
    FROM charactercreator_mage;
    """

num_cleric = """
    SELECT count (*)
    FROM charactercreator_cleric;
    """

num_necromancer = """
    SELECT count (*)
    FROM charactercreator_necromancer;
    """

total_items = """
    SELECT count(*) 
    FROM armory_item;
    """

weapons = """
    SELECT count (*) FROM armory_weapon
    """

not_weapons = """
    SELECT (SELECT count (*) FROM armory_item ) - 
    (SELECT count (*) FROM armory_weapon)
    """

items_per_character = """
    SELECT character_id, COUNT (item_id)
    FROM (charactercreator_character_inventory)
    GROUP BY (character_id)
    LIMIT 20;
    """

weapon_count = """
    SELECT character_id, COUNT (item_id)
    FROM (charactercreator_character_inventory)
    INNER JOIN armory_weapon
    ON item_ptr_id = item_id
    GROUP BY (character_id)
    LIMIT 20;
    """

avg_items = """
SELECT character_id, COUNT(item_id)
FROM charactercreator_character_inventory
GROUP BY character_id
"""

weapons_per_char = """
SELECT character_id, count(id)
FROM charactercreator_character_inventory
INNER JOIN armory_weapon
ON item_id = item_ptr_id
GROUP BY character_id
LIMIT 20
"""

avg_items_per_char = """
SELECT AVG (count_table)
FROM(
SELECT COUNT(id) as count_table
FROM charactercreator_character_inventory
GROUP BY character_id
)
"""

avg_weapons_per_char = """
SELECT AVG (count_table)
FROM(
SELECT character_id, count(id) as count_table
FROM charactercreator_character_inventory
INNER JOIN armory_weapon
ON item_id = item_ptr_id
GROUP BY character_id
)
"""

get_num_rows_in_buddy = """
SELECT count(*) FROM Table1
"""

num_users_nature = """
SELECT count([User ID])
FROM Table1
WHERE Nature > 100
"""

num_users_shopping = """
SELECT count([User ID])
FROM Table1
WHERE Shopping > 100
"""

if __name__ == "__main__":
    conn = connect_to_db()
    curs = conn.cursor()
    results = execute_query(curs, total_chars)
    print("Total Characters: ", results)
    print("Number of theives: ", execute_query(curs, num_thief))
    print("Number of fighters: ", execute_query(curs, num_fighter))
    print("Number of clerics: ", execute_query(curs, num_cleric))
    print("Number of mages: ", execute_query(curs, num_mage))
    print(
        "Number of necromancers (subset of mages)", execute_query(curs, num_necromancer)
    )
    print("Total items: ", execute_query(curs, total_items))
    print("Number of weapons: ", execute_query(curs, weapons))
    print("Non-weapon items: ", execute_query(curs, not_weapons))
    print("How many Items does each character have?", execute_query(curs,items_per_character))
    print("How many Weapons does each character have?", execute_query(curs,weapons_per_char))
    print("On average, how many Items does each Character have?", execute_query(curs, avg_items_per_char))
    print("On average, how many Weapons does each character have?", execute_query(curs, avg_weapons_per_char))

    conn = connect_to_db('buddymove_holidayiq.sqlite3')
    curs = conn.cursor()

    #df.to_sql('review', con=conn)

    print("Numbers of rows in buddy db", execute_query(curs, get_num_rows_in_buddy))
    print("How many users who reviewed at least 100 in `Nature` in the category", execute_query(curs, num_users_nature))
    print("How many users who reviewed at least 100 in `Shopping` in the category", execute_query(curs, num_users_shopping))
