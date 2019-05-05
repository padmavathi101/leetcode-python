class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        c=0
        paragraph=paragraph.lower()
        paragraph= re.sub('[\']+', '',paragraph)
        words=re.findall(r"[\w']+",paragraph)
        mapping={}
        for i in words:
            if i not in banned:
                if i not in mapping:
                    mapping[i]=0
                if i in mapping:
                    #print "hi"
                    mapping[i]=mapping[i]+1
                    if(c<mapping[i]):
                        c=mapping[i]
                        s=i  
        print mapping
        return s
        
                      
