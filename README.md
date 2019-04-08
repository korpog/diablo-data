Basic analysis of a Diablo leaderboard. Data comes from US softcore Demon Hunter leaderboard for Season 16.

If you want to use this script for your own purposes you wil need to have a `credentials.json` file
in the project directory with the following content:
```json
{"CLIENT_ID": "YOUR_CLIENT_ID",
"CLIENT_SECRET": "YOUR_CLIENT_SECRET"}
```  
You can get it at https://develop.battle.net/  

***
Each record in the csv file contains:  
player's battletag, paragon level, rank, Greater Rift level, Rift time (in ms) and date the GR was completed on.


|    Correlation table        | Paragon       | Rank  |  GR level  | Time (ms)  |
| -------------|-------------  | ----- | ---------- | -----------|
| Paragon      |     1.00       | -0.58 |0.57        | -0.19      |
| Rank         |    -0.58       |  1.00 |-0.91       |  -0.02     |
| GR level     |     0.57       | -0.91 |1.00        | 0.17       |
|Time (ms)     |     -0.19      | -0.02 |0.17        |1.00        |


__Scatter plot__ showing relationships between rank and paragon level  
(it noticeable that higher paragon levels generally get higher rank)  
![alt text](https://github.com/korpog/diablo-data/blob/master/img/rank_paragon.png "Rank/paragon plot")

__Histograms__ showing distribution of paragon levels and Rift times (in milliseconds)  
(most players seem to be in the 1500-2000 paragon level range)
![alt text](https://github.com/korpog/diablo-data/blob/master/img/time_paragon_hist.png "Histograms")

Bar plot showing number of records per week (e.g. 5 is the first week of February)  
![alt text](https://github.com/korpog/diablo-data/blob/master/img/records_per_week.png "Records per week")
