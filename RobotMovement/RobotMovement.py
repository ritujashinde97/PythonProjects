
class Robot:
    def __init__(self, instruction_file):
        self.instruction_file = instruction_file
        self.instruction_file = "instruction.txt"
    def write_instructions(self):
        f = open(self.instruction_file,'w')
        while True:
            movement_x = input('Enter horizontal movement, or q to quit:')
            if movement_x=='q':
                break
            movement_y = input('Enter vertical movement, or q to quit:')
            if movement_y == 'q':
                break
            f.write(movement_x + '\n')
            f.write(movement_y + '\n')
        f.close()
    def read_instructions(self):
        try:
            f = open(self.instruction_file,'r')
        except FileNotFoundError as error:
            print(error)
        else:
            self.instruction_list =f.readlines()
            f.close()
    def get_location(self):
        position_x , position_y = 0,0
        distance_x , distance_y = 0,0
        self.read_instructions()
        if self.instruction_list != None:
            for data in self.instruction_list :
                temp = data[:-1]
                if self.instruction_list.index(data)%2 == 0:
                    position_x += float(temp)
                    distance_x += abs(float(temp))
                else:
                    position_y += float(temp)
                    distance_y += abs(float(temp))
        return position_x, position_y, distance_x, distance_y

robot_1 = Robot('robot_1.txt')
robot_1.write_instructions()
pos_x,pos_y,dist_x,dist_y =robot_1.get_location()
print('The Robot is finally at ' + str(pos_x) + ', ' +str(pos_y))
print('The Robot has travelled a distance of ' +str(dist_x) + ' horixontally, ' + str(dist_y) +  ' vertically')

