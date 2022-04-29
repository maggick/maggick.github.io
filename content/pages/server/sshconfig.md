Title: SSH config
Status: hidden

# SSH Config file

SSH Config file can be simply life a lot.
For that you just have to edit (or create) the file `~/.shh/config`.

There is many options you can combine
in order to have a very precise connection:

* HostName: the address to you host ssh server
* Port: the ssh port on your server
* User: the username for the connection
* IdentityFile: the ssh key you use to connect with the user on the server
* DynamicForward {port}: the port if you want to configure a proxy

For exemple :

    Host yourHost
        HostName yourHost.example.com
        Port 22300
        User fooey
        IdentityFile ~/.ssh/yourKey.key
        DynamicForward 1234

Then `ssh youHost` is equivalant to
`ssh yourHost.exemple.com -p 22300 -l fooey -i ~/.ssh.yourKey.key -D 1234`.

There is a lot of other options, just read the doc.

Source: [nerderati](https://nerderati.com/2011/03/17/simplify-your-life-with-an-ssh-config-file/)

