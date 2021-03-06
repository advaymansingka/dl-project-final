from typing import Type
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
import numpy as np
import wave
import sys
import csv



def find_fourier_helper(signal, frame_rate, start, end):
    
    signal = signal[start:end]

    timesteps = np.linspace(0, len(signal) / frame_rate, num=len(signal))
    timestep = timesteps[1] - timesteps[0]

    samples = timesteps.shape[0]

    yf = fft(signal)
    xf = fftfreq(samples, timestep)[:samples//2]

    return yf, xf, samples



def run_fourier(audio_filename, time_window, shift_size, 
    pause_time = 0.1, 
    animate = False, 
    write_to_csv = False, 
    csv_filename = "testcsv", 
    save_to_numpy = False
    ):

    if animate: 
        plt.figure(1)


    if save_to_numpy:
        numpy_holder = np.zeros((1, time_window//2))

    spf = wave.open(audio_filename, "r")
    signal = spf.readframes(-1)
    signal = np.frombuffer(signal, "int16")
    frame_rate = spf.getframerate()

    # If Stereo
    if spf.getnchannels() == 2:
        print("Just mono files")
        sys.exit(0)

    signal_length = signal.size
    current_loc = 0

    print(signal_length)
    print(frame_rate)

    if write_to_csv:
        csv_filename = csv_filename + ".csv"
        f_csv = open(csv_filename, 'w')
        f_csv.truncate()
        csv_writer = csv.writer(f_csv)

    while current_loc + time_window + 1 < signal_length:

        yf, xf, samples = find_fourier_helper(signal, frame_rate, current_loc, current_loc + time_window)
        yf = yf[0:samples//2]

        y_vals = 2.0/samples * np.abs(yf[0:samples//2])

        y_vals[y_vals < 80] = 0.0

        if save_to_numpy:
            numpy_holder = np.vstack((numpy_holder, y_vals))

        if animate:
            plt.cla()
            plt.plot(xf, y_vals)
            plot_helper(pause_time, audio_filename)

        if write_to_csv: 
            csv_writer.writerow(y_vals)

        print(f"Complete: {current_loc/signal_length * 100 :.2f}")

        current_loc += shift_size

    if save_to_numpy:
        numpy_file = csv_filename + ".npy"
        with open(numpy_file, 'wb') as f:
            np.save(f, numpy_holder)

    if animate: 
        plt.show()




def plot_helper(pause_time, audio_filename):

    audio_filename = audio_filename[:-4]

    plt.xlim(0, 5000)
    plt.ylim(0, 14000)
    plt.grid()
    plt.xlabel("Frequency")
    plt.ylabel("Amplitude")
    plt.title("Fast Fourier Transform for " + audio_filename)

    plt.pause(pause_time)


pause_time = 0.001


# DL_wiki.wav
# 393.6 seconds
# 37782 datapoints

# 18892800 signal size
# 48000 sample per second
# 2000 sample window size

# 0.0104 seconds per datapoint


run_fourier("wav_tests/Advay-OAMF.wav", 2000, 500, 
    pause_time, 
    animate=False, 
    write_to_csv=True, 
    csv_filename="Advay-OAMF",
    save_to_numpy=False
    )
