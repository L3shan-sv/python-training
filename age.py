status="pending"
tries=0
max_tries=5

while status !="connected" and tries < max_tries:
    print("trying to connect..")
    tries= tries+1

    if tries==5:
        status="connected"



if status !="conected":
    print("task done") 
else:
    print("Task failed")       


