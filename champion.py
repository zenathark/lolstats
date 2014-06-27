import formulae as lol
import scipy as np


class champion(object):
    base_health = 0
    base_health_regen = 0
    base_mana = 0
    base_mana_regen = 0
    base_range = 0
    base_attack_damage = 0
    base_attack_speed = 0
    base_armor = 0
    base_magic_resist = 0
    base_mov_speed = 0
    inc_health = 0
    inc_health_regen = 0
    inc_mana = 0
    inc_mana_regen = 0
    inc_range = 0
    inc_attack_damage = 0
    inc_attack_speed = 0
    inc_armor = 0
    inc_magic_resist = 0
    inc_mov_speed = 0

    def calc_health(self):
        return _calc_stat(self.base_health, self.inc_health)

    def calc_health_regen(self):
        return _calc_stat(self.base_health_regen, self.inc_health_regen)

    def calc_mana(self):
        return _calc_stat(self.base_mana, self.inc_mana)

    def calc_mana_regen(self):
        return _calc_stat(self.base_mana_regen, self.inc_health)

    def calc_attack_damage(self):
        return _calc_stat(self.base_attack_damage, self.inc_health)

    def calc_armor(self):
        return _calc_stat(self.base_armor, self.inc_health)

    def calc_magic_resist(self):
        return _calc_stat(self.base_magic_resist, self.inc_health)

    def calc_attack_speed(self, bonus=0):
        levels = np.arange(0, 18, 1)
        ats = self.inc_attack_speed * levels
        return self.base_attack_speed * (1 + bonus + ats / 100)


def _calc_stat(base_stat, inc_stat):
    scaling = lol.scaling_level(inc_stat)
    return scaling + base_stat
