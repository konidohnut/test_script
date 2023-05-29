def max_seq_len(s):
    if len(s) == 0:
        return 0

    c = s[0]
    cur_seq = 0
    max_seq = 0

    for i in s:
        if i == c:
            cur_seq += 1
        else:
            max_seq = max(max_seq, cur_seq)
            cur_seq = 1
            c = i
    max_seq = max(max_seq, cur_seq)

    return max_seq

if __name__ == "__main__":
    max_seq_len(input())