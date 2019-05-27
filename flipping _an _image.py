class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        s = []
        a=[]
        j=0
        for count,i in enumerate(A):
            c=len(i)-1
            while c>=0:
                if(i[c]==0):
                    a.append(1)
                else:
                    a.append(0)
                #s[count][j]=i[c]
                c=c-1
            s.append(a)
            a=[]
        return s
