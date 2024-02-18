from scapy.all import *

#Read in our packet capture + define empty variables for later use
r = rdpcap('test.pcap')
a = ""
b = ""
c = ""

#Create a file to output to + define our loop logic of how we parse out the data
myfile = open("output.txt", "w")
for packet in range(0, len(r)):
    a = r[packet][DNSQR].qname
    no9 = a[18:]
    b = no9.replace(b'.microsofto365.com.', b'')
    if b == c:
        continue
    c = b
    modified_str = b.replace(b".", b"").decode("utf-8", errors="ignore")
    utf8_chars = "".join(c for c in modified_str if ord(c) < 128)
    ascii_str = bytes.fromhex(utf8_chars).decode("utf-8", errors="ignore")
    print(ascii_str)
    myfile.write(ascii_str)
    
myfile.close()
