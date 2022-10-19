class Solution:



    def synonym_grup (self, tablee):

        def tmep(tmpset, setlst):
            for sett in setlst:
                #print(sett)
                if sett.intersection(tmpset):
                    sett.update(tmpset)
                    return setlst
            setlst.append(tmpset)
            return setlst

            pass
        cnt = 0
        setlst = []
        for i in tablee:
            tmpset = set(*i.items())
            setlst = tmep(tmpset, setlst)
                    
        print(setlst)
        #return len(setlst)



ss = Solution()
ss.synonym_grup([{"Dg set": "Diesel generator"}, {"Organization": "Organisation"},
                         {"Group": "Organization"}, {"Orange": "Kinnu"}, {"Orange": "narangi"}])
