import argparse

def list_servers():
    print("Listing all registered servers...")
    servers = ["web01", "web02", "db01"]
    for s in servers:
        print(f"  - {s}")

def show_server(name, ip, env):
    print(f"Server  : {name}")
    print(f"IP Addr : {ip}")
    print(f"Environ : {env}")

def validate_server(name):
    print(f"Validating server: {name}")
    if name.startswith("web"):
        print("  Status: VALID")
    else:
        print("  Status: WARNING – unexpected prefix")

parser = argparse.ArgumentParser(
    description="Server Management CLI Tool"
)
parser.add_argument("--name", help="Server name")
parser.add_argument("--ip",   help="Server IP address")
parser.add_argument(
    "--environment",
    choices=["dev","test","prod"],
    default="dev"
)
parser.add_argument(
    "--operation",
    choices=["list","show","validate"],
    required=True
)

args = parser.parse_args()

if args.operation == "list":
    list_servers()
elif args.operation == "show":
    show_server(args.name, args.ip, args.environment)
elif args.operation == "validate":
    validate_server(args.name)

# how to run the pgm, check below commands and run it in terminal:
# python argper.py --operation list 
# python argper.py --operation show
# python argper.py --operation validate --name web01
# python argper.py --operation show --name web01 --ip 192.168.1.100 --environment test