# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 02:03:32 2022

@author: nacer
"""

"""
Problem link : https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/
"""

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        output = 0
        m = len(grid)
        n = len(grid[0])
        
        while True:
            lands, minCell = FindLandsAndMin(grid)
            neighs = neighbors(grid, minCell)
            numLands = len(lands)

            toRemove = (-1,-1)
            
            if numLands != 1:
                return output
            
            if output == 0:
                bridge = detectBridges(grid, lands)
                if bridge:
                    return 1
            
            if len(neighs)>0:
                toRemove = neighs[0]
                
            if toRemove != (-1,-1):
                grid[toRemove[0]][toRemove[1]] = 0
                output += 1
            else:
                grid[minCell[0]][minCell[1]] = 0
                output += 1

                
def detectBridges(grid,lands):
    for land in lands:
        for cell in land:
            if len(neighbors(grid, cell)) == 2:
                grid[cell[0]][cell[1]] = 0
                l,_ = FindLandsAndMin(grid)
                if len(l) != 1:
                    return cell
                grid[cell[0]][cell[1]] = 1
    return False

def FindLandsAndMin(grid):
    m = len(grid)
    n = len(grid[0])
    lands = []
    minNeighbors = -1
    minCell = (-1,-1)
    for x in range(m):
        for y in range(n):
            if grid[x][y]:
                cell = (x,y)
                neighs = neighbors(grid,cell)
                if minNeighbors > len(neighs) or minNeighbors == -1:
                    minNeighbors = len(neighs)
                    minCell = cell
                    if minNeighbors > 0:
                        toRemove = neighs[0]
                    else:
                        toRemove = (-1,-1)
                if not cellInLands(lands, cell):
                    lands.append(explore(grid,cell))
    return lands, minCell

def neighbors(grid,cell):
    m = len(grid)
    n = len(grid[0])
    x, y = cell
    possibleNeighbors = [ (x-1,y), (x+1,y), (x,y-1), (x,y+1)]
    neighbors = []
    for neighbor in possibleNeighbors:
        neighbor_x = neighbor[0]
        neighbor_y = neighbor[1]
        neighbor_x_valid = neighbor_x >= 0 and neighbor_x < m
        neighbor_y_valid = neighbor_y >= 0 and neighbor_y < n
        if neighbor_x_valid and neighbor_y_valid and grid[neighbor_x][neighbor_y] == 1:
            neighbors.append(neighbor)
    return neighbors
        
def explore(grid, cell):
    connected_cells = [cell]
    to_explore = [cell]
    while len(to_explore) > 0:
        explorer = to_explore.pop()
        neighbs = neighbors(grid,explorer)
        for neighbor in neighbs:
            if neighbor not in connected_cells:
                connected_cells.append(neighbor)
                to_explore.append(neighbor)
    return connected_cells

def cellInLands(lands, cell):
    for land in lands:
        if cell in land:
            return True
    return False