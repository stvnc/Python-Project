use sekolahku;

select users.id, users.username, courses.course, courses.mentor, courses.title from userCourse inner join users on userCourse.id_user = users.id inner join courses on userCourse.id_course = courses.id;
