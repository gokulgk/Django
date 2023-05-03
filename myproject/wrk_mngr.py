import os
import time
import csv
import networkx as nx
import paho.mqtt.client as mqtt
import pandas as pd
current_location=2
facing_direction=0
routeA,routeB=[],[]
command=[]
way,route,a,res,directionroute,current_direction,empty_list,current_directionA,current_directionB=[],[],[],[],[],[],[],[],[]

weighted_edges=[(6,7,3),(7,12,3),(7,8,5),(1,11,3),(2,26,3),
                (3,35,5),(4,27,4),(5,17,3),(8,9,3),(9,14,3),(9,12,5),
                (12,13,3),(13,14,5),(13,18,3),(18,19,5),(14,19,3),(17,18,3),
                (9,10,6),(14,15,3),(19,20,3),(15,16,3),(15,20,3),(10,16,3),
                (11,10,3),(17,21,4),(21,22,4),(22,23,4),(19,23,4),(23,24,3),(24,25,3),
                (25,26,4),(22,27,5),(23,30,3),(30,31,3),(31,24,3),(31,34,4),(31,32,3),
                (32,35,4),(35,34,3),(32,29,3),(29,33,3),(33,28,4),(28,27,4)]

########################################################################clears log.csv###############################################################
# Open the CSV file in read mode and read its contents

    
#################################################################################################################################################
    
def directionPath(start, middle, end, botDirection,temp):
    current_direction=empty_list
    G=nx.Graph()
    G.add_weighted_edges_from(weighted_edges)
    if temp==0:
        if(start!=middle):
            route=(nx.shortest_path(G,start,middle))
        #print(route)
        else:
            listA=[]
            route=listA
    if temp==1:
        route=(nx.shortest_path(G,middle,end))
        #print(route)
    if temp==0:
        current_direction.clear()
        current_directionA.clear()
        current_directionB.clear()

        y=(len(route)-1)
    else:    
        y=(len(route))
    for x in range(0,y):
        way.append(route[x])



    north,south,east,west=0,1,2,3
    count=len(route)
    present=botDirection # set the initial direction here
    headed=botDirection
   

    ##################### default point  starts #################
    rightX=[north,west,south,east]
    rightY=[east,north,west,south]
    uTurnX=[north,west,south,east]
    uTurny=[south,east,north,west]
    rightTurn=[[0 for i in range(4)] for j in range(4)]
    leftTurn=[[0 for i in range(4)] for j in range(4)]
    uTurn=[[0 for i in range(4)] for j in range(4)]
    # create an empty 2D list and enter 1 for specified position
    for i in range(0,4):
            rightTurn[rightX[i]][rightY[i]]=1
    for i in range(0,4):
        for j in range(0,4):
            leftTurn[i][j]=rightTurn[j][i]
    for i in range(0,4):
        uTurn[uTurnX[i]][uTurny[i]]=1
    #########################  default point ends #################

    ######################### map point starts ####################
    northToSouthX=[17,21,4,7,12,13,18,9,14,15,19,11,26,22,23,24,30,31,28,29,32]
    northToSouthY=[18,22,27,8,9,14,19,10,15,16,20,1,2,23,24,25,31,34,33,32,35]
    westToEastX=[6,7,12,13,5,17,22,27,8,9,14,19,23,29,15,24,31,11,10,26,34,35]
    westToEastY=[7,12,13,18,17,21,27,28,9,14,19,23,30,33,20,31,32,10,16,25,35,3]

    cols,rows=36,36
    southMap=[[0 for i in range(cols)] for j in range(rows)]
    northMap=[[0 for i in range(cols)] for j in range(rows)]
    eastMap=[[0 for i in range(cols)] for j in range(rows)]
    westMap=[[0 for i in range(cols)] for j in range(rows)]
    for i in range(0,len(northToSouthX)):
        southMap[northToSouthX[i]][northToSouthY[i]]=1
    for i in range(0,len(northMap)):
        for j in range(0,len(southMap)):
            northMap[i][j]=southMap[j][i]
    for i in range(0,len(westToEastX)):
        eastMap[westToEastX[i]][westToEastY[i]]=1
    for i in range(0,len(westMap)):
        for j in range(0,len(eastMap)):
            westMap[i][j]=eastMap[j][i]
    #################### map point ends #############################


    for i in range(0,count):
        if temp==0:
            current_directionA.append(present)
        if temp==1:
            current_directionB.append(present)
        a=route[i]
        if i+1!=count:
            b=route[i+1]
        if i!=0 :
            if present==headed:
                command.append("straight")

        if northMap[a][b]==1:
            headed=north
        if southMap[a][b]==1:
            headed=south
        if eastMap[a][b]==1:
            headed=east
        if westMap[a][b]==1:
            headed=west  

        if rightTurn[present][headed]==1:
            command.append("right")
        if leftTurn[present][headed]==1:    
            command.append("left")
        if uTurn[present][headed]==1:
            command.append("uTurn")
        present=headed
    if temp==0:
        command.append("pause")
    #print(command)
    directionroute.append(command)
    if temp==0:
        #print("temp is 0")
        directionPath(start,middle,end,present,1)
        #print(way)
    if temp==1:
        res.append(way)
        res.append(command)
        res.append(present)
        res.append(end)
        if(start!=middle):
            current_directionA.pop()
        current_direction=current_directionA+current_directionB
        res.append(str(current_direction))
        print("updated result")
  
    return res
    

i=0
previous_row_count = 1
done_rows=[]

# Set up a loop to continuously check for changes in the CSV file
while True:
    ind=0
    with open('log.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        rows = list(reader)
        
         # Check if there are any new rows added to the CSV file
    if len(rows) > previous_row_count:
        # Get the new row(s) added to the CSV file
        new_rows = rows[previous_row_count:]
        # Loop through each new row and update the data
        for row in rows:
            if(row[5]!="Completed"):
                    i=i+1
                    row[5] = 'Procesing'
                    row[0]=i
                    print(row)
                    #directionPath(start, middle, end, botDirection,temp)
                    #north,south,east,west=0,1,2,3 - botDirection
                    print('*Path Planing Started!*')
                    # mqtt comes here##
                    print(current_location)
                    print(int(row[3]))
                    print(int(row[4]))
                    result=directionPath(current_location,int(row[3]),int(row[4]),facing_direction,0)
                    print("The result is",result)
                    print(int(row[3]))
                    row[6]=str(result[0])
                    row[7]=str(result[1])

                    facing_direction=result[2]
                    current_location=result[3]
                    current_direction=result[4]
                    data=[]
                    data.append(row[6])
                    data.append(row[7])
                    data.append(current_direction)
                    
                    #broker_address = "192.168.43.248"
    ##                broker_address = "192.168.29.15"
    ##                broker_port = 1883
    ##                mqtt_topic = "testTopic"
    ##                client = mqtt.Client()
    ##                client.connect(broker_address, broker_port)
    ##                mqtt_data=str(data)
    ##
    ##                client.publish(mqtt_topic, mqtt_data)
    ##                client.loop()
    ##
    ##                print("published")
    ##                client.disconnect()
    ##                
                    way.clear()
                    command.clear()
                    res.clear()
                    row[5] = 'Completed'
                    #time.sleep(10)  ##### add mqtt complete logic here######
                    

                    # Define callback function for when a message is received
                    def on_message(client, userdata, message):
                        global msg_received
                        msg_received = True
                        print(f"Received message on topic {message.topic}: {message.payload.decode()}")

                    # Create MQTT client instance and connect to broker
                    client = mqtt.Client()
                    client.connect("192.168.1.102", 1883, 60)

                    # Subscribe to topic and wait for message
                    client.subscribe("comp")
                    client.on_message = on_message

                    # Wait for message in a while loop
                    msg_received = False
                    pr_status="none"
                    while (1):
                        with open('status.txt') as f:
                            first_line = f.readline()
                            pr_status=first_line
                        if(pr_status!="none"):
                            with open("status.txt", "w") as f: 
                                f.write("none")
                                print("Rescheduled")
                                i=i-1
                            break
                        else:
                             client.loop()
                             if(msg_received!= False):
                                 print("Message received, exiting...")
                                 print('*Request completed!*')
                    
                    

                   
                                 df = pd.read_csv('log.csv')
                              
                                 df.loc[ind] = row
                                 df.to_csv('log.csv', index=False)

                                 ind=ind+1
                                 previous_row_count = len(rows)
                                 break
                    break
