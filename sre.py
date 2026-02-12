pods = ["running","running" "pending" "crashed" "pending"]
max_tries=0
tries=0
unhealthy_count=0
healthy_count=0
Deplyoment=True

for pod in pods:
    print("Application Review Initiated")
    if pod =="running":
        print("Pod Healthy Proceed")
        healthy_count=healthy_count+1
        continue
    if pod =="pending" and tries< max_tries:
        print ("Pod Pending, Rechecking....")
    else:
        print("Pod Failed")
        unhealthy_count=unhealthy_count+1
        continue
    if pod =="crashed":
        print(" Pod Craded...")
        unhealthy_count=unhealthy_count+1
        break
    if unhealthy_count >3:
        Deplyoment=False

if Deplyoment:
    print("Auditing Required")

elif healthy_count >3:
    print("System Healthy")
else:
    (" Syetem Failed")




