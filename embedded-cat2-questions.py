import json
questions = """[{"id": "001","question": "What is the use of the library imported on line 02 of the code?"},{"id": "002","question": "What is the frequency set for radio communication in the code? [add unit]"},{"id": "003","question": "To which pin of the LoRa Board is the relay input pin connected?"},{"id": "004","question": "Write the line 14 of the code."},{"id": "005","question": "What is the baud rate set for serial communication in this code?"},{"id": "006","question": "Write the line 37 of the code"},{"id": "007","question": "Is Relay a sensor or an actuator?"},{"id": "008","question": "Is this this code for tx or rx?"},{"id": "009","question": "Describe what the function myFunc is doing?"},{"id": "010","question": "How can you apply LoRa technology to improve people\'s life?  [In 10 words at most]"}]"""


y = json.loads(questions)


for k in range(len(y)):
    print("Question-"+y[k]["id"]+":")
    print(y[k]["question"])

