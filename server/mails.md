#Mail

When I start to install my own mail server to never be dependent of a service
as Gmail, hotmail or whatever.
I choose postifix as SMTP server.

##SPF

Sender Policy Framework (SPF) is an email validation system designed to prevent
email spam by detecting email spoofing, a common vulnerability, by verifying 
sender IP addresses.

It is really easy to put an SPF in place.
You just have to add a DNS TXT entry :

    yourdomain.com. IN TXT "v=spf1 a mx ~all"

Source: [nickwilsdon](http://nickwilsdon.com/spf-domain-records/)

##DKIM

DomainKeys Identified Mail (DKIM) is a method for associating a domain name to
an email message.

###Install

First of all you need to install your DKIM solution, I use opendkim and debian:

    aptitude install opendkim opendkim-tools

###Keys generation

We should choose the directory were to put the keys, we choose
`/etc/opendkim/yourdomain/` (create the directory).
Then we need to create the private and the public rsa keys for singing:

    opendkim-genkey -b 2048 -r -d yourdomain.tld

the `-b 2048` define the longer of the key, here 2048 bits, the `-r` is for
restrict the key for use in e-mail signing only and the `-t yourdomain.tld` is
for a comment in the TXT record file.

###Configuration

Now we need to edit the configuration files:

1.  /etc/opendkim.conf – OpenDKIM’s main configuration file
1.  /etc/opendkim/KeyTable – a list of keys available for signing
1.  /etc/opendkim/SigningTable - a list of domains and accounts allowed to sign
1.  /etc/opendkim/TrustedHosts – a list of servers to “trust” when signing or
verifying

(You may have to create folders and files).

####/etc/opendkim.conf

You may have to uncomment some lines:

    Umask         002
    UserID        opendkim:opendkim
    Socket        inet:8891@localhost
    Domain        yourdomain.tld

Next, add the following line to the configuration in order to give the location of the
other configuration to opendkim:

    Selector                deflaut
    KeyTable                refile:/etc/opendkim/KeyTable
    SigningTable            refile:/etc/opendkim/SigningTable
    ExternalIgnoreList      refile:/etc/opendkim/TrustedHosts
    InternalHosts           refile:/etc/opendkim/TrustedHosts

####/etc/opendkim/KeyTable

This file contains the path to your DKIM keys (one per line) , here we have only
one key so our file is just one line:

    yourdomain.tld yourdomain.tld:default:/etc/opendkim/yourdomain/default.private


####/etc/opendkim/SigningTable

This file tells to opendkim how to use the keys, here we want every mails
send from our domain to be signed:

    *@yourdomain.tld yourdomain.tld

####/etc/opendkim/TrustedHosts

This file tells OpenDKIM who to let use your keys:

    127.0.0.1
    yourdomain.tld
    mail.yourdomain.tld

###DNS record

The DNS record is the last part of this operation. You need to do it properbly
otherwise your signature would be false and unreconized by the mailing servers.
you should have a filed who describe the way you handle your DKIM:

    _domainkey                IN TXT    "o=-;"

And an other where you put your public key:

    default._domainkey        IN TXT    ( "k=rsa;
    p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAz33vJpYC9pgwtm4JyRWLLDM5LLIn66IhgMODhW1PX7zk1eMuCdp8509sUmpk47RDbJq2VhFDGElC/9zkCMo6hrep241fVnwmOfuxA5Nvcu8YxbAvXacwusU9ct4r9Re2NjO9kshbIWBAVJ66CxBzWWsi6+ikChHbv7GsF2jbx+VG1rwbShr8AD5FbFGIh5CEVs83E"
    "qJ6g8Nla+BX2A2V2gwOxT2Xp0mCIqjIFqfoyhxIcftKHHBDFxiun2WLwsUD5ivFewy54ntgphkWJUXfob+NtZ6M8sv531Zd/mgdBgnYAPzWNy5m5MGquNZNEnA44o0sAcKiCRMb7nKpTvfDQQIDAQAB"
    )

Source: [stevejenkins](http://stevejenkins.com/blog/2011/08/installing-opendkim-rpm-via-yum-with-postfix-or-sendmail-for-rhel-centos-fedora/)    
[A DomainKey Policy Record
Tester](http://domainkeys.sourceforge.net/policycheck.html)    
[A DomainKey Selector Record
Tester](http://domainkeys.sourceforge.net/selectorcheck.html)

##Catch all

Is is really interesting to catch all e-mails directed to your domain. For
instance you will catch wahtever@yourdomain.com.
To define a catch all create the `virtual` file and add it to postmap :

    # echo '@yourdomain.com emailusername' > /etc/postfix/virtual
    # postmap /etc/postfix/virtual

Check that the virtual map is defined in postfix's configuration 
by verifing that the following line is in the `/etc/postfix/main.cf` file.

    # postmap /etc/postfix/virtual

and restart the postfix service :

    # service postfix reload

Source: [cyberciti](http://www.cyberciti.biz/faq/howto-setup-postfix-catch-all-email-accounts/)


### Trouble

In odrder that the existing users can get their e-mails when
there is a cath all :

edit the virtual_map in `/etc/postfix/virtual` and add the following line :

    user@domain.tld user

next execute the following commands:

    postmap /etc/postfix/virtual
    service postfix restart

### Catch all with regex :

You can configure some regex catch all for instance you can catch
whatever.youruser@yourdomain.com
In order to make a catch all for an user :
edit (or create) the file 

    /etc/postfix/virtual-regexp

add regexp:/etc/postfix/virtual-regexp to virtual_maps in /etc/postfix/main.cf
this will look like 

    virtual_maps = hash:/etc/postfix/virtual, regexp:/etc/postfix/virtual-regexp

add the line:

    /^.*user@domnain.tld/ user

The user will receive all mail in the form *.user@domain.tld (where * is the
classic Unix joker)

