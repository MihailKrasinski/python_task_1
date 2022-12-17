schema = '''
create table if not exists rooms (
	id int primary key,
	name text
);
create table if not exists students (
	birthday timestamp,
	id int primary key,
	name text,
	room int,
	sex varchar(1),
	CONSTRAINT room_fk
		FOREIGN key(room)
			REFERENCES rooms(id)
);
'''

# 4 queries from task:
query_1 = 'select rooms.name, count(students.id) from rooms inner join students on rooms.id = students.room group by 1 order by 2 desc;'
query_2 = 'select rooms.name, avg(now() - students.birthday) from rooms inner join students on rooms.id = students.room group by 1 order by 2 asc limit 5;'
query_3 = 'select rooms.name, max(students.birthday) - min(students.birthday) from rooms inner join students on rooms.id = students.room group by 1 order by 2 desc limit 5;'
query_4 = 'select rooms.name, count(distinct(students.sex)) from rooms inner join students on rooms.id = students.room group by 1 having count(distinct(students.sex)) = 2 order by 1 asc;'