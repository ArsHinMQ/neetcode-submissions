class Solution:
    def simplifyPath(self, path: str) -> str:
        files = []
        pathes = path.split("/")
        print(pathes)
        for p in pathes:
            if p == "..":
                if files:
                    files.pop()
                continue
            elif not p or "." == p:
                continue
            files.append(p)
        return "/" + "/".join(files)
            

        