class Solution(object):
    def findRestaurant(self, list1, list2):
        ind1 = 0
        ind2 = 0
        ind_sum = sys.maxsize
        rest = list()
        
        for restaurant1 in list1:
            for restaurant2 in list2:
                if (restaurant1 == restaurant2) and ((ind1 + ind2) < ind_sum):
                    ind_sum = ind1 + ind2
                    rest = []
                    rest.append(restaurant2)
                elif (restaurant1 == restaurant2) and ((ind1 + ind2) == ind_sum):
                    rest.append(restaurant2)
                ind2 = ind2 + 1
            ind1 = ind1 + 1
            ind2 = 0
                
        return rest