# Contact and calandar

## Install

I wish to see Google out of my life.
The requirement was being able to have my calendar and my contacts on my own
server. Moreover I need some sharing between the calendar's user
(to share a common calendar and see an other user one).
I needed to have an access to this contacts and calandars from a web interface
and from my android device.

## Back-end

That is why I install davical as back-end
see [the official website] (http://wiki.davical.org) (debian users: note that
davical is available in the jessie or wheezy repository).

## Front-end

In front-end on my server:
* for the contacts: Roundcube with a [carddav plugin](http://www.crash-override.net/carddav.html)
* for the calendar: [agenddav](http://agendav.org/)

In front end on android:
* for the contacts: [carddav (free)](https://play.google.com/store/apps/details?id=org.dmfs.carddav.sync)
* for the calendar: [caldav sync (2€)](https://play.google.com/store/apps/details?id=org.dmfs.caldav.lib)
* for the birthdays: [birthday calendar * adapter](https://play.google.com/store/apps/details?id=org.birthdayadapter)(yeah it is a bonus !)

I am very happy with all of them

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

## Usage

### Agendav

If message "The action you have requested is not allowed." when you try to login,
this is due to the variable "cookie_secure" pass it to 'False' and log again.
Edit the file `agendav/web/config/config.php` (~ligne 81).

    $config['cookie_secure']        = FALSE;

