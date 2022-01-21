import os
from functions import get_ip


def main():
    valid_ips = []
    ip = get_ip()
    base_ip = ip[:ip.rfind(".")]
    for i in range(254):
        cur_ip = "{0}.{1}".format(base_ip, i)
        res = os.popen("ping {0} -c 1".format(cur_ip)).read()
        if res.find("ttl") != -1:
            valid_ips.append(cur_ip)
            print("{0} is valid!".format(cur_ip))

    print("All valid ips are: {0}".format(valid_ips))


if __name__ == "__main__":
    main()
