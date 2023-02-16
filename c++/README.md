The code fulfills the requirements to output a list of files in a given directory, the current running processes and the mac address of the host

Instructions:
    $ make all
    $ l3harris

Assumptions:
    Running on a Linux system
    The linux system implements the /proc filesystem (required for accessing the currently running process information)
    The linux system stores the mac address in the (modern) standard location `/sys/class/net/{ifname}/address`
    C++17 or greater is used to compile the code (needed for `filesystem` API). C++11 is required for `is_number`.

    Currently the `ifname` is hard-coded into `main` as `enp0s3`. This should be altered to suit the system, although see below for improvements.

Improvements:
    Currently the code takes no user input. Processing argc/argv for parameters would allow:
    - user selection of functions to be output
    - user selection of directory for reading
    - user selection of ifname for accessing the MAC address (allowing removal of hard-coded `ifname` in `main`)
    Making concessions for non-proc filesystems
    Making concessions for systems that do not provide `/sys/class/net` storage of MAC address
    Porting to Windows (accessing process information needs addressing via Windows API)
    Addition of selectable output: either
    - wrapper functions to allow use of streams to select where data should be output.
    - wrap functions in classes to allow use of `operator<<` overloading.
