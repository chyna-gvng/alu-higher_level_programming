#!/usr/bin/python3
# python script that fetches 'https://alu-intranet.hbtn.io/status'
# 	- You must use the package 'urllib'
# 	- You are not allowed to import any packages other than urllib
# 	- The body of the response must be displayed like the,
# 	  following example (tabulation before -)
# 	- You must use a with statement
"""
	- import 'urllib' package
	- fetch ://alu-intranet.hbtn.io/status'
"""


import urllib.request
if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode(encoding="utf-8")))
