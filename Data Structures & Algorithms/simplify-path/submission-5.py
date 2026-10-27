import re

class Solution:
    def simplifyPath(self, path: str) -> str:
        path_cmpt = re.split("/+", path)[1:]

        if path_cmpt[-1] == "":
            path_cmpt.pop()

        simplified_path = []
        # print(path_cmpt)
        # print()
        for cmpt in path_cmpt:
            # print(cmpt)
            if cmpt == ".":
                continue
            elif cmpt == "..":
                if simplified_path:
                    simplified_path.pop()
                    simplified_path.pop()
            else:
                simplified_path.append("/")
                simplified_path.append(cmpt)
            # print(simplified_path)
        # when its just the root directory, the is just /
        if not simplified_path: 
            simplified_path.append("/")
        



        return "".join(simplified_path)