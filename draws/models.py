from django.contrib.postgres.fields import JSONField
from django.db import models


class Draw(models.Model):
    game = models.ForeignKey('games.Game', on_delete=models.PROTECT, related_name='draws', default=1)
    draw_date = models.DateField()
    drawn = models.BooleanField(default=False)
    numbers_drawn = JSONField(null=True, blank=True)
    jackpot_amount = models.FloatField()
    jackpot_won = models.BooleanField(null=True, blank=True)
    num_tickets_purchased = models.PositiveIntegerField(null=True, blank=True)
    winners_categories = models.IntegerField(null=True, blank=True)
    predicted_yield = models.FloatField(null=True, blank=True)
    predicted_num_tickets_purchased = models.PositiveIntegerField(null=True, blank=True)
    predicted_jackpot_probability = models.FloatField(null=True, blank=True)

    class Meta:
        ordering = ['-draw_date']

    def __str__(self):
        return self.draw_date.strftime('%Y/%m/%d')

