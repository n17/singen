import click
import numpy as np
import scipy.io.wavfile
import time
from datetime import datetime
import singen as sg


@click.command()
@click.option('--frequency', default=440.0, help='Frequency of the sine wave.')
@click.option('--duration', default=5.0, help='Duration of the sine wave in seconds.')
@click.option('--loka', default=2, help='Loka parameter for the sine wave function.')
@click.option('--sampling_rate', default=44100, help='Sampling rate.')
@click.option('-n', '--name', default=None, help='Name of the output file.')
def generate_sinewave(frequency, duration, loka, sampling_rate, name):
    length = int(duration * sampling_rate)
    channels = 1  # Assuming single channel for this example

    singen_function = sg.get_2d_singen(
        func=sg.singen,
        frequency=frequency,
        sampling_rate=sampling_rate,
        loka=loka,
    )

    array = sg.two_d_function_to_numpy(
        lambda x, y: singen_function(x, y),
        length=length,
        channels=loka,
    ).astype(np.float32)

    if name is None:
        name = datetime.now().strftime("singen_%Y%m%d%H%M%S.wav")
    else:
        name = f"{name}.wav"

    # Ensure the array is in the correct shape for writing as a wav file
    if array.ndim == 2 and array.shape[1] == 1:
        array = array.flatten()

    scipy.io.wavfile.write(name, sampling_rate, array)

    click.echo(f"Generated sine wave and saved as {name}")

if __name__ == '__main__':
    generate_sinewave()
