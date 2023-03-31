import pandas as pd
import numpy as np

from scipy.stats import norm, chi2


chat_id = 975846018 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    alpha = 1 - p
    df = 2 * n
    loc = np.sqrt(np.mean(x ** 2) / 2)
    scale = np.sqrt(chi2.ppf(1 - alpha / 2, df) / (2 * n)) - \
            np.sqrt(chi2.ppf(alpha / 2, df) / (2 * n))
    return loc - scale, loc + scale
