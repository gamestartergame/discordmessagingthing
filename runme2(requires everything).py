import datetime
import requests
import logging
print("note: you can't chat in any locked channel or privated channels."
" if you type a string in the second input it will crash.")
message = input("what message would you want to send \n")
message2 = input("how many times do you want it to be sent \n")
message3 = input("input channel id\n")
message4 = input("discord authorization(don't share this)\n")
with open("info.txt" , "w") as file:
 file.write("message sent: \n" + message + "\ntimes sent: \n" + message2 + "\nchannel id used: \n" + message3 + "\ndiscord authorization used(don't share this): \n" + message4 +"\ntime started:\n" + str(datetime.datetime.now()))

url = "https://discord.com/api/v9/channels/" + message3 + "/messages"
header2 ={
    "authorization": message4 ,
    "content": "application/json"
}
payload = {
    "content": message
}

header = {
    "authorization": message4
}

i = 1
responds = requests.post(f"https://discord.com/api/v9/channels/" + message3 + "/invites",
              headers=header2)
invitething = responds.json()
while i <= int(message2):

    res = requests.post(url, payload, headers=header)
    timething = datetime.datetime.now()
    i = i + 1
    if res.status_code == 200:
        print(i * "-" + " sent " + message + " status code: " + str(res.status_code) +"\ntime: " + str(timething))
    else:
        print("failed to send: " + message + " because: "+ str(res.status_code))

else:
    input("messages have been sent\n")

    with open("status code.txt", "w") as file:
        file.write("last message status code: \n" + str(res.status_code) +" from sent message: " +message +"\nmessage was sent to: " +message3 +"\n last message time:\n" + str(timething))
if "code" in invitething:
    invite =f"https://discord.gg/{invitething["code"]}"
    print("invite for the server: " + invite +"\n status code:\n" + str(responds.status_code))
    print("if status code 401 that means you don't have access to send messages or create invite links")
    input()
else:
    print("error making server invite")
    input()