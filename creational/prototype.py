from __future__ import annotations
import copy
from typing import Any, List, Optional, Dict


class SelfReferencingEntity:
    def __init__(self):
        self.parent = None

    def set_parent(self, parent: Any):
        self.parent = parent


class SomeComponent:
    def __init__(self, some_int: int, some_list_of_objects: List[Any], some_circular_ref: SelfReferencingEntity):
        self.some_int = some_int
        self.some_list_of_objects = some_list_of_objects
        self.some_circular_ref = some_circular_ref

    def __copy__(self):
        some_list_of_objects = copy.copy(self.some_list_of_objects)
        some_circular_ref = copy.copy(self.some_circular_ref)

        new = self.__class__(
            self.some_int, some_list_of_objects, some_circular_ref
        )
        new.__dict__.update(self.__dict__)

        return new

    def __deepcopy__(self, memo: Optional[Dict] = None):
        if memo is None:
            memo = {}

        some_list_of_objects = copy.deepcopy(self.some_list_of_objects, memo)
        some_circular_ref = copy.deepcopy(self.some_circular_ref, memo)

        new = self.__class__(
            self.some_int, some_list_of_objects, some_circular_ref
        )
        new.__dict__ = copy.deepcopy(self.__dict__, memo)

        return new


if __name__ == '__main__':
    list_of_objects = [1, {1, 2, 3}, [1, 2, 3]]
    circular_ref = SelfReferencingEntity()
    component = SomeComponent(23, list_of_objects, circular_ref)
    circular_ref.set_parent(component)

    print(f'component.list_of_objects = {component.some_list_of_objects}')
    shallow_copied_component = copy.copy(component)
    print('--- shallow copy ')
    shallow_copied_component.some_list_of_objects.append('another object')
    print("1) add 'another object' to shallow_copied_component.some_list_of_objects")
    print(f'> component.some_list_of_objects = {component.some_list_of_objects}')
    component.some_list_of_objects[1].add(4)
    print("2) add 4 to component.some_list_of_objects[1]")
    print(f'> shallow_copied_component.some_list_of_objects[1] = {shallow_copied_component.some_list_of_objects[1]}')

    deep_copied_component = copy.deepcopy(component)
    print('--- deep copy ')
    deep_copied_component.some_list_of_objects.append('one more object')
    print("1) add 'one more object' to deep_copied_component.some_list_of_objects")
    print(f'> component.some_list_of_objects = {component.some_list_of_objects}')
    component.some_list_of_objects[1].add(10)
    print("2) add 10 to component.some_list_of_objects[1]")
    print(f'> deep_copied_component.some_list_of_objects[1] = {deep_copied_component.some_list_of_objects[1]}')
    print(
        f"3) id(deep_copied_component.some_circular_ref.parent) "
        f"== id(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent) \n"
        f"> {id(deep_copied_component.some_circular_ref.parent) == id(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent)}"
    )
