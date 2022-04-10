from typing import NewType, List, Dict, Union

ItemInfo = NewType('ItemInfo', List[dict[str,  Dict[str, Union[int | List[int]]]]])
