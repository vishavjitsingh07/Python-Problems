
class Solution:
    def displayContacts(self, n, contact, s):
        # code here
        final_result = []
        for i in range(0,len(s)):
            result = []
            for j in range(0,n):
                if contact[j].startswith(s[0:i+1]):
                    result.append(contact[j])
            if result:
                result = set(result)
                result = list(result)
                result.sort()
                final_result.append(result)
            else:
                final_result.append([0])
            
        return final_result
