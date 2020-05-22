from collections import defaultdict

class Solution:
    def zero(self):
        return 0

    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        mDict = defaultdict(self.zero)
        for domain in cpdomains:
            times = int(domain.split(' ', 1)[0])
            subdomains = domain.split(' ', 1)[1].split('.')
            for i in range(len(subdomains)):
                subdomain = '.'.join(subdomains[i:])
                mDict[subdomain] += times
        
        return [ '{} {}'.format(times, subdomain) for subdomain, times in mDict.items()]