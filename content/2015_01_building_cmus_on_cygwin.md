Title:Compiling cmus for cygwin
Date: 01-21-2015
category:Programming
tags:cygwin,cmus
meta:cygwin,cmus,compilation

<img class="align-left" src="/media/2015.01/2015.01.cmus.png" alt="cmus" width="342">
I work on a Windows machine for my dally job.
On my personal desktop I use Arch Linux and i3 therefore my music player is in
curses and does not need any mouse. In fact I use
[cmus](https://cmus.github.io/). So I tried to replace my old media player
[clementine](https://www.clementine-player.org/) with
[cmus](https://cmus.github.io/) on Windows in [cygwin](https://www.cygwin.com/).

For that we need to compile [cmus](https://cmus.github.io/) from sources.
<!-- PELICAN_END_SUMMARY -->

**A [TL;DR](https://en.wikipedia.org/wiki/TL;DR) is available at the end of
the article.**

It is really easy, you just need to download the `tar.gz` archive, untar it, and
run :

    ./configure
    make
    make install

Then [cmus](https://cmus.github.io/) will be directly accessible in your
[cygwin](https://www.cygwin.com/) environment. You can access a file explorer
by pressing the `5` key and then navigate through your files and add a folder
to your libarary with the `a` key. To know more about how to use
[cmus](https://cmus.github.io/) please refer to the official documentation.

Okay then why a whole blog post about 3 classical commands ?
Well you may notice that when adding your folder(s) to your library not all your
files are added to it, in fact [cygwin](https://www.cygwin.com/) does not
package any mp3 codec so your `flac` files will be read by
[cmus](https://cmus.github.io/) but not the `mp3` one (as long as you have
install the flac codec).

In oder to read mp3 files with [cmus](https://cmus.github.io/) we need to
install (so to build) a library that read this file format: libmad

# libmad

First of all we need to download the source package from the official web site :
[http://www.underbit.com/products/mad/](http://www.underbit.com/products/mad/)
now we extract the files and make the classical commands:

    ./configure
    make
    make install

You may encounter the "guess build" error:

## guess error

This append during the make command

    configure: error: cannot guess build type; you must specify one

You may need the `automake` package and moreover you may need to replace the two
old files config.guess and config.sub from libmad with the new ones downloadable
at : [ftp://ftp.gnu.org/pub/gnu/config/README](ftp://ftp.gnu.org/pub/gnu/config/README)

**An other classical error is the `-fforce-memi` one:**

## `-fforce-mem` gcc error

This error is characterize by the following trace:

    gcc: error: unrecognized command line option '-fforce-mem'
    Makefile:383: recipe for target 'version.lo' failed
    make[2]: *** [version.lo] Error 1
    make[2]: Leaving directory '/cygdrive/c/Users/user/Downloads/libmad-0.15.1b'
    Makefile:424: recipe for target 'all-recursive' failed
    make[1]: *** [all-recursive] Error 1
    make[1]: Leaving directory '/cygdrive/c/Users/user/Downloads/libmad-0.15.1b'
    Makefile:249: recipe for target 'all' failed
    make: *** [all] Error 2

From GCC 4.3 release notes:

*The -fforce-mem option has been removed because it has had no effect in the
last few GCC releases.*

So we need to remove this option from our configure script, [some people wrote a
patch for it](http://www.linuxfromscratch.org/blfs/view/svn/multimedia/libmad.html)
but it is just a `sed` command

    sed -i '/-fforce-mem/d' configure

We need to redo the 3 basics commands:

    ./configure
    make
    make install

**At this point you should not have any error, but a classical one is the
missing library error:**

## missing library error

The error is indicating the precise missing library (here `libtool`):

    Makefile.am:27: Libtool library used but `LIBTOOL' is undefined
    Makefile.am:27:
    Makefile.am:27: The usual way to define `LIBTOOL' is to add `AC_PROG_LIBTOOL'
    Makefile.am:27: to `configure.ac' and run `aclocal' and `autoconf' again.
    Makefile:256: recipe for target 'Makefile.in' failed
    make: *** [Makefile.in] Error 1

And we just need to install the missing library using [cygwin](https://www.cygwin.com/) package manager.

**Now we have libmad install in `/usr/local/lib/`**

# cmus

But our installation is not completed we need to recompile
[cmus](https://cmus.github.io/) with the support
of this new library and if you just launch the 3 basic commands it will not
work. In fact, gcc does not search libraries in `/usr/local` by default. We need
to add a flag at the configure step:

    ./configure CPPFLAGS=-I/usr/local/include LDFLAGS=-L/usr/local/lib
    make
    make install

And now you can launch [cmus](https://cmus.github.io/) and re-add your mp3
files and **it works!**

### Workflow

* Install [libmad](http://www.underbit.com/products/mad/)
  * change the `config.gess` and `config.sub` files
  * patch the configuration to not use the `-fforce-mem` option with sed: `sed -i '/-fforce-mem/d' configure`
  * run the 3 classic commands :

    ./configure
    make
    make install

* Install [cmus](https://cmus.github.io/) and add the `gcc` flags to load libraries in /usr/local:

    ./configure CPPFLAGS=-I/usr/local/include LDFLAGS=-L/usr/local/lib
    make
    make install

*If you run a classical linux distribution to install cmus use `aptitude install
cmus` or `pacman -S cmus`. It is so much easier!*
