# Joshua Arulsamy
# Project 2 - Advanced
# 05/03/2020
# COSC 2049 500
import re

in_file = open("Scan.txt", "r")
out_file = open("Ports.txt", "w")
lineList = in_file.readlines()


def find_ports_by_num(lineList: list):
    """
    Returns a list with all the ports that are currently open.
    There are no duplicate PORT numbers but there are some duplicate service
    types, i.e if a service is listed twice but on difference port numbers.
    For this scan file, it is just unknown services that are duplicated.
    """
    port_count = {}
    for i in lineList:
        # Find portnum based on regex pattern
        match = re.search("\d{2,}/\w{3}\s+open\s+.+", i)

        if match is not None:
            port = match.group(0)

            # Remove extra whitespaces
            port_parts = port.split()
            port_parts = (port_parts[0], port_parts[-1])
            port = " ".join(port_parts)

            try:
                port_count[port] += 1
            except KeyError:
                port_count[port] = 1

    return sorted(port_count.items(), key=lambda x: x[1])


def find_ports_by_service(lineList: list):
    """
    Returns a list of ports open by service.
    """

    service_count = {}
    for i in lineList:
        match = re.search("open\s+.+", i)

        if match is not None:
            service = match.group(0)
            service = service.split()[1]

            try:
                service_count[service] += 1
            except KeyError:
                service_count[service] = 1

    return sorted(service_count.items(), key=lambda x: x[1])


def pretty_write(ports):
    for i in ports:
        out_file.write(f"{i[0]:28} {str(i[1])}\n")


ports = find_ports_by_num(lineList)
services = find_ports_by_service(lineList)

out_file.write("Open Ports by Port Number\n")
pretty_write(ports)
out_file.write("\nOpen Ports by Service\n")
pretty_write(services)

in_file.close()
out_file.close()
