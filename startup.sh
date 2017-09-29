# I got it!

# Instead of running CMD ["/usr/bin/supervisor"] I run CMD ["/root/startup.sh"] which contains:

# cd /home/django/ironman
python manage.py makemigrations --noinput
python manage.py collectstatic --noinput
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'pass')" | python manage.py shell 1>/dev/null 2>&1
/usr/bin/supervisord

#Now my database tables are created, admin user added and supervisord takes care of the rest.
#Since I export the pgsql port I can pgdump the content of the database and always restore my django app contents (app + db dump are on the host).

#It was a bit tricky to find a correct way of doing it but the only thing I have to do is 'docker-compose up' and be done with it :smile:

#Nice!
