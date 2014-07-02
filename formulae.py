from __future__ import division

import scipy as np
import math


def damage_reduction(resistance):
    """calculates the damage reduction.

    this function calculates the damage reduction from a given armor or magic
    resist rating. notice that the current equation as in patch 4.10 uses the
    same equation from both magic and physical damage reduction.

    args:
        resistance (float): the armor or magic resist rating.

    returns:
        a float that shows the percent of damage reduction from incoming
        attacks
    """
    if resistance > 0:
        return 100 / (100 + resistance)
    else:
        return 2 - (100 / (100 - resistance))


def effective_health(resistance, health=100):
    """calculates the effective health of a champion.

    this function calculates the effective health of a champios adding
    the given armor or magic resist ratio. this function uses damage_reduction
    function for calculating the result. if only a percent is wanted it is
    suggested to leave health as the default value of 100.

    args:
        health (integer): current health of a champion.
        resistance: resistance rating of a champios either armor or magic
        resist.

    returns:
        a pair (e_health, ratio) where e_helath is the effective
        health and ratio is the health increase from having the given
        armor ratio.
    """
    e_health = 1 / damage_reduction(resistance) * health
    ratio = e_health / health
    return (e_health, ratio)


def resistance_reduction_flat(resistance, reduction):
    """calculates the resistance of a champion.

    this function calculates the resistance of a champion after applying
    a flat resistance reduction. notice that the resultant resistance can
    goes to negative values.

    args:
        reduction (float): the reduction of the resistance.

    returns:
        the resultant resistance after applying the reduction.
    """
    return resistance - reduction


def resistance_reduction_percent(resistance, reduction):
    """calculates the resistance of a champion.

    this function calculates the resistance of a champion after applying
    a multiplicative (percent) resistance reduction. notice that the resultant
    resistance can have negative values.

    args:
        reduction (float): the percent reduction of the resistance.

    returns:
        the resultant resistance after applying the reduction.
    """
    return resistance - resistance * reduction


def resistance_penetration_flat(resistance, reduction):
    """calculates the resistance of a champion.

    this function calculates the resistance of a champion after applying
    a flat resistance penetration. notice that the resultant resistance can
    not go below 0.

    args:
        reduction (float): the reduction of the resistance.

    returns:
        the resultant resistance after applying the reduction.
    """
    if resistance - reduction > 0:
        return resistance - reduction
    else:
        return 0


def resistance_penetration_percent(resistance, reduction):
    """calculates the resistance of a champion.

    this function calculates the resistance of a champion after applying
    a multiplicative(percent) resistance penetration. notice that the
    resultant resistance can not go below 0.

    args:
        reduction (float): the reduction of the resistance.

    returns:
        the resultant resistance after applying the reduction.
    """
    f_reduction = resistance * reduction
    if resistance - f_reduction > 0:
        return resistance - f_reduction
    else:
        return 0


def damage_done(damage, resist, rpenetration_flat,
                rpenetration_percent, rreduction_flat,
                rreduction_percent):
    tt_resist = resistance_reduction_flat(resist, rreduction_flat)
    tt_resist = resistance_reduction_percent(tt_resist, rreduction_percent)
    tt_resist = resistance_penetration_percent(tt_resist, rpenetration_percent)
    tt_resist = resistance_penetration_flat(tt_resist, rpenetration_flat)
    dmg = damage - tt_resist
    return dmg


def pulse_abilities(seconds, samples, active, cooldown):
    saw = lambda t, a: t * a - np.floor(t * a)
    pulse = lambda t, a, duty: saw(t - a / duty, a) - saw(t, a)
    frequency = active + cooldown
    t = np.linspace(0, seconds, samples, endpoint=False)
    act = pulse(t, 1 / frequency, cooldown / frequency)
    minx = act.min()
    maxx = act.max()
    return act
