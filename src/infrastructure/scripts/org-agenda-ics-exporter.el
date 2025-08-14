(require 'org)

(setq org-icalendar-combined-agenda-file "./calendar.ics")

(setq org-agenda-files
      '("/home/jerome/misc/gtd/main.org" "/home/jerome/misc/gtd/calendar.org"))

(org-icalendar-combine-agenda-files)
