import pandas as pd
import numpy as np

from scipy.stats import norm, chi2


chat_id = 975846018 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    s2 = np.mean(x**2) / 0.45
    c = chi2.ppf((1 + p)/2, 2*n)
    left = np.sqrt((2*n*s2)/c) / 0.45
    right = np.sqrt((2*n*s2)/chi2.ppf((1 - p)/2, 2*n)) / 0.45
    return left**0.1, right**0.1
