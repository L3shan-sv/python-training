pods=["pending", "pending", "running"]

for pods in pods:
    print("checking status..")

    if pods =="pending":
        print("conducting heath checks")
        continue

    if pods =="running":
        print("pod heathly and running")



