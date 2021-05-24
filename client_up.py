from socket import socket
from socket import *
import sys
import json

if len(sys.argv)!=2:
	print("Usage python3 [Client File Name] [server Ip address] ")
	sys.exit(1)
server_ip=sys.argv[1]
PORT=5050 # Port Number
HEADER=64
FORMAT='utf-8'
DISCONNECT="DISCONNECT"



# Create a client socket
client=socket(AF_INET,SOCK_STREAM)
client.connect((server_ip,PORT))

def recieve(conn):
	msg_length=conn.recv(HEADER).decode(FORMAT)
	#print(msg_length)
	ln=0
	msg=b''
	while True:
		if msg_length:
			msg+=conn.recv(int(msg_length))
			
			#print(len(msg),msg_length)
			if int(msg_length)==len(msg):
				break
	return msg.decode(FORMAT)


#def recieve(conn):
#        msg_length=conn.recv(HEADER).decode(FORMAT)
#        #print(msg_length)
#        if msg_length:
#                msg=conn.recv(int(msg_length)).decode(FORMAT)
#                # To disconnect the client
#                if msg==DISCONNECT:
#                        connected=False
#                try:
#                        return msg
#                except:
#                        return msg


def send(msg,conn):
	message=msg.encode(FORMAT)
	msg_length=len(message)
	send_length=str(msg_length).encode(FORMAT)
	send_length+=b' '*(HEADER -len(send_length))
	conn.send(send_length)
	conn.send(message)
#send(input("Send Message..?"),client)
#r_msg=recieve(client)
#print(r_msg)
#send(DISCONNECT,client)
#client.close()
connected=True
while connected:
	m=recieve(client)
	print(m)
	choice=input("Selection :  ")

	try:
		choice = int(choice)
	except:
		print(" Enter a Valid Option ")
		client.close()
		connected=False
		break
	send(str(choice),client)
	if choice==1:

		r=recieve(client)
		r=json.loads(r)
		print('\n\n')
		for e in r:
			print(e,' : ',r[e])
	elif choice==2:

		state=input("Enter the state ? ").capitalize()
		send(state,client)
		m=recieve(client)
		if m!="Error":
			print('\n\n')
			m=json.loads(m)
			for e in m:
				print(e, ': ',m[e])
		else:
			state_name=recieve(client)
			for ele in json.loads(state_name).keys():
				print(ele)
			





	elif choice==3:
		state= input("Enter the State : ").capitalize()
		send(state,client)
		dist=input("Enter the district : ").capitalize()
		send(dist,client)
		res=recieve(client)
		print(type(res))
		print('\n\n')
		if res=="Error":
			dists=recieve(client)
			dists=json.loads(dists)
			print("Select from the below Districts\n")
			for e in dists.keys():
				print(e)

			new_dist=input("District : ")
			while new_dist not in dists.keys():
				new_dist=input("Please Enter a valid District: ")
			print('\n\n')
			for e in dists[new_dist]:
				print(e,' : ',dists[new_dist][e])
		else:
#			print(len(res))
			res=json.loads(res)
			for e in res:
				print(e,' : ',res[e])


	elif choice==4:
		count=input("Enter Name of Country? ").capitalize()
		send(count,client)
		msg=recieve(client)
		msg=json.loads(msg)
		#print(msg,type(msg))
		print('\n\n')
		if msg!="Error":
			for ele in msg:
				print(ele,' : ',msg[ele])
		else:
			print("Enter a valid country name")
	elif choice==5:
		msg=recieve(client)
		print('\n\n',msg)
	elif choice==6:
		t=recieve(client)
		print('\n\n',t)
	elif choice==7:
		state=input("Name of the State :").capitalize()
		send(state,client)
		dist=input("Name of the District : ").capitalize()
		send(dist,client)
		m=recieve(client)
		if m=="Error":
			e_m=recieve(client)
			print(e_m)
			if e_m!="Error":
				e_m=json.loads(e_m)
				for ds in e_m['districts']:
					print(ds)
			else:
				print("Check the name of the State and Try again\n\n")
			
		else:
			print(type(m),len(m))
			main_data = json.loads(m)['centers']
			print(type(main_data))
			for e in main_data:
    				for i in e:
        				if i == 'sessions':
            					for ele in e[i]:
                					print('\n')
                					for key in ele:
                    						print(key, ' : ', ele[key])

        				else:
            					print(i, ': ', e[i])
    				print('\n\n\n\n')

	elif choice==8:
		print("Thank you for Using The Service")
		send(str(choice),client)
		client.close()
		break
	else:
		print("Enter the values in the Option")
		client.close()
		break

































