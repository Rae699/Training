"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature: int or float - temperature in kelvin.
    :param neutrons_emitted: int or float - neutrons emitted per second.
    :return: bool - is criticality balanced?

    A reactor is critical if:
    - Temperature < 800 K
    - Neutrons emitted > 500
    - Product of temp and neutrons < 500000
    """
    return (temperature < 800 
            and neutrons_emitted > 500 
            and temperature * neutrons_emitted < 500000)


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param voltage: int/float - voltage value
    :param current: int/float - current value
    :param theoretical_max_power: int/float - 100% efficiency power
    :return: str - efficiency zone color
    """
    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power) * 100
    
    if efficiency >= 80:
        return 'green'
    elif efficiency >= 60:
        return 'orange'
    elif efficiency >= 30:
        return 'red'
    return 'black'


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess reactor status code.

    :param temperature: int/float - temperature in kelvin
    :param neutrons_produced_per_second: int/float - neutron flux
    :param threshold: int/float - safety threshold
    :return: str - status code ('LOW', 'NORMAL', 'DANGER')

    1. LOW: product < 90% of threshold
    2. NORMAL: product within ±10% of threshold
    3. DANGER: product outside above ranges
    """
    product = temperature * neutrons_produced_per_second
    low_limit = threshold * 0.9
    high_limit = threshold * 1.1

    if product < low_limit:
        return 'LOW'
    if low_limit <= product <= high_limit:
        return 'NORMAL'
    return 'DANGER'
