create database if not exists sekolahku;
use sekolahku;
create table if not exists users (id int(11) not null auto_increment primary key, username varchar(50) not null, email varchar(50) not null, password varchar(50) not null, created_at timestamp default current_timestamp, updated_at timestamp default current_timestamp on update current_timestamp);
create table if not exists courses(id int(11) auto_increment primary key, course varchar(50) not null, mentor varchar(50) not null, title varchar(50) not null);
create table if not exists userCourse(id_user int(11), id_course int(11));

insert into users (username, email, password) values 
('Andi', 'andi@andi.com', 12345),
('Budi', 'budi@budi.com', 67890), 
('Caca', 'caca@caca.com', 'abcde'), 
('Deni', 'deni@deni.com', 'fghij'),
('Euis', 'euis@euis.com', 'klmno'), 
('Fafa', 'fafa@fafa.com', 'pqrst');


