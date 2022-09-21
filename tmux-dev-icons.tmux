#!/usr/bin/env python3

import os

cwd = os.path.dirname(os.path.realpath(__file__))

placeholder = "#{pane_icon}"
call = f"#(python3 {cwd}/tmux-dev-icons.py #W)"

# Get the format strings for selected and unselected windows
status_current_format = os.popen('tmux show-option -gqv window-status-current-format').read()
status_format = os.popen('tmux show-option -gqv window-status-format').read()

if placeholder in status_current_format:
    # Add the icon to the current window
    os.system(f'tmux set-window-option -g window-status-current-format "{status_current_format.replace(placeholder, call)}"')

if placeholder in status_format:
    # Add the icon to the other windows
    os.system(f'tmux set-window-option -g window-status-format "{status_format.replace(placeholder, call)}"')
