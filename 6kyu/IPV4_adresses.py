# Implement a function that receives two IPv4 addresses,
# and returns the number of addresses between them
# (including the first one, excluding the last one).
# All inputs will be valid IPv4 addresses in the form of strings.
# The last address will always be greater than the first one.


def find_difference_ipv4(address, second_address):
    address = list(map(int, address.split(".")))
    second_address = list(map(int, second_address.split(".")))
    address.reverse()
    second_address.reverse()
    for item in range(len(address)):
        address[item] = address[item] * (256 ** item)
        second_address[item] = second_address[item] * (256 ** item)
    summary = -(sum(address) - sum(second_address))
    return summary


# optimize resolve
import ipaddress


def ips_between(start, end):
    return int(ipaddress.ip_address(end)) - int(ipaddress.ip_address(start))


print(ips_between("1.0.0.0", "10.0.0.50"))
