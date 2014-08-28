from sys import exit
import time
import textwrap
import string
from random import randint

class Scene(object):
    
    def __init__(self):

        self.description = 'scene'
       

    def enter(self, player):
        print "\n\nYou have entered %s." % self.description
        
        
    def slow_print(self, text):
        lines = text.split('\n')
        for line in lines:
            print line
            time.sleep(0.1)
            
        

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map
            
        
    def play(self, player):
        current_scene = self.scene_map.opening_scene()
        
        
        while current_scene:
           # if current_scene:
                print "\n ------------------"
                next_scene_name = current_scene.enter(player)
                current_scene = self.scene_map.next_scene(next_scene_name)
           # if current_scene == None:
              #  break
        
class Death(Scene):
    
    def __init__(self):
        self.dead = 'Game over!'
        self.code_death = textwrap.dedent(
        """\n\n
        You have taken too long to guess the code! Gothons appear out of 
        nowhere and throw you out of the ship into space. GAME OVER!""")
        self.bridge_death = textwrap.dedent(
        """\n\n 
        As you stand there frozen in fear, more Gothons show up and it's 
        game over for you!""")
        self.pod_death = textwrap.dedent(
        """\n\n
        WRONG! It's too late now. Gothons have surrounded you. Game over!
        """)
         

    def enter(self, player):
        print "\n\n%s." % self.dead
        return None
        
        
        
class CentralCorridor(Scene):
    
    def __init__(self):
        #super(CentralCorridor, self).__init__()
      
        self.central_text = textwrap.dedent(
        """\n\n
        Aliens have invaded the space ship! You are the ship's only hope!
        You run into the central corridor of the ship hoping to make it to
        the escape pod. Alas! There is a Gothon standing in the middle of the
        corridor! \'Puny human! Answer this riddle and you may pass! 
            I'm the part of a bird that's not in the sky,
            I can swim in the ocean and remain dry.
            What am I\'?""")
        self.riddle_text = textwrap.dedent(
        """ \n\n
        The Gothon steps aside and lets you pass.
        You have obtained item Laser Gun.""")
        self.description = 'Central Corridor'
        self.scenes = 'scenes'
        self.dead = textwrap.dedent(
        """\n\n 
        'THAT IS THE WRONG ANSWER!' The Gothon booms. Then he grabs you 
        and drags you off to be a prisoner of war.""")
        self.found_item = 'gun'
       
    
    def enter(self, player):
        super(CentralCorridor, self).enter(player)
        
    
        self.slow_print(self.central_text)
        answer = str(raw_input('> '))
        answer = answer.lower()
        if answer == 'a bird\'s shadow':
            
            print self.riddle_text
            player.obtain_item(self.found_item)
            print player.items
            return 'laser_weapon_armory'
        else:
            return 'death'
            

class LaserWeaponArmory(Scene):
    
    def __init__(self):
       # super(LaserWeaponArmory, self).__init__(scenes)
        self.laser_entry = textwrap.dedent(
        """\n\n
        You know there is a bomb in the vault in the room. Only the
        captain knows the code for the keypad to the vault. The captain
        is likely dead so it is up to you to figure it out!""")
        self.description = 'Laser Weapon Armory'
        self.found_item = 'bomb'

    def enter(self, player):
        super(LaserWeaponArmory, self).enter(player)
        
        self.slow_print(self.laser_entry)
        
        guesses = ''
        print "Input 4 numbers please.\n\n"
        code = "%d%d%d%d" %(randint(1,9), randint(1,9), randint(1,9), randint(1,9))
        cheat_code = "%d%d%d%d" % (1, 2, 3, 4)
        while True:

            guess = str(raw_input('> '))
            guesses = guesses + guess
        
            allowed_numbers = set('0123456789')
        
            if len(guess) > 4:
                raw_input('Please type in 4 numbers.\n\n> ')
            elif len(guess) < 4:
                raw_input('Please type in 4 numbers.\n\n> ')
            elif set(guess).issubset(allowed_numbers) == False:
                raw_input('Please type in 4 numbers.\n\n> ')
            if guess == cheat_code:
                print "You have unlocked the vault!."
                player.obtain_item('Key')
                return 'the_cheatbridge'
                
            if guess == code:
                print "You have unlocked the vault!."
                print "You have obtained item 'Bomb', 'Grenade' and item 'Key'"
                player.obtain_item('Bomb')
                player.obtain_item('Key')
                player.obtain_item('Grenade')
                print player.items
                return 'the_bridge'
            else: 
                print "Wrong code."
                # I want a person to get three tries. then it's game over.
                if len(guesses) == len(guess) * 3:
                    print "\nYou took too long! A Gothon ate you."
                    print "GAME OVER!"
                    exit()
                    
                    
class TheCheatBridge(Scene):
    
    def __init__(self):
        self.cheatbridge_entry = textwrap.dedent(
        """\n\n
        All you need to do is cross the bridge and get to the escape pods!
        Oh no! There is a Gothon standing in your way. The Gothon snarls. 
        With a gleam in its eye it reaches for its club. 
        'ROAAAAAAAAAAAAAAAAAAR!' The Gothon charges.""")
        self.fight_text = textwrap.dedent(
        """\n\n
        You choose to fight the Gothon. You bring your fists up ready to 
        show it who's boss. The Gothon stops in it's track and let's out a
        loud howl. Is he... is he laughing? Your confidence drops a little and 
        you lower your fists. The Gothon howls and howls and drops to it's
        knees. You look around nerrvously but no other Gothons are around. 
        You begin to tiptoe your way around the Gothon. The Gothon continues
        to snort and howl slamming his club repeatedly on the ground. As soon 
        as you are on the other side of the Gothon you make a break for it. 
        The howling stops. Your heart begins to pound furiously in fear and
        you try to will your legs to go faster. You leap through the entrance of 
        the escape pod and yell out 'COMPUTER CLOSE DOOR'. The Gothon snarls
        and reaches out and grabs the back of your suit just as the escape pod's
        metal door slams shut slicing off it's arm. You stare wide-eyed at the door
        and the Gothon's severed arm. You pry your suit out of the Gothon's
        claws and back away.""")
        self.dodge_text = textwrap.dedent(
        """\n\n
        The Gothon advances towards you with his club. You veer left as the Gothon swings 
        towards you. The Gothon momentarily loses sight of you and you make a break 
        for the escape pod room. Just as you are about to reach the entrance of the
        escape pod room the Gothon wacks you on the side of your head with 
        his club. You fall unconscious and the Gothon drags you away.""")
        self.run_text = textwrap.dedent(
        """\n\n
        You make a break for the escape pod room which is behind the Gothon. 
        The Gothon stops in it's tracks when it sees you running towards him. 
        He takes a hard swing and knocks you out with his club.""")
        self.description = 'The Bridge'
        
        
        
    def enter(self, player):
        super(TheCheatBridge, self).enter(player)
        self.slow_print(self.cheatbridge_entry) 
        
        what_to_do = str(raw_input("Available commands: Fight, Dodge, Run\n"))
        what_to_do = what_to_do.lower()
        
        if what_to_do == 'fight':
            self.slow_print(self.fight_text)
            return 'escape_pod'
        if what_to_do == 'dodge':
            self.slow_print(self.dodge_text)
            return 'death'
        if what_to_do == 'run':
            self.slow_print(self.run_text)
            return 'death'
            

        
class TheBridge(Scene):
    
    def __init__(self):
       # super(TheBridge, self).__init__()
        self.bridge_entry = textwrap.dedent(
        """ \n\n
        All you need to do is cross this bridge and get to the esape pods!
        Oh no! There is a Gothon standing in your way. The Gothon snarls.
        With a gleam in its eye it reaches for its club. 
        'ROAAAAAAAAAAAAAAAAAAAAAAR!' The Gothon charges.""")
        self.gun_text = textwrap.dedent(
        """\n\n
        You quickly remember you picked up a laser gun earlier. You aim 
        at the Gothon and start shooting like crazy.
        PEW PEW PEW!
        The Gothon screams in agony as he clutches his laser wounds. The
        Gothon collapses and bleeds a gooey green substance. It is over.
        The Gothon is dead. You feel bad for him for a second and then 
        hear the ship's alarms. You hurriedly run towards the escape pod
        room, stepping over the suffering Gothon.""")
        self.grenade_text = textwrap.dedent(
        """\n\n
        You remember you picked up a grenade in the previous room. You 
        quickly get it out of your pack and pull the pin. You throw it in 
        direction of the Gothon and dive behind a pillar. 
        BOOOOOOOOOOOOOOMBABABABABBABABABABABBAABBOOOOOOMBOOOOOOOM!
        It's a miracle you're sitll alive and not deaf. You peek out from 
        behind the pillar. Gothon guts. Gothon guts everywhere.
        The good news is the coast is clear. You make a break for the escape
        pod, being careful not to slip on any Gothon guts.""")
        
        self.description = 'The Bridge'

    def enter(self, player):
        super(TheBridge, self).enter(player)
        self.slow_print(self.bridge_entry)
        
        while True: 
            use_gun = raw_input('Type a command\n\n> ')
         
            if "gun" in use_gun:
                self.slow_print(self.gun_text)
                return 'escape_pod'
            elif "grenade" in use_gun:
                self.slow_print(self.grenade_text)
                return 'escape_pod'
            elif "bomb" in use_gun:
                print "No, no. That's for blowing up the ship as you escape."
                continue
            else:
                print "You should have thought about the items you have picked up!"
                print "As in the weapons!"
                print "Oh well, game over for you!"
                return 'death'


         
class EscapePod(Scene):

    def __init__(self):
      #  super(EscapePod, self).__init__()
        self.description = 'Escape Pod Room'
        self.escape_entry = textwrap.dedent(
        """ \n\n
        You burst into the escape pod room. There are five escape pods 
        available. You have the key for one of the escape pods and very 
        little time left.""")
        self.pod_text = textwrap.dedent(
        """\n\n
        The key turns and the escape pod opens! You jump inside and hit 
        the green start button. Just before the escape pod closes you
        hurl the bomb into the space ship. As the escape pod begins to 
        leave the ship you see Gothons running up. One of them picks up 
        the bomb and looks at it curiously. The escape pod zooms away and 
        the ship explodes. It's over. You made it. Congratulations. You
        take a moment to register what just happened and sink into your 
        seat. 'Everyone I know is dead.' You begin to cry uncontrollably
        as the pod makes it's way down to your home planet. """)

    def enter(self, player):
        super(EscapePod, self).enter(player)
        self.slow_print(self.escape_entry)
        escape = str(raw_input('Which escape pod do you pick (1-5)?\n\n> '))
        
        if escape == '1':
            pass
            return 'death'
        elif escape == '2':
            pass
            return 'death'
        elif escape == '3':
            pass
            return 'death'
        elif escape == '4':
            self.slow_print(self.pod_text)
            return None
            
        elif escape == '5':
            pass
            return 'death'


        
class Map(object):

    scenes = {'central_corridor' : CentralCorridor(),
              'laser_weapon_armory' : LaserWeaponArmory(),
              'the_bridge' : TheBridge(),
              'escape_pod' : EscapePod(),
              'death' : Death(),
              'the_cheatbridge': TheCheatBridge()
              }
              
              
    def __init__(self, start_scene):
        self.start_scene = start_scene
        
    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)
        
    def opening_scene(self):
        return self.next_scene(self.start_scene)
        
   
class Player(object):
    
    def __init__(self):
        self.items = []
        
    def obtain_item(self, found_item):
        supplies = self.items.append(found_item)
        
        
    def use_item(self, found_item):
        pass

def ask_user_question():

    while True:
        print "\n Would you like to play again?"
        response = str(raw_input("y or n?\n> "))
        response = response.lower()
        if response == 'y':
            return response
        if response == 'n':
            exit()
        else:
            continue

response = "y"
while True:
    
    if response == "y":        
        a_player = Player()
        a_map = Map('central_corridor') 
        a_game = Engine(a_map)
        a_game.play(a_player)
        ask_user_question()
    
        

