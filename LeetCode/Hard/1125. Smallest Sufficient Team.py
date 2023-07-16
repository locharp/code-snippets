class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        req = (1 << len(req_skills)) - 1
        req_skills = {s: k for k, s in enumerate(req_skills)}
        pp = {}
        
        for i, p in enumerate(people):
            if not p:
                continue
            t = sum(1 << req_skills[s] for s in p)
            pp[t] = 1 << i
            
        dp = pp.copy()
                 
        while req not in dp:
            dp2 = {}
            k = {j: False for j in pp.values()}
            for t, j in pp.items():
                for s, i in dp.items():
                    u = t | s
                    if u > s:
                        dp2[u] = i | j
                        k[j] = True
            
            pp = {t: j for t, j in pp.items() if k[j]}
            dp = dp2
            
        return [i for i in range(len(people)) if (1 << i) & dp[req]]