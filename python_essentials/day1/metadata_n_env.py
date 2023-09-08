#!/opt/homebrew/bin/env python3

"""
super documentation
author: @minhadona
"""

__version__ = "0.0.1"

import os 
current_lg= os.getenv("LANG","default_case_env_var_doesnt_exist").split(".")[0]
if not current_lg in ["en","fr"]:
    print(f"current language is weird: {current_lg}")

    