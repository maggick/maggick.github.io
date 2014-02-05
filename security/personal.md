# Personal Security

This page resume most of the solution I use to keep my privacy on the internet.

## GPG

[GPG (GNU Privacy Guard)](http://www.gnupg.org/) is a cryptographic software.
It allows you to cypher texts or files with
[ublic-key cryptography](http://en.wikipedia.org/wiki/Public-key_cryptography).
Feel free to use my GPG [public Key](/publickey) to discuss about our new world
domination plan.

## KeePassX

[KeePassX](http://www.keepassx.org) is a password manager.
It is a database wherein we can put our logins and associated passwords, this
base is encrypted with
[AES](http://en.wikipedia.org/wiki/Advanced_Encryption_Standard) or
[Twofish](http://en.wikipedia.org/wiki/Twofish)
using 256 bit key and protected by password and optional "key file".
You can also generate your passwords with a lot of criteria.

## SSH / Openssh

I use [ssh](http://en.wikipedia.org/wiki/Secure_Shell) to get connected from my
computers to my servers from all over the world.
This service is really useful but when I consult my connexions logs I see a lot
of attempt over ssh using wrong login. That is why I choose to:
* authorize ssh connexion using public key authentication,
* change from the 22 standard port,
* let only a non root user login and this user only

## Openvpn

[Openvpn](http://en.wikipedia.org/wiki/Openvpn) aim to get create a virtual
private network. On of its use is to get anonymous on the internet by cyphering
your traffic between your computer and your server.

