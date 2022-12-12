import numpy as np

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

def singen_to_numpy(
        length: int,
        frequency: float,  # Hz
        sampling_rate: int,  # Hz
        loka: int = 1,
        amplitude: float = 1,
        phase_offset: float = 0,  # radians
):
    return np.array(
        [
            [
                singen(
                    time = t,
                    alternative = a,
                    loka = loka,
                    frequency = frequency,
                    sampling_rate = sampling_rate,
                    amplitude = amplitude,
                    phase_offset = phase_offset,
                ) for a in range(loka)
            ] for t in range(length * sampling_rate)
        ]
    )

def singen_to_numpy2(
        function,
        length: int,
        channels: int,
):
    array = np.empty([length, channels])
    for n in range(channels):
        for m in range(length):
            array[n][m] = function(
                
            )

