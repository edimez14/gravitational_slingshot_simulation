import pygame
import math

# configuration variables
pygame.init()
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravitational Slingshot Simulation")

# mass of the planet
PLANET_MASS = 100
# mass of the ship
SHIP_MASS = 5
G = 5
FPS = 60
# size of the planet in the window
PLANET_SIZE = 50
# size of the object or vessel
OBJ_SIZE = 5
# scale speed
VEL_SCALE = 100

# image of background
BG = pygame.transform.scale(pygame.image.load(
    "assets/background.jpg"), (WIDTH, HEIGHT))

# image of planet
PLANET = pygame.transform.scale(pygame.image.load(
    "assets/jupiter.png"), (PLANET_SIZE * 2, PLANET_SIZE * 2))

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


# The `Planet` class represents a celestial body with coordinates and mass, and has a method to draw
# it on a window.
class Planet:
    def __init__(self, x, y, mass):
        """
        The function initializes an object with attributes for x-coordinate, y-coordinate, and mass.
        
        :param x: The `x` parameter in the `__init__` method is typically used to represent the
        x-coordinate of an object in a 2D space. It is a positional parameter that initializes the `x`
        attribute of an object with the value passed to it during object creation
        :param y: The `y` parameter in the `__init__` method is typically used to represent the
        y-coordinate of an object in a two-dimensional space. It helps define the position of the object
        along the vertical axis
        :param mass: The `mass` parameter in the `__init__` method of a class is used to initialize the
        mass attribute of an object. It represents the mass of the object being created
        """
        self.x = x
        self.y = y
        self.mass = mass

    def draw(self):
        """
        The `draw` function in the given Python code snippet is responsible for rendering an image of a
        planet on a window at the specified coordinates.
        """
        window.blit(PLANET, (self.x - PLANET_SIZE, self.y - PLANET_SIZE))


# The Spacecraft class represents a spacecraft object with attributes for position, velocity, and
# mass, along with methods for moving the spacecraft based on gravitational forces and drawing it on a
# window using Pygame.
class Spacecraft:
    def __init__(self, x, y, vel_x, vel_y, mass):
        """
        This Python function initializes an object with attributes for position, velocity, and mass.
        
        :param x: The `__init__` method you provided seems to be a constructor for a class. It
        initializes the object with the given parameters
        :param y: The `y` parameter in the `__init__` method represents the initial y-coordinate of an
        object in a 2D space. It is used to define the starting position of the object along the
        vertical axis
        :param vel_x: The `vel_x` parameter in the `__init__` method of your class appears to represent
        the initial velocity of an object in the x-direction. This parameter is used to initialize the
        `vel_x` attribute of an instance of the class with a specific value when the object is created
        :param vel_y: The `vel_y` parameter in the `__init__` method of your class appears to represent
        the initial velocity of the object in the y-direction. This parameter is used to initialize the
        `vel_y` attribute of the object when an instance of the class is created
        :param mass: The `__init__` method you provided seems to be part of a class definition. The
        parameters `x`, `y`, `vel_x`, `vel_y`, and `mass` are used to initialize the attributes of an
        object of that class
        """
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.mass = mass

    def move(self, planet=None):
        """
        The `move` function calculates the gravitational force between two objects and updates the
        position of one object based on the force and acceleration.
        
        :param planet: The `planet` parameter in the `move` method represents an object that the current
        object is interacting with. The method calculates the distance between the current object and
        the planet, determines the force of gravity between them, calculates the acceleration, and
        updates the velocity and position of the current object accordingly based on
        """
        distance = math.sqrt((self.x - planet.x)**2 + (self.y - planet.y)**2)
        force = (G * self.mass * planet.mass) / distance ** 2

        acceleration = force / self.mass
        angle = math.atan2(planet.y - self.y, planet.x - self.x)

        acceleration_x = acceleration * math.cos(angle)
        acceleration_y = acceleration * math.sin(angle)

        self.vel_x += acceleration_x
        self.vel_y += acceleration_y

        self.x += self.vel_x
        self.y += self.vel_y

    def draw(self):
        """
        The function `draw` uses Pygame to draw a red circle at the coordinates `(self.x, self.y)` with
        a specified size.
        """
        pygame.draw.circle(window, RED, (int(self.x), int(self.y)), OBJ_SIZE)


def create_ship(location, mouse):
    """
    This Python function creates a spacecraft object with a specified location and velocity based on the
    mouse position.
    
    :param location: The `location` parameter represents the current position of the ship in the game
    world. It is a tuple containing the x and y coordinates of the ship
    :param mouse: The `mouse` parameter likely represents the current position of the mouse cursor on
    the screen. It is being used in the `create_ship` function to calculate the velocity components of
    the spacecraft based on the difference between the target location (`location`) and the mouse
    position
    :return: An object of the Spacecraft class with the specified parameters (t_x, t_y, vel_x, vel_y,
    SHIP_MASS) is being returned.
    """
    t_x, t_y = location
    m_x, m_y = mouse
    vel_x = (m_x - t_x) / VEL_SCALE
    vel_y = (m_y - t_y) / VEL_SCALE
    obj = Spacecraft(t_x, t_y, vel_x, vel_y, SHIP_MASS)
    return obj


def main():
    """
    The main function in this Python code creates a simulation where objects are launched from a central
    planet and interact with it based on user input.
    """
    # The code snippet `run = True`, `clock = pygame.time.Clock()`, `planet = Planet(WIDTH // 2,
    # HEIGHT // 2, PLANET_MASS)`, `objects = []`, and `tem_obj_pos = None` within the `main()`
    # function serves the following purposes:
    run = True
    clock = pygame.time.Clock()
    planet = Planet(WIDTH // 2, HEIGHT // 2, PLANET_MASS)
    objects = []
    tem_obj_pos = None

    # The code snippet you provided is the main game loop in the Python script. Here's a breakdown of
    # what each part of the loop is doing:
    while run:
        clock.tick(FPS)
        # `mouse_pos = pygame.mouse.get_pos()` is a line of code in the main game loop that retrieves
        # the current position of the mouse cursor on the screen using Pygame.
        mouse_pos = pygame.mouse.get_pos()

        # The code snippet you provided is part of the main game loop in the Python script. Here's a
        # breakdown of what each part of the loop is doing:
        for event in pygame.event.get():
            # The code snippet `if event.type == pygame.QUIT: run = False` is checking if the event
            # type triggered by the user is a request to quit the Pygame window.
            if event.type == pygame.QUIT:
                run = False

            # The code snippet you provided is handling the logic for creating a spacecraft object
            # when the user performs a mouse click action in the Pygame window.
            if event.type == pygame.MOUSEBUTTONDOWN:
                # The code snippet `if tem_obj_pos:
                #                     obj = create_ship(tem_obj_pos, mouse_pos)
                #                     objects.append(obj)
                #                     tem_obj_pos = None` is responsible for creating a spacecraft
                # object when the user performs a mouse click action in the Pygame window.
                if tem_obj_pos:
                    obj = create_ship(tem_obj_pos, mouse_pos)
                    objects.append(obj)
                    tem_obj_pos = None
                # The `else: tem_obj_pos = mouse_pos` part of the code snippet you provided is
                # handling the scenario where the user has not clicked to create a spacecraft object
                # (`tem_obj_pos` is not set).
                else:
                    tem_obj_pos = mouse_pos

        # `window.blit(BG, (0, 0))` is a Pygame function call that is used to draw an image onto the
        # game window at a specified position. In this case, it is drawing the background image `BG`
        # onto the game window starting from the top-left corner (position `(0, 0)`). This function
        # essentially copies the pixels of the background image onto the game window, allowing it to
        # serve as the backdrop for the game simulation.
        window.blit(BG, (0, 0))

        # The code snippet `if tem_obj_pos: pygame.draw.line(window, WHITE, tem_obj_pos, mouse_pos, 1)
        # pygame.draw.circle(window, RED, tem_obj_pos, OBJ_SIZE)` is responsible for drawing a line
        # and a circle on the Pygame window when a temporary object position (`tem_obj_pos`) exists.
        if tem_obj_pos:
            pygame.draw.line(window, WHITE, tem_obj_pos, mouse_pos, 1)
            pygame.draw.circle(window, RED, tem_obj_pos, OBJ_SIZE)

        # The code snippet you provided is a loop that iterates over the list of objects in the
        # simulation. Here's a breakdown of what each part of the loop is doing:
        for obj in objects[:]:
            obj.draw()
            obj.move(planet)
            off_screen = obj.x < 0 or obj.x > WIDTH or obj.y < 0 or obj.y > HEIGHT
            collided = math.sqrt((obj.x - planet.x)**2 +
                                 (obj.y - planet.y)**2) <= PLANET_SIZE
            # The code snippet `if off_screen or collided: objects.remove(obj)` is a conditional
            # statement within the loop that iterates over the list of objects in the simulation.
            # Here's what it does:
            if off_screen or collided:
                objects.remove(obj)

        # `planet.draw()` is a method call that is responsible for rendering an image of a planet on
        # the game window at the specified coordinates. In the context of the provided code snippet,
        # the `draw()` method of the `Planet` class is used to display an image of the planet
        # (Jupiter) on the game window. This method utilizes Pygame's `blit()` function to draw the
        # planet image at the position defined by the planet's x and y coordinates, adjusting for the
        # size of the planet image.
        planet.draw()
        # `pygame.display.update()` is a Pygame function that is used to update the contents of the
        # entire display window. When this function is called, any changes made to the display, such
        # as drawing shapes, images, or text, become visible to the user.
        pygame.display.update()

    # `pygame.quit()` is a function in Pygame that is used to uninitialize all Pygame modules. When
    # you call `pygame.quit()`, it shuts down all Pygame modules and frees up any resources that were
    # being used by Pygame during the program's execution. This function is typically called at the
    # end of a Pygame program to ensure proper cleanup and release of resources before the program
    # exits.
    pygame.quit()


if __name__ == '__main__':
    main()
