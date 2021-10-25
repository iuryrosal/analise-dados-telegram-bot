import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import io

def barv_npsmean_by(dataframe, axisX):
    buf = io.BytesIO()

    axisX_labels = dataframe.groupby([f"{axisX}"]).mean()["NPS interno"].index
    nps_mean_by_axisX = dataframe.groupby([f"{axisX}"]).mean()["NPS interno"].values

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.bar(axisX_labels, nps_mean_by_axisX)
    ax.set_ylabel("NPS interno mensal médio")
    ax.set_yticks(np.array(range(0, 11, 1)))
    ax.set_title(f"Média de NPS Interno Mensal por {axisX}")
    fig.savefig(buf, format='png')
    plt.close(fig)
    print("####")
    print(buf)
    return buf

def hist_nps(dataframe):
    buf = io.BytesIO()

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.hist(dataframe["NPS interno"])
    ax.set_title("Distribuição do NPS interno mensal")
    ax.set_xlabel("Nps Interno")
    fig.savefig(buf, format='png')
    plt.close(fig)
    return buf
