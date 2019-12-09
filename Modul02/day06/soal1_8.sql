use world;
select country.name as Negara_G20, country.population as Populasi_Negara, GNP, city.name as Ibukota, city.population as Populasi_Ibukota 
from country inner join city on country.capital = city.id
where country.name in ('Argentina', 'Australia', 'Brazil', 'Canada', 'China', 'France', 'Germany'
, 'India', 'Indonesia', 'Italia', 'Japan', 'Mexico'
, 'Russian Federation', 'Saudi Arabia', 'South Africa', 'South Korea'
, 'Turkey', 'United Kingdom', 'United States') order by country.name;