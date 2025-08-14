'''
Sync org-agenda with iCalendar (ics) file.
'''

from src.domain.org_agenda_rules import OrgAgendaExporter

class SyncOrgAgendaUseCase:
    def __init__(self, exporter: OrgAgendaExporter):
        self.exporter = exporter

    def execute(self) -> str:
        self.exporter.export_org_agenda_to_ics()
