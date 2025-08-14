#!/usr/bin/env bash


DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

emacs -Q --script "$DIR/org-agenda-ics-exporter.el"
