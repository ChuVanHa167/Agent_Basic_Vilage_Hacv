import pygame
import time
import math

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
        self.weather = "rainy" if day % 3 == 0 else "sunny"

    def apply_action(self, action):
        if action == "farm":
            self.food += 5 if self.weather == "sunny" else 2
        elif action == "eat":
            self.food -= 1


# ================= AGENT (LOGIC) =================
class VillageAgent:
    def __init__(self):
        self.goal = "survive"
        self.action = None

    def decide(self, perception):
        if perception["food"] < 5:
            self.action = "farm"
        else:
            self.action = "eat"
        return self.action


# ================= AGENT (RENDER + MOVEMENT) =================
class RenderAgent:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 2
        self.target = None

    def set_target(self, pos):
        self.target = pos

    def update(self):
        if not self.target:
            return True

        tx, ty = self.target
        dx = tx - self.x
        dy = ty - self.y
        dist = math.hypot(dx, dy)

        if dist < 2:
            self.target = None
            return True
        else:
            self.x += self.speed * dx / dist
            self.y += self.speed * dy / dist
            return False

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 224, 189), (self.x, self.y, 20, 30))


# ================= GUI =================
class VillageGUI:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Agent AI – Pixel Village")
        self.font = pygame.font.SysFont("consolas", 16)
        self.clock = pygame.time.Clock()

        self.farm_pos = (140, 140)
        self.house_pos = (440, 140)

    def draw_map(self):
        # Farm
        pygame.draw.rect(self.screen, (139, 69, 19), (50, 50, 200, 200))
        # House
        pygame.draw.rect(self.screen, (178, 34, 34), (350, 50, 200, 200))
        # Lake
        pygame.draw.ellipse(self.screen, (30, 144, 255), (80, 380, 160, 100))
        # Market
        pygame.draw.rect(self.screen, (218, 165, 32), (350, 350, 200, 200))

    def draw_info(self, env, day, action):
        texts = [
            f"Day: {day}",
            f"Food: {env.food}",
            f"Weather: {env.weather}",
            f"Action: {action}"
        ]
        for i, t in enumerate(texts):
            text = self.font.render(t, True, (0, 0, 0))
            self.screen.blit(text, (10, 10 + i * 20))

    def render(self, env, agent_render, day, action):
        bg = (144, 238, 144) if env.weather == "sunny" else (170, 170, 170)
        self.screen.fill(bg)

        self.draw_map()
        agent_render.draw(self.screen)
        self.draw_info(env, day, action)

        pygame.display.flip()
        self.clock.tick(60)


# ================= CONTROL LOOP =================
def run_simulation(days=20):
    env = VillageEnvironment()
    agent = VillageAgent()
    gui = VillageGUI()

    render_agent = RenderAgent(300, 300)

    for day in range(1, days + 1):
        env.update_weather(day)
        perception = env.observe()
        action = agent.decide(perception)

        # đặt điểm đến
        if action == "farm":
            render_agent.set_target(gui.farm_pos)
        else:
            render_agent.set_target(gui.house_pos)

        arrived = False
        while not arrived:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            arrived = render_agent.update()
            gui.render(env, render_agent, day, action)

        # khi tới nơi → action ảnh hưởng môi trường
        env.apply_action(action)

        time.sleep(0.5)

        if env.food <= 0:
            print("Village has starved")
            break

    pygame.quit()


run_simulation()
