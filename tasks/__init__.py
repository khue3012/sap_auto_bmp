# tasks/__init__.py

# Make Invoke aware of all task files in the tasks folder
from .launch import launch
from .enter import enter

# inv launch && inv enter --txn=ZNUMENTR --matnr=000012345
# TODO: Install pywin32 (Windows only) to use win32com.client