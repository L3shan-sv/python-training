pod_status="pending"
tries=0
max_tries=10


while pod_status !="trying" and tries<max_tries:
    tries= tries+1
    print("trying to connect")

    if tries==10:
        pod_status="connected"


if pod_status =="connected":
    print("task accomplished")
else:
    print("task failed")    




