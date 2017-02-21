__author__ = 'jiangxiaowei-006'
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    if i==0 and j==0:
                        perimeter+=4
                    elif i==0 and j!=0:
                        if grid[i][j-1]==1:
                            perimeter+=2
                        else:
                            perimeter+=4
                    elif i!=0 and j==0:
                        if grid[i-1][j]==1:
                            perimeter+=2
                        else:
                            perimeter+=4
                    else:
                        if grid[i-1][j]!=1 and grid[i][j-1]!=1:
                            perimeter+=4
                        elif grid[i-1][j]==1 and grid[i][j-1]!=1:
                            perimeter+=2
                        elif grid[i-1][j]!=1 and grid[i][j-1]==1:
                            perimeter+=2
        return perimeter

if __name__=="__main__":
    grid=[[0,1,0,0], [1,1,1,0], [0,1,0,0], [1,1,0,0]]
    s=Solution()
    print s.islandPerimeter(grid)


