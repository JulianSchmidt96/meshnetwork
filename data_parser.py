import pandas as pd

def get_iperf_data(iperf_df):

    """_summary_

    Args:
        df (pd.DataFrame): iperf log as csv

    Returns:
        pandas Dataframe with timestamp as datetime format, and all iperf information

    """

    iperf_df.columns = ['timestamp',
                        'source',
                        'src_port_udp',
                        'destination',
                        'dst_port_udp',
                        'a','intervall',
                        'data',
                        'datarate']
    iperf_df.timestamp = pd.to_datetime(iperf_df.timestamp, exact=False, format= '%Y%m%d%H%M%S')
    iperf_df = iperf_df.drop(columns=['a','intervall'])

    return iperf_df

def get_pcap_udp_data(udp_df):

    """_summary_

    Args:
        udp_df (pd.DataFrame): UDP data from pcap file, prefiltered for udp only with wireshark

    Returns:
        pandas Dataframe with timestamp as datetime format,
        packet length as int, source and destination ip as string,
        source and destination port as int

    """

    # Change Time col to date time timestamp format
    udp_df.Time = pd.to_datetime(udp_df.Time)
    udp_df = udp_df.rename(columns={'Time': 'timestamp'})

    # Grep UDP src port from Info column
    info = pd.DataFrame(udp_df.Info.str.split(' ',1).tolist(),
                        columns = ['src_port_udp','rest'])
    udp_df['src_port_udp'] = info.src_port_udp

    # Cut > from Info column
    info = pd.DataFrame(info.rest.str.split(' > ',1).tolist(),
                        columns = ['>','rest'])[['rest']]

    # Grep UDP dst port from Info column
    udp_df['dst_port_udp'] = pd.DataFrame(info.rest.str.split(' Len=',1).tolist(),
                                      columns = ['dst_port_udp','len']).dst_port_udp

    udp_df['len'] = pd.DataFrame(info.rest.str.split(' Len=',1).tolist(),
                             columns = ['dst_port_udp','len']).len # Grep UDP len from Info column
    udp_df = udp_df.drop(columns=['Info'])
    return udp_df

def get_ping_data(ping_df):
    """
    _summary_

        Args:
            df (pandas DataFrame): ping log data ( csv)
        Returns:
            cleaned DataFrme

    _description_
            This functions renamed the ping data columns and delete unnecessary columns
    """

    ping_df.columns = [['timestamp', 'idx', 'domain', 'delay']]
    ping_df = ping_df.drop(columns=['domain', 'idx'])

    return ping_df
    