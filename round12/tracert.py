import socket
import struct
import sys
# Here is the program that using the TRACERT.EXE command the find out the number of hops that
# we pass message from our PC top the destination hop
# we have to use the SOCKET

# We want unbuffered stdout so we can provide live feedback for
# each TTL. You could also use the "-u" flag to Python.
# class flushfile("tracer.txt"):
#     def __init__(self, f):
#         self.f = f
#
#     def write(self, x):
#         self.f.write(x)
#         self.f.flush()

#
# sys.stdout = flushfile(sys.stdout)


def main():
    dest_name="google.com"
    file_open = open("tracert_result.txt", 'a')
    dest_addr = socket.gethostbyname(dest_name)
    port = 33434
    max_hops = 30
    icmp = socket.getprotobyname('icmp')
    udp = socket.getprotobyname('udp')
    ttl = 1
    while True:
        recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
        send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, udp)
        send_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)

        # Build the GNU timeval struct (seconds, microseconds)
        timeout = struct.pack("ll", 5, 0)

        # Set the receive timeout so we behave more like regular traceroute
        recv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVTIMEO, timeout)

        recv_socket.bind(("", port))
        file_open.write(" %d  " % ttl)
        send_socket.sendto("".encode(), (dest_name, port))
        curr_addr = None
        curr_name = None
        finished = False
        tries = 3
        while not finished and tries > 0:
            try:
                curr_addr = recv_socket.recvfrom(512)
                finished = True
                curr_addr = curr_addr[0]
                try:
                    curr_name = socket.gethostbyaddr(str(curr_addr[0]))
                    file_open.write(curr_name.decode())
                except socket.error:
                    curr_name = curr_addr
            except socket.error as e:
                tries = tries - 1
                file_open.write("* ")

        send_socket.close()
        recv_socket.close()

        if not finished:
            pass

        if curr_addr is not None:
            curr_host = "%s (%s)" % (curr_name, curr_addr)
        else:
            curr_host = ""
        file_open.write("%s\n" % (curr_host))

        ttl += 1
        if curr_addr == dest_addr or ttl > max_hops:
            break



main()



# import socket
#
# def main(dest_name):
#         dest_addr = socket.gethostbyname(dest_name)
#         port = 33434
#         max_hops = 30
#         icmp = socket.getprotobyname('icmp')
#         udp = socket.getprotobyname('udp')
#         ttl = 1
#         while True:
#             recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
#             send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, udp)
#             send_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
#             recv_socket.bind(("", port))
#             send_socket.sendto("".encode(), (dest_name, port))
#             curr_addr = None
#             curr_name = None
#             try:
#                 _, curr_addr = recv_socket.recvfrom(512)
#                 curr_addr = curr_addr[0]
#                 try:
#                     curr_name = socket.gethostbyaddr(curr_addr)[0]
#                 except socket.error:
#                     curr_name = curr_addr
#             except socket.error:
#                 pass
#             finally:
#                 send_socket.close()
#                 recv_socket.close()
#
#             if curr_addr is not None:
#                 curr_host = "%s (%s)" % (curr_name, curr_addr)
#             else:
#                 curr_host = "*"
#             print ("%d\t%s" % (ttl, curr_host))
#
#             ttl += 1
#             if curr_addr == dest_addr or ttl: #&gt; max_hops:
#                 break
#
#
# main('google.com')