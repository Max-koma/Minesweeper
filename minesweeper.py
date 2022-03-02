#Class blank squares
class Blanksquare:
    def __init__(self, input_row, input_column):
        #Set coordinates on the field and boolean variable for check on picking
        self.row = input_row
        self.column = input_column
        self.coordinates = str(self.row) + str(self.column)
        self.repr = self.coordinates
        self.picked = False
    def __repr__(self):
        return str(self.repr) + " "
    #Method that change display of picked square, marked this square as picked, and do this for all blank squares and 
    # squares with class "Aroundmines" around, that we aren't picked all squares manually
    def pick(self):
        if not self.picked:
            self.picked = True
            del check_for_win[self.coordinates]
            self.repr = "  "
            for l in range(self.row-1, self.row+2):
                for m in range(self.column-1, self.column+2):
                    if (l == self.row and m == self.column) or l not in range(0, 10) or m not in range(0, 10):
                        continue
                    else: field[l][m].pick()


#Class of mines
class Mines:
    def __init__(self, input_row, input_column):
        #Set coordinates on the field
        self.row = input_row
        self.column = input_column
        self.coordinates = str(self.row) + str(self.column)
        self.repr = self.coordinates
    def __repr__(self):
        return str(self.repr) + " "
    

#Class of squares around mines, that indicate numper of mines around
class Around_mines:
    def __init__(self, input_row, input_column):
        #Set coordinates on the field and boolean variable for check on picking
        self.row = input_row
        self.column = input_column
        self.coordinates = str(self.row) + str(self.column)
        #Set counter of mines around
        self.quantity_of_mines_around = 1
        self.repr = self.coordinates
        self.picked = False
    def __repr__(self):
        return str(self.repr) + " "
    #Method for raising the counter of mines
    def add_mine_around(self):
        self.quantity_of_mines_around += 1
    #Method that change display of picked square and marked this square as picked
    def pick(self):
        if not self.picked:
            self.picked = True
            del check_for_win[self.coordinates]
            self.repr = str(self.quantity_of_mines_around) + " "

# Creating our field and fill it with blank squares i -row, j - column
field = [[Blanksquare(i, j) for j in range(10)] for i in range(10)]

# Create mines and change class of square around them
lst_of_mines = []
from random import randint
for k in range(10):
    #Create two random integer
    i = randint(0, 9)
    j = randint(0, 9)
    #Check if its already mine
    while type(field[i][j]) == Mines:
        i = randint(0, 9)
        j = randint(0, 9)
    #Placing bomb
    else:field[i][j] = Mines(i, j)
    lst_of_mines.append(str(i)+str(j))
    #For all squares around mine we change class on "Aroundmines". If square already has that type, we raise counter of mine of that square +1
    for l in range(i-1, i+2):
        for m in range(j-1, j+2):
            #print ("l= ", l,"m = ", m)
            #Delete excess squares from our cycle
            if (l == i and m == j) or l not in range(0, 10) or m not in range(0, 10) or type(field[l][m]) == Mines:
               continue
            #Check if its already has that type. If so, raise the counter
            elif type(field[l][m]) == Around_mines:
                field[l][m].add_mine_around()
            
            else:
                field[l][m] = Around_mines(l , m)
#Print our field
for row in field:
    print (" ".join(map(str,row))) 

#The cycle of the game itself.
#Create dictionary with coordinates of every square as key and type of square as value
check_for_win = {j.coordinates:type(j) for i in field for j in i}
#variable for win condition
win = False
while not win: 
    try: 
        s = int(input("Enter coordinates: "))
    except ValueError: 
        print("Error. Enter integer coordinates please")
        continue
    if s not in range(101):
        print("Error. There is no square with such coordinates")
        continue
    else:
        #Transform input into indices
        i = int(s/10)
        j = s % 10
        #Check if its mine
        if type(field[i][j]) == Mines:
            print("YOU DIED")
            break
        #Check if its already been picked
        elif field[i][j].picked:
            print("You already picked that square. Pick another")
            continue
        #Pick that square
        else: field[i][j].pick()
    #Printing update field
    for row in field:
        print (" ".join(map(str,row)))
    #Check if its only Mines left unpicked. If so, then you are win
    if Blanksquare not in check_for_win.values() and Around_mines not in check_for_win.values():
        win = True
        print("You WIN!!")
