import pygame
import time

# ================= ENVIRONMENT =================
class VillageEnvironment:
    def __init__(self):
        self.food = 10
        self.weather = "sunny"

    def observe(self):
        return {
            "food": self.food,
            "weather": self.weather
        }

    def update_weather(self, day):
        if day % 3 == 0:
            self.weather = "rainy"
        else:
            self.weather = "sunny"

    def apply_action(self, action):
        if action == "farm" and self.weather == "sunny":
            self.food += 5
        elif action == "farm" and self.weather == "rainy":
            self.food += 2
        elif action == "eat":
            self.food -= 1


# ================= AGENT =================
class VillageAgent:
    def __init__(self):
        self.goal = "survive"
        self.last_action = None

    def decide(self, perception):
        if perception["food"] < 5:
            self.last_action = "farm"
        else:
            self.last_action = "eat"
        return self.last_action


# ================= GUI =================
class VillageGUI:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Agent AI Village")
        self.font = pygame.font.SysFont(None, 24)

    def draw(self, env, agent):
        # Background
        if env.weather == "sunny":
            self.screen.fill((135, 206, 235))  # sky blue
        else:
            self.screen.fill((100, 100, 100))  # rainy gray

        # Farm
        pygame.draw.rect(self.screen, (139, 69, 19), (100, 300, 200, 100))

        # House
        pygame.draw.rect(self.screen, (150, 75, 0), (400, 300, 120, 100))

        # Agent
        if agent.last_action == "farm":
            agent_pos = (160, 260)
        else:
            agent_pos = (440, 260)

        pygame.draw.rect(self.screen, (255, 224, 189), (*agent_pos, 20, 30))

        # Text
        food_text = self.font.render(f"Food: {env.food}", True, (0, 0, 0))
        weather_text = self.font.render(f"Weather: {env.weather}", True, (0, 0, 0))

        self.screen.blit(food_text, (10, 10))
        self.screen.blit(weather_text, (10, 40))

        pygame.display.flip()


# ================= CONTROL LOOP =================
def run_simulation(days=20):
    env = VillageEnvironment()
    agent = VillageAgent()
    gui = VillageGUI()

    for day in range(1, days + 1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        env.update_weather(day)
        perception = env.observe()
        action = agent.decide(perception)
        env.apply_action(action)

        gui.draw(env, agent)

        if env.food <= 0:
            print("Village has starved")
            time.sleep(2)
            break

        time.sleep(1)

    pygame.quit()


run_simulation()
