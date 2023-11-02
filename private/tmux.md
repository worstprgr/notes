# tmux
Enter tmux: `tmux`  
Tmux cmd prompt: `C-b :` -> separate multiple commands with `;`  
Split vertical: `C-b "` or `split-window -v`  
Split horizontal: `C-b %` or `split-window -h`  
Switch between panes: `C-b <arrow-keys>`  
Close active pane: `Ctrl + b + x` -> `y`  
Choose sessions, windows and panes: `C-b s` -> Tag & untag: `t` & `T` -> kill tagged: `X` -> kill all: `x` -> exit tree: `q`  
Scroll through current pane:  `C-b [` quit with `q`. Or activate the mouse with `echo "set -g mouse on" >> ~/.tmux.conf` (but didn't worked for me)  

