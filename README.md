# ARQ Protocols Simulator

There are three ARQ protocols simulated: 
1. Stop & Wait
2. Go-Back-N
3. Selective Repeat

## Inputs
* p - the probability of error in frame transmission
* q - the probability of error in ACK transmission
* Tp - propagation time of a frame
* T - simulation time
* *sender_sz -* size of sender's window (for SR)
* *receiver_sz* - size of receiver's windows (for SR)

## Output
Utilization rate for each protocol
