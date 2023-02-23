import base64

while True:
  dcmsg = input('Enter Your Base64 Encoded Message: ')

  base64_message = (dcmsg)
  base64_bytes = base64_message.encode('ascii')
  message_bytes = base64.b64decode(base64_bytes)
  message = message_bytes.decode('ascii')

  print(message)