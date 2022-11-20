#!/usr/bin/python3
# python script that fetches 'https://alu-intranet.hbtn.io/status'
# 	- You must use the package 'urllib'
# 	- You are not allowed to import any packages other than urllib
# 	- The body of the response must be displayed like the,
# 	  following example (tabulation before -)
# 	- You must use a with statement
"""
	import 'urllib' package
"""
import urllib.request


if __name__ == "__main__":
    request = urllib.request.Request("https://intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
