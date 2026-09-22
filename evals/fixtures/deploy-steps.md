My manual deploy for our Django app (single VPS, ~2 deploys/week):

1. ssh into the box
2. `cd /srv/app && git pull`
3. copy `.env.production` from my laptop via scp (in case it changed)
4. `pip install -r requirements.txt`
5. `python manage.py migrate`
6. `python manage.py collectstatic --noinput`
7. run `python manage.py check --deploy` and read the output
8. take a manual DB dump to /backups (we also have nightly automated backups from the host)
9. restart gunicorn: `sudo systemctl restart gunicorn`
10. restart celery: `sudo systemctl restart celery` (we stopped using celery tasks in March, it just runs idle)
11. clear the redis cache with `redis-cli FLUSHALL` (not sure why, the previous dev always did it)
12. open the site in a browser and click around for a minute
13. post "deployed" in Slack #general
