# Write your code here
import random


class Robogotchi:
    def __init__(self):
        self.name = self.get_name()
        self.battery = 100
        self.overheat = 0
        self.skills=0
        self.boredom=0
        self.rust = 0
        self.game_stats = {'robot':0,'user':0,'draw':0}
        self.games = {'numbers': self.num_game, 'rock-paper-scissors': self.rps_game}
    def get_name(self):
        return input('How will you call your robot?')
    def check_vitals(self):
        string = f'''{self.name}\'s stats are: the battery is {self.battery},
overheat is {self.overheat},
skill level is {self.skills},
boredom is {self.boredom},
rust is {self.rust}.'''
        print(string)
    def sleep(self):
        if self.overheat==0:
            self.overheat=0
            print(f'{self.name} is cool!')
        else:
            if self.overheat-20<0:
                new_heat = 0
            else:
                new_heat = self.overheat-20
            print(f"""{self.name} cooled off!
{self.name}'s level of overheat was {self.overheat}. Now it is {new_heat}..""")
            print(f'{self.name} is cool!')
            self.overheat=new_heat

    def check_error(self):
        if self.overheat==100:
            print(f"""The level of overheat reached 100, {self.name} has blown up! Game over. Try again?""")
            return True
        elif self.rust==100:
            print(f"""{self.name} is too rusty! Game over. Try again?""")
            return True
        elif self.battery==0:
            print(f"""The level of the battery is {self.battery}, {self.name} needs recharging!""")
            return True
        elif self.boredom==100:
            print(f"""{self.name} is too bored! {self.name} needs to have fun!.""")
        return False
    def rechage(self):
        if self.battery == 100:
            print(f'{self.name} is charged!\n')
        else:
            old_battery = self.battery
            if old_battery+10>100:
                new_battery = 100
            else:
                new_battery = old_battery+10
            print(f"""{self.name}'s level of overheat was {self.overheat}. Now it is {self.overheat-5}.
{self.name}'s level of the battery was {old_battery}. Now it is {new_battery}.
{self.name}'s level of boredom was {self.boredom}. Now it is {self.boredom+5}.
{self.name} is recharged!""")
            self.battery = new_battery
            self.overheat -= 5
            self.boredom += 5
    def learn(self):
        if self.skills == 100:
            print(f'{self.name} is already at max skill level!')
        else:

            if self.skills + 10 > 100:
                new_skills = 100
            else:
                new_skills = self.skills + 10
            if self.boredom +5>100:
                new_boredom = 100
            else:
                new_boredom = self.boredom+5
            if self.overheat +10>100:
                new_overheat = 100
            else:
                new_overheat = self.overheat+10
            if self.battery -10<0:
                new_battery = 0
            else:
                new_battery = self.battery-10

            string=f"""{self.name}'s level of skill was {self.skills}. Now it is {new_skills}.
{self.name}'s level of overheat was {self.overheat}. Now it is {new_overheat}.
{self.name}'s level of the battery was {self.battery}. Now it is {new_battery}.
{self.name}'s level of boredom was {self.boredom}. Now it is {new_boredom}.
{self.name} has become smarter!"""
            self.overheat = new_overheat
            self.skills = new_skills
            self.battery=new_battery
            self.boredom = new_boredom

            string_2 = self.unpleasant()

            print(string)
            print(string_2,'\n',sep='')
    def exit(self):
        print('Game over')
        self.check_error()
        exit()
    def work(self):
        if self.skills <50:
            print(f"{self.name} has got to learn before working!")
        else:
            if self.battery-10<0:
                new_battery = 0
            else:
                new_battery = self.battery-10
            if self.boredom+10>100:
                new_boredom = 100
            else:
                new_boredom = self.boredom+10
            if self.overheat+10>100:
                new_overheat = 100
            else:
                new_overheat = self.overheat+10


            string = f"""
{self.name}'s level of boredom was {self.boredom}. Now it is {new_boredom}.
{self.name}'s level of overheat was {self.overheat}. Now it is {new_overheat}.
{self.name}'s level of the battery was {self.battery}. Now it is {new_battery}."""
            self.battery = new_battery
            self.overheat=new_overheat
            self.boredom=new_boredom
            string_2 =self.unpleasant()
            print(string)
            print(string_2,'\n',sep='')
            print("Daneel's level of rust was 0. Now it is 10.")
            print(f"{self.name} did well!\n")

    def unpleasant(self):
        if self.battery <= 10:
            return self.fall_pool()
        elif 10 < self.battery <= 30:
            return self.step_on_puddler()
    def step_on_puddler(self):
        if self.rust+10>100:
            new_rust = 100
        else :
            new_rust = self.rust+10
        print(f"Oh no, {self.name} stepped into a puddle!")
        string = f"{self.name}'s level of rust was {self.rust}. Now it is {new_rust}."
        self.rust = new_rust
        return string
    def oil(self):
        if self.rust==0:
            print(f"{self.name} is fine, no need to oil!")
        else:
            if self.rust-20<0:
                new_rust = 0
            else:
                new_rust = self.rust-20
            print(f"""{self.name}'s level of rust was {self.rust}. Now it is {new_rust}. {self.name} is less rusty!""")
            self.rust = new_rust
    def fall_pool(self):
        if self.rust+50>100:
            new_rust = 100
        else :
            new_rust = self.rust+50
        print(f"Guess what! {self.name} fell into the pool!")
        string=f"{self.name}'s level of rust was {self.rust}. Now it is {new_rust}."
        self.rust = new_rust
        return string
    def menu(self):
        interactions = {'exit':self.exit,'info':self.check_vitals,'recharge':self.rechage ,'sleep':self.sleep,'play':self.choose_game,
                        'learn':self.learn,'work':self.work,'oil':self.oil}
        while True:
            action = input(f'''Available interactions with {self.name}:
exit - Exit
info - Check the vitals
work - Work
play - Play
oil - Oil
recharge - Recharge
sleep - Sleep mode
learn - Learn skills

Choose:\n''')
            if action in interactions:
                break
            else:
                print('Invalid option! Try again!\n')
        interactions[action]()
    def choose_game(self):
        self.game_stats = {'robot': 0, 'user': 0, 'draw': 0}
        while True:

            game = input('Which game would you like to play?\n').lower()
            if game in self.games:
                self.games[game]()
                break
            else:
                print('Please choose a valid option: Numbers or Rock-paper-scissors?\n')
        new_boredom_value = self.boredom - 20
        if self.boredom - 20 < 0:
            new_boredom_value = 0
        new_overheat_value = self.overheat + 10
        if self.overheat + 10 > 100:
            new_overheat_value = 100
        print(f"""{self.name}'s level of boredom was {self.boredom}. Now it is {new_boredom_value}.
{self.name}'s level of overheat was {self.overheat}. Now it is {new_overheat_value}.""")
        self.boredom = new_boredom_value
        self.overheat = new_overheat_value
        if self.boredom == 0:
            print(f'{self.name} is in great mood!')


    def num_game(self):
        game_end = False
        while True:
            number = random.randint(1, 1000000)
            while True:
                user_number = input('What is your number?\n')
                if user_number=='exit game':
                    game_end =True
                    break
                if user_number[1:].isdigit():
                    if int(user_number) <= 0:
                        print('The number can\'t be negative!')
                        continue
                    elif int(user_number) > 1000000:
                        print('Invalid input! The number can\'t be bigger than 1000000')
                        continue
                    user_number = int(user_number)
                    break
                print('A string is not a valid input!.')
            if game_end:
                print(f'\nYou won: {self.game_stats["user"]},')
                print(f'Robot won: {self.game_stats["robot"]},')
                print(f'Draws: {self.game_stats["draw"]}.')
                break
            robot_number = random.randint(1, 1000000)
            print(f'The robot entered the number {robot_number}.')
            print(f'The goal number is {number}.')
            if robot_number == user_number:
                print('It\'s a draw!')
                self.game_stats['draw'] += 1
            elif abs(number - robot_number) < abs(number - user_number):
                print('The robot won!')
                self.game_stats['robot'] += 1
            else:
                print('You won!')
                self.game_stats['user'] += 1
    def rps_game(self):
        moves = ['rock', 'paper', 'scissors']
        game_end = False
        while True:
            while True:
                user_move = input('What is your move?\n')
                if user_move == 'exit game':
                    print(f'\nYou won: {self.game_stats["user"]},')
                    print(f'Robot won: {self.game_stats["robot"]},')
                    print(f'Draws: {self.game_stats["draw"]}.')
                    game_end = True
                    break
                elif user_move in moves:
                    break
                else:
                    print('No such option! Try again!\n')
            if game_end:
                break
            robot_move = random.choice(moves)
            print(f'The robot chose {robot_move}.')
            if robot_move == user_move:
                print('It\'s a draw!\n')
                self.game_stats['draw'] += 1
            elif (robot_move == 'rock' and user_move == 'scissors') or (
                    robot_move == 'scissors' and user_move == 'paper') or (
                    robot_move == 'paper' and user_move == 'rock'):
                print('The robot won!\n')
                self.game_stats['robot'] += 1
            else:
                print('You won!\n')
                self.game_stats['user'] += 1



def main():
    robot_kun = Robogotchi()
    while robot_kun.check_error()!=True:

        robot_kun.menu()
if __name__ == '__main__':
    main()