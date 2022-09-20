import sys

icons = {
    "nvim" : "", 
    "vim " : "", 
    "python" : "", 
    "python3" : "",
    "pwsh" : "",
    "zsh " : "",
}

colours = {
    "nvim" : "#93e75a",
    "vim" : "#078a2a",
    "python" : "#4b8bbe",
    "Python3" : "#4b8bbe",
    "pwsh" : "#4568a9",
    "zsh" : "#eb5620",
}

pane_title = sys.argv[1]

icon = ""
colour = ""

if pane_title in icons:
    icon = icons[pane_title]
else:
    icon = ""

if pane_title in colours:
    colour = colours[pane_title]
else:
    colour = "#89b4fa"

print("#[fg={}]{}#[default]".format(colour, icon))
