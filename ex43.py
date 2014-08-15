from sys import exit
import time
import textwrap
import string

class Scene(object):
    
    def __init__(self):

        self.items = []
        self.description = 'scene'

    def enter(self):
        print "\n\nYou have entered %s." % self.description
        
        
    def slow_print(self, text):
        lines = text.split('\n')
        for line in lines:
            print line
            time.sleep(0.1)
        
        

class Engine(object):

    def __init__(self, scene_map):
        pass
        
    def play(self):
        pass
        
class Death(Scene):

    def enter(self):
        pass
        
class CentralCorridor(Scene):
    
    def __init__(self):
        super(CentralCorridor, self).__init__()
      
        self.central_text = textwrap.dedent(
        """\n\n\n
        Aliens have invaded the space ship! You are the ship's only hope!
        You run into the central corridor of the ship hoping to make it to
        the escape pod. Alas! There is a Gothon standing in the middle of the
        corridor! \'Puny human! Answer this riddle and you may pass! 
            I'm the part of a bird that's not in the sky,
            I can swim in the ocean and remain dry.
            What am I\'?""")
        self.riddle_text = textwrap.dedent(
        """ \n\n\n
        The Gothon steps aside and lets you pass.
        You have obtained item Laser Gun.""")
        self.description = 'Central Corridor'
        self.items.append('Laser Gun')
    
    def enter(self):
        super(CentralCorridor, self).enter()
        
    
        self.slow_print(self.central_text)
        answer = str(raw_input('> '))
        answer = answer.lower()
        if answer == 'a bird\'s shadow':
            
            print self.riddle_text
            #self.items.append('Laser Gun')
            #LaserWeaponArmory()
        else:
            pass
            #Death()
            
test = CentralCorridor()
test.enter()


class LaserWeaponArmory(Scene):
    
    def __init__(self):
        super(LaserWeaponArmory, self).__init__()
        self.laser_entry = textwrap.dedent(
        """\n\n\n
        You know there is a bomb in the vault in the room. Only the
        captain knows the code for the keypad to the vault. The captain
        is likely dead so it is up to you to figure it out!""")
        self.description = 'Laser Weapon Armory'

    def enter(self):
        super(LaserWeaponArmory, self).enter()
        
        self.slow_print(self.laser_entry)
        
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
            
test2 = LaserWeaponArmory()
test2.enter()
        
class TheBridge(Scene):
    
    def __init__(self):
        super(TheBridge, self).__init__()
        self.bridge_entry = textwrap.dedent(
        """ \n\n\n
        All you need to do is cross this bridge and get to the esape pods!
        Oh no! There is a Gothon standing in your way. The Gothon snarls.
        With a glean in it's eye he reaches for his club. 
        'ROAAAAAAAAAAAAAAAAAAAAAAR!' The Gothon charges.""")
        self.gun_text = textwrap.dedent(
        """\n\n\n
        You quickly remember you picked up a laser gun earlier. You aim 
        at the Gothon and start shooting like crazy.
        PEW PEW PEW!
        The Gothon screams in agony as he clutches his laser wounds. The
        Gothon collapses and bleeds a gooey green substance. It is over.
        The Gothon is dead. You feel bad for him for a second and then 
        hear the ship's alarms. You hurriedly run towards the escape pod
        room, stepping over the suffering Gothon.""")
        self.grenade_text = textwrap.dedent(
        """\n\n\n
        You remember you picked up a grenade in the previous room. You 
        quickly get it out of your pack and pull the pin. You throw it in 
        direction of the Gothon and dive behind a pillar. 
        BOOOOOOOOOOOOOOMBABABABABBABABABABABBAABBOOOOOOMBOOOOOOOM!
        It's a miracle you're sitll alive and not deaf. You peek out from 
        behind the pillar. Gothon guts. Gothon guts everywhere.
        The good news is the coast is clear. You make a break for the escape
        pod, being careful not to slip on any Gothon guts.""")
        
        self.description = 'The Bridge'

    def enter(self):
        super(TheBridge, self).enter()
        self.slow_print(self.bridge_entry)
        
        while True: 
            use_gun = raw_input('Type a command\n\n> ')
         
            if "gun" in use_gun:
                self.slow_print(self.gun_text)
                #EscapePod
            elif "grenade" in use_gun:
                self.slow_print(self.grenade_text)
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
    
    def __init__(self):
        super(EscapePod, self).__init__()
        self.description = 'Escape Pod Room'
        self.escape_entry = textwrap.dedent(
        """ \n\n\n
        You burst into the escape pod room. There are five escape pods 
        available. You have the key for one of the escape pods and very 
        little time left.""")
        self.pod_text = textwrap.dedent(
        """\n\n\n
        The key turns and the escape pod opens! You jump inside and hit 
        the green start button. Just before the escape pod closes you
        hurl the bomb into the space ship. As the escape pod begins to 
        leave the ship you see Gothons running up. One of them picks up 
        the bomb and looks at it curiously. The escape pod zooms away and 
        the ship explodes. It's over. You made it. Congratulations. You
        take a moment to register what just happened and sink into your 
        seat. 'Everyone I know is dead.' You begin to cry uncontrollably
        as the pod makes it's way down to your home planet. """)

    def enter(self):
        super(EscapePod, self).enter()
        self.slow_print(self.escape_entry)
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
            self.slow_print(self.pod_text)
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
