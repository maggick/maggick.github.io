# IRC

Internet Chat Relay, is a protocol for live interactive Internet text messaging (chat).
It necessitate a client.

## weechat

Personally I use [weechat](http://www.weechat.org/) and here some notes about
it:

### Connect to an SSL server without checking certificat

There is a wonderful doc but I never remember how to connect on a server who
as an non standard port and with ssl and with a non-valid certificate :

    /connect my_server.expl/port -ssl -password=foo

and then on the server buffer :

    /set irc.server.my_server.expl.ssl_verify off

### Configuration

wee-chat is highly configurable.

For instance you can choose the maximum length of the nickname (the right one)
in order to reduce the very long nickname:

    /set weechat.look.prefix_align_max 12

One other cool thing: after an upgrade you can just type the `/upgrade` command
in order to upgrade without restarting weechat.

You can found my whole config file for weechat on my
[github dotfiles](https://github.com/maggick/dotfiles)

## Bitlbee

[BitlBee](http://bitlbee.org) brings IM (instant messaging) to IRC clients.
It's a great solution for people who have an IRC client running all the time and don't want to run
an additional MSN/AIM/whatever client.

### Install

In order to install BitlBee (from source, the package are outdated and for pussy)
go on the [download page](http://www.bitlbee.org/main.php/download.html) and take the last tarball.
`wget` should be great. Then untar it with `tar -xvf` and go on the directory.
Now make a `./configure` to see if you have all dependency (the main dependence is with libg,
the debian package for that is `libglib2.0-dev`). The `make`.
Now you should be able to run it with  `./bitlbee` (don't hesitate to make `./bitlbee -h` and read `./doc/README`
to see more information) or more probably with `./bitlbee -F -p 6679`.
Then you just have to connect with your favorite irc client with `/connect localhost/6667` (6667 is the default port
for irc and so for BitlBee who is just an other irc server) or `/connect
localhost/6679`.

Then you should go on the beautiful [wiki of BitlBee](http://wiki.bitlbee.org) to learn
more about how to connect to Twitter, gtalk, facebook and whatever.
