import os
from fastapi import FastAPI
from src.application.sync_org_agenda import SyncOrgAgendaUseCase
from src.infrastructure.emacs_org_agenda_exporter import EmacsAgendaExporter

app = FastAPI()

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPT_PATH = os.path.abspath(
    os.path.join(CURRENT_DIR, "..", "infrastructure", "scripts", "org-agenda-ics-exporter-runner.sh")
)

exporter = EmacsAgendaExporter(SCRIPT_PATH)
use_case = SyncOrgAgendaUseCase(exporter)

@app.get("/generate-ics")
def generate_ics():
    try:
        use_case.execute()
        return {"message": "calendar successfully updated"}
    except Exception as e:
        return {"error": str(e)}
