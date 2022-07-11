import os
import pandas as pd
import data_parser as dp

def findall(directory, data_type):

    """
    _summary_
    Args:   directory (str): path to directory
            type (str): file type to find
    """
    # find all files in directory that have "iperf" in file name
    return [os.path.join(directory, f) for f in os.listdir(directory) if data_type in f]


for i in range(1,7):

    print(i)


    iperfFile = findall(f"/home/schmijul/Desktop/OpenFieldDay/router5/OpenField{i}", 'iperf')

    #pingFile = findall(f"/home/schmijul/Desktop/OpenFieldDay/router5/OpenField{i}", 'ping')

    parsedIperfFile = dp.get_iperf_data(pd.read_csv(iperfFile[0]))

    #parsedPingFile = dp.get_ping_data(pd.read_csv(pingFile[0]))

    path = f"/home/schmijul/Desktop/OpenFieldDay/parsed/router5/OpenField{i}"

    if not os.path.exists(path):
        os.makedirs(path)

    parsedIperfFile.to_csv(f"{path}/iperfData.csv")
    #parsedPingFile.to_csv(f"{path}/pingData.csv")
