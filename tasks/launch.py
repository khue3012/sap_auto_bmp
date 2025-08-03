# tasks/launch.py
from invoke import task
import time
import os

SAP_LOGON_PATH = (
    r"C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe"
)

@task
def launch(c, sid="YOUR_SID"):
    """Starts SAP Logon and waits for GUI to initialize."""
    c.run(f'start "" "{SAP_LOGON_PATH}" /system="{sid}"', echo=True)
    time.sleep(5)
