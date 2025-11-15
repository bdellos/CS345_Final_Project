## Data Loaders

**Ready features:**

| Feature                                                     | Index | Feature name     |
|-------------------------------------------------------------|-------|------------------|
| **TARGET** - was shot a goal?                               | 15    | goal             |
| ShotID                                                      | 0     | shotID           | 
| Playoff game                                                | 4     | isPlayoffGame    |
| Time into game (in seconds)                                 | 8     | time             |
| Home team score                                             | 21    | homeTeamGoals    |
| Away team score                                             | 22    | awayTeamGoals    |
| Shot angle                                                  | 27    | shotAngle        |
| Shot distance                                               | 31    | shotDistance     |
| Empty net                                                   | 33    | shotOnEmptyNet   |
| Rebound                                                     | 34    | shotRebound      |
| Rush                                                        | 36    | shotRush         |
| Shooter style (L/R) -- may not be needed with OffWing [106] | 63    | shooterLeftRight |
| Shooter TOI                                                 | 64    | shooterTimeOnIce |
| Off wing (shot from dominant side?)                         | 106   | offWing          | 

  
**Features found/discussed that need more work**  

| Feature                                   | Comments                                                                                                                                 |
|-------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Shot type [32]                            | Need to implement one-hot encoding.                                                                                                      |
| Shooter position [53]                     | Need to either implement one-hot encoding if we want to have LW/RW/C/D or could just use boolean values if we only want forward/defense. |
| Score of game when shot taken             | Home team score [21] and away team score [22] to be used with shooter's team [14].                                                       |
| Power play                                | Home skaters on ice [47] away skaters on ice [48] with shooter team [14]                                                                 |
| Time between shots                        | Maybe time since last event [11]? Would need to figure out if last event was a shot by home or away team.                                |
| Time difference between team line changes | 112? "The shooting team's average time on ice since a faceoff minus the defending team's average time on ice since a faceoff"            |

## Models

## Main
