use world;

select name as nama, continent as benua, lifeexpectancy as AngkaHarapanHidup,
gnp from country
where continent = 'Asia' and lifeexpectancy > (select avg(lifeexpectancy) from country where continent = 'Europe') 
order by angkaharapanhidup desc;