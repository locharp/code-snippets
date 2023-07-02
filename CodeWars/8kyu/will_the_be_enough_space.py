def enough(cap, on, wait):
    need = wait + on - cap
    return need if need > 0 else 0