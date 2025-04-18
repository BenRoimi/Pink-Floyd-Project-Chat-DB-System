import socket
import hashlib


def login_server(sock):
    MSG_MAX_LEN = 2048

    password_try = input("Please enter the password: ")
    msg = hashlib.sha256(password_try.encode())
    msg = msg.hexdigest()  # the password after the hash
    sock.sendall(msg.encode())

    server_msg = sock.recv(MSG_MAX_LEN)
    server_msg = server_msg.decode()

    if server_msg == "Correct":
        passed = True
        print(server_msg)
    else:
        passed = False

    return passed


def server_comms(sock):
    OPTIONS = """
    1 Get Albums
    2 Get Album Songs
    3 Get Song Length
    4 Get Song Lyrics
    5 Get Song Album
    6 Search Song by Name
    7 Search Song by Lyrics
    8 Quit
    """
    MSG_MAX_LEN = 2048
    EXIT_OPTION = 8
    MIN_OPTION = 1
    MAX_OPTION = 8
    NO_REQ_DATA_OPTION = 1
    CLIENT_TXT_SEPERATOR = "$"
    SERVER_TXT_SEPERATOR = "%"
    SERVER_DATA_PART = 2
    INPUT2 = "Enter album name: "
    INPUT3 = "Enter song name: "
    INPUT4 = "Enter song name: "
    INPUT5 = "Enter song: "
    INPUT6 = "Enter text: "
    INPUT7 = "Enter text: "
    BYE_MSG = "Thank you for using the Pink-Floyd Server! Bye Bye!"

    inputs_dict = {2: INPUT2, 3: INPUT3, 4: INPUT4, 5: INPUT5, 6: INPUT6, 7: INPUT7}

    server_msg = sock.recv(MSG_MAX_LEN)
    server_msg = server_msg.decode()
    print(server_msg)
    option = 0
    data_req = " "

    if login_server(sock):
        while option != EXIT_OPTION: # runs until the user decides to quit (option 8)
            print(OPTIONS)
            try:
                option = int(input("Enter number: "))
            except ValueError as e:
                print("Error: ", e)
            while not (MIN_OPTION <= option <= MAX_OPTION):
                print("You can only choose options 1-8")
                option = int(input("Enter number: "))

            if option == EXIT_OPTION: # checks if the user exited
                msg = "REQUEST" + CLIENT_TXT_SEPERATOR + str(option) + CLIENT_TXT_SEPERATOR + "QUIT"
                sock.sendall(msg.encode())
                break
            if option != NO_REQ_DATA_OPTION: # option 1 is the only option without req data
                data_req = input(inputs_dict[option])

            msg = "REQUEST" + CLIENT_TXT_SEPERATOR + str(option) + CLIENT_TXT_SEPERATOR + data_req  # makes a msg back
            sock.sendall(msg.encode())

            server_msg = sock.recv(MSG_MAX_LEN)
            server_msg = server_msg.decode()
            server_msg_parts = server_msg.split(SERVER_TXT_SEPERATOR)
            print(server_msg_parts[SERVER_DATA_PART])

        print(BYE_MSG)
    else:
        print("Incorrect password! Disconnecting...")


def main():
    SERVER_IP = "127.0.0.1"
    SERVER_PORT = 1000

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connecting to remote computer 80
    server_address = (SERVER_IP, SERVER_PORT)
    sock.connect(server_address)

    server_comms(sock)

    # Closing the conversation socket
    sock.close()


if __name__ == "__main__":
    main()
