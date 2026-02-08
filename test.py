import database

database.delete_all_players()
database.add_player(6, "Shadow")
database.add_player(9, "Rouge")
database.show_all_players()
database.delete_player(6)
database.delete_player(9)
database.show_all_players