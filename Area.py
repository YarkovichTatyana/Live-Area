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
        self.eats_season=eats_season
    def reproduction(self):
        self.population *= self.koef_repr
    def info_population(self):
        print("count plants:", self.population)
    def rabbits_food(self, count_rabbits):
        self.population -= count_rabbits * self.eats_season
    def add_plants(self,count_plants):
        self.population += count_plants


class Rabbit(Creature):
    def __init__(self, koef_repr, koef_death, population):
        super().__init__(population)
        self.koef_repr = koef_repr
        self.koef_death = koef_death
    def reproduction(self):
        self.population *= self.koef_repr
    def death(self):
        self.population -= int(self.population * self.koef_death)
    def info_population(self):
        print("count rabbits:", self.population)
    def teke_away(self,count_rabbits):
        self.population -= count_rabbits
    def add_rabbits(self,count_rabbits):
        self.population += count_rabbits
plants = Plants(7, 500)
rabbits = Rabbit(10, 0.3, 11)

year = 1
while year <= 10:
    if plants.population <= 0 or rabbits.population <=0:
        print("fatality")
        print("You lose on year",year)
        break
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
    if plants.population >(((rabbits.population*rabbits.koef_repr*rabbits.koef_death)*plants.eats_season)*5):
        print("warning!!!")
        print(f" plants ({plants.population} are a 1000 times largen than rabbits ({rabbits.population})")
        choise = int(input("1 - add rabbits 2 - moving plants:"))
        if choise == 1:
            print("you need to add no more",
                  plants.population //plants.eats_season-rabbits.info_population()//rabbits.koef_repr//rabbits.koef_death)
            count_rabbits = int(input("enter rabbits:"))
            rabbits.add_rabbits(count_rabbits)
        elif choise == 2:
            print("you need to mov the plants no more:",
                  plants.population-((rabbits.population*rabbits.koef_repr*rabbits.koef_death)*plants.eats_season)*2)
            count_plants = int(input("enter count:"))
            plants.add_plants(count_plants)

    print("year is:", year)
    plants.rabbits_food(rabbits.population)
    plants.reproduction()
    plants.info_population()
    rabbits.reproduction()
    rabbits.death()
    rabbits.info_population()
    year += 1