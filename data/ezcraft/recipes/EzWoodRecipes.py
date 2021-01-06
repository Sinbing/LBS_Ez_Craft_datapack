# -*- coding: UTF-8 -*-

woods = ['oak', 'spruce', 'birch', 'jungle', 'acacia', 'dark_oak', 'crimson', 'warped']
logs = ['logs', 'stems']
products = {'stairs': ['''
        "#  ",
        "## ",
        "###"
    ''', 1], 'slab': ['''
        "###"
    ''', 2]}


def ezProductWood():
    for wood in woods:
        for product in products:
            file_name = f'ez_{wood}_{product}.json'
            json_file = open(file=file_name, mode='w+')
            file_contents = f'''{{
    "type": "minecraft:crafting_shaped",
    "group": "wooden_{product}",
    "pattern": [{products[product][0]}],
    "key": {{
        "#": {{
            "tag": "minecraft:{wood}_{logs[woods.index(wood) // 6]}"
        }}
    }},
    "result": {{
        "item": "minecraft:{wood}_{product}",
        "count": {(products[product][1] + 1) * 8}
    }}
}}
'''
            json_file.write(file_contents)
            json_file.close()


def woodCutter():
    for wood in woods:
        for product in products:
            file_name = f'woodcutter_{wood}_{product}.json'
            json_file = open(file=file_name, mode='w+')
            file_contents = f'''{{
    "type": "minecraft:stonecutting",
    "group": "wooden_{product}",
    "ingredient": {{
        "item": "minecraft:{wood}_planks"
    }},
    "result": "minecraft:{wood}_{product}",
    "count": {products[product][1]}
}}
'''
            json_file.write(file_contents)
            json_file.close()


if __name__ == '__main__':
    ezProductWood()
    woodCutter()
