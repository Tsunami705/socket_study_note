# README.md

API for connecting to different hosts, working on TCP/IP stack.
Browser, mobile app, SSH client are implemented via sockets
Need to specify the ip address and port number of the host (to distinguish between different applications on the host)
There are two types of sockets: TCP/UDP
After starting the server in the terminal you can use nmap to establish a connection: `ncat -C ip [port]`
To establish a listen: `ncat -l ip [port]`