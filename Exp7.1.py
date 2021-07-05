'''
7.1)
Write a function ball_collide that takes two balls as parameters and computes if they are colliding. 
Your function should return a Boolean representing whether or not the balls are colliding. 
Hint: Represent a ball on a plane as a tuple of (x, y, r), r being the radius 
If (distance between two balls centers) <= (sum of their radii) then (they are colliding).
'''

import math
def distance(point1, point2):
    return math.sqrt((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2)

def ball_collide(ball1,ball2):
    dst = distance((ball1[0],ball1[1]),(ball2[0],ball2[1]))
    total_radius = ball1[2] + ball2[2]
    
    return dst <= total_radius
    
if __name__ == "__main__":
    ball1 = tuple(map(int,input('Enter center coordinates and radius of Ball 1: ').split()))
    ball2 = tuple(map(int,input('Enter center coordinates and radius of Ball 2: ').split()))
    
    if ball_collide(ball1,ball2):
        print('Balls Collide')
    else:
        print('Balls don\'t Collide')
    
'''
Output1:
Enter center coordinates and radius of Ball 1: -2 -2 3
Enter center coordinates and radius of Ball 2: 1 1 3
Balls Collide
Output2:
Enter center coordinates and radius of Ball 1: 5 5 3
Enter center coordinates and radius of Ball 2: 7 53 7
Balls don't Collide
'''
