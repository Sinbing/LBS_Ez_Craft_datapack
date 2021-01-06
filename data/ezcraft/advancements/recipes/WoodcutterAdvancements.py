# -*- coding: UTF-8 -*-

woods = ['acacia', 'birch', 'crimson', 'dark_oak', 'jungle', 'spruce', 'oak', 'warped']


def jsonGenerate():
    for wood in woods:
        file_name = f'rnc_woodcutters_{wood}_products.json'
        json_file = open(file=file_name, mode='w+')
        file_contents = f'''{{
    "parent": "ruecraft:recipes/root",
    "rewards": {{
        "recipes": [
            "ruecraft:rnc_woodcutters_{wood}_slabs",
            "ruecraft:rnc_woodcutters_{wood}_stairs"
        ]
    }},
    "criteria": {{
        "has_{wood}_planks": {{
            "trigger": "minecraft:inventory_changed",
            "conditions": {{
                "items": [
                    {{
                        "item": "minecraft:{wood}_planks"
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
    jsonGenerate()
