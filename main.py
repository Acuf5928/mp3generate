import boto3
import os
from contextlib import closing
import APRIFILE

key = APRIFILE.aprifile("key.txt")

for a in range(0, len(key)):
        key[a] = key[a].split("=")

        if key[a][1][-1] == "\n":
            key[a][1] = key[a][1][:-1]

polly = boto3.client("polly", 'us-east-2', aws_access_key_id=key[0][1], aws_secret_access_key=key[1][1])

voce=""
nome=""

while voce != "0" and nome != "0":
    nome = input("mp3 file's title:")

    if nome == "0":
        break

    nome = nome + ".mp3"
    voce = input("Text:")

    if voce == "0":
        break

    response = polly.synthesize_speech(
        Text= voce,
        OutputFormat="mp3",
        VoiceId="Carla")

    if "AudioStream" in response:
        with closing(response["AudioStream"]) as stream:
            data = stream.read()
            with open(nome, "bw+") as file:
                file.write(data)

#    os.system("\"C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe\" C:\\Users\\alber\\PycharmProjects\\auguri\\audio.mp3")
