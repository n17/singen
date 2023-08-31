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

def get_2d_singen(
        func,
        frequency: float,  # Hz
        sampling_rate: int,  # Hz
        loka: int = 1,
        amplitude: float = 1,
        phase_offset: float = 0,  # radians
):
    def two_d_singen(a, t):
        return func(
            time = t,
            alternative = a,
            loka = loka,
            frequency = frequency,
            sampling_rate = sampling_rate,
            amplitude = amplitude,
            phase_offset = phase_offset,
        )
    return two_d_singen

def two_d_function_to_numpy(
        function,
        length: int,
        channels: int,
):
    # channels -= 1
    array = np.empty([length, channels])
    for t in range(length):
        for n in range(channels):
            array[t][n] = function(t, n)
    return array
