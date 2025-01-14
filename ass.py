import requests, uuid, time

# For interacting with the Robot's hardware
class ShinyMetal:
    def bend(self):
        print("Bending girder.")

    def move_forward(self, distance):
        print("Moving " + distance + " feet.")
        return 10

    def read(self, input):
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }

        json_data = {
            'uuid_idempotency_token': str(uuid.uuid4()),
            'tts_model_token': 'TM:7wbtjphx8h8v',
            'inference_text': input
        }

        response = requests.post('https://api.fakeyou.com/tts/inference', headers=headers, json=json_data)
        pollUrl = 'https://api.fakeyou.com/tts/job/' + str(response.json()['inference_job_token'])
        print(pollUrl)
        # Polling
        flag = True
        while (flag):
            pollResponse = requests.get(pollUrl, headers)
            print(pollResponse)
            time.sleep(1)
            if(pollResponse.json()['state']['status'] != 'pending' and pollResponse.json()['state']['status'] != 'started'):
                flag = False
                print(pollResponse.json()['state']['maybe_public_bucket_wav_audio_path'])
