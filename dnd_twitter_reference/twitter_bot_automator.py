import random
import name_generator
import catch_phrase_list
import dice_roller

"""A program to roll and print a stat sheet for D&D 5e"""


class Dandd:
    """A Class that rolls dice, adds them and prints out the six stats needed to start a character"""

    def __init__(self, dice_sides=6):
        self.dice_sides = dice_sides

    def roll_stat(self):
        """the sum of the three highest values out of four dice rolls"""
        roll_total = []
        for g in range(4):
            roll_total.append(dice_roller.Dice(self.dice_sides).roll_the_die())
        roll_total.remove(min(roll_total))
        return sum(roll_total)

    def roll_abilities(self):
        """A function that returns six values that are the starting six ability stats before racial stat bonuses"""
        stat_totals = []
        for t in range(6):
            stat_totals.append(self.roll_stat())
        return stat_totals

    def stat_roll_select(self):
        """A function that rolls 3 lines of stats and lets the user select one"""
        stat_list = {}
        for x in range(1, 4):
            stat_list[x] = self.roll_abilities()
        u = random.randint(1, 3)
        return stat_list[u]

    def race_select(self):
        """Choose a race from a list with associated stats. stat_library established to hold ability values"""
        stat_library = {'STR': 0, 'DEX': 0, 'CON': 0, 'INT': 0, 'WIS': 0, 'CHA': 0}
        races = ['Dragonborn', 'Dwarf', 'Elf', 'Gnome', 'Half-Elf', 'Halfling', 'Half-Orc', 'Human', 'Teifling']
        alpha = random.sample(list(stat_library.keys()), k=3)
        char_race = random.choice(races)
        echo = random.choice(alpha)
        stat_library[f'{echo}'] += 1
        for delta in alpha:
            stat_library[f'{delta}'] += 1
        return {"char_race": char_race, "stat_library": stat_library}

    def stat_distribution(self):
        """Lets the user distribute the attributes rolled to the stat_library."""
        stat_library = self.race_select()["stat_library"]
        roll_selected = self.stat_roll_select()
        random.shuffle(roll_selected)
        det_list = list(stat_library)
        for att_key_number in range(6):
            holder = roll_selected.pop()
            stat_library[det_list[att_key_number]] += holder
        str1 = (stat_library['STR'] - 10) // 2
        dex1 = (stat_library['DEX'] - 10) // 2
        con1 = (stat_library['CON'] - 10) // 2
        int1 = (stat_library['INT'] - 10) // 2
        wis1 = (stat_library['WIS'] - 10) // 2
        cha1 = (stat_library['CHA'] - 10) // 2
        review_2 =  f"STR .... {stat_library['STR']} .... {str1:+g}" \
                    f"\nDEX .... {stat_library['DEX']} .... {dex1:+g}" \
                    f"\nCON ... {stat_library['CON']} .... {con1:+g}" \
                    f"\nINT ..... {stat_library['INT']} .... {int1:+g}" \
                    f"\nWIS ..... {stat_library['WIS']} .... {wis1:+g}" \
                    f"\nCHA .... {stat_library['CHA']} .... {cha1:+g}"
        return {"review_2": review_2, "con1": con1}

    def profession(self):
        char_race = self.race_select()["char_race"]
        review_2 = self.stat_distribution()["review_2"]
        char_name = name_generator.generator()
        char_phrase = catch_phrase_list.catch_phrase()
        profession_list = ['barbarian', 'bard', 'cleric', 'druid', 'fighter', 'monk', 'paladin', 'ranger', 'rogue',
                           'sorcerer', 'warlock', 'wizard']
        char_profession = random.choice(profession_list)
        review_3 = f'{char_name} the {char_race} {char_profession.title()}\n\t"{char_phrase}"' \
                   f'\n{review_2}'
        return review_3