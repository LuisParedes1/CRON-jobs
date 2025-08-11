# CRON jobs

Cron Jobs allow you to start a service based on a crontab expression.

# CRON Jobs on Railway

* We deploy our task which performs its operation and exits. It does not keep any long running threads or open connections.
* The CRON job will run this task every 5 minutes (`*/5 * * * *`) and log the timestamp on stdout