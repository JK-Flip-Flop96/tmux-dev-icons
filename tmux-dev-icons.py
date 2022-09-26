import sys

icons = {
    "tmux" : "",
    "[tmux]" : "",
    "nvim" : "", 
    "vim" : "", 
    "python" : "", 
    "python3" : "",
    "pwsh" : "",
    "zsh " : "",
    "bash" : "",
    "git" : "",
    "fzf" : "",
}

colours = {
    "tmux" : "#21a819",
    "[tmux]" : "#21a819",
    "nvim" : "#93e75a",
    "vim" : "#078a2a",
    "python" : "#4b8bbe",
    "Python3" : "#4b8bbe",
    "pwsh" : "#5da4b5",
    "zsh" : "#eb5620",
    "bash" : "#4ba244",
    "git" : "#e14528",
    "fzf" : "#ee0058"
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
