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
    assert 0 < alternative
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
                    alternative = a + 1, # Zero vs one-based indexing
                    loka = loka,
                    frequency = frequency,
                    sampling_rate = sampling_rate,
                    amplitude = amplitude,
                    phase_offset = phase_offset,
                ) for t in range(length)
            ] for a in range(loka)
        ]
    )
