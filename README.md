# tmux-dev-icons

A plugin which provides icons for tmux panes.

## Installation

### Prerequisites

This plugin requires a NerdFont to be used. Grab one from [here](https://www.nerdfonts.com/font-downloads).

This plugin also assumes that your terminal supports truecolor (24-bit). 8 and 256 colour modes are planned.

### Tmux Plugin Manager

Add the following line to `~/.tmux.conf`:

```
set -g @plugin 'JK-Flip-Flop96/tmux-dev-icons'
```

Ensure this line is set before the plugin manager is run i.e. before `run '~/.tmux/plugins/tpm/tpm'`

## Usage

Add `#{pane_icon}` to your `window-status-format` and `window-status-format-current` to decide where the icon will be placed

The active foreground colour is not reset after the pane icon so the foreground colour of anything after it will match the colour of the icon unless the colour is explicitly changed.

### Adding icons

Currently the only way to add your own custom icons/colours is to manually edit the dictionaries in `tmux-dev-icons.py`. This isn't ideal as changes to the file may/will be overwritten whenever the plugin is updated by TPM. *THIS WILL CHANGE*

## Planned Features

- More colour modes - monochrome, 8, 16 and 256 colour.
	- `#{pane_icon_active}` element to allow for having only the active window's icon highlighted.
- Option to alter background colour instead.
- Loading of custom configuration file for icons from a location of the user's choosing.
