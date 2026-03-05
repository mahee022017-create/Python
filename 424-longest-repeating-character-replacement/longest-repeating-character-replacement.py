class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        freq={}
        mf=0
        n=len(s)
        ans=0
        for r in range(n):
            if s[r]in freq:
                freq[s[r]]+=1
            else:
                freq[s[r]]=1
            mf=max(mf,freq[s[r]])
            while(r-left+1)-mf>k:
                freq[s[left]]-=1
                left+=1
            if(r-left+1)-mf<=k:
                ans=max(ans,r-left+1)
        return ans