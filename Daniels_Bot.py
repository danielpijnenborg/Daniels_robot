import random
from ..bot_control import Move

class Daniels_Bot:
    def get_name(self):
        return "Picasso"

    def get_contributor(self):
        return "Daniel Pijnenborg"
        
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
        elif abs(id - tile) % 3 == 2 : return self.get_bot_score(grid, tile) # take tile from other
        elif abs(id - tile) % 3 == 1 : return 0.5 * self.get_bot_score(grid, tile) # clear tile from other
        else : return 2                         # goto other without take with chance of two bots result in 0

    def determine_next_move(self, grid, enemies, game_info):
        # Check each adjacent tile and see if it can overwrite that
        # tile by moving there. If it finds one, maybe move there. Otherwise
        # do a random movement

        x = self.position[0]
        y = self.position[1]
        l = grid.shape[0] # always square
        max_move = [Move.STAY]
        max_score = 0

        if y < l - 1:
            score = self.score_outcome(self.id, grid[y+1][x], grid)
            if score == max_score:
                max_move+= [Move.UP]
            if score > max_score:
                max_move = [Move.UP]
                max_score = score
                
        if y > 0:
            score = self.score_outcome(self.id, grid[y-1][x], grid)
            if score == max_score:
                max_move+= [Move.DOWN]
            if score > max_score:
                max_move = [Move.DOWN]
                max_score = score
                
        if x < l - 1:
            score = self.score_outcome(self.id, grid[y][x+1], grid)
            if score == max_score:
                max_move+= [Move.RIGHT]
            if score > max_score:
                max_move = [Move.RIGHT]
                max_score = score
                 
        if x > 0:
            score = self.score_outcome(self.id, grid[y][x-1], grid)
            if score == max_score:
                max_move+= [Move.LEFT]
            if score > max_score:
                max_move = [Move.LEFT]
                max_score = score       

        # score = self.score_outcome(self.id, grid[y][x], grid)
        # if score > max_score:
            # max_move = Move.STAY
            # max_score = score  

        # Pick one of the possible moves randomly
        return max_move[random.randint(0, len(max_move) - 1)]

#   def __init__(self):
#       self.move_ydir = -1
#       self.move_xdir = -1
#
#  def determine_next_move(self, grid, enemies, game_info):
#      x = self.position[0]
#      y = self.position[1]
#      l = grid.shape[0] # always square
#
#      if y + self.move_ydir < l and y + self.move_ydir >= 0:
#          if self.move_ydir > 0:
#              return Move.UP
#          else:
#              return Move.DOWN
#      else:
#          self.move_ydir = self.move_ydir * -1
#          if x + self.move_xdir < l and x + self.move_xdir >= 0:
#              if self.move_xdir > 0:
#                  return Move.RIGHT
#              else:
#                  return Move.LEFT
#          else:
#              self.move_xdir = self.move_xdir * -1
#              if self.move_xdir > 0:
#                  return Move.RIGHT
#              else:
#                  return Move.LEFT
#          
