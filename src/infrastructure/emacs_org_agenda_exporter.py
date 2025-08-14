'''
Use Emacs to export org-agenda to iCalendar (ics) format.
'''

import subprocess
from src.domain.org_agenda_rules import OrgAgendaExporter

class EmacsAgendaExporter(OrgAgendaExporter):
    def __init__(self, org_agenda_exporter_path: str):
        self.org_agenda_exporter_path = org_agenda_exporter_path

    def export_org_agenda_to_ics(self):
        result = subprocess.run(
            [self.org_agenda_exporter_path],
            capture_output=True,
        )

        if result.returncode != 0:
            raise RuntimeError(f"Emacs export failed: {result.stderr}")
