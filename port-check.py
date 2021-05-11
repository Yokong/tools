import socket


def get_ips():
    with open('ips.txt') as f:
        for i in f.readlines():
            yield i.strip()


def get_ports():
    with open('ports.txt') as f:
        for i in f.readlines():
            yield i.strip()


def connect_check(ip, port):
    try:
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.settimeout(1)
        sk.connect((ip, port))
        sk.close
        print(f"Connect {ip} {port} Success!")
    except socket.error as e:
        print(f"Connect {ip} {port} Failed! {e}")


def main():
    for ip in get_ips():
        for port in get_ports():
            connect_check(ip, int(port))


if __name__ == "__main__":
    main()
