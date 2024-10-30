# Introduction

We have 2 files. A pcap and a php files.

# PCAP

I lookup the pcap before deobfuscate entirely the support.php
We filter for only POST method. We get only 4 entries.
![POST](./assets/2024-09-28T23:17:53,862253486+02:00.png)
If we follow the http stream we get weird entries like this : 0UlYyJHG87EJqEz66f8af44abea0QKxO/n6DAwXuGEoc5X9/H3HkMXv1Ih75Fx1NdSPRNDPUmHTy351039f4a7b5
![STREAM](./assets/2024-09-28T23:22:19,040121186+02:00.png)

# PHP

Let's go deobfuscate this. I use online gdb for execute the php code.
You can manually deobfuscate it. Or try to do it automatically with tool online or AI.
Once decoded (cf. script.php) the script want a input string.
Obviously we take strings from the pcap files which is send to the support.php
Here is the result :
![Decoded](./assets/2024-09-26T16:53:58,355254103+02:00.png)
Once decode, with cyberchef for example :
![Base64](./assets/2024-09-26T16:54:07,295914068+02:00.png)
We download the file and check what is it :
![Download](./assets/2024-09-26T16:54:11,809199160+02:00.png)

# Keepassxc

We use [keepass4brute](https://github.com/r3nt0n/keepass4brute) with the standard [rockyou.txt](https://github.com/zacheller/rockyou):
![Bruteforce](./assets/2024-09-26T20:42:23,017970501+02:00.png)
And after 21444 attempts, we got the password and open the database:
![Database](./assets/2024-09-26T20:44:16,536587309+02:00.png)
