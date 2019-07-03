Information flow reveals prediction limits in online social activity
====================================================================

James P. Bagrow, Xipei Liu, Lewis Mitchell<br>
Last modified: 2018-02-21

This README describes the data release for the above project. There are four
CSV files associated with project. We describe these data below




## The files:

### `twitter_data.csv` 

The text statistics, entropies and predictabilities for the $n = 927$
egos and their top-ranked alters. Fields:

1.  `ID1` - Hashed identifier for user 1 (ego)
2.  `ID2` - Hashed identifier for user 2 (alter)
3.  `H1` - Entropy of 1 (bits)
4.  `H2` - Entropy of 2 (bits)
5.  `Hx1G2` - Cross-entropy of 1 given 2 (bits)
6.  `Hx2G1` - Cross-entropy of 2 given 1 (bits)
7.  `N1m2` - Number of times 1 @-mentions 2
8.  `N2m1` - Number of times 2 @-mentions 1
9.  `R2b1` - Ranking of 2 by 1 (ie rank of mentions of 2 in 1's feed) (0 means no mentions)
10. `R1b2` - Ranking of 1 by 2 (ie rank of mentions of 1 in 2's feed) (0 means no mentions)
11. `N1` - Number of words from 1
12. `N2` - Number of words from 2
13. `Nuniq1` - Number of unique words from 1
14. `Nuniq2` - Number of unique words from 2
15. `Ntweets1` - Total number of tweets posted by 1
16. `Nfriends1` - Number of distinct individual's @-mentioned by 1
17. `Nmentions1` - Total number of @-mentions by 1
18. `Ntweets2` - Total number of tweets posted by 2
19. `Nfriends2` - Number of distinct individual's @-mentioned by 2 
20. `Nmentions2` - Total number of @-mentions by 2
21. `KL12` - KL-divergence
22. `KL21` - KL-divergence
23. `Pi1` - Predictability of 1
24. `Pi2` - Predictability of 2
25. `Pix1G2` - "Cross-predictability" of 1 given 2
26. `Pix2G1` - "Cross-predictability" of 2 given 1


### `cumulative_data_original.csv ` 

Cumulative entropy and predictability for ego-alter pairs. Fields:

1. `r` - rank of alter
2. `Hx` - cross-entropy ego from rank-r alter
3. `CHx` - cumulative cross-entropy of ego from rank-1 through rank-r alters
4. `CHxA` - cumulative cross-entropy of ego from rank-1:-r alters and ego
5. `PiEgoGalters` - Predictability of ego given alters 1:r
6. `PiEgoGaltersAndEgo` - Predictability of ego given alters 1:r and ego


### `cumulative_data_timeControl.csv` and `cumulative_data_socialControl.csv` 

As per `cumulative_data_origin.csv` but for the temporal and social controls.
respectively. Fields:

1. `r` - rank of this alter
2. `Hx` - Cross-entropy of ego given rank-r alter
3. `CHx` - Cumulative cross-entropy of ego given alters ranked 1:r
4. `Ne` - Number of words of ego
5. `Ve` - Number of unique words of ego
6. `Na` - Number of words of alter
7. `Va` - Number of unique words of alter
8. `PiEgoGalter` - Predictability of ego given rank-r alter
9. `PiEgoGalters` - Predictability of ego given alter ranked 1:r

