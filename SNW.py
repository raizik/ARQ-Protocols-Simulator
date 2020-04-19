#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Racheli
#
# Created:     27/05/2018
# Copyright:   (c) Racheli 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------


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
    snw_file = open("snw.csv", "w+")
    for t_p in np.arange(0.1, 3.1, 0.5):
        for p in np.arange(0, 0.8, 0.04):
            for q in np.arange(0, 0.8, 0.04):
                    # initializing parameters...
                    p_success_received_info = 1-p
                    p_success_received_ack = 1-q
                    p_success = p_success_received_ack * p_success_received_info
                    context = Context()
                    num_msgs_received = 0
                    num_msgs_sent = 0
                    random_n = random.Random(t)
                    seq_number = 0
                    request_number = 0
                    while context.time <= t:
                        context.tick()
                        # check if received message from network layer
                        if random.uniform(0, 1) > p_success:
                            continue
                        # a packet is ready to send
                        # #source sends SN info frame to target
                            # last_time_sent = context.getTime()
                        context.inc_by(t_i + 2 * t_p)
                        num_msgs_sent += 1
                        # check if target received SN
                        if random_n.uniform(0, 1) < p_success_received_info and seq_number == request_number:
                            request_number += 1
                            num_msgs_received += 1
                            # target sends ack frame to source#
                            # check if source received SN+1#
                        if random_n.uniform(0, 1) < p_success_received_ack and request_number == seq_number + 1:
                            seq_number += 1
                    snw_file.write("Tp-value %.2f, p-value %.2f, q-value %.2f, Utilization: %.2f %%\n" %
                                   (t_p, p, q, (100.0 * (num_msgs_received / num_msgs_sent))))
    snw_file.close()


if __name__ == "__main__":
    main()
