import socket
import data


def login_check(client_soc):
    PASSWORD = "698d60ae40ad03bb179010488d33089a757aaa1f8e62e425b097eadab917d8fd"
    MSG_MAX_LEN = 2048

    client_msg = ""
    try:
        client_msg = client_soc.recv(MSG_MAX_LEN)
    except (ConnectionResetError, ConnectionAbortedError) as e:  # checks if the client disconnected
        print("Error: ", e)
    client_msg = client_msg.decode()

    if client_msg == PASSWORD: # checks if the user entered the correct password
        msg = "Correct"
        client_soc.sendall(msg.encode())
        print("User gained access.")
        return True
    else:
        msg = "Incorrect"
        client_soc.sendall(msg.encode())
        print("User failed to gain access.")
        return False


def client_comms(client_soc):
    REQ_NUM_PART = 1
    REQ_DATA_PART = 2
    MSG_MAX_LEN = 2048
    EXIT_OPTION = 8
    CLIENT_TXT_SEPERATOR = "$"
    SERVER_TXT_SEPERATOR = "%"
    ANSWER8 = "Bye Bye!"
    NO_REQ_DATA_OPTION = 1
    FIRST_REQ_DATA_OPTION = 2
    LAST_REQ_DATA_OPTION = 7

    req_data = ""
    answers_dict = {1: data.answer1, 2: data.answer2, 3: data.answer3, 4: data.answer4, 5: data.answer5, 6: data.answer6, 7: data.answer7, 8: ANSWER8}

    client_msg_parts = [0, 0]

    if login_check(client_soc):  # activate the login function and giving or denying access according to the password correction
        while client_msg_parts[REQ_NUM_PART] != EXIT_OPTION:
            try:
                client_msg = client_soc.recv(MSG_MAX_LEN)
            except (ConnectionResetError, ConnectionAbortedError) as e:  # checks if the client disconnected
                print("Error: ", e)
            try:
                client_msg = client_msg.decode()
            except AttributeError as e:  # after the client disconnects, this error may appear
                print("Error: ", e)
            print(client_msg)

            client_msg_parts = client_msg.split(CLIENT_TXT_SEPERATOR)
            req_num = int(client_msg_parts[REQ_NUM_PART])
            req_data = client_msg_parts[REQ_DATA_PART]

            # applying the right function from the data file
            if req_num == NO_REQ_DATA_OPTION:
                answer = answers_dict[req_num]()
            elif FIRST_REQ_DATA_OPTION <= req_num <= LAST_REQ_DATA_OPTION:
                try:
                    answer = answers_dict[req_num](req_data)
                except Exception:
                    answer = "Nothing found"
            else:
                answer = answers_dict[EXIT_OPTION]
            msg = "CODE" + SERVER_TXT_SEPERATOR + client_msg_parts[REQ_NUM_PART] + SERVER_TXT_SEPERATOR + str(answer)  # makes a msg back
            client_soc.sendall(msg.encode())
    else:
        print("Disconnecting...")


def main():
    LISTEN_PORT = 1000
    LISTENERS_AMOUNT = 1

    ANSWER1 = "Here's the list of all the alboms of the band: "
    ANSWER2 = "Here's the list of all the songs in the given albom: "
    ANSWER3 = "Here's the length of the given song: "
    ANSWER4 = "Here are all the lyrics of the given song: "
    ANSWER5 = "Here's the albom of the given song: "
    ANSWER6 = "Here are all the songs that contains this word: "
    ANSWER7 = "Here are all the songs that their lyrics contains this word: "
    ANSWER8 = "Bye Bye!"

    answers_dict = {1: ANSWER1, 2: ANSWER2, 3: ANSWER3, 4: ANSWER4, 5: ANSWER5, 6: ANSWER6, 7: ANSWER7, 8: ANSWER8}

    # Create a TCP/IP socket
    listening_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Binding to local port 1000
    server_address = ('', LISTEN_PORT)
    listening_sock.bind(server_address)

    # Listen for incoming connections
    listening_sock.listen(LISTENERS_AMOUNT)

    # Create a new conversation socket
    client_soc, client_address = listening_sock.accept()

    msg = "Welcome!"
    client_soc.sendall(msg.encode())

    client_comms(client_soc)

    # Closing the listening socket
    listening_sock.close()


if __name__ == "__main__":
    main()
