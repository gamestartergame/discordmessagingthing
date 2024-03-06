import  requests
print("message deletion")
input1 =input("channel id\n")
input2 =input("message id\n")
input3 =input("Auth\n")
header ={
 "authorization": input3
}

print("deleting message")
response = requests.delete("https://discord.com/api/v9/channels/"+input1+"/messages/"+input2+"" , headers=header)

if response.status_code ==204:
 print(str(response.status_code) + " :deleted")

else:
 print("failed deleting got " + str(response.status_code))


