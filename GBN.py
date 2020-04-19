# -------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Racheli
#
# Created:     27/05/2018
# Copyright:   (c) Racheli 2018
# Licence:     <your licence>
# -------------------------------------------------------------------------------


class Context:
    def __init__(self):
        self.time = 0
        self.lastTimeLogged = 0

    def get_time(self):
        return self.time

    def tick(self):
        self.time += 1

    def inc_by(self, val):
        self.time += val


def main():
    t = 1000
    t_i = 1
    import numpy as np
    import random
    # last_time_sent = 0
    gbn_file = open("gbn.csv", "w+")
    for t_p in np.arange(0.1, 3.1, 0.5):
        for p in np.arange(0, 0.8, 0.04):
            for q in np.arange(0, 0.8, 0.04):
                context = Context()
                # network = Network(context)
                num_msgs_received = 0
                num_msgs_sent = 0
                random_n = random.Random(t)
                seq_number_min = 0                  # SN_min
                seq_number_max = 0                  # SN_max
                seq_number = 0
                request_number = 0                  # RN
                timeout = 2 * t_p
                p_success_received_info = 1-p
                p_success_received_ack = 1-q
                p_success = p_success_received_ack * p_success_received_info
                # last_time_received_ack = 0;
                beta = 2 * t_p
                sender_sz = beta + 1
                last_time_sent = 0
                while context.time <= t:
                    # check if received message from network layer
                    if random.uniform(0, 1) > p_success:
                        context.tick()
                        continue
                    # a packet is ready to send
                    # sending packet SN
                    # source sends SN info frame to target
                    if seq_number_max - seq_number_min < sender_sz:
                        last_time_sent = context.get_time()
                        context.inc_by(t_i + 2 * t_p)
                        num_msgs_sent += 1
                        seq_number_max = seq_number #changed
                        seq_number_max += 1
                        if random_n.uniform(0, 1) < p_success_received_info and seq_number == request_number:
                            num_msgs_received += 1
                            request_number += 1
                          #  seq_number = request_number
                    # seq_number += 1
                    # check if target received SN
                    # target send ack to source
                    if request_number > seq_number_min and random_n.uniform(0, 1) < p_success_received_ack:
                            seq_number_min = request_number
                            seq_number = request_number     # changed
                    # timedout. (assuming timeout = 2*t_p) resending frames [sn_min,...,sn_max]
                    else:
                        seq_number = seq_number_min
                        request_number = seq_number
                    context.tick()
            gbn_file.write("Tp-value %.2f, p-value %.2f, q-value %.2f, Utilization: %.2f %%\n" %
                           (t_p, p, q, (100.0 * (num_msgs_received / num_msgs_sent))))
    gbn_file.close()


if __name__ == '__main__':
    main()
