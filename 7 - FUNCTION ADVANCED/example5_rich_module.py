# import rich
# cara ini akan import keseluruh rich library, cara lebih efisien sbb:

# from rich import print

# print("""
#            [red]
# **************************************************
# *   WARNING: Authorized personnel only!          *
# *   All activities are monitored and logged.     *
# **************************************************
# [/red]"""
# )

# karena print rich mirip dengan print regular, kita bisa pakai alias

from rich import print as richprint

richprint("""
           [red]
**************************************************
*   WARNING: Authorized personnel only!          *
*   All activities are monitored and logged.     *
**************************************************
[/red]"""
)

richprint("8.8.8.8")
print("8.8.8.8")