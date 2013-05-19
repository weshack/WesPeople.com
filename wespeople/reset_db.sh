./manage.py sqlclear maps | ./manage.py dbshell
./manage.py syncdb
pip install -r ../REQUIREMENTS.txt
#./manage.py loaddata fixtures/db.json
psql wespeople < fixtures/dbdump.sql
