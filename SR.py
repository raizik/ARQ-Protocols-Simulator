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
    t = 10000
    t_i = 1
    t_p = 1.5
    import numpy as np
    import random
    # network = Network(context)
    sr_file = open("sr.csv", "w+")
    for p in np.arange(0, 0.8, 0.1):
        for q in np.arange(0, 0.8, 0.1):
            for sender_sz in range(1, 15):
                for receiver_sz in range(1, 15):
                        # initializing parameters...
                        context = Context()
                        num_msgs_received = 0
                        num_msgs_sent = 0
                        num_received_ack = 0
                        random_n = random.Random(t)
                        seq_number = 0
                        request_number = 0  # RN
                        p_success_received_info = 1 - p
                        p_success_received_ack = 1 - q
                        while context.time <= t:
                            # a packet is ready to send
                            # sending packet SN
                            # source sends SN info frame to target
                            if num_msgs_received - num_received_ack <= sender_sz:
                                context.inc_by(t_i + 2 * t_p)
                                num_msgs_sent += 1
                                # seq_number_max_sender += 1
                                if random_n.uniform(0, 1) < p_success_received_info and seq_number >= request_number:
                                    num_msgs_received += 1
                                    # sending info message seq_number + 1...
                                    seq_number += 1
                                    request_number = seq_number + 1
                            # timed out....

                            if request_number <= seq_number <= request_number + receiver_sz - 1 and \
                                    random_n.uniform(0, 1) < p_success_received_ack:
                                num_received_ack += 1
                                request_number = seq_number + 1
                    # timedout. (assuming timeout = 2*t_p) resending frames [RN,...,RN + M - 1]
                            else:
                                seq_number = request_number
                            context.tick()
                        sr_file.write("Tp-value:, %.2f, p-value:, %.2f, q-value:, %.2f, Utilization:, %.2f %%\n" %
                                      (t_p, p, q, (100.0 * (num_msgs_received / num_msgs_sent))))
    sr_file.close()


if __name__ == '__main__':
    main()
