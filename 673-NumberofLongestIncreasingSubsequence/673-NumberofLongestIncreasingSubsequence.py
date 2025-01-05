    int n = nums.size();
    int dp[n];
    dp[0]=1;
    
    int ans=0;
    
    for(int i=0;i<n;i++)
    {
        int maxi=0;
        for(int j=0;j<i;j++)
        {
            if(nums[i]>nums[j])
            {
                maxi = max(maxi,dp[j]);
            }
        }
        
       dp[i] = maxi+1;
       if(dp[i]>ans)
       {
           ans=dp[i];
       }
        
    }
    
    return ans;
    
}