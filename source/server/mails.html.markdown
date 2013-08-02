#Mail

When I start to install my mail server
I choose postifix.

##SPF

http://nickwilsdon.com/spf-domain-records/

##Catch all

http://www.cyberciti.biz/faq/howto-setup-postfix-catch-all-email-accounts/
pour que les utilisateurs existant recoivent leurs mail mettre
in odrder that the existing user can get their mail when
there is a cath all :

edit the virtual_map in /etc/postfix/virtual and add the following line :

    user@domain.tld user

next execute the following commands:

    postmap /etc/postfix/virtual 
    postfix restart

## Catch all with regex :

in order to make a catch all for an user :
edit (or create) the file 

    /etc/postfix/virtual-regexp

add regexp:/etc/postfix/virtual-regexp to virtual_maps in /etc/postfix/main.cf
this will look like 

    virtual_maps = hash:/etc/postfix/virtual, regexp:/etc/postfix/virtual-regexp

add the line:
 
    /^.*user@domnain.tld/ user

The user will receive all mail in the form *.user@domain.tld (where * is the classis Unix joker)
