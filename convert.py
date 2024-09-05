#Audio file conversion
#Libraries
import numpy as np
from pydub import AudioSegment
from pydub.playback import play

def ignore(none):
#if ffmpeg cannot be put on root, use these commands to connect it to the script.
    '''
    AudioSegment.converter = r"path\of\directory\ffmpeg"
    AudioSegment.ffmpeg = r"path\of\directory\ffmpeg"
    AudioSegment.ffprobe = r"path\of\directory\ffprobe"
    '''

#Scripts
from main import save_data , current_song

#----------------------------------------------------------
#Global variables

# Load the MP3 file
audio = AudioSegment.from_mp3(current_song + '.mp3')

# Convert to mono and get raw audio data
audio = audio.set_channels(1)
raw_data = np.array(audio.get_array_of_samples())

processed_data = []
#----------------------------------------------------------
# Main function

# Process the audio data in chunks
chunk_size = 1024
for i in range(0, len(raw_data), chunk_size):
    chunk = raw_data[i:i + chunk_size]

    # Perform FFT on the audio data
    fft_data = np.fft.fft(chunk)
    magnitude = np.abs(fft_data)

    # Calculate brightness and color based on the audio data
    brightness = int(np.mean(magnitude) / 256)
    red = int(np.mean(magnitude[:len(magnitude) // 3]) / 256)
    green = int(
        np.mean(magnitude[len(magnitude) // 3:2 * len(magnitude) // 3]) / 256)
    blue = int(np.mean(magnitude[2 * len(magnitude) // 3:]) / 256)

    # Append the processed data
    processed_data.append([brightness, red, green, blue])

# Save the processed data to a file
save_data(current_song + '.txt', processed_data, ',')
print()
