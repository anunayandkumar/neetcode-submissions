class Solution {
public:
    bool isPalindrome(string s) {
        for(int i=0;i<s.size();i++){
            s[i]=tolower(s[i]);
        }
        int p1=0;
        int p2=s.size()-1;
        while(p1<p2){
        if(isalnum(s[p1])==false){
            p1++;
            continue;
        }
        if(isalnum(s[p2])==false){
            p2--;
            continue;
        }
            if(s[p1]!=s[p2]){
                cout<<p1<<" "<<p2;
                return false;
            }
            else{
                p1++;
                p2--;
            }
        }
        return true;
    }
};
