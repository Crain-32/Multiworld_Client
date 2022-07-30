from typing import NewType, List, Dict, Union, AnyStr, Tuple

# This should be broken down more
ItemInfo = NewType('ItemInfo', List[Dict[str, Dict[str, Union[int | List[int]]]]])
EventInfo = NewType('EventInfo', Tuple[str, int, bool])
PlayerNames = NewType('PlayerNames', Dict[int, AnyStr])
