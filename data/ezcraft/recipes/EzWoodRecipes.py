# -*- coding: UTF-8 -*-

woods = ['acacia', 'birch', 'crimson', 'dark_oak', 'jungle', 'spruce', 'oak', 'warped']
products = ['stairs', 'slab']


def ezWoodSlab():
    for wood in woods:
        for product in products:
            file_name = f'woodcutters_{wood}_{product}.json'
            json_file = open(file=file_name, mode='w+')
            file_contents = f'''{{
        "type": "minecraft:stonecutting",
        "group": "wooden_{product}",
        "ingredient": {{
            "item": "{wood}_planks"
        }},
        "result": "{wood}_{product}",
        "count": {products.index(product) + 1}
    }}
    '''
            json_file.write(file_contents)
            json_file.close()


def ezWoodStairs():
    for wood in woods:
        for product in products:
            file_name = f'woodcutters_{wood}_{product}.json'
            json_file = open(file=file_name, mode='w+')
            file_contents = f'''{{
        "type": "minecraft:stonecutting",
        "group": "wooden_{product}",
        "ingredient": {{
            "item": "{wood}_planks"
        }},
        "result": "{wood}_{product}",
        "count": {products.index(product) + 1}
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
        "item": "{wood}_planks"
    }},
    "result": "{wood}_{product}",
    "count": {products.index(product) + 1}
}}
'''
            json_file.write(file_contents)
            json_file.close()


if __name__ == '__main__':
    woodCutter()
