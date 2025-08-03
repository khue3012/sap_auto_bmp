# tasks/enter.py
from invoke import task
import sap_entry

@task
def enter(c, txn="ZMYTX", matnr="000000000001234567"):
    """
    Runs a transaction and enters a material number.
    Example: inv enter --txn=ZMM01 --matnr=000000000001234567
    """
    sap_entry.run_transaction(txn, {
        "PA_MATNR": matnr
    })
