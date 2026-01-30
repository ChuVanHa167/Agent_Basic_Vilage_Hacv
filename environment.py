### Hướng dẫn chạy code: ###
### ngoi lang(Environment) ###
class VillageEnvironment: 
    def __init__(self):
        """Moi truong giu trang thai nay 
        và Agent khong so huu trang thai nay
        """
        self.food = 10 # kho luong thuc
        self.weather = "sunny" #thoi tiet
    def observe(self):
        """Perception: moi truong tra ve trang thai
        Moi truong chu dong cung cap percept
        o day percept = {food, weather} và mỗi vòng loop agent nhận 1 percept
        """
        return{
            "food": self.food,
            "weather": self.weather
        }
    def update_weather(self, day):
        """moi truong tự thay doi theo thoi gian
        Agent không điều khiển được thời tiết
        => Agent không toàn năng và môi trường không tĩnh
        """
        if day % 3 == 0:
            self.weather = "rainy"
        else:
            self.weather = "sunny"
    def apply_action(self, action):
        """Action tac dong len moi truong
        Agent chọn action và môi trường quyết định hậu quả
        """
        if action == "farm" and self.weather == "sunny":
            self.food += 5
        elif action == "farm" and self.weather == "rainy":
            self.food += 2
        elif action == "eat":
            self.food -= 1
### Nguoi dan(Agent) ###
class VillageAgent:
    def __init__(self):
        """"Goal = sinh tồn"""
        self.goal = "survive" 
    def decide(self, perception):
        """Agent function: perception -> action
        Agent chỉ biết những gì perception cung cấp, 
        không biết tình trạng nội bộ môi trường
        """
        food = perception["food"]
        weather = perception["weather"]

        if food < 5:
            return "farm"
        else:
            return "eat"

### Vong doi Agent(Control loop)###
def run_simulation(days=10):
    #khởi tạo môi trường và agent
    env = VillageEnvironment()
    agent = VillageAgent()
    #mỗi vòng là một timestep
    for day in range(1, days + 1):
        print(f"\n Day {day}") 
        #môi trường thay đổi, agent quan sát và hành động
        env.update_weather(day) 
        #agent nhận percept
        perception = env.observe()
        print("Perception: ", perception)
        #agent chọn action
        action = agent.decide(perception)
        print("Agent decides to: ", action)
        #action tác động lên môi trường
        env.apply_action(action)
        print("Food after action: ", env.food)

        if env.food <= 0:
            print(" The village has starved")
            break

#run
run_simulation(15)