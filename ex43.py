from sys import exit
import time
import textwrap

class Scene(object):
   # 
   # def __init__(self):

        #self.items = []

    def enter(self):
        #print "You have entered"
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
    
    #def __init__(self):
        #super(CentralCorridor, self).__init__()
    
    def enter(self):
        centralcorridor_text = """Aliens have invaded the space ship! You are the ship's only hope!"
        You run into the central corridor of the ship hoping to make it to the escape pod."
        Alas! There is a Gothon standing in the middle of the corridor!"
        \'Puny human! Answer this riddle and you may pass! 
            I'm the part of a bird that's not in the sky,
            I can swim in th eocean and remain dry.
            What am I\'?"""
        answer = raw_input('> ')
        if answer == 'A bird\'s shadow':
            
            print "The Gothon steps aside and lets you pass."
            print "You have obtained item Laser Gun."
            #self.items.append('Laser Gun')
            #LaserWeaponArmory()
        else:
            pass
            #Death()
            
test = CentralCorridor()
test.enter()


class LaserWeaponArmory(Scene):

    def enter(self):
        print "You have entered the Laser Weapon Armory."
        print "You know there is a bomb in the vault in the room."
        print "Only the captain knows the code for the keypad to the vault."
        print "The captain is likely dead so it is up to you to figure it out."
        
        code = str(raw_input('Input 4 numbers please.\n\n> '))
        
        allowed_numbers = set('0123456789')
        
        if len(code) > 4:
            raw_input('Please type in 4 numbers.\n\n> ')
        elif len(code) < 4:
            raw_input('Please type in 4 numbers.\n\n> ')
        elif set(code).issubset(allowed_numbers) == False:
            raw_input('Please type in 4 numbers.\n\n> ')
        if code == '2389':
            print "You have unlocked the vault!."
            print "You have obtained item 'Bomb', 'Grenade' and item 'Key'"
            #items.append['Bomb', 'Key']
            #TheBridge()
        else: 
            print "Wrong code."
            # I want a person to get three tries. then it's game over.
            
#test2 = LaserWeaponArmory()
#test2.enter()
        
class TheBridge(Scene):

    def enter(self):
        print "\n\n\nAll you need to do is cross this bridge and get to the escape pods!"
        print "Oh no! There is a Gothon standing in your way."
        print "The Gothon snarls. With a gleam in his eye he reaches for his club."
        print "ROAAAAAAAAAAAAAAAAAR! The Gothon charges."
        
        while True: 
            use_gun = raw_input('Type a command\n\n> ')
         
            if "gun" in use_gun:
                print "You quickly remember you picked up a laser gun."
                print "You aim at the Gothon and start shooting like crazy."
                print "PEW PEW PEW!"
                print "The Gothon screams in agony as he clutches his laser wounds."
                print "The Gothon collapses and bleeds a gooey green substance."
                print "It is over. The Gothon is dead."
                print "You feel bad for him for a second and then hear the ship's alarms."
                print "Quickly you run towards the escape pod room."
                #EscapePod
            elif "grenade" in use_gun:
                print "You remember you picked up a grenade in the previous room."
                print "You quickly get it out of your pack and pull the pin"
                print "You throw it in the Gothon's direction and dive behind a pillar"
                print "BOOOOOOOOOOOOMBABABABABABABABAOOOOOOMOBOOOOOM"
                print "It's a miracle you're still alive and not deaf."
                print "You peek out from behind the pillar."
                print "Gothon guts. Gothon guts everywhere."
                print "The good news is the coast is clear."
                print "You make a run for the escape pod."
                #EscapePod
            elif "bomb" in use_gun:
                print "No, no. That's for blowing up the ship as you escape."
                continue
            else:
                print "You should have thought about the items you have picked up!"
                print "As in the weapons!"
                print "Oh well, game over for you!"
                #DeathScene

#bridge_test = TheBridge()
#bridge_test.enter()
         
class EscapePod(Scene):

    def enter(self):
        print "You burst into the escape pod room."
        print "There are 5 escape pods available." 
        print "You have a key for one of the escape pods and very little time left."
        escape = str(raw_input('Which escape pod do you pick (1-5)?\n\n> '))
        
        if escape == '1':
            pass
            #death
        elif escape == '2':
            pass
            #death
        elif escape == '3':
            pass
            #death
        elif escape == '4':
            print "\n\n\nThe key turns and the escape pod opens!"
            print "You jump inside and hit the green start button."
            print "Just before the escape pod closes you hurl the bomb into the space ship."
            print "As the escape pod begins to leave the ship you see Gothons running up."
            print "One of them picks up the bomb and looks at it curiously."
            print "The escape pod zooms away and the ship explodes."
            print "It's over. You made it. Congratulations."
            print "You take a moment to register what just happened and sink into your seat."
            print "'Everyone I know is dead.'"
            print "You begin to cry uncontrollably as the pod makes it's way down to your home planet."
        elif escape == '5':
            pass
            #death

escape_test = EscapePod()
escape_test.enter()

        
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
