class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(image, i , j , val , color) :
            if(i < 0 or i >= len(image) or j < 0 or j >= len(image[0]) or image[i][j] == color or image[i][j] != val) :
                return 
            image[i][j] = color

            dfs(image,i-1,j,val,color)
            dfs(image,i+1,j,val,color)
            dfs(image,i,j-1,val,color)
            dfs(image,i,j+1,val,color)
        
        val = image[sr][sc]
        dfs(image,sr,sc,val,color)
        return image