
class Journey:
    def __init__(self,*movement_list):
        self.travel = movement_list
    def is_round_trip(self):
        x_pos ,y_pos = 0,0
        for movement in self.travel:
            x_pos= x_pos + movement[0]
            y_pos = y_pos + movement[1]
        return x_pos==0 and y_pos == 0


#movement in east and north . '-' represents west and south
ross_itinerary =[[90,50],[-80,-40],[-10,-10]]
ross_journey = Journey(*ross_itinerary)
print(ross_journey.is_round_trip())

rachel_itinerary =[[90,50],[-80,-40],[-10,-10]]
rachel_journey = Journey(*rachel_itinerary)
print(rachel_journey.is_round_trip())

chandler_itinerary =[[40,50],[-20,-30],[-10,-10]]
chandler_journey = Journey(*chandler_itinerary)
print(chandler_journey.is_round_trip())

monica_itinerary =[[70,60],[-80,-50],[-20,-10]]
monica_journey = Journey(*monica_itinerary)
print(monica_journey.is_round_trip())

joey_itinerary =[[80,50],[-50,-20],[-20,-20]]
joey_journey = Journey(*joey_itinerary)
print(joey_journey.is_round_trip())

phoebe_itinerary =[[50,50],[-80,-40],[-20,-60]]
phoebe_journey = Journey(*phoebe_itinerary)
print(phoebe_journey.is_round_trip())

