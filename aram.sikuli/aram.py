# Open League Client
lolClient = App(r'"C:\Riot Games\League of Legends\LeagueClient.exe"')
lolClient.open()
wait('logo.png', FOREVER)

# Click Play
lol_logo = Pattern('logo.png')
play_button = lol_logo.targetOffset(100, 0)
click(play_button)

# Select ARAM
wait('aram.png', 5000)
aram = Pattern('aram.png')
click(aram)

# Confirm Selection
confirm = Pattern('confirm.png')
confirm_button = confirm.targetOffset(50, 0)
click(confirm_button)

# Find Match
find_match = Pattern('find_match.png')
find_match_button = find_match.targetOffset(50, 0)
click(find_match_button)

# Accept Match
match_found = Pattern('match_found.png')
accept_button = match_found.targetOffset(0, 100)
decline_button = match_found.targetOffset(0, 130)
wait('match_found.png', FOREVER)
click(accept_button)
