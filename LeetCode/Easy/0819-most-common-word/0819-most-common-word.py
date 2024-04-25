class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub("[^a-zA-Z]", " ", paragraph)
        words = paragraph.lower().split()
        cnt_dic = {}
        max_cnt = 0
        answer = ""
        
        for word in words:
            if word in banned:
                continue
            
            if word not in cnt_dic:
                cnt_dic[word] = 0
            cnt_dic[word] += 1
            
            if cnt_dic[word] > max_cnt:
                max_cnt = cnt_dic[word]
                answer = word
            
        return answer
                