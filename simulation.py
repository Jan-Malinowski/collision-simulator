import pygame
import time

pygame.init()
screen = pygame.display.set_mode((900, 600))
clock = pygame.time.Clock()
pygame.display.set_caption("Collistion simulator")
font = pygame.font.SysFont(None, 40)

class Slider:
    def __init__(self, x, y, w, min_val, max_val, start_val, txt, label=''):
        self.rect = pygame.Rect(x, y, w, 6)
        self.w = w
        self.handle_radius = 10
        self.min_val = min_val
        self.max_val = max_val
        self.value = start_val
        self.txt = txt
        self.label = label
        self.dragging = False
        self.enabled = True

    def get_pos_from_value(self):
        return self.rect.x + (self.value - self.min_val) / (self.max_val - self.min_val) * self.rect.w

    def get_value_from_pos(self, x):
        ratio = (x - self.rect.x) / self.rect.w
        ratio = max(0, min(1, ratio))
        return self.min_val + ratio * (self.max_val - self.min_val)

    def handle_event(self, event):
        if not self.enabled:
            return
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_hovering_handle(event.pos):
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                self.value = self.get_value_from_pos(event.pos[0])

    def is_hovering_handle(self, pos):
        handle_x = self.get_pos_from_value()
        return pygame.Rect(handle_x - self.handle_radius, self.rect.centery - self.handle_radius,
                           self.handle_radius * 2, self.handle_radius * 2).collidepoint(pos)

    def draw(self, screen):
        line_color = (220, 220, 220) if self.enabled else (180, 180, 180)
        handle_color = (0, 120, 255) if self.enabled else (150, 150, 150)

        pygame.draw.rect(screen, line_color, self.rect)
        handle_x = int(self.get_pos_from_value())
        pygame.draw.circle(screen, handle_color, (handle_x, self.rect.centery), self.handle_radius)

        if self.txt:
            text = font.render(f"{self.label}: {self.value:.1f}", True, (0, 0, 0))
            screen.blit(text, (self.rect.x, self.rect.y - 37))
        else:
            text = font.render(f"{self.label}", True, (0, 0, 0))
            screen.blit(text, (self.rect.x, self.rect.y - 37))

    def get_value(self):
        return self.value

    def set_enabled(self, state: bool):
        self.enabled = state

colors = {
    "Red": {
        "normal": (255, 0, 0),
        "hover": (255, 100, 100)
    },
    "Green": {
        "normal": (0, 255, 0),
        "hover": (100, 255, 100)
    },
    "Blue": {
        "normal": (0, 0, 255),
        "hover": (100, 100, 255)
    },
    "Grey": {
        "normal": (128, 128, 128),
        "hover": (180, 180, 180)
    },
    "Yellow": {
        "normal": (255, 255, 0),
        "hover": (255, 255, 150)
    },
    "Black": (0, 0, 0),
    "White": (255, 255, 255)
}

button_color = colors["Green"]["normal"]
button_hover_color = colors["Green"]["hover"]
button_rect = pygame.Rect(350, 410, 200, 60)
button_text = font.render("Start", True, colors["White"])
border_thickness = 3

running = True
simulation = -1
cube1 = {'pos': [53, 322-25], 'vel':[0, 0], 'mass':[5], 'size':[50]}
cube2 = {'pos': [500, 322-25], 'vel':[0, 0], 'mass':[5], 'size':[50]}

slider_mass_c1 = Slider(50, 410, 250, 1, 10, 5, 1, label="Mass")
slider_velocity_c1 = Slider(50, 480, 250, 0, 10, 0, 1, label="Velocity")
slider_position_c1 = Slider(50, 550, 250, 50+border_thickness, 345, 50+border_thickness, 0, label="Position", )
slider_mass_c2 = Slider(600, 410, 250, 1, 10, 5, 1, label="Mass")
slider_velocity_c2 = Slider(600, 480, 250, 0, 10, 0, 1, label="Velocity", )
slider_position_c2 = Slider(600, 550, 250, 555, 850-border_thickness, 850-border_thickness, 0, label="Position")

def get_params():
    cube1["mass"][0]=slider_mass_c1.get_value()
    cube1["size"][0]=slider_mass_c1.get_value()*10
    cube1["vel"][0]=slider_velocity_c1.get_value()
    cube1["pos"][0]=slider_position_c1.get_value()
    cube1["pos"][1]=348-slider_mass_c1.get_value()*10
    cube2["mass"][0]=slider_mass_c2.get_value()
    cube2["size"][0]=slider_mass_c2.get_value()*10
    cube2["vel"][0]=slider_velocity_c2.get_value()*-1
    cube2["pos"][0]=slider_position_c2.get_value()-slider_mass_c2.get_value()*10
    cube2["pos"][1]=348-slider_mass_c2.get_value()*10

def sliders_on_off(flag):
    slider_mass_c1.set_enabled(flag)
    slider_velocity_c1.set_enabled(flag)
    slider_position_c1.set_enabled(flag)
    slider_mass_c2.set_enabled(flag)
    slider_velocity_c2.set_enabled(flag)
    slider_position_c2.set_enabled(flag)
    
while running:
    screen.fill("gray")
    pygame.draw.rect(screen, colors["White"], (50, 50, 800, 300))
    pygame.draw.rect(screen, colors["Black"], (50, 50, 800, 300), border_thickness)

    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    #Start/stop button section
    if button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, button_hover_color, button_rect)
        if mouse_click[0]:
            simulation *=-1
            if(simulation==-1):
                button_text = font.render("Start", True, colors["White"])
                button_color = colors["Green"]["normal"]
                button_hover_color = colors['Green']["hover"]
                get_params()
                sliders_on_off(True)
            else:
                button_text = font.render("Stop", True, colors["White"])
                button_color = colors["Red"]["normal"]
                button_hover_color = colors["Red"]["hover"]
                sliders_on_off(False)
            pygame.draw.rect(screen, button_hover_color, button_rect)
            time.sleep(0.2)
    else:
        pygame.draw.rect(screen, button_color, button_rect)
    
    text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, text_rect)

    if simulation==1:
        cube1['pos'][0]+=cube1['vel'][0]
        cube1['pos'][0]=max(cube1['pos'][0], 50+border_thickness)
        cube1['pos'][0]=min(cube1['pos'][0], 850-cube1['size'][0]-border_thickness)
        if(cube1['pos'][0]==850-cube1['size'][0]-border_thickness):
            cube1["vel"][0]*=-1
        if(cube1['pos'][0]==50+border_thickness):
            cube1["vel"][0]*=-1
        
        cube2['pos'][0]+=cube2['vel'][0]
        cube2['pos'][0]=max(cube2['pos'][0], 50+border_thickness)
        cube2['pos'][0]=min(cube2['pos'][0], 850-cube2['size'][0]-border_thickness)
        if(cube2['pos'][0]==850-cube2['size'][0]-border_thickness):
            cube2["vel"][0]*=-1
        if(cube2['pos'][0]==50+border_thickness):
            cube2["vel"][0]*=-1
    
        if(cube2["pos"][0]-cube1["pos"][0]-cube1["size"][0]<=0):
            v1=cube1["vel"][0]
            v2=cube2["vel"][0]
            m1=cube1["mass"][0]
            m2=cube2["mass"][0]
            cube1["vel"][0]=((m1-m2)*v1+2*m2*v2)/(m1+m2)
            cube2["vel"][0]=((m2-m1)*v2+2*m1*v1)/(m1+m2)
    
    pygame.draw.rect(screen, colors["Blue"]["normal"], (cube1['pos'][0], cube1['pos'][1], cube1['size'][0], cube1['size'][0]))
    pygame.draw.rect(screen, colors["Red"]["normal"], (cube2['pos'][0], cube2['pos'][1], cube2['size'][0], cube2['size'][0]))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION and simulation==-1:
            get_params()
        slider_mass_c1.handle_event(event)
        slider_velocity_c1.handle_event(event)
        slider_position_c1.handle_event(event)
        slider_mass_c2.handle_event(event)
        slider_velocity_c2.handle_event(event)
        slider_position_c2.handle_event(event)
        

    slider_mass_c1.draw(screen)
    slider_velocity_c1.draw(screen)
    slider_position_c1.draw(screen)
    slider_mass_c2.draw(screen)
    slider_velocity_c2.draw(screen)
    slider_position_c2.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
