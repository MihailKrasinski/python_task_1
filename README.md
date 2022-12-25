You need to create yours db and configure it + save credentials to .env file in project repository.

RENAME way to rooms.json and students.json ('students', '/home/mikra/MikraPythonProjects/python_task_1/data/in/students.json') in call json_to_sql method("main.py" file and "test.py")

P.S.
Logger shows only that DB already filled and data already exists.
To successfully (re)create db and see empty log after run script you need to drop database or tables.

WARNING::: NEED TO RUN TESTS('test.py') ONLY AFTER COMPLETING PUT DATA TO DATABASE and IF YOU ALREADY COMPLETED PUT => YOU NEED TO DROP DATABASE TO RUN SCRIPT('main.py') AGAIN
