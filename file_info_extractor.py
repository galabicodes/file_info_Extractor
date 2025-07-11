import os
from datetime import datetime
folder_path = os.path.expanduser("~/Desktop/gold")
for filename in os.listdir(folder_path) :
	file_path = os.path.join(folder_path, filename) 
	if not os.path.isfile(file_path):
		continue
	size = os.path.getsize(file_path)
	created = datetime.fromtimestamp(os.path.getctime(file_path))
	modified = datetime.fromtimestamp(os.path.getmtime(file_path))
	print(f"file:{filename}")
	print(f"size: {size} bytes")
	print(f"created: {created}")
	print(f"modified: {modified}")
	print("_" * 30)
