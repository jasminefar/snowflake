import turtle

class KochSnowflakeDrawer:
    def __init__(self, initial_length=300, min_length=5, speed=1):
        """
        Initialize the KochSnowflakeDrawer with initial parameters.
        
        initial_length: The starting length of each side of the snowflake.
        min_length: The minimum length of a segment before stopping recursion.
        speed: The drawing speed of the turtle.
        """
        self.initial_length = initial_length
        self.min_length = min_length
        self.speed = speed
        self.t = turtle.Turtle()
        self.t.speed(speed)
    
    def draw_koch_segment(self, length):
        """
        Recursively draw a Koch segment.
        
        length: The current length of the segment.
        """
        if length <= self.min_length:
            self.t.forward(length)
        else:
            length /= 3
            self.draw_koch_segment(length)
            self.t.left(60)
            self.draw_koch_segment(length)
            self.t.right(120)
            self.draw_koch_segment(length)
            self.t.left(60)
            self.draw_koch_segment(length)
    
    def draw_koch_snowflake(self, length):
        """
        Draw the full Koch snowflake by combining three Koch segments.
        
        length: The current length of each side of the snowflake.
        """
        for _ in range(3):
            self.draw_koch_segment(length)
            self.t.right(120)
    
    def start_drawing(self):
        """Start the drawing process."""
        turtle.bgcolor("black")
        self.t.color("white")
        self.t.penup()
        self.t.goto(-self.initial_length / 2, self.initial_length / 3)  # Position the turtle at the starting point
        self.t.pendown()
        self.draw_koch_snowflake(self.initial_length)
        turtle.done()
    
    def set_colors(self, background_color="black", snowflake_color="white"):
        """
        Set the colors for the background and the snowflake.
        
        background_color: The color of the background.
        snowflake_color: The color of the snowflake.
        """
        turtle.bgcolor(background_color)
        self.t.color(snowflake_color)

    def start_drawing_with_colors(self, background_color="black", snowflake_color="white"):
        """Start the drawing process with custom colors."""
        self.set_colors(background_color, snowflake_color)
        self.t.penup()
        self.t.goto(-self.initial_length / 2, self.initial_length / 3)  # Position the turtle at the starting point
        self.t.pendown()
        self.draw_koch_snowflake(self.initial_length)
        turtle.done()

# Create an instance of KochSnowflakeDrawer with parameters to extend drawing time and start drawing
snowflake = KochSnowflakeDrawer(initial_length=600, min_length=2, speed=1)
snowflake.start_drawing_with_colors(background_color="darkblue", snowflake_color="cyan")
