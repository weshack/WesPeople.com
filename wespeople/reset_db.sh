./manage.py sqlclear map | ./manage.py dbshell
./manage.py syncdb
./manage.py loaddata fixtures/db.json
