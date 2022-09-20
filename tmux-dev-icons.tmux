#!/usr/bin/env python3

import os

placeholder = "#{pane_icon}"
call = "#(python3 tmux-dev-icons.py #W)"

# Get the format strings for selected and unselected windows
status_current_format = os.popen('tmux show-option -gqv window-status-current-format').read()
status_format = os.popen('tmux show-option -gqv window-status-format').read()

format_current = placeholder in status_current_format
format_other = placeholder in status_format

if format_current:
    # Add the icon to the current window
    os.system('tmux set-window-option -g window-status-current-format ' + status_current_format.replace(placeholder, call))

if format_other:
    # Add the icon to the other windows
    os.system('tmux set-window-option -g window-status-format ' + status_format.replace(placeholder, call))
