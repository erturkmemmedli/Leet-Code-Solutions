class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hashmap = {}
        for string in cpdomains:
            split = string.split()
            count = int(split[0])
            domains = split[1].split('.')
            d1 = '.'.join(domains)
            d2 = '.'.join(domains[1:])
            if d1 not in hashmap: hashmap[d1] = count
            else: hashmap[d1] += count
            if d2 not in hashmap: hashmap[d2] = count
            else: hashmap[d2] += count
            if len(domains) == 3:
                d3 = '.'.join(domains[2:])
                if d3 not in hashmap: hashmap[d3] = count
                else: hashmap[d3] += count
        output = []
        for key, value in hashmap.items():
            output.append(str(value) + ' ' + key)
        return output
