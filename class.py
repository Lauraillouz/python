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

    def nail_in(self, nail):
        nail.nail_in()

    def nail_out(self, nail):
        nail.nail_out()


class Screwdriver:
    def __init__(self, size_in_mm=2):
        self.size_in_mm = size_in_mm

    def screw_in(self, screw):
        screw.screw_in()

    def screw_out(self, screw):
        screw.screw_out()


hammer = Hammer("blue")
screwdriver = Screwdriver(3)
toolbox = ToolBox([hammer, screwdriver])

print(toolbox.tools)
