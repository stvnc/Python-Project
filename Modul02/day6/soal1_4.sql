use world;

select * from country;
select country.continent Benua, count(country.Name) Jumlah_Negara, 
sum(country.Population) Populasi, avg(country.LifeExpectancy) Rata_AngkaHrpnHdp
from country group by country.continent having count(country.Name) > 10 order by Populasi desc;