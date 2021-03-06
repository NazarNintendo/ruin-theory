import numpy as np

from claim import generate_claim


# Returns an array of arrival times.
def generate_arrival_times(rate: float, t_end: float = 1000) -> list[float]:
    t = 0
    arrival_times = []

    while t < t_end:
        tau = np.random.exponential(1 / rate)
        t += tau
        arrival_times.append(t)

    arrival_times.pop()

    return arrival_times


# Returns an array of claims for relevant arrival times.
def generate_claims(arrival_times: list[float]) -> list[float]:
    return [generate_claim() for _ in arrival_times]


# Returns the sum of claims for the time t.
def get_claims_sum(t: float, claims: list[float], arrival_times: list[float]) -> float:
    claims_sum = 0
    for ind, arrival_time in enumerate(arrival_times):
        if arrival_time <= t:
            claims_sum += claims[ind]
        else:
            break

    return claims_sum
