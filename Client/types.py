from typing import NewType, List, Dict, Union, AnyStr

# This should be broken down more
ItemInfo = NewType('ItemInfo', List[Dict[str,  Dict[str, Union[int | List[int]]]]])

PlayerNames = NewType('PlayerNames', Dict[int, AnyStr])
