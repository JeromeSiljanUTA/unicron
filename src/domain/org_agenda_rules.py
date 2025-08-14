'''
Export org-agenda to iCalendar (ics) format.
'''
from abc import ABC, abstractmethod

class OrgAgendaExporter(ABC):
    @abstractmethod
    def export_org_agenda_to_ics(self) -> str:
        '''Export the current org-agenda to ICS file and return the value as a string.'''
        pass


class OrgAgendaFileWatcher():
    @abstractmethod
    def watch_org_agenda_files(self, callback: callable):
        '''Watch org-agenda files and trigger a callback on change.'''
        pass
