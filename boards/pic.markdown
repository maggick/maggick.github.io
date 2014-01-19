---
title: PIC
---

# PIC

It is not easy to find out how to compile a C code for a PIC16F886 on GNU/Linux.

## Installation

Installation is really simple:

``` bash
# aptitude install sdcc
```

You can test your installation with the following code :

``` c
char test;
void main(void) {
   test=0;
}
```

``` bash
# sdcc test.c
```

There your installation of sdcc is working. Now we are going to the hard part:

Under construction


