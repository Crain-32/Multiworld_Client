from typing import NewType, List, Dict, Union

# This should be broken down more
ItemInfo = NewType('ItemInfo', List[Dict[str,  Dict[str, Union[int | List[int]]]]])
