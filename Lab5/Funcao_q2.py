from math import exp, cos, pi, sin


class FuncQ2():
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.const = ((10 * pi) - 3) / 3  # constante

    def a(self):  # primeira função
        self.result = 3 * self.x - cos(self.y * self.z) - 0.5
        return self.result

    def b(self):  # segunda função
        self.result = self.x ** 2 - 625 * self.y ** 2 - 0.25
        return self.result

    def c(self):  # terceira função
        self.result = exp(-self.x * self.y) + 20 * self.z + self.const
        return self.result

    # Derivadas de a:
    def da_x(self):
        return 3

    def da_y(self):
        self.result = -sin(self.y * self.z) * self.z
        return self.result

    def da_z(self):
        self.result = -sin(self.y * self.z) * self.y
        return self.result

    # Derivadas de b:
    def db_x(self):
        self.result = 2 * self.x
        return self.result

    def db_y(self):
        self.result = -625 * 2 * self.y
        return self.result

    def db_z(self):
        return 0

    # Derivadas de c:
    def dc_x(self):
        self.result = exp(-self.x * self.y) * (-self.y)
        return self.result

    def dc_y(self):
        self.result = exp(-self.x * self.y) * (-self.x)
        return self.result

    def dc_z(self):
        return 20
