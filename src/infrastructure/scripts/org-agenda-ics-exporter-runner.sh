#!/usr/bin/env bash

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

chown 1000:1000 /appdata/calendar/calendar.ics
emacs -Q --script "$DIR/org-agenda-ics-exporter.el"
