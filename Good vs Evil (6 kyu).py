def goodVsEvil(good, evil):
    worths = [1, 2, 3, 3, 4, 10, 1, 2, 2, 2, 3, 5, 10]
    g_e = [int(j) for i in [good, evil] for j in i.split() if j.isdigit()]
    result = [g_e[i]*worths[i] for i in list(range(13))]

    if sum(result[:6]) > sum(result[6:]):
        return "Battle Result: Good triumphs over Evil"
    elif sum(result[:6]) < sum(result[6:]):
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victor on this battle field"
