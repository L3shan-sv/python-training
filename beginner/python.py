pods = ["running", "pending", "running", "pending", "running"]
unhealthy_count=0
healthy_count=0
deployment_failed=False
tries=0
max_tries=2

for pod in pods:
    print ("Syetem Check Initiated")
    if pod =="running":
        print("Pod Heatlty")
        healthy_count=healthy_count+1
        continue
    if pod =="pending" and tries< max_tries:
        print("Pod Pending , Retrying")
        tries=tries+1
    else:
        print("Pod stuck")
        unhealthy_count=unhealthy_count+1
        continue
    if pod =="crashed":
        print("Failed pod")
        unhealthy_count=unhealthy_count+1
        break
    if unhealthy_count>3:
        deployment_failed=True


if deployment_failed:
    print("Deployment Failed")
elif unhealthy_count==3:
    print(" Application Unstable, ")
else:
    ("application ready for deplyment")


            