## Reverse engineering dnscat unencrypted comms in a packet capture

### Ascertain how DNSCat is sending data back in wireshark:
1. Find the big talkers via stats:
![image](https://github.com/Broomey28/reverse_engineering_dnscat2/assets/56151530/dd355045-3172-461b-b2d5-2d1e55e6b406)
2. Filter out the DNS traffic between these two (you can select these packets and save to another pcap file for further speed):

   
   ```ip.addr==<ip>  && <ip> && dns ```
   
      ![image](https://github.com/Broomey28/reverse_engineering_dnscat2/assets/56151530/f93dcbe3-0e97-4656-9adb-fa56b24b1d4a)
3. It should be pretty obvious what the [root domain](https://en.wikipedia.org/wiki/Root_name_server#:~:text=The%20root%20domain%20does%20not,.example.com.%22 "What is a root domain") is from here:

   ![image](https://github.com/Broomey28/reverse_engineering_dnscat2/assets/56151530/c49965f6-5d21-4bb2-9005-d9f7a1785752)
5. Figure out how many bytes of nonsense data is before/after each DNS Query (we'll need this to remove it in our script).
   - Add the Qnames into your wireshark column and take a good look at the queries, you should be able to notice a pattern here:
   - Notice how the first 18 bits of the hex have a similar pattern for each and every query, it seems to be a boundary separating the actual data:
   ![image](https://github.com/Broomey28/reverse_engineering_dnscat2/assets/56151530/5ccc1e4c-394e-431c-95a9-a87a8ca57043)
   - We can see this further if we look at the converted output in CyberChef (this is a single QName Sample):
   - Notice the non-ascii characters at the beginning!
```
=¾Í¡¼w«",fhill,Stephen Cline,M,"3988 Weber Dale Suite 754 New Anthonyhaven, UT 92327",ebarnett@hotmail
```
**Now we can see the characters marking the boundary, we know we need to take them out otherwise it's going to make the output of our script difficult to read.**
### Running the script
  - Change these variables in the script, based upon our findings above:
 ![image](https://github.com/Broomey28/reverse_engineering_dnscat2/assets/56151530/bb7420a5-77c4-4a0c-beb7-018654798b39)

  - Now, run it + get your perfectly formatted output of everything sent over DNS:
 ![image](https://github.com/Broomey28/reverse_engineering_dnscat2/assets/56151530/874634ef-c0fd-4427-a4de-1038dc2219d8)

## Simple, easy and most importantly - *VERY* quick.
