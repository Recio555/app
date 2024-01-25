class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        return "Drawing Circle"

class Square(Shape):
    def draw(self):
        return "Drawing Square"

class ShapeFactory:
    def create_shape(self, shape_type):
        if shape_type == "Circle":
            return Circle()
        elif shape_type == "Square":
            return Square()
        else:
            raise ValueError("Invalid shape type")

# Uso del Factory
factory = ShapeFactory()

circle = factory.create_shape("Circle")
square = factory.create_shape("Square")

print(circle.draw())  # Debería imprimir "Drawing Circle"
print(square.draw())  # Debería imprimir "Drawing Square"
