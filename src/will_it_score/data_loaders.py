"""
File to be used for data imports. Should keep our code
cleaner this way.
"""

"""
=== keep features at these indices ===
0 shotID
4 playoff game
8 time of game (in seconds)
15 was shot a goal (could use 14? tells if SOG/goal/miss)
21 home team score
22 away team score
27 shot angle
31 shot distance
32 shot type
33 empty net
34 rebound status
36 rush
53 shooter position
63 shooter style L/R (may not need with 106)
64 shooter TOI
106 off wing - basically, was shot from shooter's dominant side

=== features we considered and need to do more work to get ===
score of game when shot taken
    home team score [21] and away team score [22] with team [14]
power play
    will probably have to use home skaters on ice [47] and away on ice [48] with
    team [14]
time between shots
    maybe time since last event [11]? would need to figure out if we could determine
    if the last event was a shot taken by the same team or different team
time difference since line change
    no idea
"""