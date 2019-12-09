use world;
select Code as code, Name as name, Continent as continent, Region as region, IndepYear as tahun_merdeka from country where Indepyear is not null order by IndepYear limit 10;