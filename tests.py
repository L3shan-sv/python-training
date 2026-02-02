pods = ["running", "running", "pending", "running", "crashed", "running"]
healthy_pods=0
unhealthy_pods=0
rollback_status=False
tries=0
max_tries=2


for pod in pods:
    if pod =="running":
        print("Pod Healty, Continuing Rollout")
        healthy_pods= healthy_pods+1
        continue
    while pod =="pending"and tries<max_tries:
        print("Pod pending, Retrying")
        tries= tries+1
        if tries==max_tries:
            print("Pod stuck, Stopping rollout")
            unhealthy_pods=unhealthy_pods+1
            rollback_status==True
            break
    if pod =="crashed":
        print("Pod crashed, Rollback Initiated")
        break

if unhealthy_pods<4:
    print("Rollout Unstabale") 

if rollback_status:
    print("Rollout succesfull")
else:
    print("Rollout Complete")           


