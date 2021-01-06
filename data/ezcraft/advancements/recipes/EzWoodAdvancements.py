# -*- coding: UTF-8 -*-

woods = ['acacia', 'birch', 'crimson', 'dark_oak', 'jungle', 'spruce', 'oak', 'warped']
requirements = {'ez': ['tag', 'log'], 'woodcutter': ['item', 'planks']}


def woodCutter():
    for wood in woods:
        for crafting in requirements:
            file_name = f'{crafting}_{wood}.json'
            json_file = open(file=file_name, mode='w+')
            file_contents = f'''{{
    "parent": "ezcraft:recipes/root",
    "rewards": {{
        "recipes": [
            "ezcraft:{crafting}_{wood}_slabs",
            "ezcraft:{crafting}_{wood}_stairs"
        ]
    }},
    "criteria": {{
        "has_{wood}_{requirements[crafting][1]}": {{
            "trigger": "minecraft:inventory_changed",
            "conditions": {{
                "items": [
                    {{
                        "{requirements[crafting][0]}": "minecraft:{wood}_{requirements[crafting][1]}"
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
