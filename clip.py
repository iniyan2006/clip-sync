import time

import sweech
import win32clipboard as cp

"""
connecting to the phone with
sweech cli app

credits : alberithier sweech-cli
"""
connection = sweech.Connector("http://192.168.43.1:4444")
cp.OpenClipboard()
text = cp.GetClipboardData()
cp.SetClipboardData(cp.CF_UNICODETEXT,connection.clipboard())
cp.CloseClipboard()

connection.clipboard(text)
#========================== local clip board history in a list ==========>>>
history = []
cp_history = []
while True:

	cp_text = connection.clipboard()
	cp_history.append(cp_text)
	
	cp.OpenClipboard()
	data = cp.GetClipboardData()
	cp.CloseClipboard()
	history.append(data)
	for x in range(1):
		if data != cp_text:
			pass
		else:
			connection.clipboard(data)
	if cp_text not in history:
		cp.OpenClipboard()
		cp.SetClipboardData(cp.CF_UNICODETEXT,cp_text)
		cp.CloseClipboard()	
		connection.clipboard(data)
	time.sleep(1)
