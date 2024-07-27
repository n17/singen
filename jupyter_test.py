import matplotlib.pyplot as plt
import numpy as np
from scipy.io.wavfile import write

def singen(
        time: int = 0,
        frequency: float = 110,  # Hz
        sampling_rate: int = 30,  # Hz
        loka: int = 1,
        alternative: int = 1,
        amplitude: float = 1,
        phase_offset: float = 0,  # radians
):
    assert 0 <= alternative
    total_phase_offset = np.pi * (alternative / loka * 2 + phase_offset)
    return amplitude * np.sin(
        2 * np.pi * frequency * time / sampling_rate + total_phase_offset
    )

def plot_lists(list_of_lists):
    """
    Plots multiple curves given a list of lists of float values.

    Parameters:
    list_of_lists (list of lists of floats): The input data to plot, where each inner list represents a curve.

    Returns:
    None
    """
    # Check if the input is a list of lists
    if not all(isinstance(inner_list, list) for inner_list in list_of_lists):
        raise ValueError("Input should be a list of lists.")
    
    # Plot each inner list as a separate curve
    for i, data in enumerate(list_of_lists):
        plt.plot(data)
    
    # Adding legend to the plot
    plt.legend()
    
    # Display the plot
    plt.show()

def export_to_wav(list_of_lists, filename, sample_rate=44100):
    """
    Exports a list of lists of float values as a .wav file.

    Parameters:
    list_of_lists (list of lists of floats): The input data to export, where each inner list represents a channel.
    filename (str): The name of the output .wav file.
    sample_rate (int): The sample rate for the .wav file. Default is 44100 Hz.

    Returns:
    None
    """
    # Check if the input is a list of lists
    if not all(isinstance(inner_list, list) for inner_list in list_of_lists):
        raise ValueError("Input should be a list of lists.")
    
    # Determine the number of channels and the length of the longest channel
    num_channels = len(list_of_lists)
    max_length = max(len(channel) for channel in list_of_lists)
    
    # Initialize a NumPy array to hold the data, filled with zeros
    data = np.zeros((max_length, num_channels))
    
    # Populate the array with the input data
    for i, channel in enumerate(list_of_lists):
        data[:len(channel), i] = channel
    
    # Normalize the data to the range of int16
    data = np.int16(data / np.max(np.abs(data)) * 32767)
    
    # Write the data to a .wav file
    write(filename, sample_rate, data)

sine_list = [
                [singen(time=t, loka=2, sampling_rate=500, frequency=4, alternative=1) /2 + 0.5 for t in range(501)],
                [singen(time=t, loka=2, sampling_rate=500, frequency=2, alternative=1) /2 + 0.5 for t in range(501)],
]
plot_lists(sine_list)
export_to_wav(sine_list, "wavtest1.wav")
