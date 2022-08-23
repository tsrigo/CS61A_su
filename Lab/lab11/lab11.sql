.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet from students where color == 'blue' and pet == 'dog';

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song from students where color == 'blue' and pet == 'dog';


CREATE TABLE smallest_int_having AS
  select time, smallest from students group by smallest having count(*) == 1;


CREATE TABLE matchmaker AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";

