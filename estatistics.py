def FUNC_MEAN_SAMPLE(DF):
    SUM = 0
    for i in range(0, len(DF)):
        SUM += DF.iloc[i]
    MEAN = SUM / len(DF)
    return MEAN


def FUNC_STANDARD_VARIANCE(DF):
    MEAN = FUNC_MEAN_SAMPLE(DF)
    SUM = 0
    for i in range(0, len(DF)):
        SUM += (DF.iloc[i] - MEAN) ** 2
    STANDARD_VARIANCE = SUM / (len(DF) - 1)
    return STANDARD_VARIANCE


def FUNC_STANDARD_DEVIATION(DF):
    STANDARD_VARIANCE = FUNC_STANDARD_VARIANCE(DF)
    STANDARD_DEVIATION = STANDARD_VARIANCE ** (1 / 2)
    return STANDARD_DEVIATION


def FUNC_STANDARD_COVARIANCE(DF_1, DF_2):
    MEAN_1 = FUNC_MEAN_SAMPLE(DF_1)
    MEAN_2 = FUNC_MEAN_SAMPLE(DF_2)
    DEVIATION = 0
    for i in range(0, len(DF_1)):
        DEVIATION += (DF_1.iloc[i] - MEAN_1) * (DF_2.iloc[i] - MEAN_2)
    STANDARD_COVARIANCE = DEVIATION / (len(DF_1) - 1)
    return STANDARD_COVARIANCE


def FUNC_STANDARD_CORRELATION(DF_1, DF_2):
    COVARIANCE = FUNC_STANDARD_COVARIANCE(DF_1, DF_2)
    STANDARD_DEVIATION_1 = FUNC_STANDARD_DEVIATION(DF_1)
    STANDARD_DEVIATION_2 = FUNC_STANDARD_DEVIATION(DF_2)
    STANDARD_CORRELATION = COVARIANCE / (STANDARD_DEVIATION_1 * STANDARD_DEVIATION_2)
    return STANDARD_CORRELATION
