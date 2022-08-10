import numpy as np

def singen(
        loka: int,
        time: int,
        alternative: int,
        amplitude: float,
        frequency: float,  # Hz
        sampling_rate: int,  # Hz
        phase_offset: float = 0,  # radians
):
    assert 0 < alternative <= loka
    total_phase_offset = np.pi * (alternative / loka * 2 + phase_offset)
    return amplitude * np.sin(
        2 * np.pi * frequency * time / sampling_rate + total_phase_offset
    )

