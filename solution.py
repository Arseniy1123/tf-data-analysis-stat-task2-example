import pandas as pd
import numpy as np

from scipy.stats import norm, chi2


chat_id = 975846018 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    s_squared = np.mean(x**2) / 0.45
    alpha = 1 - p
    left = (n - 1) * s_squared / chi2.ppf(1 - alpha/2, n - 1)
    right = (n - 1) * s_squared / chi2.ppf(alpha/2, n - 1)
    return (left, right)
