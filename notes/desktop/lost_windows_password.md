# Recover lost Windows password

If you append to "loose" your windows password. Here is a simple trick to reset
it, you only need a physical access to the computer in order to boot it on a
Linux system:

## Get an administration command console

Let's replace the sticky keys executable file with a command one:

* boot your computer on a your Linux
* mount the C partition file (for instance sda1) with `#mount /dev/sda1 /mnt/`
* backup `cp /mnt/windows/system32/sethc.exe /mnt/windows/system32/sethc.exe_old`
* replace `cp /mnt/windows/system32/cmd.exe /mnt/windows/system32/sethc.exe`
* boot on Windows
* press `Shift` 5 times

## Change the user password

In the administration console just type:
`net user my_user my_new_password`

## Done

You may want to replace back your `sethc.exe` file with the original one:
`copy c:\windows\system32\sethc.exe_old c:\windows\system32\sethc.exe`

