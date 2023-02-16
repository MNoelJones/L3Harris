import argparse
from fcntl import ioctl
import socket
import struct
from pathlib import Path
from psutil import Process

from typing import List


def parse_args(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--files", action="store_true")
    parser.add_argument("--procs", "--processes", action="store_true")
    parser.add_argument("--mac", action="store_true")
    parser.add_argument("-d", "--dir", default=".")
    parser.add_argument("-r", "--recurse", action="store_true")
    parser.add_argument("-i", "--ifname", default="eth0")
    return parser.parse_args(args)


def collect_files(directory: str = ".", recursive: bool = False) -> List[Path]:
    path = Path(directory).resolve()
    files = [*(path.rglob("*.*") if recursive else path.glob("*.*"))]
    return files


def collect_procs() -> List[Process]:
    return Process(1).children(recursive=True)


def get_mac_address(ifname: str = "eth0") -> str:
    with open(Path("/sys/class/net") / ifname / "address") as f:
        mac_addr = f.read().strip()
    return mac_addr

def main(files, procs, mac, directory=".", ifname="eth0", recurse=False):
    if files:
        print([str(file) for file in collect_files(directory, recurse)])
    if procs:
        print(collect_procs())
    if mac:
        print(get_mac_address(ifname))


if __name__ == "__main__":
    args = parse_args()
    main(
        args.files,
        args.procs,
        args.mac,
        directory=args.dir,
        ifname=args.ifname,
        recurse=args.recurse,
    )
