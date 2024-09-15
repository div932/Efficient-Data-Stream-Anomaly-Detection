import numpy as np

def generate_data_stream(length=1000, frequency=10, amplitude=10, noise_level=0.1):
    """
    Generate a simulated data stream.

    Args:
        length (int, optional): The length of the data stream (default: 1000)
        frequency (int, optional): The frequency of the seasonal element (default: 10)
        amplitude (int, optional): The amplitude of the seasonal element (default: 10)
        noise_level (float, optional): The level of random noise (default: 0.1)

    Returns:
        list: A list of floating-point numbers representing the data stream
    """
    data_stream = []
    for i in range(length):
        value = amplitude * np.sin(2 * np.pi * frequency * i / length) + np.random.normal(0, noise_level)
        data_stream.append(value)
    return data_stream