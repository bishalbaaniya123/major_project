from scapy.all import *
from scapy.layers.inet import ICMP,IP
import subprocess

subprocess.call(["ifconfig", "wlp6s0", "promisc"], stdout=None, stderr=None, shell=False)
sniffer_log = open("log.txt", "w")
sniffer_logtest = open("test.txt", "w")

proto_sniff="0"
packet_no = 0

def packet_log(pkt):

    global packet_no
    if proto_sniff.lower() in pkt[0][1].summary().lower():
        packet_no = packet_no + 1
        # Writing the data for each packet to the external file
        sniffer_log.write("Packet " + str(packet_no) + ": " + "SMAC: " + pkt[0].src + " DMAC: " + pkt[0].dst)
        print(pkt.show())
        # sniffer_logtest.write(pkt.show())

pkt = sniff(iface="wlp6s0", timeout=int(10), prn=packet_log)

sniffer_log.close()
