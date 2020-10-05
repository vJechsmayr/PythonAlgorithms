class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> pq(stones.begin(), stones.end());
        while(pq.size() > 1){
            int stone_1 = pq.top(); pq.pop();
            int stone_2 = pq.top(); pq.pop();
            if(stone_1 == stone_2) 
                continue;
            else
                pq.push(abs(stone_1 - stone_2));
        }
        
        if(pq.size())
            return pq.top();
        
        return 0;
    }
};
