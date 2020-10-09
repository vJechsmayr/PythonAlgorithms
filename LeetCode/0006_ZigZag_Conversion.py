class Solution():

	def __init__(self):
		pass

	def StringConvert(self,string,numRows): 
		StrLen = len(string)
		if StrLen <= numRows :
			return string
		else:
			MainColumn = [" "]*numRows						# MainColumn = agregate of fina; column of all iterates of ladder and vertical column routine (line 9)
			if numRows >= 2:								#-------------------------------------------------------	
				ladderSize = numRows - 2					#ladder - slant single char columns between two consecutive vertical columns
			else:											# n-2 as it leaves firast and last char of a vertical column 
				ladderSize = 0								#-------------------------------------------------------		
			string = list(string)							#
			StrLen = len(string)							#
			while StrLen > 0:                       # routine to create final column out of a pair of vertical and ladder column (ladder and vertical column routine)
				column = string[:numRows]						#-------------------------------------------------------
				string = string[numRows:]						#      column variable - vertical column
				if numRows >= StrLen :							#
					diff = numRows - StrLen						#    subroutine mainly to output vertical column 
					column += [" "]*diff						#
					StrLen = 0									#
					tempColumn = [" "]*numRows					#-------------------------------------------------------
				else:
					StrLen -= numRows											#----------------------------------------------------	
					tempColumn = string[:ladderSize]							#	 tempColumn - ladder column
					tempColumn.reverse()										#		
					string = string[ladderSize:]								#	subroutine mainly to output ladder column
					StrLen -= ladderSize										#
					diff = numRows - len(tempColumn) - 1						#
					tempColumn = [" "]*diff + tempColumn + [" "]				#-------------------------------------------------------
				MainColumn = self.listmerge(MainColumn,column,tempColumn,numRows)	# merging maincolumn vertical; and ladder column -> final column
				ZigZagStr = ""													#-------------------------------------------------------					
				for chars in MainColumn:										# merging all  final columns 
					ZigZagStr += chars											#-------------------------------------------------------
			return ZigZagStr
					

	def listmerge(self,lst1,lst2,lst3,LstLen):   # function to merge output columns of vertical and ladder subroutines
		retLst = [" "]*LstLen               # list containing all rows after each merging routine iterations
		for i in range(LstLen) :			#-------------------------------------------------------
			tempStr = ""					#			
			char1 = lst1[i]					#   merging routine
			char2 = lst2[i]					#
			char3 = lst3[i]					#
			if char1 != " " :				#	only adds if the row is not empty
				tempStr += char1			#
			if char2 != " " :				#
				tempStr += char2			#
			if char3 != " ":				#
				tempStr += char3			#
			if tempStr != "":				#
				retLst[i] = tempStr			#-------------------------------------------------------
		return retLst

