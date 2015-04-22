Title: Restore USB key
Status: hidden

# Restore an USB key

After using an USB drive to install a new OS (arch, debian, whatever)
your key may have a size under the expected one.

In order to restore it to the original size you have to follow the next command
lines:

First of all you need to put to zero the first 512 bytes

    # dd count=1 bs=512 if=/dev/zero of=/dev/sdx && sync

Then you must create a new partiton using cfdisk:

    # cfdisk /dev/sdx


Finally you nedd to write the file system on your USB stick :

If you want an ext4 partition:

    # mkfs.ext4 /dev/sdx1
    # e2label /dev/sdx1 USB_STICK

And if you want a FAT32 partition:

    # mkfs.vfat -F32 /dev/sdx1
    # dosfslabel /dev/sdx1 USB_STICK

Source: [archwiki](https://wiki.archlinux.org/index.php/USB_Flash_Installation_Media#How_to_restore_the_USB_drive)

