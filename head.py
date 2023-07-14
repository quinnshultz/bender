# Robot: Head
# Written by Quinn Shultz
import os
import openai
from pocketsphinx import LiveSpeech

# Don't you dare push this key to Github!
openai.api_key = ""

conversation = [
    {"role": "system", "content": "You are bender the robot."},
    {"role": "user", "content": "Hello!"}
]

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=conversation
)

myRetort = completion.choices[0].message.content

print(myRetort)
os.system("say " + myRetort)
conversation.append({"role" : "system", "content" : myRetort})


for phrase in LiveSpeech():
    humanSpeech = str(phrase)
    print(humanSpeech)
    conversation.append({"role" : "user", "content" : humanSpeech})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    myRetort = str(completion.choices[0].message.content)

    print(myRetort)
    os.system("say " + myRetort)
    conversation.append({"role" : "system", "content" : myRetort})
