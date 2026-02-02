import random

pods = []
states = ["running", "pending", "crashed"]

for i in range(6):
    pods.append(random.choice(states))

print("Pod statuses for this rollout:", pods)

healthy_pods = 0
unhealthy_pods = 0
rollback_status = False
max_tries = 2

for pod in pods:
    print("Checking pod:", pod)

    if pod == "running":
        print("Pod healthy, continuing rollout")
        healthy_pods += 1
        continue

    if pod == "pending":
        tries = 0
        while tries < max_tries:
            print("Pod pending, retrying...")
            tries += 1
            if tries == max_tries:
                print("Pod stuck, stopping rollout")
                unhealthy_pods += 1
                rollback_status = True
                break
        if rollback_status:
            break

    if pod == "crashed":
        print("Pod crashed, rollback initiated")
        rollback_status = True
        unhealthy_pods += 1
        break

if rollback_status:
    print("ROLLBACK COMPLETE")
elif healthy_pods < 4:
    print("ROLLOUT UNSTABLE")
else:
    print("ROLLOUT SUCCESSFUL")
