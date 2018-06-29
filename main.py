import turtle
import random


class EternalGoldenBraid(object):
    def __init__(self):
        # todo find limit of ratio between length and width
        # todo record polygons?
        # todo input color and get three shades of it
        # todo limit
        self.length = 75
        self.width = int(self.length / 4)  # width cannot be greater than a quarter of the length
        window = turtle.Screen()
        window.bgcolor("black")  # background color
        max_x, max_y = window.screensize()
        # todo generate a ton of coordinates
        coordinates = []

        # todo calculate start, end and spacing based on length and width
        y_spacing = int(self.length + (1.2 * self.width))
        y_end = int(max_y + y_spacing)# ((3*self.length)/7))
        y_start = -y_end

        x_spacing = int(self.length + (2 * self.width))
        x_end = int(max_x + x_spacing)# (self.length/2))
        x_start = -x_end

        for y in range(y_start, y_end, y_spacing):
            for x in range(x_start, x_end, x_spacing):
                coordinates.append([x, y])
        random.shuffle(coordinates)  # shuffle order braids are drawn
        for coordinate_set in coordinates:
            self.draw_eternal_golden_braid(coordinate_set)
        window.exitonclick()

    def draw_eternal_golden_braid_third(self, my_turtle, fill_color):
        my_turtle.color('black', fill_color)
        my_turtle.begin_fill()
        my_turtle.pendown()
        my_turtle.forward(self.width)
        my_turtle.left(120)

        my_turtle.forward(self.length)
        my_turtle.left(120)

        my_turtle.forward(self.length+self.width)
        my_turtle.left(60)

        my_turtle.forward(self.width)
        my_turtle.left(120)

        my_turtle.forward(self.length)
        my_turtle.right(120)

        my_turtle.forward(self.length-(self.width*2))
        my_turtle.end_fill()
        my_turtle.penup()

    @staticmethod
    def center_turtle_for_drawing(my_turtle):
        my_turtle.hideturtle()
        my_turtle.penup()
        my_turtle.forward(70)
        my_turtle.right(90)
        my_turtle.forward(70)
        my_turtle.left(90)

    def generate_random_color_gradient_list(self):
        # todo get input color and convert to hex
        # todo get hex stopping point programmatically
        start_color = generate_random_hex_color_code()
        color_int = int(start_color[1:], base=16)
        color_int += 12800
        if color_int > 16777214:  # handles when end color is out of bounds #FFFFFF
            return self.generate_random_color_gradient_list()
        end_color = '#' + str(hex(color_int))[2:]
        # todo handle out of range
        # todo make sure they are shades of same color
        return linear_gradient(start_color, end_color, 3)

    def draw_eternal_golden_braid(self, coordinates):

        tom = turtle.Turtle()
        tom.speed(0)
        tom.hideturtle()
        tom.penup()
        tom.goto(coordinates[0], coordinates[1])
        # self.center_turtle_for_drawing(tom)
        color_list = self.generate_random_color_gradient_list()
        for i in range(3):
            # determine color
            color = color_list['hex'][i]
            self.draw_eternal_golden_braid_third(tom, color)
            # resets
            tom.backward(self.length-(self.width*3))
            tom.left(180)
        tom.penup()


def generate_random_hex_color_code():
    values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
    hex_values = {'10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}
    color = "#"
    for _ in range(6):
        x = values[random.randint(0, len(values) - 1)]
        if x in hex_values.keys():
            x = hex_values[x]
        color += x
    return color



def hex_to_RGB(hex):
    # https://bsou.io/posts/color-gradients-with-python
    ''' "#FFFFFF" -> [255,255,255] '''
    # Pass 16 to the integer function for change of base
    return [int(hex[i:i + 2], 16) for i in range(1, 6, 2)]


def RGB_to_hex(RGB):
    # https://bsou.io/posts/color-gradients-with-python
    ''' [255,255,255] -> "#FFFFFF" '''
    # Components need to be integers for hex to make sense
    RGB = [int(x) for x in RGB]
    return "#" + "".join(["0{0:x}".format(v) if v < 16 else
                          "{0:x}".format(v) for v in RGB])


def color_dict(gradient):
    ''' Takes in a list of RGB sub-lists and returns dictionary of
      colors in RGB and hex form for use in a graphing function
      defined later on '''
    return {"hex": [RGB_to_hex(RGB) for RGB in gradient],
            "r": [RGB[0] for RGB in gradient],
            "g": [RGB[1] for RGB in gradient],
            "b": [RGB[2] for RGB in gradient]}


def linear_gradient(start_hex, finish_hex="#FFFFFF", n=10):
    ''' returns a gradient list of (n) colors between
      two hex colors. start_hex and finish_hex
      should be the full six-digit color string,
      inlcuding the number sign ("#FFFFFF") '''
    # Starting and ending colors in RGB form
    s = hex_to_RGB(start_hex)
    f = hex_to_RGB(finish_hex)
    # Initilize a list of the output colors with the starting color
    RGB_list = [s]
    # Calcuate a color at each evenly spaced value of t from 1 to n
    for t in range(1, n):
        # Interpolate RGB vector for color at the current value of t
        curr_vector = [
            int(s[j] + (float(t) / (n - 1)) * (f[j] - s[j]))
            for j in range(3)
        ]
        # Add it to our list of output colors
        RGB_list.append(curr_vector)

    return color_dict(RGB_list)

EternalGoldenBraid()
