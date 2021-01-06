# -*- coding: UTF-8 -*-

woods = ['oak', 'spruce', 'birch', 'jungle', 'acacia', 'dark_oak', 'crimson', 'warped']
requirements = {'ez': ['tag', 'logs', 'stems'], 'woodcutter': ['item', 'planks', 'planks']}


def woodCutter():
    for wood in woods:
        for crafting in requirements:
            file_name = f'{crafting}_{wood}.json'
            json_file = open(file=file_name, mode='w+')
            file_contents = f'''{{
    "parent": "ezcraft:recipes/root",
    "rewards": {{
        "recipes": [
            "ezcraft:{crafting}_slab_{wood}",
            "ezcraft:{crafting}_stairs_{wood}"
        ]
    }},
    "criteria": {{
        "has_{wood}_{requirements[crafting][woods.index(wood) // 6 + 1]}": {{
            "trigger": "minecraft:inventory_changed",
            "conditions": {{
                "items": [
                    {{
                        "{requirements[crafting][0]}": "minecraft:{wood}_{requirements[crafting][woods.index(wood) // 6 + 1]}"
                    }}
                ]
            }}
        }}
    }}
}}
'''
            json_file.write(file_contents)
            json_file.close()


if __name__ == '__main__':
    woodCutter()
