class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for i in range(len(strs)):
            for j in range(len(strs[i])):
                ans=ans+str(ord(strs[i][j]))
                ans=ans+" "
            ans = ans + "-"
        return ans
        
    

    def decode(self, s: str) -> List[str]:
        ans_list = []
        each_item_list_str = s.split("-")
        for i in range(len(each_item_list_str)):
            each_item_list = each_item_list_str[i].split()
            temp = ""
            for j in range(len(each_item_list)):
                temp += chr(int(each_item_list[j]))
            ans_list.append(temp)
        ans_list.pop()
        return ans_list


        

