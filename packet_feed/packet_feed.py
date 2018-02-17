from scapy.all import *
from scapy.layers.inet import ICMP,IP
import subprocess

class packet_feed:
    sniffer_log = open("packet_feed/log.txt", "w")

    proto_sniff="0"
    packet_no = 0

    def __init__(self):
        subprocess.call(["ifconfig", "wlp6s0", "promisc"], stdout=None, stderr=None, shell=False)


    def packet_log(self,pkt):

        packet_no=self.packet_no
        if self.proto_sniff.lower() in pkt[0][1].summary().lower():
            packet_no = packet_no + 1
            # Writing the data for each packet to the external file
            self.sniffer_log.write("Packet " + str(packet_no) + ": " + "SADDR: " + pkt[0].src + " DADDR: " + pkt[0].dst +"\n")

    def sniff_pkt(self):
        pkt = sniff(iface="wlp6s0", timeout=int(10), prn=self.packet_log)

    def __del__(self):
        self.sniffer_log.close()
