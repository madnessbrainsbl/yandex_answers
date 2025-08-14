import sys

input = sys.stdin.read
data = input().splitlines()

N, L, S = map(int, data[0].split())
events = data[1:]

taxi_last = {}
outputs = []

line_idx = 0
while line_idx < N:
    parts = events[line_idx].split()
    cmd = parts[0]
    timestamp = int(parts[1])
    if cmd == 'TAXI':
        taxi_id = int(parts[2])
        pos = int(parts[3])
        taxi_last[taxi_id] = (timestamp, pos)
    else:  # ORDER
        order_id = int(parts[2])
        A = int(parts[3])
        order_time = int(parts[4])
        max_allowed_dist = S * order_time
        good_taxis = []
        for tid, (lt, lpos) in taxi_last.items():
            delta_t = timestamp - lt
            D = S * delta_t
            C = (A - lpos + L) % L
            if D >= L:
                max_dist = L - 1
            else:
                if C <= D:
                    remaining = D - C
                    if remaining > 0:
                        min_pos = 1
                    else:
                        min_pos = L - C
                else:
                    min_pos = L - C
                if min_pos == L:
                    max_dist = 0
                else:
                    max_dist = L - min_pos
            if max_dist <= max_allowed_dist:
                good_taxis.append(tid)
        if not good_taxis:
            outputs.append('-1')
        else:
            good_taxis.sort()
            if len(good_taxis) > 5:
                good_taxis = good_taxis[:5]
            outputs.append(' '.join(map(str, good_taxis)))
    line_idx += 1

print('\n'.join(outputs))
