#include<iostream>
#include<unordered_map>
#include<vector>
#include<unordered_set>
#include<stack>

using namespace std;

// In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

// If the town judge exists, then:

// The town judge trusts nobody.
// Everybody (except for the town judge) trusts the town judge.
// There is exactly one person that satisfies properties 1 and 2.
// You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

// Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

 

// Example 1:

// Input: n = 2, trust = [[1,2]]
// Output: 2
// Example 2:

// Input: n = 3, trust = [[1,3],[2,3]]
// Output: 3
// Example 3:

// Input: n = 3, trust = [[1,3],[2,3],[3,1]]
// Output: -1
 

// Constraints:

// 1 <= n <= 1000
// 0 <= trust.length <= 104
// trust[i].length == 2
// All the pairs of trust are unique.
// ai != bi
// 1 <= ai, bi <= n

class Solution {
    public:

        int findJudge(int n, vector<vector<int>>& trust) {

            int *trustsOther = new int[n] {0};
            int *peopleTrustHer = new int[n] {0};

            for(int i=0;i<trust.size();i++){
                vector<int> edge = trust[i];
                trustsOther[edge[0]-1]++;
                peopleTrustHer[edge[1]-1]++;
            }

            for(int i=0;i<n;i++){

                if(trustsOther[i]==0 && peopleTrustHer[i]==n-1){
                    return i+1;
                }

            }

            return -1;
        }

};


int  main(){

    vector<vector<int>> input = {
        {1,3},
        {1,4},
        {2,3},
        {2,4},
        {4,3}
    };

    Solution solution;

    int answer = solution.findJudge(4,input);

    cout << "Answer: " << answer << endl;

}
