# # 6. Создать класс «Живое». Определить наследуемые классы – «лиса», «кролик» и «растение». Лиса ест кролика.
# # Кролик ест растения. Растение поглощает солнечный свет. Представитель каждого класса может умереть, если
# # достигнет определенного возраста или для него не будет еды. Напишите виртуальные методы поедания и
# # определения состояния живого существа (живой или нет, в зависимости от достижения предельного возраста
# # и наличия еды (входной параметр)).


class Creature:
    def __init__(self, population):
        self.population = population

class Plants(Creature):
    def __init__(self, koef_repr, population,eats_season = 12):
        super().__init__(population)
        self.koef_repr = koef_repr
        self.eats_season=eats_season #сколько травы съедается кроликом
    def reproduction(self):
        self.population *=int(self.koef_repr)
    def info_population(self):
        print("count plants:", self.population)
    def rabbits_food(self, count_rabbits):
        self.population -= count_rabbits * self.eats_season
    def add_plants(self,count_plants):
        self.population += count_plants


class Rabbit(Creature):
    def __init__(self, koef_repr, koef_death, population,eats_season = 5):
        super().__init__(population)
        self.koef_repr = koef_repr
        self.koef_death = koef_death
        self.eats_season=eats_season #сколько кроликов съедается лисой
    def reproduction(self):
        self.population *=int (self.koef_repr)
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
    def __init__(self, koef_repr, koef_death, population):
        super().__init__(population)
        self.koef_repr = koef_repr
        self.koef_death = koef_death
    def reproduction(self):
        self.population *= int(self.koef_repr)
    def death(self):
        self.population = int(self.population*(1-self.koef_death))
    def info_population(self):
        print("count foxes:", self.population)

plants = Plants(5, 600)
rabbits = Rabbit(5, 0.3, 30)
foxes=Fox(2,0.1,3)


year = 1
while year <= 10:

    if plants.population <= 0 or rabbits.population <=0 or foxes.population<=0:
        print("fatality")
        print("You lose on year",year)
        break
    # plants-rabbits
    if plants.population <= rabbits.population * plants.eats_season:
        print("warning!!!")
        print(f" rabbits {rabbits.population} plants {plants.population}")
        choise = int(input("1 - add plants 2 - takeaway rabbits:"))
        if choise == 1:
            print("you need to add",rabbits.population*plants.eats_season - plants.population)
            count_plants = int(input("enter plants:"))
            plants.add_plants(count_plants)
        elif choise == 2:
            print("you need take away:",rabbits.population - plants.population // plants.eats_season )
            count_rabbits = int(input("enter rabbits:"))
            rabbits.teke_away(count_rabbits)
         #foxes-rabbit
        if rabbits.population <= foxes.population * rabbits.eats_season:
            print("warning!!!")
            print(f" rabbits {rabbits.population} foxes {foxes.population}")
            choise = int(input("1 - add rabbits 2 - takeaway foxes:"))
            if choise == 1:
                print("you need to add", foxes.population * rabbits.eats_season - rabbits.population)
                count_rabbits = int(input("enter rabbits:"))
                rabbits.add_rabbits(count_rabbits)
            elif choise == 2:
                print("you need take away foxes:", foxes.population - rabbits.population // rabbits.eats_season)
                count_rabbits = int(input("enter rabbits:"))
                rabbits.teke_away(count_rabbits)

    print("year is:", year)
    plants.rabbits_food(rabbits.population)
    rabbits.foxes_food(foxes.population)
    plants.reproduction()
    plants.info_population()
    rabbits.reproduction()
    rabbits.death()
    rabbits.info_population()
    foxes.reproduction()
    foxes.death()
    foxes.info_population()
    year += 1