# Horde

Horde is a all in one webmail, managing e-mails, calendars, contacts, notes and
todo lists.

Horde is written in PHP and is accessible using Pear (PHP Extension and
Application Repository).

## Installing Horde

### Necessary packages

First of all some dependencies should be meet. Considering you are on Debian
and using `apt-get` you may run the following command:

apt-get install php5-sasl php5-intl libssh2-php php5-curl php-http php5-xmlrpc
php5-geoip php5-ldap php5-memcache php5-memcached php5-tidy

### Pear install

We want to use Pear to get the last version of Horde. So we add the channel, the
Horde role, and we install Horde.
You will be prompt with the question `Filesystem installation for base Horde
application: /var/www/horde` you can change this location the only
constrain to configure your web server (Apache, Nginx, or whatever) in order to
make this folder accessible.

pear channel-discover pear.horde.org
pear install horde/horde_role
pear run-scripts horde/horde_role
pear install -a -B horde/webmail 

### Database creation

Horde use a database to store your Calendars, contact, task lists and
notes. Nevertheless the script does not create this database. Therefore we must
do it manually for instance with the following commands and a MySQL database:

mysql -u root -p
CREATE DATABASE horde;
*GRANT ALL ON horde.* TO horde@localhost IDENTIFIED BY 'PASSWORD';
FLUSH PRIVILEGES;
exit;

You'll be asked the following questions:

What database backend should we use? *mysql*

Request persistent connections? *no*

Username to connect to the database as: *The username you set in the previous
step*

Password to connect with: *The password you set in the previous step*

How should we connect to the database? *unix*

Location of UNIX socket: *Just press [enter]*

Database name to use: *The database name you set in the previous step*

Internally used charset: *utf-8*

Use SSL to connect to the server: *no*

Certification Authority to use for SSL connection: *Just press [enter]*

Split reads to a different server? *false*

Filesystem installation for base Horde application: */var/www/horde*

Specify an existing mail user who you want to give administrator permissions
(optional): *user@domain.com* This user will have access to the administration
interface within horde.

This is all an you should get access to the horde interface.

## Activating the exchange server

The administrator user will have a lot of options one of them is the activation
of the exchange server.

[source](http://www.howtoforge.com/install-horde-5-webmail-for-ispconfig-on-debian-wheezy)
