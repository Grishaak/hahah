def unique_in_order(sequence):
    new_order = []
    if len(sequence) == 0:
        return new_order
    i = 0
    while i < len(sequence):
        if i >= 1:
            if sequence[i] == sequence[i-1]:
                pass
            else:
                new_order.append(sequence[i])
        else:
            new_order.append(sequence[i])
        i += 1
    return new_order


seq = ("AAABBBCCCDAABBФффA")
order = unique_in_order(seq)
print(order)
