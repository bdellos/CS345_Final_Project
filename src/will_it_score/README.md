## Data Loaders

**Ready features:**

| Feature                                                     | Index |  
|-------------------------------------------------------------|-------|
| ShotID                                                      | 0     |
| Playoff game                                                | 4     |
| Time into game (in seconds)                                 | 8     |
| Was shot a goal?                                            | 15    |
| Home team score                                             | 21    |
| Away team score                                             | 22    |
| Shot angle                                                  | 27    |
| Shot distance                                               | 31    |
| Empty net                                                   | 33    |
| Rebound                                                     | 34    |
| Rush                                                        | 36    |
| Shooter style (L/R) -- may not be needed with OffWing [106] | 63    |
| Shooter TOI                                                 | 64    |
| Off wing (shot from dominant side?)                         | 106   |  

  
**Features found/discussed that need more work**  

| Feature                                   | Comments                                                                                                                                 |
|-------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Shot type [32]                            | Need to implement one-hot encoding.                                                                                                      |
| Shooter position [53]                     | Need to either implement one-hot encoding if we want to have LW/RW/C/D or could just use boolean values if we only want forward/defense. |
| Score of game when shot taken             | Home team score [21] and away team score [22] to be used with shooter's team [14].                                                       |
| Power play                                | Home skaters on ice [47] away skaters on ice [48] with shooter team [14]                                                                 |
| Time between shots                        | Maybe time since last event [11]? Would need to figure out if last event was a shot by home or away team.                                |
| Time difference between team line changes | No idea.                                                                                                                                 |

## Models

## Main
