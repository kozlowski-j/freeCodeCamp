class Rectangle:

    def __init__(self, width, height):
        self.height = height
        self.width = width

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 2 * self.height + 2 * self.width

    def get_diagonal(self):
        return (self.height ** 2 + self.width ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            top = "*" * self.width + "\n"
            bottom = top
            walls = "*" * self.width + "\n"
            walls = walls * (self.height - 2)
            picture = top + walls + bottom
            return picture

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def get_amount_inside(self, shape):
        if self.width > shape.width:
            if self.height > shape.height:
                width_fits = int(self.width / shape.width)
                height_fits = int(self.height / shape.height)
                return width_fits * height_fits

            else:
                return 0
        else:
            return 0


class Square(Rectangle):

    def __init__(self, side_length):
        super().__init__(side_length, side_length)
        self.side_length = side_length

    def __str__(self):
        return f"Square(side={self.side_length})"

    def set_side(self, new_side_length):
        super().set_width(new_side_length)
        super().set_height(new_side_length)
        self.side_length = new_side_length

    def set_width(self, new_width):
        self.set_side(new_width)

    def set_height(self, new_height):
        self.set_side(new_height)
