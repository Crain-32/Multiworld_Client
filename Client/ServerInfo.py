
# STOMP Exposed Endpoints
item_endpoint = "/item/{GameRoom}"
event_endpoint = "/event/{GameRoom}"
connect_endpoint = "/connect/{GameRoom}"  # This is NOT FOR THE CONNECT FRAME | Rather to set a Player as connected
coop_endpoint = "/coop/{GameRoom}"

# GameRoom Endpoints
create_game_room_endpoint = "/rest/gameroom"
add_player_endpoint = "/rest/gameroom/{GameRoom}"
check_player_endpoint = "/rest/gameroom/{GameRoom}/player"

# Admin Endpoints - useful for Local Servers, twwmultiplayer.com has it enabled behind authentication.

get_all_gamerooms_endpoint = "/rest/admin/gameroom"
delete_gameroom_endpoint = "/rest/admin/{GameRoom}" # HTTP DELETE
toggle_tournament_mode_endpoint = "/rest/admin/{GameRoom}" # HTTP PUT
get_all_connected_players_endpoint = "/rest/admin/total/players"
get_empty_gamerooms_endpoint = "/rest/admin/gameroom/empty"