select courses.mentor, count(courses.course) as jumlah_peserta, count(courses.course) * 2000000 as total_fee 
from courses inner join userCourse on userCourse.id_course = courses.id 
inner join users on userCourse.id_user = users.id group by courses.mentor;