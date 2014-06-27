from __future__ import division

import formulae as lol


class battlefield(object):
    ticks = 300
    defender = 0
    attacker = 0

    def simulate(time):
        defender.init()
        attacker.init()
        lapsed = 0
        for i in range(time / ticks):
            patt, arpen_f, arpen_p, arred_f, arred_p = attacker.get_aadamage()
            pdef = defender.get_aadefense()
            dd = lol.damage_done(patt, pdef, arpen_f, arpen_p, arred_p, arred_f)
                patt, pdef, attacker.arpen, attacker.
            next_attack = attacker.get_next_att_time()



