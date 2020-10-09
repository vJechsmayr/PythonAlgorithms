class Solution():

	def __init__(self):
		pass

	def convert(self,string,numRows): 
		StrLen = len(string)
		if StrLen <= numRows :
			return string
		else:
			MainColumn = [" "]*numRows					
			if numRows >= 2:								
				ladderSize = numRows - 2					
			else:											
				ladderSize = 0								
			string = list(string)							
			StrLen = len(string)							
			while StrLen > 0:                       
				column = string[:numRows]					
				string = string[numRows:]					
				if numRows >= StrLen :							
					diff = numRows - StrLen					
					column += [" "]*diff						
					StrLen = 0									
					tempColumn = [" "]*numRows				
				else:
					StrLen -= numRows											
					tempColumn = string[:ladderSize]							
					tempColumn.reverse()									
					string = string[ladderSize:]							
					StrLen -= ladderSize									
					diff = numRows - len(tempColumn) - 1					
					tempColumn = [" "]*diff + tempColumn + [" "]				
				MainColumn = self.listmerge(MainColumn,column,tempColumn,numRows)	
				ZigZagStr = ""																		
				for chars in MainColumn:										
					ZigZagStr += chars											
			return ZigZagStr
					

	def listmerge(self,lst1,lst2,lst3,LstLen):  
		retLst = [" "]*LstLen               
		for i in range(LstLen) :			
			tempStr = ""								
			char1 = lst1[i]					
			char2 = lst2[i]					
			char3 = lst3[i]					
			if char1 != " " :				
				tempStr += char1			
			if char2 != " " :				
				tempStr += char2			
			if char3 != " ":				
				tempStr += char3			
			if tempStr != "":				
				retLst[i] = tempStr			
		return retLst

