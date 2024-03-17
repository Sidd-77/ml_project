### Playground for trying things out. It will be removed...

from typing import List


def test(fpath:str)->List[str]:
    requirements =[]
    with open(fpath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
    return requirements

too = test('requirements.txt')
print(too)