## TODO
Rewarding:
- Avant virage, extérieur ++
- Dans le virage, intérieur ++
- Après virage, extérieur ++

Gradient de rewarding inter-exter / exter-inter

Plus le virage est sérré plus il faut être à l'intérieur

## HOW

Get distance from edges ✔️

Waypoints:
  waypoints[closest_waypoints[1]]
  waypoints[closest_waypoints[0]]

Calcul de direction:
  track_direction = math.atan2(waypoints[n][1] - waypoints[n+1][1], waypoints[n][0] - waypoints[n+1][0])

Calcul des 5 directions suivantes et précédentes

Si la variation des directions est importante, virage

Avant virage = virage dans les directions suivantes
Dans le virage = ?
Après virage = virage dans les directions précédentes

Definir "Dans le virage":
  Test multi-Waypoints
    - plus ou moins de distance entre les waypoints
    - check sur Deep Racer
    - plus ou moins de directions calculées
