import pandas as pd
import numpy
import csv

dataset_headers = ["duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes", "land",
                   "wrong_fragment",
                   "urgent", "hot", "num_failed_logins", "logged_in", "num_compromised", "root_shell",
                   "su_attempted", "num_root",
                   "num_file_creations", "num_shells", "num_access_files", "num_outbound_cmds",
                   "is_host_login", "is_guest_login", "count",
                   "srv_count", "serror_rate", "srv_serror_rate", "rerror_rate", "srv_rerror_rate",
                   "same_srv_rate", "diff_srv_rate",
                   "srv_diff_host_rate", "dst_host_count", "dst_host_srv_count", "dst_host_same_srv_rate",
                   "dst_host_diff_srv_rate",
                   "dst_host_same_src_port_rate", "dst_host_srv_diff_host_rate", "dst_host_serror_rate",
                   "dst_host_srv_serror_rate",
                   "dst_host_rerror_rate", "dst_host_srv_rerror_rate", "type"]


class preprocessing:
    # reading the txt dataset file as a dataframe
    def read_data_txt(self, txt_file):
        global dataset_headers
        df = pd.read_csv(txt_file, names=dataset_headers)
        lst = [each[:-1] for each in df['type']]
        df['type'] = lst
        return df

    # adding header to txt file dataset
    # no need can be done while reading csv by passing headers as argument
    def add_headers(self, txt_file):
        with open(txt_file, 'r+') as in_file:
            precontent = in_file.read()
            in_file.seek(0, 0)
            in_file.write("duration, protocol_type, service, flag, src_bytes, dst_bytes, land, wrong_fragment,urgent, hot, num_failed_logins, logged_in, num_compromised, root_shell, su_attempted, num_root,\
                            num_file_creations, num_shells, num_access_files, num_outbound_cmds, is_host_login, is_guest_login, count,\
                            srv_count, serror_rate, srv_serror_rate, rerror_rate, srv_rerror_rate,same_srv_rate,diff_srv_rate,\
                            srv_diff_host_rate, dst_host_count, dst_host_srv_count, dst_host_same_srv_rate, dst_host_diff_srv_rate,\
                            dst_host_same_src_port_rate, dst_host_srv_diff_host_rate, dst_host_serror_rate, dst_host_srv_serror_rate,\
                            dst_host_rerror_rate, dst_host_srv_rerror_rate, type" + "\n" + precontent)
            in_file.close()

    # converting the original text dataset into csv
    # this function not needed since panda's read_csv does this auto
    def text_to_csv(self, txt_file):
        with open(txt_file, 'r') as in_file:
            stripped = (line.strip() for line in in_file)
            lines = (line.split(",") for line in stripped if line)
            with open('data_original.csv', 'w') as out_file:
                writer = csv.writer(out_file)
                writer.writerows(lines)
                out_file.close()
            in_file.close()
        df = pd.read_csv('data_original.csv')
        return df

    # remove redundant rows in the dataframe
    def dropduplicates(self,df):
        ddf=pd.DataFrame.drop_duplicates(df)
        return ddf

    # converting categorical to numerical values
    def cat_to_num(self,df):
        count = 0
        for each in df['service'].unique():
            df['service'].replace([each], [count], inplace=True)
            count += 1
        count = 0
        for each in df['flag'].unique():
            df['flag'].replace([each], [count], inplace=True)
            count += 1

        df.replace(['icmp', 'udp', 'tcp'], [2, 1, 0], inplace=True)
        df['type'].replace(['normal', '.*'], [0, 1], regex=True, inplace=True)
        # df.to_csv('output.csv',index=False)
        return df
