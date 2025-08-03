# sap_entry.py
import time
import win32com.client

def attach_session():
    """
    Return the first available SAP GUI scripting session.
    Must run while SAP GUI is open and logged in.
    """
    SapGuiAuto = win32com.client.GetObject("SAPGUI")
    app = SapGuiAuto.GetScriptingEngine
    conn = app.Children(0)
    sess = conn.Children(0)
    return sess

def run_transaction(txn_code: str, field_values: dict[str, str]):
    sess = attach_session()
    sess.findById("wnd[0]/tbar[0]/okcd").text = f"/n{txn_code}"
    sess.findById("wnd[0]").sendVKey(0)
    time.sleep(0.5)

    for id_suffix, val in field_values.items():
        path = f"wnd[0]/usr/ctxt{id_suffix}"
        sess.findById(path).text = val

    sess.findById("wnd[0]/tbar[1]/btn[8]").press()
