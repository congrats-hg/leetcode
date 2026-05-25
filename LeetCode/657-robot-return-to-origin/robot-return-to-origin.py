class Solution:
    def judgeCircle(self, moves: str) -> bool:
        origin = {
            "x": 0,
            "y": 0
        }

        for move in moves:
            if move == "R":
                origin["x"] += 1
            elif move == "L":
                origin["x"] -= 1
            elif move == "U":
                origin["y"] += 1
            elif move == "D":
                origin["y"] -= 1
        
        if origin == {'x': 0, 'y': 0}:
            return True
        
        return False