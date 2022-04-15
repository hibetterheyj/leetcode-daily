class Solution {
public:
    int maxArea(vector<int>& height) {
        int res(0), i(0), j(height.size()-1);
        while(i<j){
            res = max(res, (j-i)*min(height[i], height[j]));
            height[i] < height[j] ? i++: j--;
        }
        return res;
    }
};
