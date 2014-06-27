from __future__ import division

import scipy as np
import math


def damage_reduction(resistance):
    """Calculates the damage reduction.

    This function calculates the damage reduction from a given armor or magic
    resist rating. Notice that the current equation as in patch 4.10 uses the
    same equation from both magic and physical damage reduction.

    Args:
        resistance (float): The armor or magic resist rating.

    Returns:
        A float that shows the percent of damage reduction from incoming
        attacks
    """
    if resistance > 0:
        return 100 / (100 + resistance)
    else:
        return 2 - (100 / (100 - resistance))


def effective_health(resistance, health=100):
    """Calculates the effective health of a champion.

    This function calculates the effective health of a champios adding
    the given armor or magic resist ratio. This function uses damage_reduction
    function for calculating the result. If only a percent is wanted it is
    suggested to leave health as the default value of 100.

    Args:
        health (integer): Current health of a champion.
        resistance: Resistance rating of a champios either armor or magic
        resist.

    Returns:
        A pair (e_health, ratio) where e_helath is the effective
        health and ratio is the health increase from having the given
        armor ratio.
    """
    e_health = 1 / damage_reduction(resistance) * health
    ratio = e_health / health
    return (e_health, ratio)


def resistance_reduction_flat(resistance, reduction):
    """Calculates the resistance of a champion.

    This function calculates the resistance of a champion after applying
    a flat resistance reduction. Notice that the resultant resistance can
    goes to negative values.

    Args:
        reduction (float): The reduction of the resistance.

    Returns:
        The resultant resistance after applying the reduction.
    """
    return resistance - reduction


def resistance_reduction_percent(resistance, reduction):
    """Calculates the resistance of a champion.

    This function calculates the resistance of a champion after applying
    a multiplicative (percent) resistance reduction. Notice that the resultant
    resistance can have negative values.

    Args:
        reduction (float): The percent reduction of the resistance.

    Returns:
        The resultant resistance after applying the reduction.
    """
    return resistance - resistance * reduction


def resistance_penetration_flat(resistance, reduction):
    """Calculates the resistance of a champion.

    This function calculates the resistance of a champion after applying
    a flat resistance penetration. Notice that the resultant resistance can
    not go below 0.

    Args:
        reduction (float): The reduction of the resistance.

    Returns:
        The resultant resistance after applying the reduction.
    """
    if resistance - reduction > 0:
        return resistance - reduction
    else:
        return 0


def resistance_penetration_percent(resistance, reduction):
    """Calculates the resistance of a champion.

    This function calculates the resistance of a champion after applying
    a multiplicative(percent) resistance penetration. Notice that the
    resultant resistance can not go below 0.

    Args:
        reduction (float): The reduction of the resistance.

    Returns:
        The resultant resistance after applying the reduction.
    """
    f_reduction = resistance * reduction
    if resistance - f_reduction > 0:
        return resistance - f_reduction
    else:
        return 0


def scaling_level(scaling):
    levels = np.arange(1, 19, 1)
    return levels * scaling

# def damage_done(damage, resistance, resistance_penetration_flat,
#                 resistance_penetration_percent, resistance_reduction_flat,
#                 resistance_reduction_percent):


