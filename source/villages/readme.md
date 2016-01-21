## Villages

This package contains the code for interacting with villages.

### Neutral actions

#### Recruit

#### Buy goods

#### Buy cattle

### Hostile actions

#### Take food

Takes 1 hour.
Gets each of the items in the town inventory with probability `p`.
Loses:
`r` relations with village, 
`rFac` with town faction, 
`rLord` with lord and 
`h` of honor:

    p = 0.3 + 0.03*looting

    r = 10
    rFac = 20
    rLord = 15
    h = 0

#### Steal cattle

Takes 3 hours.
Gets `c` of cattle.
Loses:
`r` relations with village, 
`rFac` with town faction, 
`rLord` with lord, and 
`h` of honor:

    c = min[2*looting + (1 + men_fit/10), total_cattle]

    r = 40
    rFac = 20
    rLord = 25
    h = 5

#### Force recruit

Like normal recruitment, but costs relations instead of gold.
Loses:
`r` relations with village, 
`h` of honor,
`m` of morale:

    r = 10
    h = 5
    m = 5

#### Make prisoners

Takes 3 hours.
Gets `p` prisoners and `g` of gold.
Loses: 
`r` relations with village,
`rLord` with the lord,
`rAll` with all places, and 
`h` of honor:

    p = min[U(0, 20) + 2*looting, capacity]
    g = p*[U(1, 10) + looting/2]

    r = 5*p - 2*p/persuasion
    h = 13
    rLord = -10
    rAll = 2

#### Loot

Takes 3 hours.
Gets [add how items are calculated], `g` of gold and `c` cattle.
Loses:
`r` relations with village,
`rFac` with town faction, 
`rLord` with lord:

    c = min[2*looting + (1 + men_fit/10), total_cattle]
    g = 50 + 5*prosperity

    r = U(25, 35)
    rFac = 20 + 20
    rLord = 15 + 25
    h = 5
