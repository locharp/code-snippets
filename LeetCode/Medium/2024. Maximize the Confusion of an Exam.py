class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        max = 0
        dict = { "T": 0, "F": 0 }
        
        for i in range( len( answerKey ) ):
            dict[answerKey[i]] += 1  
            
            if min( dict.values() ) <= k:
                max += 1
            else:
                dict[answerKey[i - max]] -= 1
                
        return max