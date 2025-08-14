(require 'org)

(setq org-icalendar-combined-agenda-file "/appdata/calendar/calendar.ics")

(setq org-agenda-files
      '("/appdata/agenda/main.org" "/appdata/agenda/calendar.org"))

(org-icalendar-combine-agenda-files)
