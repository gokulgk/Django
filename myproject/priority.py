import csv
import os
import signal
import psutil
import subprocess
import paho.mqtt.client as mqtt

# MQTT broker configuration
BROKER_ADDRESS = "192.168.29.15"
BROKER_PORT = 1883
TOPIC = "interrupt"

# Create an MQTT client instance
client = mqtt.Client()

# Connect to the MQTT broker
client.connect(BROKER_ADDRESS, BROKER_PORT)

# Publish a message to the specified topic
message = str(1)
client.publish(TOPIC, message)
client.loop()
# Disconnect from the MQTT broker
client.disconnect()


##def stop_process(process_name):
##    for proc in psutil.process_iter():
##        if proc.name() == process_name:
##            os.kill(proc.pid, signal.SIGTERM)
##            print(f"Process {process_name} (PID {proc.pid}) stopped.")
##            return
##    print(f"No process named {process_name} was found.")
##
### Example usage: stop a program named "myprogram.py"
##stop_process("py.exe")


i=0
k=0
# Open the CSV file in read mode
with open('log.csv', mode='r') as file:

    # Create a CSV reader object
    reader = csv.reader(file)

    # Read all rows into a list
    rows = list(reader)
    
    for row in rows:
        if(row[5]!="Completed" ):
            if(row[8]=="High"):
                row[8]="High(Prority Assigned)"
                new_row=row
                index2=k
                rows.pop(k)
                print(k)
                break
        k=k+1
        
    for row in rows:
        if(row[5]!="Completed" and row[5]!="Status" and row[8]!="High(Prority Assigned)"):
            index=i
            print(i)
            rows.insert(index, new_row)
            break
        i=i+1
            

# Open the CSV file in write mode
with open('log.csv', mode='w', newline='') as file:
## with open('log.csv', mode='w', newline='') as file:

    # Create a CSV writer object
    writer = csv.writer(file)

    # Write all rows to the CSV file
    writer.writerows(rows)


##subprocess.run(["python", "wrk_mngr.py"])








