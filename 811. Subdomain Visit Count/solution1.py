class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        subdomain_dict = collections.defaultdict(int)
        
        for cpdomain in cpdomains:
            cpdomain = cpdomain.split(" ", 1)
            times = cpdomain[0]
            domains = cpdomain[1].split(".")
            
            curr_domain = ""
            for i in range(len(domains) - 1, -1, -1):
                curr_domain = domains[i] + curr_domain
                subdomain_dict[curr_domain] += int(times)
                curr_domain = "." + curr_domain
                
        return ['{} {}'.format(times, subdomain) for subdomain, times in subdomain_dict.items()]