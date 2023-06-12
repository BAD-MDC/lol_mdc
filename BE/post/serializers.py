from rest_framework import serializers
from .models import Review,Champion_stats

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','title','content','updated_at')
        model = Review

class Champion_stats_Serializer(serializers.ModelSerializer):
    class Meta:
        fields=('name','id','hp','hp_perlevel','mp','mp_perlevel','armor','armor_perlevel','spellblock','spellblock_perlevel','hpregen','hpregen_perlevel','mpregen','mpregen_perlevel','crit','crit_perlevel','attackdamage','attackdamage_perlevel','attackspeed','attackspeed_perlevel')
        model=Champion_stats