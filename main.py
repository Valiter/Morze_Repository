import pyaudio
import wave

p = pyaudio.PyAudio()

for i in range(p.get_device_count()):
    print(i, p.get_device_info_by_index(i)['name'])
# Строка ниже позволяет узнать ВСЕ данные по девайсам. Например, мой розовый микрофон принимает только один "канал"
    print(p.get_default_input_device_info())


"""PyAudio example: Record a few seconds of audio and save to a WAVE file."""


CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                input_device_index=2,
                frames_per_buffer=CHUNK
                )

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
