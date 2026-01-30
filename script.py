pod_status= "pending"
max_attempts =5
attempts= 0

while pod_status !="connected" and attempts < max_attempts:
    print("tryna connect")
    attempts = attempts + 1

    if attempts ==3:
        pod_status= "connected"



if pod_status =="connected":
    print("done sir")

else:
    print("failed to connect")