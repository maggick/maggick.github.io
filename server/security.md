# Security

On a server security is really important.
Some simple change can make a great gain in security.


## ssh

I choose an other port than 22 for my ssh server.
Moreover I just let one user log in with his sshkey.

And finaly I have improve the security of my ssh private key file by changing
the encryption of the passphrase to
[PKCS#8](http://en.wikipedia.org/wiki/PKCS#8) following [this
article](http://martin.kleppmann.com/2013/05/24/improving-security-of-ssh-private-keys.html)
in resume there is a few manipulation:

    mv ~/.ssh/id_rsa ~/.ssh/id_rsa.old
    openssl pkcs8 -topk8 -v2 des3 -in ~/.ssh/id_rsa.old -out ~/.ssh/id_rsa
    chmod 600 ~/.ssh/id_rsa
    # Check that the converted key works; if yes, delete the old one:
    rm ~/.ssh/id_rsa.old

## Ip Tables - Firewall

It is important to filtre what come in and come out of a server.

[source](http://www.alsacreations.com/tuto/lire/622-Securite-firewall-iptables.html)

