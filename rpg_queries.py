import os.path
import sqlite3 
import pandas as pd

conn = sqlite3.connect('rpg_db.sqlite3')
cursor = conn.cursor()


#How many total Characters are there? 
query = 'SELECT COUNT(*) FROM charactercreator_character;'
print(f"There are a total of {cursor.execute(query).fetchall()[0][0]} characters")


#How many of each specific subclass?

query2 = 'SELECT COUNT (character_ptr_id) FROM charactercreator_mage;'
print(f"There are a total of {cursor.execute(query2).fetchall()[0][0]} mages")

query3 = 'SELECT COUNT (character_ptr_id) FROM charactercreator_thief;'
print(f"There are a total of {cursor.execute(query3).fetchall()[0][0]} theives")

query4 = 'SELECT COUNT (character_ptr_id) FROM charactercreator_cleric;'
print(f"There are a total of {cursor.execute(query4).fetchall()[0][0]} clerics")

query5 = 'SELECT COUNT (character_ptr_id) FROM charactercreator_fighter;'
print(f"There are a total of {cursor.execute(query5).fetchall()[0][0]} fighter")

query6 = 'SELECT COUNT (mage_ptr_id) FROM charactercreator_necromancer;'
print(f"There are a total of {cursor.execute(query6).fetchall()[0][0]} necromancer")

#How many total items?

query7 = 'SELECT COUNT(item_id) FROM armory_item;'
print(f"There are a total of {cursor.execute(query7).fetchall()[0][0]} items")

#How many of the items are weapons? 

query8 = 'SELECT COUNT(item_ptr_id) FROM armory_weapon;'
print(f"There are a total of {cursor.execute(query8).fetchall()[0][0]} weapons")

#How many are not?

query9 = '''
SELECT sum(w.item_ptr_id is null) AS non_weapon_count
,sum(w.item_ptr_id is not null) AS weapon_count
FROM armory_item i
LEFT JOIN armory_weapon w ON i.item_id = w.item_ptr_id
 '''
print(f"These {cursor.execute(query9).fetchall()[0][0]} are not weapons")

#How many items does each character have? (Return first 20 rows)

query10 = '''
SELECT character.character_id, 
COUNT (inventory.item_id)
FROM charactercreator_character AS character, 
charactercreator_character_inventory AS inventory, armory_item AS armory
WHERE character.character_id = inventory.character_id
AND armory.item_id = inventory.item_id
GROUP BY character.character_id
LIMIT 20
'''

rows = cursor.execute(query10)
print('Number of items each character has: ')
for row in rows:
    name = row[0]
    print('char_id', " ", 'items')
    print(name, "       " , row[1])


#How many weapons does each character have?

query11 = '''
SELECT character.character_id, 
COUNT (armory.item_id)
FROM charactercreator_character AS character, 
charactercreator_character_inventory AS inventory, armory_item AS armory
WHERE character.character_id = armory.item_id
AND inventory.item_id = armory.item_id
GROUP BY character.character_id
LIMIT 20
'''

rows = cursor.execute(query11)
print('Number of weapons each character has: ')
for row in rows:
    name = row[0]
    print('char_id', " ", 'weapons')
    print(name, "       " , row[1])


#On average, How many weapons does each character have?

query12 = '''
SELECT AVG(weapon_count)
FROM(
    SELECT character.name, count(weapon.item_ptr_id) as weapon_count
    FROM charactercreator_character AS character,
    charactercreator_character_inventory AS inventory,
    armory_weapon AS weapon

    WHERE character.character_id = inventory.character_id
    AND inventory.item_id = weapon.item_ptr_id
    GROUP BY character.name
    ORDER BY character.name
    LIMIT 20
)
'''

print(f"On average each character has {cursor.execute(query12).fetchall()[0][0]} weapons")





