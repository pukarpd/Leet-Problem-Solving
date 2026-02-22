class Solution {
public:
    int binaryGap(int n) {

        if (n == 1) {

            return 0;
        }

        std::bitset<32> bits(n); 
        std::string s = bits.to_string();

        // cout << s << endl;

        s.erase(0, s.find_first_not_of('0')); 
        cout << s << endl;

        int i = 0, j = 1; 
        int res = 0;

        while (j < s.size()){
            if (s[i] == '1' & s[j] != '1'){
                j ++;
            }
            else if (s[i] == '1' and s[j] == '1') {
                res = max(res, (j-i)); 
                i = j; 
                j ++;

            }
            else {
                i++;
                j--;
            }

        }


        return res;

    }
};