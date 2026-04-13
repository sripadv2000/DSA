class Solution {
public:
    vector<int>a;
    vector<int>officialNums;

    Solution(vector<int>& nums) {
        a = nums;
        officialNums = nums;
    }
    
    vector<int> reset() {
        return officialNums;
    }
    
    vector<int> shuffle() {
        a = officialNums;
        vector<int>ss;
        while(a.size()){
            int r = rand()%a.size();
            ss.push_back(a[r]);
            swap(a[r], a[a.size()-1]);
            a.pop_back();
        }
        return ss;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * vector<int> param_1 = obj->reset();
 * vector<int> param_2 = obj->shuffle();
 */