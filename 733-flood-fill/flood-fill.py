class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        temp = image[sr][sc]
        if temp == color:
            return image
        def fill(r,c):
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != temp:
                return
            image[r][c] = color
            fill(r - 1,c)
            fill(r,c - 1)
            fill(r + 1,c)
            fill(r,c + 1)
        fill(sr,sc)
        return image


