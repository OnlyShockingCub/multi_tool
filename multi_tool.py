import argparse
import os
import shutil
import psutil
import socket
from datetime import datetime

def system_info():
    print(f"CPU Usage: {psutil.cpu_percent()}%")
    print(f"Memory Usage: {psutil.virtual_memory().percent}%")
    print(f"Disk Usage: {psutil.disk_usage('/').percent}%")

def get_time():
    now = datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

def ping_host(host):
    response = os.system(f"ping -c 4 {host}")
    if response == 0:
        print(f"Host {host} is reachable.")
    else:
        print(f"Host {host} is not reachable.")

def rename_file(old_name, new_name):
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"File renamed from {old_name} to {new_name}")
    else:
        print(f"The file {old_name} does not exist.")

def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"File {filename} deleted.")
    else:
        print(f"The file {filename} does not exist.")

def copy_file(source, destination):
    if os.path.exists(source):
        shutil.copy(source, destination)
        print(f"File copied from {source} to {destination}")
    else:
        print(f"The file {source} does not exist.")

parser = argparse.ArgumentParser(description="Python Multitool")
parser.add_argument('--systeminfo', action='store_true', help="Get system info")
parser.add_argument('--time', action='store_true', help="Get current time")
parser.add_argument('--ping', metavar='HOST', type=str, help="Ping a host")
parser.add_argument('--rename', nargs=2, metavar=('OLD', 'NEW'), help="Rename a file")
parser.add_argument('--delete', metavar='FILENAME', type=str, help="Delete a file")
parser.add_argument('--copy', nargs=2, metavar=('SOURCE', 'DEST'), help="Copy a file")

args = parser.parse_args()

if args.systeminfo:
    system_info()
if args.time:
    get_time()
if args.ping:
    ping_host(args.ping)
if args.rename:
    rename_file(args.rename[0], args.rename[1])
if args.delete:
    delete_file(args.delete)
if args.copy:
    copy_file(args.copy[0], args.copy[1])
