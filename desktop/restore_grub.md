# How to restore grub

When you use dual boot computer there is a risk that reinstalling windows
destroy your grub. It happeend to me several times.

Here is a simple How to reinstall grub :

## Requirement

You need a live whatever (Live CD, Live USB-key). Personnaly I used a live arch
USB-key.

## Commands

Restoring your grub is really easy with a few commands:

First of all we mount the partition in order to reinstall grub:

    sudo mount /dev/sdXY /mnt

Now bind the directories that grub needs access to to detect other operating
systems, like so:

    sudo mount --bind /dev /mnt/dev && sudo mount --bind /dev/pts /mnt/dev/pts
    && sudo mount --bind /proc /mnt/proc && sudo mount --bind /sys /mnt/sys

We chroot the partition:

    sudo chroot /mnt

Install check and update grub:

    grub-install /dev/sdX
    grub-install --recheck /dev/sdX
    update-grub

Exit chroot environnment and unmount everything:

    exit && sudo umount /mnt/dev && sudo umount /mnt/dev/pts && sudo umount
    /mnt/proc && sudo umount /mnt/sys && sudo umount /mnt

[Source](http://howtoubuntu.org/how-to-repair-restore-reinstall-grub-2-with-a-ubuntu-live-cd#.UwSjNoVkFGd)

