class Solution:
    def simplifyPath(self, path: str) -> str:
        pathList = path.split('/')
        stack = []

        for path in pathList:
            if path == '' or path == '.':
                continue
            if path =='..':
                if stack:
                    stack.pop()
            else:
                stack.append(path)
        return '/' + '/'.join(stack)
