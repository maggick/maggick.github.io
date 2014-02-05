# Contact and calandar

## Install

I wish to see Google out of my life.
The requirement was being able to have my calendar and my contacts on my server.
Moreover I need some sharing between the calendar's user
(to share a common calendar and see an other user one)

That is why I install davical as backup end
see [the official website] (http://wiki.davical.org) (note that davical is available in the 
jessie or wheezy repository)

In front end on my server, I choose :
* for the contacts : Roundcube with a [carddav plugin](http://www.crash-override.net/carddav.html)
* for the calendar : [agenddav](http://agendav.org/)
I am very happy with all of them

In front end on android, I choose :
* for the contacts : [carddav (free)](https://play.google.com/store/apps/details?id=org.dmfs.carddav.sync)
* for the calendar : [caldav sync (2€)](https://play.google.com/store/apps/details?id=org.dmfs.caldav.lib)

I tried an other [caldav app (free)](https://play.google.com/store/apps/details?id=org.dmfs.caldav.lib)
but I was not fully satisfied.
In fact, there is no two way synchronization (yet on July 2013) and the color of my calendar were not synchronized.


## Backup

In order to make a backup of all my data (ie. all the user, calendar and address books)
I use a cron job witch would use postgres dump to dump the davical database.

I use the [official instructions](http://wiki.davical.org/w/Backups)
and a full backup fill my needs

as postgres user :
pg_dump -Fc davical >davical.pgdump

then my user will backup the data on my NAS with a simple scp

This is not fully working now, work in progress...

## Usage

### Agendav

If message "The action you have requested is not allowed." when you try to login,
this is due to the variable "cookie_secure" pass it to 'False' and log again.
Edit the file `agendav/web/config/config.php` (~ligne 81).


    $config['cookie_secure']        = FALSE;

