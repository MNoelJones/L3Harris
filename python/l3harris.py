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
    parser.add_argument("-r", "--recurse", action="set_true")
    parser.add_argument("-i", "--ifname", default="eth0")
    return parser.parse_args(args)


def collect_files(directory: str = ".", recursive: bool = False) -> List[Path]:
    path = Path(directory).resolve()
    files = [*(path.rglob("*.*") if recursive else path.glob("*.*"))]
    return files


def collect_procs() -> List[Process]:
    return Process(1).get_children(recursive=True)


def get_mac_address(ifname: str = "eth0") -> str:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = ioctl(s.fileno(), 0x8927, struct.pack("256s", bytes(ifname, "utf-8")[:15]))
    return ":".join("%02x" % b for b in info[18:24])


def main(files, procs, mac, directory=".", ifname="eth0", recurse=False):
    if files:
        print(collect_files(directory, recurse))
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
