import matplotlib.pyplot as plt
import matplotlib.animation as animation

def visualize_data_stream(data_stream, anomalies):
    """
    Visualize the data stream and detected anomalies.

    Args:
        data_stream (list): A list of floating-point numbers representing the data stream
        anomalies (list): A list of booleans indicating whether each data point is an anomaly (True) or not (False)
    """
    fig, ax = plt.subplots()
    line, = ax.plot(data_stream)

    def update(i):
        line.set_ydata(data_stream[:i])
        return line,

    ani = animation.FuncAnimation(fig, update, frames=len(data_stream), blit=True)
    plt.show()

    # Add anomaly markers
    anomaly_markers = [i for i, x in enumerate(anomalies) if x]
    plt.plot(anomaly_markers, [data_stream[i] for i in anomaly_markers], 'ro')
    plt.show()