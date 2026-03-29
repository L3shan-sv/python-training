status="pending"

for attempt in range(1,5):
    print("attempt: checking service")

    if attempt<3:
        print("service isnt ready yet")
        continue

    if attempt==3:
        status ="connected"
        print("connected")
        break

if status =="connected":
    print("task done")
else:
    print("task failed")    
