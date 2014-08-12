from sys import exit

class Scene(object):

    def enter(self):
        pass
        

class Engine(object):

    def __init__(self, scene_map):
        pass
        
    def play(self):
        pass
        
class Death(Scene):

    def enter(self):
        pass
        
class CentralCorridor(Scene):

    def enter(self):
        print "Aliens have invaded the space ship! You are the ship's only hope!"
        print "You run into the central corridor of the ship hoping to make it to the escape pod."
        print "Alas! There is a Gothon standing in the middle of the corridor!"
        print """\'Puny human! Answer this riddle and you may pass! 
                    I'm the part of a bird that's not in the sky,
                    I can swim in th eocean and remain dry.
                    What am I\'?"""
        answer = raw_input('> ')
        if answer == 'A bird\'s shadow':
            print "The Gothon steps aside and let's you pass."
            #LaserWeaponArmory()
        else:
            pass
            #Death()
            
test = CentralCorridor()
test
class LaserWeaponArmory(Scene):

    def enter(self):
        pass
        
class TheBridge(Scene):

    def enter(self):
         pass
         
class EscapePod(Scene):

    def enter(self):
        pass
        
        
class Map(object):

    def __init__(self, start_scene):
        pass
        
    def next_scene(self, scene_name):
        pass
        
    def opening_scene(self):
        pass
        
        
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
