The code fulfills the requirements to output a list of files in a given directory, the current running processes and the mac address of the host

Instructions:

    l3harris.py [-h] [--files] [--procs] [--mac] [-d DIR] [-r] [-i IFNAME]

    Optionally:
        $ make venv
            to try and generate the virtual environment - assumes pipenv and python3.11 installed. Adjust `Pipfile` for python version (3.8 ought to be sufficient)
        $ make run
            runs all section outputs, and passes in the ifname `enp0s3`


Assumptions:
    A Python venv is installed with `pipenv` (alternatively a virtual environment meeting the requirements specified in `Pipfile` can be used)
    The python code relies on `psutils` (see Pipfile for requirements)
    Running on a Linux system
    The linux system stores the mac address in the (modern) standard location `/sys/class/net/{ifname}/address`

Improvements:
    Output to a stream:
        - wrap the display calls such that they allow different TextIO options
    Handle cases where the mac address is not stored under `/sys/class/net`