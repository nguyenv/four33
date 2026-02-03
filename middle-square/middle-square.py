from seed import FOURTHIRTYTHREE
from scipy.io.wavfile import write
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# audio samples per second; value is standard CD quality
SAMPLE_RATE = 44100

def make_sound(seq, filename="output.wav"):
    # Scale down into a normal audible frequency range
    # Most musical sounds are between 50Hz-5000Hz
    seq = [n / 10 for n in seq]

     
    duration = 0.1 # how long each tone lasts (100ms/note)

    audio = np.array([], dtype=np.float32)

    for freq in seq:
        # create evenly space numbers
        t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
        
        # Convert time into radians
        # np.sin -> generate sine wave tone
        # 2 * np.pi * freq * t -> standard sine formula / pure tone
        # 0.2 -> reduce volume

        # Freq (Hz) = cycles/sec
        # cycles = freq * sec
        # radians = 2π * cycles
        # one full wave cycle = 360° = 2π radians = full circle
        
        # sine
        # tone = 0.2 * np.sin(2 * np.pi * freq * t)

        # square
        # tone = 0.2 * np.sign(np.sin(2 * np.pi * freq * t))

        # sawtooth
        # tone = 0.2 * (2 * (t * freq - np.floor(0.5 + t * freq)))

        # triangle
        # tone = 0.2 * (2 * np.abs(2 * (t * freq - np.floor(t * freq + 0.5))) - 1)

        # ADSR envelope
        attack = 0.02
        decay = 0.03
        sustain = 0.6
        release = 0.05

        env = np.ones_like(t)
        env[:int(attack*SAMPLE_RATE)] = np.linspace(0,1,int(attack*SAMPLE_RATE))
        env[int(attack*SAMPLE_RATE):int((attack+decay)*SAMPLE_RATE)] = np.linspace(1,sustain,int(decay*SAMPLE_RATE))
        env[int((attack+decay)*SAMPLE_RATE):int((duration-release)*SAMPLE_RATE)] = sustain
        env[int((duration-release)*SAMPLE_RATE):] = np.linspace(sustain,0,int(release*SAMPLE_RATE))

        tone = env * np.sin(2*np.pi*freq*t)

        audio = np.concatenate([audio, tone])

    # Normalize to avoid clipping/distortion
    # SAMPLE_RATE * duration = samples long
    audio = audio / np.max(np.abs(audio))

    # np.int16 converts float audio into 16-bit PCM format
    # 32767 is the max value for 16-bit audio
    write(filename, SAMPLE_RATE, np.int16(audio * 32767))
    print("Saved:", filename)

def middle_squares(seed_value, n):
    """Generate n pseudo-random numbers using the middle squares method.

    Args:
        seed_value (int): The initial seed value (should be a 4-digit number).
        n (int): The number of pseudo-random numbers to generate.

    Returns:
        list: A list of n pseudo-random numbers generated.
    """
    random_numbers = []
    current_value = seed_value

    for _ in range(n):
        # Square the current value
        squared_value = str(current_value ** 2).zfill(8)  # Ensure it's at least 8 digits
        # Extract the middle 4 digits
        middle_digits = squared_value[2:6]
        # Convert back to integer
        current_value = int(middle_digits)
        random_numbers.append(current_value)

    return random_numbers

def make_visual(seq):
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(seq, marker='o', markersize=3, linewidth=1)

    marker, = ax.plot([0], [seq[0]], marker='o', color='red', markersize=8)

    ax.set_title("Middle-Square PRNG Walk")
    ax.set_xlabel("Iteration")
    ax.set_ylabel("Value")

    def update(frame):
        marker.set_data([frame], [seq[frame]])
        return marker,

    ani = FuncAnimation(fig, update, frames=len(seq), interval=100, blit=True)
    ani.save("animation.mp4", writer="ffmpeg", dpi=150)
    print("Saved animation: animation.mp4")

if __name__ == "__main__":
    n = 120  # Number of random numbers to generate
    random_numbers = middle_squares(FOURTHIRTYTHREE, n)
    make_sound(random_numbers)
    make_visual(random_numbers)
