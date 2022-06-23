# # 6. Создать класс «Живое». Определить наследуемые классы – «лиса», «кролик» и «растение». Лиса ест кролика.
# # Кролик ест растения. Растение поглощает солнечный свет. Представитель каждого класса может умереть, если
# # достигнет определенного возраста или для него не будет еды. Напишите виртуальные методы поедания и
# # определения состояния живого существа (живой или нет, в зависимости от достижения предельного возраста
# # и наличия еды (входной параметр)).


class Creature:
    def __init__(self, population):
        self.population = population

class Plants(Creature):
    def __init__(self, koef_repr, population,eats_season = 10):
        super().__init__(population)
        self.koef_repr = koef_repr
        self.eats_season=eats_season #сколько травы съедается кроликом
    def reproduction(self):
        self.population = int(self.population*(self.koef_repr))
    def info_population(self):
        print("count plants:", self.population)
    def rabbits_food(self, count_rabbits):
        self.population -= count_rabbits * self.eats_season
    def add_plants(self,count_plants):
        self.population += count_plants
    def winter_population(self):
        self.population=int(self.population*0.2)


class Rabbit(Creature):
    def __init__(self, koef_repr, koef_death, population,eats_season):
        super().__init__(population)
        self.koef_repr = koef_repr
        self.koef_death = koef_death
        self.eats_season=eats_season #сколько кроликов съедается лисой
    def reproduction(self):
            self.population = int(self.population*(self.koef_repr))
    def death(self):
        self.population = int(self.population*(1-self.koef_death))
    def info_population(self):
        print("count rabbits:", self.population)
    def teke_away(self,count_rabbits):
        self.population -= count_rabbits
    def add_rabbits(self,count_rabbits):
        self.population += count_rabbits
    def foxes_food(self, count_foxes):
        self.population -= count_foxes * self.eats_season

class Fox (Creature):
    def __init__(self, koef_repr, koef_death, population,count_killed):
        super().__init__(population)
        self.koef_repr = koef_repr
        self.koef_death = koef_death
        self.count_killed = count_killed
    def reproduction(self):
            self.population = int(self.population*self.koef_repr)
    def death(self):
        self.population = int(self.population*(1-self.koef_death))
    def info_population(self):
        print("count foxes:", self.population)
    def teke_away(self,count_foxes):
        self.population -= count_foxes
    def kill_season(self):
        self.population=self.population-(self.count_killed)
    def add_foxes(self,count_foxes):
        self.population += count_foxes

plants = Plants(5, 5000)
rabbits = Rabbit(4, 0.4, 300,6)
foxes=Fox(2,0.2,20,10)





season=('Winter', 'Spring', 'Summer', 'Autumn')
ban_hunting=0
year = 1
while year <= 10:
    print("*************")
    print("year is:", year)
    print("*************")
    if plants.population <= 0 or rabbits.population <= 0 or foxes.population <= 0:
        print("fatality")
        print("You lose on year", year)
        break

    for i in season:

        print('-------------')
        print(i,'came')
        print('-------------')
        if plants.population <= 0 or rabbits.population <=0 or foxes.population<=0:
            print("fatality")
            print("You lose on year",year)
            break
        # plants-rabbits
        if plants.population <= (rabbits.population-plants.eats_season) * plants.eats_season:
            print("warning!!!")
            print(f" plants {plants.population}, rabbits {rabbits.population}, foxes {foxes.population}")
            choise = int(input("1 - add plants, 2 - takeaway rabbits, 3 - add foxes:"))

            if choise == 1:
                print("you need to add plants",
                      rabbits.population * plants.eats_season -plants.population)
                count_plants = int(input("enter plants:"))
                plants.add_plants(count_plants)
            elif choise == 2:
                print("you need take away:",rabbits.population - plants.population // plants.eats_season )
                count_rabbits = int(input("enter rabbits:"))
                rabbits.teke_away(count_rabbits)
            elif choise == 3:
                print(f"you need add foxes not more: {1 if int((rabbits.population*plants.eats_season - plants.population) / plants.eats_season/rabbits.eats_season)<1 else int((rabbits.population*plants.eats_season - plants.population) / plants.eats_season/rabbits.eats_season)}")
                count_foxes = int(input("enter rabbits:"))
                foxes.add_foxes(count_foxes)
             #foxes-rabbit
        if rabbits.population <= int(foxes.population * rabbits.eats_season+rabbits.population*rabbits.koef_death):
            print("warning!!!")
            print(f" rabbits {rabbits.population} foxes {foxes.population}")
            choise = int(input("1 - add rabbits 2 - takeaway foxes:"))
            if choise == 1:
                print("you need to add rabbits", foxes.population * rabbits.eats_season - rabbits.population)
                count_rabbits = int(input("enter rabbits:"))
                rabbits.add_rabbits(count_rabbits)
            elif choise == 2:
                print("you need take away foxes more than:",  rabbits.population // rabbits.eats_season -foxes.population)
                count_foxes = int(input("enter foxes:"))
                foxes.teke_away(count_foxes)
        #foxes-hunter
        if foxes.population <= int(foxes.count_killed+foxes.population*foxes.koef_death) and ban_hunting==0:
            print("warning!!!")
            print(f" foxes {foxes.population} , can kill foxes  {foxes.count_killed}")
            choise = int(input("1 - add foxes 2 - ban hunting:"))
            if choise == 1:
                print("you need to add foxes more than", foxes.population - foxes.count_killed)
                count_foxes = int(input("enter foxes:"))
                foxes.add_foxes(count_foxes)
            elif choise == 2:
                print("for how many seasons to ban hunting:")
                count_season_not_hunter = int(input("enter season:"))
                ban_hunting=count_season_not_hunter



        if i != 'Spring' and i!='Winter':
            plants.rabbits_food(rabbits.population)  # кролики зимой и весной из-за отсутствия
                    # травы едят кору деревьев, при этом весной трава начинает уже расти
        rabbits.foxes_food(foxes.population)
        if i!='Winter':
            plants.reproduction() # зимой растения (зелень) не растут
            rabbits.reproduction()  #размножение кроликов происходит с марта по октябрь-ноябрь

        if i=='Spring' or i=='Summer':
            foxes.reproduction() #лисы рождаются весной и в начале лета
        print(' ban_hunting =', ban_hunting )
        if i == 'Winter':
            plants.winter_population()
            if ban_hunting == 0:
                foxes.kill_season()
        if ban_hunting!=0:
            ban_hunting-=1
        plants.info_population()
        rabbits.info_population()
        foxes.info_population()
    year += 1
    foxes.death()
    rabbits.death()









    # if plants.population <= 0 or rabbits.population <=0 or foxes.population<=0:
    #     print("fatality")
    #     print("You lose on year",year)
    #     break
    # # plants-rabbits
    # if plants.population <= rabbits.population * plants.eats_season:
    #     print("warning!!!")
    #     print(f" rabbits {rabbits.population} plants {plants.population}")
    #     choise = int(input("1 - add plants 2 - takeaway rabbits:"))
    #     if choise == 1:
    #         print("you need to add",rabbits.population*plants.eats_season - plants.population)
    #         count_plants = int(input("enter plants:"))
    #         plants.add_plants(count_plants)
    #     elif choise == 2:
    #         print("you need take away:",rabbits.population - plants.population // plants.eats_season )
    #         count_rabbits = int(input("enter rabbits:"))
    #         rabbits.teke_away(count_rabbits)
    #      #foxes-rabbit
    # if rabbits.population <= foxes.population * rabbits.eats_season:
    #     print("warning!!!")
    #     print(f" rabbits {rabbits.population} foxes {foxes.population}")
    #     choise = int(input("1 - add rabbits 2 - takeaway foxes:"))
    #     if choise == 1:
    #         print("you need to add rabbits", foxes.population * rabbits.eats_season - rabbits.population)
    #         count_rabbits = int(input("enter rabbits:"))
    #         rabbits.add_rabbits(count_rabbits)
    #     elif choise == 2:
    #         print("you need take away foxes:", foxes.population - rabbits.population // rabbits.eats_season)
    #         count_foxes = int(input("enter foxes:"))
    #         foxes.teke_away(count_foxes)
    #
    # print("year is:", year)
    # plants.rabbits_food(rabbits.population)
    # rabbits.foxes_food(foxes.population)
    # plants.reproduction()
    # plants.info_population()
    # rabbits.reproduction()
    # rabbits.death()
    # rabbits.info_population()
    # foxes.reproduction()
    # foxes.death()
    # foxes.info_population()
    # year += 1