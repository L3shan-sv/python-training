pods=["running", "running", "pending", "crashloopback", "MMrom"]
unhealty_count=0

for pod in pods:
    if pod=="running":
        print("pod healthy")
        
    else:
        print("pod unhealthy")    
        unhealty_count=(unhealty_count +1)\
        
    if unhealty_count==3:
        print("system critical Please review")
        break
if unhealty_count<3:
    print("system perfectly fine Ready for deployment")     
    

