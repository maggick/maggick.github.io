Title:Lost Windows password
Date: 10-07-2014
category:desktop

Few weeks ago my girlfriend lost her laptop Windows password, I do not have any
hint about it and of course I am not an other of it (otherwise mimicatz would have been
my friend). I asked her to try basic password ("12345", "password"…) then she
asked me to reset it in order not to retrieve some data on it but to use an
already install program. Therefore just mount the "C" partition and copy the data
to an USB disk in not a possibility. I really need to change its user Windows
password by a known one.

* Let's boot on a Linux live ISO
* mount the "C" partition (here sda1) : `mount /dev/sda1 /mnt/`
* backup sethc.exe: `cp /mnt/windows/system32/sethc.exe /mnt/windows/system32/sethc.exe_old`
* replace sethc.exe with cmd.exe: `cp /mnt/windows/system32/cmd.exe /mnt/windows/system32/sethc.exe`
* reboot on Windows
* press "Shift" 5 times, an administration command prompt will open
* change the user password for "lol": `net user my_user my_new_password`
* replace the sethc.exe with the original one
* done !

She was happy, nevertheless the needed program was not on this laptop.

(You can found the manipulations in my notes section)[www.matthieukeller.com/notes/desktop/lost_windows_password.md]
