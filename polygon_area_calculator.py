def add_time(start, duration, day_of_week=False):

  days_of_the_week_index = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6}

days_of_the_week_array = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

duration_tuple = duration.partition(":")
print(duration_tuple)
duration_hours = int(duration_tuple[0])
duration_minutes = int(duration_tuple[2])

start_tuple = start.partition(":")
start_minutes_tuple = start_tuple[2].partition(" ")
start_hours = int(start_tuple[0])
start_minutes = int(start_minutes_tuple[0])
am_or_pm = start_minutes_tuple[2]
am_and_pm_flip = {"AM": "PM", "PM": "AM"}

amount_of_days = int(duration_hours / 24)

class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, w):
        self.width = w

    def set_height(self, h):
        self.height = h

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'

        pic = '*' * self.width + '\n'
        pic = pic * self.height
        return pic

    def get_amount_inside(self, ob):
        return self.get_area() // ob.get_area()


class Square(Rectangle):
    def __init__(self, s):
        super().__init__(s, s)

    def __str__(self):
        return f'Square(side={self.width})'

    def set_side(self, s):
        self.width = s
        self.height = s