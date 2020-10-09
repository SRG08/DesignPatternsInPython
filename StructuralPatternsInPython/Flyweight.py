'''
Credits:
Darinka Zobenica
'''

# The Flyweight Pattern calls for a common pool when many instances of an object with the same value could exist

# Analogy : Bullets while firing , coordinates and velocity

class BulletContext:
    def __init__(self, x, y, z, velocity):
        self.x = x
        self.y = y
        self.z = z
        self.velocity = velocity

class BulletFlyweight:
    def __init__(self):
        self.bullets = []

    def bullet_factory(self, x, y, z, velocity):
        bull = [b for b in self.bullets if b.x==x and b.y==y and b.z==z and b.velocity==velocity]
        if not bull:
            bull = BulletContext(x,y,z,velocity)
            self.bullets.append(bull)
        else:
            bull = bull[0]

        return bull

    def print_bullets(self):
        print('Bullets:')
        for bullet in self.bullets:
            print(str(bullet.x)+' '+str(bullet.y)+' '+str(bullet.z)+' '+str(bullet.velocity))


if __name__ == "__main__":
    bf = BulletFlyweight()
    # adding bullets
    bf.bullet_factory(1,1,1,1)
    bf.bullet_factory(1,2,5,1)
    bf.print_bullets()