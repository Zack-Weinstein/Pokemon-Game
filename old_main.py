# UNLINTED CODE

'''
------------- TO DO -------------
 - run final code through a linter




-------- IF TIME ---------
 - fix print statements with '-------' to be the same length
'''



from data import *
import random
from IPython.display import clear_output
import time as t


# pm = pokemon
# pd = pokedex

class Pokemon():
  def __init__(self, name):
    '''This class gives our pokemon important attributes that we can reference later in the code'''
    self.name = name
    self.type = CHARACTERS[self.name]['Type']
    self.HP = HIT_POINTS[self.name]
    self.attack = STATS[self.name]['Attack'] #Attack power of pokemon
    self.defense = STATS[self.name]['Defense'] #Defense power
    self.experience = CHARACTERS[self.name]['Experience']
    self.moves = ATTACKS[self.name] #Just the moves
    self.speed = CHARACTERS[self.name]['Speed']
    self.alive = True

  def print_info(self, indent):
    '''used to print all relevant information of a pokemon'''
    info = ["NAME:", self.name, "TYPE:", self.type, "HP:", self.HP, "ATTACK:", self.attack, "DEFENSE:", self.defense, "EXPERIENCE:",self.experience, "MOVES:", self.moves, "SPEED:",self.speed,"LEVEL:", self.level]
    if indent:
      print('\t',end = '')
    for item in info:
      if type(item) == list:
        print(', '.join(item), end = '')
      else:
        print(item, end = "")
      if str(item)[-1] == ':':
        print(' ', end = '')
      else:
        if indent:
          print('\n\t',end = '')
        else:
          print()
      
  def lotOfUsefullInfo(self, other):
    '''Prints the Your and Computer pokemon's HP'''
    print(f'You:    {round(self.HP)} ({self.name})')
    print(f'Comp:   {round(other.HP)} ({other.name})')
  
  def battle(self, comp_pokemon): #self is the playerpokemon in this case
    '''Runs the battle between the Player and Computer pokemon'''
    print()
    battling = True
    maxSpeed = max(sorted([self.speed, comp_pokemon.speed]))
    if maxSpeed == self.speed:
      attacking = self
      attacked = comp_pokemon
    else:
      attacking = comp_pokemon
      attacked = self
    
    self.lotOfUsefullInfo(comp_pokemon)
    while battling:
      print('\n*****\n\n')
      t.sleep(1)
      if attacking == self:
        print('player turn...')
        print("Which attack would you like to use? \n")
        for i in range(len(attacking.moves)):
          print(f'{i + 1}. {attacking.moves[i]} (Damage: {attacked.calculate_damage(attacking.moves[i],attacking)})')

        # continues to ask for a move until it receives a valid input
        valid = False
        msg = '\nWhat move would you like to make? '
        while valid == False:
          move = input(msg).strip()
          if len(move) > 0:
            try:
              move = int(move)
              if move <= len(attacking.moves):
                valid = True
              else:
                msg = 'Please enter a number corresponding with a move: '
            except:
              msg = 'Please enter a number corresponding with a move: '
          else:
            msg = 'Please enter a number corresponding with a move: '

          
        currentMove = attacking.moves[(int(move)) - 1]
        print(f'You selected {currentMove} which deals {attacked.calculate_damage(currentMove, attacking)} damage.')
      
      else:
        print('computer turn...')
        currentMove = attacking.moves[1]
        for move in attacking.moves:
          if attacked.calculate_damage(move, attacking) >= attacked.calculate_damage(currentMove, attacking):
            currentMove = move
      
      attacked.HP -= attacked.calculate_damage(currentMove, attacking)
      print(f'{attacking.name} used {currentMove} on {attacked.name}, dealing {attacked.calculate_damage(currentMove, attacking)} damage.\n')
      if self.HP < 0:
        self.HP = 0
      if comp_pokemon.HP < 0:
        comp_pokemon.HP = 0
      self.lotOfUsefullInfo(comp_pokemon)
      
      #nothing else after this line plz very much thenks
      if attacking == self:
        attacking = comp_pokemon
        attacked = self
      elif attacking == comp_pokemon:
        attacking = self
        attacked = comp_pokemon

      
      global player_pd

      if self.isItDead():
        print(f"\n\nYOUR {self.name.upper()} FAINTED. :(")
        attack_next = comp_pokemon
        return comp_pokemon
        battling = False
      elif comp_pokemon.isItDead():
        print(f"\n\nYOU WON! YOU ACQUIRED A NEW {comp_pokemon.name.upper()}. ")
        self.experience += 10
        attack_next = 'new'
        return  'new'
        player_pd.add_pokemon(Pokemon(comp_pokemon.name))
        battling = False
     
      

  def calculate_damage(self, currentMove, attacker):
    '''Calculates the damage that a pokemon takes from an attack'''
    #self can be the computer and player
    #c.calculate_damage-- outputs damge #c is self #c is also pokemon class
    #damage dealt to other pokemon
    #Zack is doing (HP- calculate_damage)
    ###
    attack_def_ratio = (self.attack/self.defense)
    movepower = MOVES_DICTIONARY[currentMove]['power']
    
    rando = (random.randint(85,101))/100
    type_multiplier = 1
    if self.type in MOVES_DICTIONARY[currentMove]['not very effective against']:
      type_multiplier = 0.5

    if self.type in MOVES_DICTIONARY[currentMove]['super effective against']:
       type_multiplier = 2

    #MOVES_DICTIONARY[currentMove]['type'] is the type of the current attacker, n and you need to compare it to the self to see if the c
    #modifier = critical x random x type
    modifier = rando * type_multiplier
  
    damage = ((((((2*self.level)/5)+2)* movepower)* attack_def_ratio)/50)* modifier
    return round(damage)
  
    
  # the @property makes it so that the level is updated when experience is updated
  @property
  def level(self):
    return round(self.experience**(1/3)) + 1

  def isItDead(self):
    if self.HP <= 0:
      self.alive = False
      return True
    else:
      self.alive = True
      return False

class Pokedex():
  '''This class holds different pokemon in a list'''
  def __init__(self, *pokemen):
    self.contents = list(pokemen)
    self.dead = []
    
  def add_pokemon(self, poke):
    '''Allows pokemon to be added to the Pokedex'''
    self.contents.append(poke)

  def remove_pokemon(self):
    '''Removes the pokemon from the pokedex when they have fainted'''
    for poke in self.contents:
      if poke.isItDead():
        self.dead.append(self.contents.pop(self.contents.index(poke)))
  
  def check_empty(self):
    '''Checks if the pokedex is empty'''
    self.remove_pokemon()
    if len(self.contents) == 0:
      return True
    elif len(self.contents) > 0:
      return False

      
  


def splash_screen():
  '''Creates a splashscreen *Splashy Splashy*'''
  with open('splashy.txt') as splash:
    for line in splash.read().splitlines():
      print(line)

def game_rules():
  '''This prints the rules of the game'''
  print("\n------------ HOW TO PLAY POKEMON ------------\n")
  print(" In Pokemon, you use characters to fight other characters. \n You start out by choosing an initial pokemon and use that to fight the computer pokemon.\n After beating the computer's pokemon, you collect their pokemon to your pokedex.\n Your objective is to catch them all!!! ")

def p_choose_pokemon(choices):
  '''Shows the pokemon choices at game intro'''
  # prints numbered choices
  for i in range(len(choices)):
    print(f'{i+1}. {choices[i].name}')

  # printing instructions
  print("\n _________________________________________________________")
  print("| To view more information about a pokemon, type 'v#'.    |")
  print("|\t Example: type v1 for more info on the first pokemon. |")
  print("| To select a pokemon, enter just the number.             |")
  print("|\t Example: type 3 to select the third pokemon.         |")
  print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

  # asks for input until it player decides on a pokemon
  final = False
  msg = "Type here: "
  while final == False:
    choice = input(msg).strip()
    if len(choice) == 0:
      msg = "Please enter a valid input (v# or #): "
    elif choice[0] == 'v':
      if int(choice[1:]) <= len(choices):
        print()
        choices[int(choice[1:])-1].print_info(False)
        print()
      else:
        msg = "Please enter a valid input (v# or #): "
        
    else:
      try:
        choice = choices[int(choice)-1]
        final = True
      except:
        final = False
        msg = "Please enter a valid input (v# or #): "

  return choice

def game_loss(rounds, dead):
  '''Prints GAME OVER if you lose'''
  print("\n\n------------------------------------------\n                GAME OVER!\n------------------------------------------\n")
  print("You have no Pokemon left. :(")
  print("\nRESULTS:")
  print(f"You battled a total of {rounds} Pokemon!")
  print(f"{dead} fainted while fighting nobly for you.")
  

def game_win(rounds, dead):
  '''Prints YOU WON and related info'''
  print("\n\n------------------------------------------\n                GAME OVER!\n------------------------------------------\n")
  print("You collected every single type of Pokemon! Congrats. ")
  print(f"You battled a total of {rounds} Pokemon!")
  print(f"{dead} fainted while fighting nobly for you.")




def run_game():
  '''It runs the game by controlling the order of what happens'''
  from IPython.display import clear_output
  clear_output()
  splash_screen()
  rules = input("\nView game instructions? (Y/N)  ").lower().strip()
  unseen = [poke for poke in CHARACTERS.keys()]
  dead_tally = 0
  # if new to the game, loads game rules page
  if rules in ['yes', 'y', 'ya', 'yea', 'yeah', 'yep', 'yes please', 'of course', 'hell yeah']:
    game_rules()
  t.sleep(2)
  clear_output()
  round = 1
  dfhzxkj = True
  print(f'\n\n------------------ ROUND {round} ------------------')

  # initializing player's pokedex
  ## user chooses starting pokemon (add to pokedex)
  print("\nWhat Pokemon would you like to start with?\n")
  #print(f"What Pokemon would you like to start with?":<40) 
  choices = [Pokemon('Bulbasaur'), Pokemon('Charmander'),Pokemon('Squirtle')]
  choice = p_choose_pokemon(choices)
  player_pm = choice # bulbasaur, charmander, or squirtle
  global player_pd #makes player_pokedex a global variable
  player_pd = Pokedex(player_pm)
  
  # initializing computer's pokedex
  ## random computer choice
  comp_pm = Pokemon(random.choice(list(CHARACTERS.keys())))
  comp_pd = Pokedex(comp_pm)
  
  playing = True
  while playing:
    #print("aha")
    attack_next = player_pm.battle(comp_pm)
    
    
    
    # when player runs out of pokemon (all pokemon have run out of hp), game is over
    if player_pd.check_empty():
      playing = False
      loss = True
      break
    if len(unseen) == 0:
      playing = False
      loss = False
      break

    round += 1
    clear_output()

    if (len(player_pd.contents)-1) % 3 == 0 and dfhzxkj:
      print()
      dfhzxkj = False
      for i in range(len(player_pd.contents)):
        print(f'{i}. {player_pd.contents[i].name}')
      toRestore = int(input("Which one shall we fix up? "))
      player_pd.contents[toRestore].HP = HIT_POINTS[player_pd.contents[toRestore].name]
      print()
    
    if attack_next == 'new':
      print(f'\n\n------------------ ROUND {round} ------------------')
      player_pd.add_pokemon(Pokemon(comp_pm.name))
      if comp_pm.name in unseen:
        unseen.remove(comp_pm.name)
      comp_pm = Pokemon(random.choice(list(CHARACTERS.keys())))
      comp_pd = Pokedex(comp_pm)
    if type(attack_next) == Pokemon:
      dead_tally += 1
      
    print("Choose a Pokemon from your Pokedex: ")
    player_pm = p_choose_pokemon(player_pd.contents)
  clear_output()
  if loss:
    game_loss(round, len(player_pd.dead))
  else:
    game_win(round, len(player_pd.dead))
run_game()
