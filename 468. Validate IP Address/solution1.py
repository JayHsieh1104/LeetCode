import re

class Solution:
    def validIPAddress(self, IP: str) -> str:
        chunk_IPv4 = r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'
        patten_IPv4 = re.compile(r'^(' + chunk_IPv4 + r'\.){3}' + chunk_IPv4 + r'$')
        
        chunk_IPv6 = r'([0-9a-fA-F]{1,4})'
        patten_IPv6 = re.compile(r'^(' + chunk_IPv6 + r'\:){7}' + chunk_IPv6 + r'$')
        
        if patten_IPv4.match(IP):
            return "IPv4"
        elif patten_IPv6.match(IP):
            return "IPv6"
        else:
            return "Neither"