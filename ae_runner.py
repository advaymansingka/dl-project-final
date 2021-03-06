import argparse
import math
from operator import mod
from pickletools import optimize
from turtle import shape
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
import os
import random
import tensorflow as tf
from tqdm import tqdm
from ae_full import AE, loss_function
from ae_one_layer import AE_small, loss_function_small
from ae_extreme import AE_extreme
import csv
import pandas as pd


def train_vae(model, data):
    """
    Train your VAE with one epoch.

    Inputs:
    - model: Your VAE instance.

    Returns:
    - total_loss: Sum of loss values of all batches.
    """
    
    optimizer = tf.keras.optimizers.Adam(learning_rate = 0.001)
    total_loss = 0

    batch_size = 64
    num_batches = data.shape[0] // batch_size

    for i in range(num_batches):

        x_train = data[i*batch_size : (i+1)*batch_size]

        with tf.GradientTape() as tape:

            x_hat, _ = model.call(x_train)
            loss = loss_function(x_hat, x_train)

            train_vars = model.trainable_variables
            gradients = tape.gradient(loss, train_vars)
            optimizer.apply_gradients(zip(gradients, train_vars))

        total_loss += loss

    return total_loss



def visual_test(model, data, write_to_csv = False, show_plot = True, csv_filename = "encoded_test_def.csv"):

    if show_plot:
        plt.figure(1)

    if write_to_csv:
        f_csv = open(csv_filename, 'w')
        f_csv.truncate()
        csv_writer = csv.writer(f_csv)


    for i in range(data.shape[0]):

        x_train = data[i : (i+1)]
        x_hat, encoded = model.call(x_train)

        x_train = x_train.numpy()
        x_hat = x_hat.numpy()

        if write_to_csv:
            encoded = np.squeeze(encoded.numpy())
            csv_writer.writerow(encoded)

        if show_plot:
            plt.cla()
            plt.plot(x_train[0], color='blue', linewidth=1)
            plt.plot(x_hat[0], color='red', linewidth=1)
            plt.xlim(0, 400)
            plt.ylim(0, 10000)
            plt.pause(0.003)


    if show_plot: 
        plt.show()


def main():

    with open('advayOAMF.csv', 'r') as f:
        data = list(csv.reader(f, delimiter=","))
 
    data = np.array(data)
    data = tf.convert_to_tensor(data, dtype=tf.float32)

    print(data.shape)

    num_features = data.shape[1]

    # Get an instance of VAE
    model = AE_extreme(num_features, encoded_size=2, checkpoint_file='./save_vals/advayOAMF_2000epo_2hid_extreme')

    # Train AE
    for epoch_id in range(2000):
        total_loss = train_vae(model, data)
        print(f"Epoch: {epoch_id} \tLoss: {total_loss/len(data):.4f}")

    model.save_model()
    # model.load_model()

    visual_test(model, data, write_to_csv=True, csv_filename="advayOAMF_2000epo_2hid_extreme.csv", show_plot=False)
    


if __name__ == "__main__":
    main()