#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

# sample address:
# 870 Valencia St, San Francisco, CA 94110

# SCAMMER HOUSE:
# 1143 Madison Ave SE, Grand Rapids, MI 49507
