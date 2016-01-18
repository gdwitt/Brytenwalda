## Economy

### Villages

Farmers transport goods from villages to towns. They trade resources in the
village in the town.

When a farmer party dies, with time it is replaced by another.

Each time there is a successful drop, town's prices change, the village has
a probability to have its prosperity increased, and the town food stocks increase
(not the food goods, a hidden variable used for sieges).

The dynamics contains two simple triggers:

- `Spawn village farmer parties`
- `Troop AI: Village Farmer`

and one script:

- `script_create_village_farmer_party`

that are inside this package.
