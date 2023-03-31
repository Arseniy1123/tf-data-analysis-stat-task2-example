import pandas as pd
import numpy as np

from scipy.stats import norm, chi2


chat_id = 975846018 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    alpha = 1 - p
    chi2_alpha_2 = chi2.ppf(alpha / 2, df=n - 1)
    chi2_1_minus_alpha_2 = chi2.ppf(1 - alpha / 2, df=n - 1)
    s2 = np.var(x, ddof=1)
    left = (n - 1) * s2 / chi2_1_minus_alpha_2
    right = (n - 1) * s2 / chi2_alpha_2
    return np.sqrt(left / 45), np.sqrt(right / 45)
