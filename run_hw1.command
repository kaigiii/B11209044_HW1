#!/bin/zsh
# Launcher to open two Terminal windows and run server and client executables
# Double-click this file in Finder to start both programs.

DIR="$(cd "$(dirname "$0")" && pwd)"

osascript <<EOF
tell application "Terminal"
    do script "cd '$DIR'; ./macOS_dist/HW1_server; exec $SHELL"
    do script "cd '$DIR'; ./macOS_dist/HW1_client; exec $SHELL"
    activate
end tell
EOF
