import subprocess

subprocess.run("python chrome_tests/chrome_pyszne_tests.py & python chrome_tests/chrome_olx_tests.py", shell=True)
subprocess.run("python edge_tests/edge_pyszne_tests.py & python edge_tests/edge_olx_tests.py", shell=True)
subprocess.run("python firefox_tests/firefox_pyszne_tests.py & python firefox_tests/firefox_olx_tests.py", shell=True)
