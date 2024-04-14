# Postmortem

Upon the release of ALX's Web stack debugging #3 project, approximately 03:00 (GMT),
An outage occurred on an isolated Ubuntu container running an Apache web server.
GET requests on the server led to `500 Internal Server Error`.

## Debugging Process

1. Checked running processes using `ps -ef | grep apache`.
Two `apache2` processes - `root` and `www-data` - were running.

2. In one terminal, ran `strace -p PID` using the `root` process PID.
In another, ran `curl -sI 127.0.0.1`.
`strace` gave no useful information.

3. Repeated step 2, using the `www-data` process PID.
`strace` raise an `-1 ENOENT (No such file or directory)` error upon accessing the file
`/var/www/html/wp-includes/class-wp-locale.phpp`.

4. Located line 137 in `wp-settings.php` file.
`require_once( ABSPATH . WPINC . '/class-wp-locale.phpp' );`.

5. Removed the trailing `p` from the line.

6. Ran `curl -sI 127.0.0.1` again, got `HTTP/1.1 200 OK` this time.

## Summation

In short, a typo. In full, the WordPress app was encountering an error
while tyring to access the file `class-wp-locale.phpp`.
The correct file name was `class-wp-locale.php`.
Patch involved fixing the typo, by removing the trailing `p`.

## Prevention

This outage was not a web server error, but an application error. To prevent such outages
moving forward, please keep the following in mind.

* Testing the application before deployment. This error could have been addressed earlier.

* Status monitoring. using uptime-monitoring service.
