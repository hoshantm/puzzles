include "globals.mzn";

% Zebra puzzle
int: nc = 5;

% Colors
int: red = 1;
int: green = 2;
int: ivory = 3;
int: yellow = 4;
int: blue = 5;
array[1..nc] of var 1..nc:color;
constraint alldifferent([color[i] | i in 1..nc]);

% Nationalities
int: eng = 1;
int: spa = 2;
int: ukr = 3;
int: nor = 4;
int: jap = 5;
array[1..nc] of var 1..nc:nationality;
constraint alldifferent([nationality[i] | i in 1..nc]);

% Pets
int: dog = 1;
int: snail = 2;
int: fox = 3;
int: horse = 4;
int: zebra = 5;
array[1..nc] of var 1..nc:pet;
constraint alldifferent([pet[i] | i in 1..nc]);

% Drinks
int: coffee = 1;
int: tea = 2;
int: milk = 3;
int: orange = 4;
int: water = 5;
array[1..nc] of var 1..nc:drink;
constraint alldifferent([drink[i] | i in 1..nc]);

% Smokes
int: oldgold = 1;
int: kools = 2;
int: chesterfields = 3;
int: luckystrike = 4;
int: parliaments = 5;
array[1..nc] of var 1..nc:smoke;
constraint alldifferent([smoke[i] | i in 1..nc]);

% The Englishman lives in the red house.
constraint forall ([nationality[i] == eng <-> color[i] == red | i in 1..nc]);

% The Spaniard owns the dog.
constraint forall ([nationality[i] == spa <-> pet[i] == dog | i in 1..nc]);

% Coffee is drunk in the green house.
constraint forall ([color[i] == green <-> drink[i] == coffee | i in 1..nc]);

% The Ukrainian drinks tea.
constraint forall ([nationality[i] == ukr <-> drink[i] == tea | i in 1..nc]);

% The green house is immediately to the right of the ivory house.
constraint forall ([color[i] == ivory -> if i<nc then color[i+1] == green else false endif | i in 1..nc]);

% The Old Gold smoker owns snails.
constraint forall ([smoke[i] == oldgold <-> pet[i] == snail | i in 1..nc]);

% Kools are smoked in the yellow house.
constraint forall ([smoke[i] == kools <-> color[i] == yellow | i in 1..nc]);

% Milk is drunk in the middle house.
constraint drink[3] == milk;

% The Norwegian lives in the first house.
constraint nationality[1] == nor;

% The man who smokes Chesterfields lives in the house next to the man with the fox.
constraint forall ([smoke[i] == chesterfields -> (if i>1 then pet[i-1] == fox else false endif \/ if i<nc then pet[i+1] == fox else false endif) | i in 1..nc]);

% Kools are smoked in the house next to the house where the horse is kept.
constraint forall ([smoke[i] == kools -> (if i>1 then pet[i-1] == horse else false endif \/ if i<nc then pet[i+1] == horse else false endif)| i in 1..nc]);

%The Lucky Strike smoker drinks orange juice.
constraint forall ([smoke[i] == luckystrike <-> drink[i] == orange | i in 1..nc]);

% The Japanese smokes Parliaments.
constraint forall ([nationality[i] == jap <-> smoke[i] == parliaments | i in 1..nc]);

% The Norwegian lives next to the blue house.
constraint forall ([color[i] == blue -> (if i > 1 then nationality[i-1] == nor else false endif \/ if i<nc then nationality[i+1] == nor else false endif) | i in 1..nc]);

solve satisfy;
