from pad.raw.skills.active_skill_text import AsTextConverter
from pad.raw.skills.en_skill_common import EnBaseTextConverter


class EnAsTextConverter(AsTextConverter, EnBaseTextConverter):
    def fmt_repeated(self, text, amount):
        return '{} {} times'.format(text, amount)
    
    def fmt_mass_atk(self, mass_attack):
        if mass_attack:
            return 'all enemies'
        else:
            return 'an enemy'
    
    def fmt_duration(self, duration):
        return 'For {} {}, '.format(duration, 'turns' if duration > 1 else 'turn')
    
    def attr_nuke_text(self, mult, attr, target):
        return 'Deal {}x ATK {} damage to {}'.format(mult, attr, target)
    
    def fixed_attr_nuke_text(self, damage, attr, target):
        return 'Deal {} {} damage to {}'.format(damage, attr, target)
