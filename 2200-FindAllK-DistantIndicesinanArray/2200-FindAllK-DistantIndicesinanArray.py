class Solution {
public:
    vector<int> findKDistantIndices(vector<int>& nums, int key, int k) {
        vector<int> ans;
        int len = nums.size();
        int maxVal=-1;
        int start=0,end=0;
        
        
        for(int i =0;i<len;i++){
            if(nums[i]==key){
                if( (i-k<0 || i+k>len-1)){
                if(i-k<0 && i+k>len-1){
                    for(int i =0;i<len;i++) ans.push_back(i);
                    return ans;
                }
               else if(i-k<0){
                    start=max(0,maxVal+1);
                    end = i+k;
                    maxVal = end;
                } else{
                     start=max(i-k,maxVal+1);
                     end = min(i+k,len-1);
                    maxVal = end;
                }
            }else{
                start=max(i-k,maxVal+1);
                    end = i+k;
                    maxVal = end;
            }
               for(int i =start;i<=end;i++) ans.push_back(i);
            }

        }
        
        return ans;
    }
};