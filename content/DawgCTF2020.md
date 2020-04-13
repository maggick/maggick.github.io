
# Crypto
## Take It Back Now, Y'all (25)


    # -*- coding: utf-8 -*-
    """
    Created for Spring 2020 CTF
    Cryptography 0
    10 Points
    Welcome to my sanity check.  You'll find this to be fairly easy.
    The oracle is found at umbccd.io:13370, and your methods are:
        flg - returns the flag
        tst - returns the message after the : in "tst:..."

We connect using telnet and call the `flg` method.

    :::text
    telnet crypto.ctf.umbccd.io 13370
    Trying 3.81.180.84...
    Connected to crypto.ctf.umbccd.io.
    Escape character is '^]'.
    flg
    DawgCTF{H3ll0_W0rld!}Connection closed by foreign host.

## One Hop This Time, One Hop This Time (75)


    :::python
    # -*- coding: utf-8 -*-
    """
    Created for Spring 2020 CTF
    Cryptography 1
    40 Points
    Welcome to the one time pad oracle!
    Our oracle's function is enc := key ^ msg | dec := key ^ ct
    The oracle is found at umbccd.io:13371, and your methods are:
        flg - returns the encrypted flag
        enc - returns the encryption of the message after the : in "enc:..."
        dec - returns the decryption of the ciphertext after the : in "dec:..."

    @author: pleoxconfusa
    """

We open a socket, grab the encrypted flag and decrypt it.

    :::python
    import socket

    s = socket.socket()

    port = 13371
    host = 'crypto.ctf.umbccd.io'

    # connect to the server on local computer
    s.connect((host, port))

    s.send(b'flg')
    flag=(s.recv(1024))
    print(flag)
    s.send(b'dec:'+flag)
    print(s.recv(1024))
    s.close()

## Right Foot Two Stomps (200)


    :::python
    # -*- coding: utf-8 -*-
    """
    Created for Spring 2020 CTF
    Cryptography 2
    100 Points
    Welcome to the AES-CBC oracle!
    Our oracle's function is AES-CBC.
    The oracle is found at umbccd.io:13372, and your methods are:
        flg - returns the encrypted flag
        enc - returns the encryption of the message after the : in "enc:..."
              as 16 bytes of initialization vector followed by the ciphertext.
        dec - returns the decryption of the ciphertext after the : in "dec:<16 bytes iv>..."
              as a bytes string.

We open a socket, grab the encrypted flag, send some data to get the IV, and
send back the flag with the IV to decrypt it.

    :::python
    import socket

    s = socket.socket()

    port = 13372
    host = 'crypto.ctf.umbccd.io'

    s.connect((host, port))

    s.send(b'flg')
    flag=(s.recv(1024))
    #print(flag)
    s.send(b'enc:test')
    r=(s.recv(1024))
    #print(r)
    iv=r[0:16]
    #print(iv)
    s.send(b'dec:'+iv+flag)
    r=(s.recv(1024))
    print(r)
    s.close()

`b"\xd6z\xbd\xfb\x9a\x82\xb91\xa5\x12\n['\xfb\x92\xb5DawgCTF{!_Th0ugh7_Th3_C!ph3rt3x7_W@s_Sh0rt3r.}"`

## Left Foot Two Stomps (250)

>n=960242069 e=347 c=346046109,295161774,616062960,790750242,259677897,945606673,321883599,625021022,731220302,556994500,118512782,843462311,321883599,202294479,725148418,725148418,636253020,70699533,475241234,530533280,860892522,530533280,657690757,110489031,271790171,221180981,221180981,278854535,202294479,231979042,725148418,787183046,346046109,657690757,530533280,770057231,271790171,584652061,405302860,137112544,137112544,851931432,118512782,683778547,616062960,508395428,271790171,185391473,923405109,227720616,563542899,770121847,185391473,546341739,851931432,657690757,851931432,284629213,289862692,788320338,770057231,770121847

RSA with "small number" ;)

    :::text
    n=960242069=151*6359219
    Phi = (p-1)(q-1) = 150*6359218 = 953882700
    e = 347
    ed = 1 mod 953882700

    >>> while (347*i%953882700 !=1):
    ...     i+=1
    ...
    >>> i
    5497883

We create a list `c` of the number as in the challenge description.

    :::text
    >>> for elem in c:
    ...     print(chr((elem**5497883)%960242069))

xhBQCUIcbPf7IN88AT9FDFsqEOOjNM8uxsFrEJZRRifKB1E=|key=visionary

I struggle a lot before thinking about that beeing a Vigenere cipher.

zJIOHIldUx7QF88MG9FMHxiMGAwNV8wckNjQWZATnxST1Q=

 echo -ne 'czJIOHIldUx7QF88MG9FMHxiMGAwNV8wckNjQWZATnxST1Q=' | base64 -d
s2H8r%uL{@_<0oE0|b0`05_0rCcAf@N|ROT

And then a ROT47 give us the flag.

DawgCTF{Lo0k_@t_M3_1_d0_Cr4p7o}

here is the [Cyber Chef receipe](https://gchq.github.io/CyberChef/#recipe=Vigen%C3%A8re_Decode('visionary')From_Base64('A-Za-z0-9%2B/%3D',true)ROT47(47)&input=eGhCUUNVSWNiUGY3SU44OEFUOUZERnNxRU9Pak5NOHV4c0ZyRUpaUlJpZktCMUU9)

## Slide To The Left (350)

The code is exactly the same as "Right Foot Two Stomps".

    :::python
    # -*- coding: utf-8 -*-
    """
    Created for Spring 2020 CTF
    Cryptography 2.5
    200 Points
    Welcome to the AES-CBC oracle!
    Our oracle's function is AES-CBC.
    The oracle is found at umbccd.io:13373, and your methods are:
        flg - returns the encrypted flag
        enc - returns the encryption of the message after the : in "enc:..."
              as 16 bytes of initialization vector followed by the ciphertext.
        dec - returns the decryption of the ciphertext after the : in "dec:<16 bytes iv>..."
              as a bytes string.

    @author: pleoxconfusa
    """

    import socket


    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('crypto.ctf.umbccd.io', 13373)
    sock.connect(server_address)

    #available methods: flg, enc, dec.

    msg = 'flg'.encode()
    sock.sendall(msg)
    ct = sock.recv(1024)
    print(ct)#not decoded, because now the oracle sends encrypted bytes.

    msg = 'enc:LET ME IN!!!'.encode()
    sock.sendall(msg)
    enc = sock.recv(1024)#receive the encryption as 16 bytes of iv followed by ct.
    print(enc)

    iv = enc[:16]
    ct = enc[16:]

    msg = b'dec:' + iv + ct #sanity check, also other way to encode
    sock.sendall(msg)
    dec = sock.recv(1024)
    print(dec)

    sock.close()

If we rerun the code for the previous challenge we get:

b'We already did this one.'

Which is obviously is not the flag.

# Misc

## Let Her Eat Cake! 75

Hwyjpgxwkmgvbxaqgzcsnmaknbjktpxyezcrmlja?

GqxkiqvcbwvzmmxhspcsqwxyhqentihuLivnfzaknagxfxnctLcchKCH{CtggsMmie_kteqbx}

Simple viegener cipher

AICGBIJC
Howdoyoukeepaprogrammerintheshowerallday?

GivehimabottleofshampoowhichsaysLatherrinserepeatDawgCTF{ClearEdge_crypto}
