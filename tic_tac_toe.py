class Crossboard:
    def __init__(self):
        self.crs = [[-1 for _ in range(3)] for _ in range(3)]

    def check_row(self):
        if self.crs[0][0]==self.crs[0][1]==self.crs[0][2] and self.crs[0][0]!=-1:
            print("R1")
            return True

        if self.crs[1][0]==self.crs[1][1]==self.crs[1][2] and self.crs[1][0]!=-1:
            print("R2")
            return True

        if self.crs[2][0]==self.crs[2][1]==self.crs[2][2] and self.crs[2][0]!=-1:
            print("R3")
            return True

        return False

    def check_column(self):
        if self.crs[0][0]==self.crs[1][0]==self.crs[2][0] and self.crs[0][0]!=-1:
            print("C1")
            return True

        if self.crs[0][1]==self.crs[1][1]==self.crs[2][1] and self.crs[0][1]!=-1:
            print("C2")
            return True

        if self.crs[0][2]==self.crs[1][2]==self.crs[2][2] and self.crs[0][2]!=-1:
            print("C3")
            return True

        return False

    def check_diagonal(self):
        if self.crs[0][0]==self.crs[1][1]==self.crs[2][2] and self.crs[0][0]!=-1:
            return True

        if self.crs[0][2]==self.crs[1][1]==self.crs[2][0] and self.crs[0][2]!=-1:
            return True

        return False

    def is_valid(self,pos):
        if self.crs[pos[0]][pos[1]]!=-1:
            return False

        else:
            return True

    def move(self,pos,user):
        if self.is_valid(pos):
            self.crs[pos[0]][pos[1]] = user
            print(self.crs)
            if (self.check_diagonal() or self.check_row() or self.check_column()):
                return str("Winner is User "+str(user)+"!!!")

            return "Move applied!!"
                

        else:
            return "Invalid Move!!"

    def check_all_occupied(self):
        for i in self.crs:
            for j in i:
                if j==-1:
                    return False

        return True


c = Crossboard()
user = [1,0]
while(1):
    if c.check_all_occupied():
        print("Draw!!")
        break

    print("Enter the position of the move:")
    x,y = map(int,input().split())


    res = c.move([x,y],user[0])
    user[0],user[1] = user[1],user[0]
    if res.split()[0]=="Winner":
        print(res)
        break

    else:
        print(res)