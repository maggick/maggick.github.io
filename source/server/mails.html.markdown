---
title: Mail
---

#Mail

When I start to install my own mail server to never be dependent of a service
as Gmail, hotmail or whatever.
I choose postifix as SMTP server.

##SPF

Sender Policy Framework (SPF) is an email validation system designed to prevent
email spam by detecting email spoofing, a common vulnerability, by verifying 
sender IP addresses.

It is realy easy to put an SPF in place.
You just have to add a DNS TXT entry :

    yourdomain.com. IN TXT "v=spf1 a mx ~all"

[Source](http://nickwilsdon.com/spf-domain-records/)

##Catch all

to define a catch all create the `virtual` file and add it to postmap :

    # echo '@yourdomain.com emailusername' > /etc/postfix/virtual
    # postmap /etc/postfix/virtual
    
Check that the virtual map is defined in postfix's configuration 
by verifing that the following line is in the `/etc/postfix/main.cf` file.

    # postmap /etc/postfix/virtual
    
and restart the postfix service :

    # service postfix reload
    
[Source](http://www.cyberciti.biz/faq/howto-setup-postfix-catch-all-email-accounts/)
    

### Trouble

in odrder that the existing user can get their mail when
there is a cath all :

edit the virtual_map in `/etc/postfix/virtual` and add the following line :

    user@domain.tld user

next execute the following commands:

    postmap /etc/postfix/virtual 
    postfix restart

### Catch all with regex :

in order to make a catch all for an user :
edit (or create) the file 

    /etc/postfix/virtual-regexp

add regexp:/etc/postfix/virtual-regexp to virtual_maps in /etc/postfix/main.cf
this will look like 

    virtual_maps = hash:/etc/postfix/virtual, regexp:/etc/postfix/virtual-regexp

add the line:
 
    /^.*user@domnain.tld/ user

The user will receive all mail in the form *.user@domain.tld (where * is the classis Unix joker)

