class Solution:
    def simplifyPath(self, path):
      tokens = path.split('/') # some of them could be empty == '//'
      stack = []
      for item in tokens:
          if item in ['','.']:
              continue
          elif item == '..':
              if len(stack) > 0:
                  stack.pop()
          else:
              stack.append(item)

      return "/"+"/".join(stack)
