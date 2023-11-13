#Posted in the Programming problems folder under easy
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        w = len(image)
        h = len(image[0])
        replacing = image[sr][sc]
        kyu = []
        kyu.append((sr,sc))
        while kyu:
            cur = kyu.pop(0)
           
            if cur[0] >= w or cur[0] < 0 or cur[1] >= h or cur[1] < 0:
                continue
            else:
                if image[cur[0]][cur[1]] == color:
                    continue
                
                elif image[cur[0]][cur[1]] == replacing:
                    image[cur[0]][cur[1]] = color
                    kyu.append((cur[0] + 1, cur[1]))
                    kyu.append((cur[0] - 1, cur[1]))
                    kyu.append((cur[0], cur[1] + 1))
                    kyu.append((cur[0], cur[1] - 1))
        return image
