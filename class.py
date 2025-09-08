class ToolBox:
    def __init__(self, tools=[]):
        self.tools = tools

    def add_tool(self, tool):
        self.tools.append(tool)

    def remove_tool(self, tool):
        self.tools.remove(tool)


class Hammer:
    def __init__(self, color="red"):
        self.color = color

    def paint(self, color):
        self.color = color

    def nail_in(self, nail):
        nail.nail_in()

    def nail_out(self, nail):
        nail.remove()

    def __repr__(self):
        """Représentation de l'objet."""
        return f"Marteau de couleur {self.color}"


class Screwdriver:
    def __init__(self, size_in_mm=2):
        self.size_in_mm = size_in_mm

    def screw_in(self, screw):
        screw.tighten()

    def screw_out(self, screw):
        screw.loosen()

    def __repr__(self):
        """Représentation de l'objet."""
        return f"Tournevis de taille {self.size_in_mm}"


class Screw:
    """Vis."""

    MAX_TIGHTNESS = 5

    def __init__(self, tightness=0):
        """Initialise son degré de serrage."""
        self.tightness = tightness

    def loosen(self):
        """Déserre le vis."""
        if self.tightness > 0 and self.tightness < self.MAX_TIGHTNESS:
            self.tightness -= 1
        else:
            self.tightness = 0
            print("La vis est déjà relâchée")

    def tighten(self):
        """Serre le vis."""
        if self.tightness < self.MAX_TIGHTNESS and self.tightness > 0:
            self.tightness += 1
        else:
            self.tightness = self.MAX_TIGHTNESS
            print("La vis est déjà serrée au maximum")

    def __repr__(self):
        """Représentation de l'objet."""
        return f"Vis avec un serrage de {self.tightness}"

    def __str__(self):
        """Retourne une forme lisible de l'objet."""
        return "Vis avec un serrage de {}".format(self.tightness)


class Nail:
    """Clou."""

    def __init__(self, in_wall=False):
        """Initialise son statut "dans le mur"."""
        self.in_wall = in_wall

    def nail_in(self):
        """Enfonce le clou dans un mur."""
        if not self.in_wall:
            self.in_wall = True
        else:
            print("Le clou est déjà dans le mur")

    def remove(self):
        """Enlève le clou du mur."""
        if self.in_wall:
            self.in_wall = False
        else:
            print("Le clou est déjà hors du mur")

    def __repr__(self):
        """Représentation de l'objet."""
        return f"Clou {'dans le mur' if self.in_wall else 'hors du mur'}"

    def __str__(self):
        """Retourne une forme lisible de l'objet."""
        wall_state = "dans le mur" if self.in_wall else "hors du mur"
        return f"Clou {wall_state}."


hammer = Hammer("blue")
screwdriver = Screwdriver(3)
toolbox = ToolBox([hammer, screwdriver])

print(toolbox.tools)

screw = Screw(tightness=6)
print(screw)

screwdriver.screw_in(screw)
print(screw)

nail = Nail(in_wall=True)
print(nail)

hammer.nail_in(nail)
print(nail)
