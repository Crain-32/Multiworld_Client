## Read Me ##

Welcome to the Client implementation for the Wind Waker Multiworld project! 
Please understand that the project is still under development. At times one aspect
may seem more refined than others, and that is to be expected.

### Set Up ###
1. Download the Source Code.
2. Open up your preferred shell and install the dependencies `pip install -r requirements.txt`
3. Click `main.py`

*Optional - You can enter a Testing Menu by running `main.py` with any extra arguments.*

### FAQ ###
- Yes, nothing works! Welcome to the early stages of development.
- Make sure you have Dolphin running before using the Testing Menu.
- I'm using Python 3.10
- I have no idea if this can support Mac/Linux yet.

### Current Plans ###
- Get STOMP to actually work.
- More dialog in the Dialog Box.
- Buttons/Label swap based on connection type (Set Up Room vs Connect to Room)
- STOMP/DME integration (Likely some sort of Pub/Sub method, needs testing first)

### Known Problems ###
- Not all items can be given, this is expected behavior for now.
- Server refused the connection, this is currently being looked at.