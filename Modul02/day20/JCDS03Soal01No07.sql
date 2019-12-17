use sekolahku;

select courses.course, courses.mentor, courses.title, count(users.id) as jumlah_peserta from users inner join userCourse on users.id = userCourse.id_user inner join courses on courses.id = userCourse.id_course group by courses.id; 