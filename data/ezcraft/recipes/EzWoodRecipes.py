# -*- coding: UTF-8 -*-

woods = ['acacia', 'birch', 'crimson', 'dark_oak', 'jungle', 'spruce', 'oak', 'warped']
products = ['stairs', 'slab']
patterns = {'stairs': '''
        "#  ",
        "## ",
        "###"
    ''', 'slab': '''
        "###"
    '''}


def ezProductWood():
    for wood in woods:
        for product in products:
            file_name = f'ez_{product}_{wood}.json'
            json_file = open(file=file_name, mode='w+')
            file_contents = f'''{{
    "type": "minecraft:crafting_shaped",
    "group": "wooden_{product}",
    "pattern": [{patterns[product]}],
    "key": {{
        "#": {{
            "tag": "minecraft:{wood}_logs"
        }}
    }},
    "result": {{
        "item": "minecraft:{wood}_{product}",
        "count": {(products.index(product) + 2) * 8}
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
    "count": {products.index(product) + 1}
}}
'''
            json_file.write(file_contents)
            json_file.close()


if __name__ == '__main__':
    ezProductWood()
    woodCutter()
