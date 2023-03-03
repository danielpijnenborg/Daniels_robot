import random
from ..bot_control import Move

class Daniels_Bot:
    def get_name(self):
        return "Picasso"

    def get_contributor(self):
        return "Daniel"
     
    def __init__(self):
       self.last_tile_x = -1
       self.last_tile_y = -1
        
    def enemy_on_tile (self, enemies, x,y):
        if self.last_tile_x == x and self.last_tile_y == y:
          return 0 # don't go back
        for e in enemies:
            xe = e['position'][0]
            ye = e['position'][1]
            if xe == x and ye == y: return 0
        return 1
        
    def get_bot_score (self,grid,enemy):
        l = grid.shape[0]
        score = 0;
        for x in range (l):
            for y in range (l):
                if grid[y][x] == enemy:
                    score += 1
        return score

    def score_outcome(self,id,tile, grid):
        l = grid.shape[0]
        if tile == 0 : return 0.10*l*l         # take empty tile
        elif tile == id: return 1              # take own tile with risk of two bots result in 0
        elif (id - tile) % 3 == 2 : return self.get_bot_score(grid, tile) # take tile from other
        elif (id - tile) % 3 == 1 : return 3 # clear tile from other
        else : return 2                        # goto other without take with chance of two bots result in 0

    def determine_next_move(self, grid, enemies, game_info):
        x = self.position[0]
        y = self.position[1]
        l = grid.shape[0] # always square
        max_move = [Move.STAY]
        max_score = 0

        if y < l - 1:
            score = self.score_outcome(self.id, grid[y+1][x], grid) * self.enemy_on_tile (enemies, x,y+1)
            if score == max_score:
                max_move+= [Move.UP]
            if score > max_score:
                max_move = [Move.UP]
                max_score = score
                
        if y > 0:
            score = self.score_outcome(self.id, grid[y-1][x], grid) * self.enemy_on_tile (enemies, x,y-1)
            if score == max_score:
                max_move+= [Move.DOWN]
            if score > max_score:
                max_move = [Move.DOWN]
                max_score = score
                
        if x < l - 1:
            score = self.score_outcome(self.id, grid[y][x+1], grid) * self.enemy_on_tile (enemies, x+1,y)
            if score == max_score:
                max_move+= [Move.RIGHT]
            if score > max_score:
                max_move = [Move.RIGHT]
                max_score = score
                 
        if x > 0:
            score = self.score_outcome(self.id, grid[y][x-1], grid) * self.enemy_on_tile (enemies, x-1,y+1)
            if score == max_score:
                max_move+= [Move.LEFT]
            if score > max_score:
                max_move = [Move.LEFT]
                max_score = score     
               
        self.last_tile_x = self.position[0]
        self.last_tile_y = self.position[1]
        # Pick one of the possible moves randomly to reduce getting stuck in a loop
        return max_move[random.randint(0, len(max_move) - 1)]
