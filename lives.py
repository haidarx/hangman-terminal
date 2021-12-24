import textwrap
import os
import time

Live0 = textwrap.dedent("""
 ________
|       |
|     (*_*)
|       |
|    ---|---
|      /\\
|     /  \\
|    /    \\
|
|  
----
"""
)
Live1 = textwrap.dedent("""
 ________
|       |
|     (*_*)
|       |
|    ---|---
|      /
|     /  
|    /    
|
|  
----
"""
)

Live2 = textwrap.dedent("""
 ________
|       |
|     (*_*)
|       |
|    ---|---
|
|
|
|
|  
----
"""
)

Live3 = textwrap.dedent("""
 ________
|       |
|     (*_*)
|       |
|    ---|
|
|
|
|
|  
----
"""
)

Live4 = textwrap.dedent("""
 ________
|       |
|     (*_*)
|       |
|       |
|
|
|
|
|  
----
"""
)

Live5 = textwrap.dedent("""
 ________
|       |
|     (*_*)
|       
|    
|
|
|
|
|  
----
"""
)

Live6 = textwrap.dedent("""
 ________
|       |
|
|
|
|
|
|
|
|  
----
"""
)

hangmanDrawing = [Live0, Live1, Live2, Live3, Live4, Live5, Live6]
nLives = 6

def getLives(live):
    return hangmanDrawing[live]

def drawLives(live):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(getLives(live))
    print(f"Live: {live}")
    # time.sleep(1)
    


class drawLoop:
    def __init__(self, n= 6):
        self.n = n

    def draw(self):
        for i in range(self.n, -1, -1):
            drawLives(i)
            time.sleep(1)

    def reverse(self):
        for j in range(0, self.n + 1):
           drawLives(j)
           time.sleep(1)
        




if __name__ == "__main__":
    print("Test Loop!\n")
    time.sleep(2)
    d = drawLoop(6)
    d.draw()
    d.reverse()
