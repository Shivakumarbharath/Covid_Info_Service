from socket import *
import threading

from Covid_India import *
#get_number_data()
# get_state(state)
# get_district(state,dist)
# total()

from Covid_world import *

# get_country(country)

from cowin_data import *
#get_sessions(dist,state)

from tests import *
#get_test()
from vaccination import *
#get_vaccination()




# To get the host ip address
server_ip=gethostbyname(gethostname())
# server_ip='127.0.0.1'
PORT=5050 # Port Number
HEADER=64
FORMAT='utf-8'
DISCONNECT="DISCONNECT"

# Socket Creation
server=socket(AF_INET,SOCK_STREAM)

# Bind the socket to host ip and port number
server.bind((server_ip,PORT))

# sending a message
def send(msg,client):
        message=msg.encode(FORMAT)
        msg_length=len(message)
        send_length=str(msg_length).encode(FORMAT)
        send_length+=b' '*(HEADER -len(send_length))
        client.send(send_length)
        client.sendall(message)


#def send(msg,client):
#        message=msg.encode(FORMAT)
#        msg_length=len(message)
#        send_length=str(msg_length).encode(FORMAT)
#        send_length+=b' '*(HEADER -len(send_length))
#        client.sendall(send_length)
#        client.sendall(message)


def recieve(conn):
	msg_length=conn.recv(HEADER).decode(FORMAT)
	if msg_length:
		msg=conn.recv(int(msg_length)).decode(FORMAT)
		return msg

# Handling a indivudual client
def handle_client(conn,addr):
	print(f"NEW CONNECTION {addr}")
	connected=True
	while connected:
		# To get the length of the message

		#msg=recieve(conn)
		# To disconnect the client
		#if msg==DISCONNECT:
		#	conn.close()
		#	connected=False
		#else:
		#	send("Thank You For using my service",conn)
		#	print(f' {addr} {msg}')


		intro_str='\n\n\nWelcome to Covid Info Service\n\n\tChoose an Option:\n1.Covid cases in India\n2.Covid cases in Indian States\n3.Covid cases in Indian Districts\n4.Covid cases in World\n5.Vaccinations Doses Administrated in India\n6.Samples Tested so Far.\n7.Vaccination centers in Indian Districts\n8.Exit'

		send(('-'*60)+intro_str,conn)
		choice=recieve(conn)
		try:
			choice=int(choice)
		except:
			send("Please enter a valid option\Try Again",conn)
			connected=False
			break

		if choice==1:
			get_number_data()
			s=total()
			send(json.dumps(s),conn)
		elif choice==2:
			get_number_data()
			stateR=recieve(conn)
			#print(state)
			#try:
			res=get_state(stateR)
			if res=='Error':
				send(res,conn)
				send(json.dumps(error_state_cov()),conn)
			else:
				send(json.dumps(res),conn)
		elif choice==3:
			get_number_data()
			state=recieve(conn)
			district=recieve(conn)
			
			result=get_district(state,district)

			if result=='Error':
				send(result,conn)
				try:
					names=dist_error(state,district)
					send(json.dumps(names),conn)
				except KeyError:
					send("state_Error",conn)
					send(json.dumps(error_state_cov()),conn)
			

			else:
				send(json.dumps(result),conn)
		elif choice==4:
			count=recieve(conn)
			result=get_country(count)
			send(json.dumps(result),conn)
		elif choice==5:
			v=get_vaccination()
			send(v,conn)
		elif choice==6:
			t=get_tests()
			send(t,conn)
		elif choice==7:
			
			state=recieve(conn)
			dist=recieve(conn)
			#print(state,dist)
			try:
				msg=get_sessions(dist,state)
			#print(msg)
				send(json.dumps(msg),conn)
			#print(len(json.dumps(msg)))
			except:
				send("Error",conn)
				msg=error_dist(state)
			#	print(msg)
				if msg!="Error":
					send(json.dumps(msg),conn)
					

				else:
					send(msg,conn)
					send(json.dumps({'states':error_state()}),conn)
		elif choice==8:
			print(f"Disconnected With {addr}")
			conn.close()
			break
		else:
			print("Wrong option selected Disconnecting")
			print(f"Disconnected With {addr}")
			conn.close()
			break
		print(f"[Data Transmitted to {addr} ]")

def start_server():
	# To listen to clients with a waiting list of 10
	server.listen(5)
	print(f"SERVER IS LISTENING ON {server_ip}")
	while True:
		# To accept the connection from the client
		# socket object is stored in conn,address is stored in addr
		conn,addr=server.accept()
		# For handling multiple clients
		thread=threading.Thread(target=handle_client,args=(conn,addr))
		thread.start()
		print(f"[Active Connections ] {threading.activeCount()-1}")





if __name__=="__main__":
	try:
		print("Server Started ...")
		start_server()
	except KeyboardInterrupt:

		print("\nServer Has been Stopped")

	finally:
		server.close()

