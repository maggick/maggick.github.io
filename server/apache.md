# Apache
The recent update (August 2013) to apache 2.4.6 broke some permissions
and my pages accessible by Alias where Forbidden.
I had to add:

    <Directory "/myfile/">
    Options All
    AllowOverride All
    Require all granted
    </Directory>

in the config of /etc/apach2/site-avaible

[source](http://dabase.com/blog/AH01630:_client_denied_by_server_configuration/)
