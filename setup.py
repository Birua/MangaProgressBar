from distutils.core import setup
import sys
import py2exe

sys.path.append("C:\\Windows\\winsxs\\x86_microsoft.vc90.crt_1fc8b3b9a1e18e3b_9.0.30729.1_none_e163563597edeada")

setup(windows=[{"script":"MangaProgressBar.py"}], options={"py2exe":{"includes":["sip"]}})
