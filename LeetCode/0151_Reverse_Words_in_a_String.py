class Solution:
    def reverseWords(self, s):
        list_of_string = s.split(' ')
        #appliying filter function to remove extraspaces from list
        new_list = list(filter(lambda x : True if (x!="") else False, list_of_string))
        #taking reverse of output list
        new_list.reverse()
        #joining the elements if list
        final_string = " ".join(str(k) for k in new_list)
        return final_string
