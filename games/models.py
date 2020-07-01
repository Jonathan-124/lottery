from django.contrib.postgres.fields import JSONField
from django.db import models
from django.dispatch import receiver
from draws.models import Draw
from math import factorial, floor
from numpy import array, exp
from scipy.optimize import curve_fit


# a - lower asymptote
# b - upper asymptote
# c - horizontal translation
# d - growth rate
def gompertz_curve(x, a, b, c, d):
    return a + b * exp(-c * exp(-d * x))


# x - advertised Jackpot amount (in millions)
# lmbda - gompertz_output * 1/292201338
# a partial sum estimates the infinite series, which includes cases up to 10 simultaneous jackpot winners in a draw
# returns a 2-tuple of probability of jackpot win, the expected return per powerball ticket
def powerball_expected_return(x, gompertz_output):
    jackpot_not_won_probability = (292201337/292201338) ** (floor(gompertz_output))
    partial_sum = 0
    lmbda = gompertz_output / 292201338
    for i in range(1, 11):
        partial_sum += (exp(-lmbda) * (lmbda ** i)) / (i * factorial(i))
    return 1 - jackpot_not_won_probability, (x * 1000000 * (partial_sum + jackpot_not_won_probability) - 490936628) / 292201338


class Game(models.Model):
    name = models.CharField(max_length=63)
    odds = JSONField()
    prediction_funcs = JSONField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_past_data(self):
        return list(self.draws.exclude(drawn=False).values('jackpot_amount', 'num_tickets_purchased'))

    def get_next_draw_data(self):
        next_draw = self.draws.filter(drawn=False)[0]
        return [next_draw.draw_date.strftime("%B %d, %Y"), next_draw.jackpot_amount, next_draw.predicted_yield, next_draw.predicted_jackpot_probability, next_draw.predicted_num_tickets_purchased]

    def get_most_recent_draw_data(self):
        most_recent_draw = self.draws.exclude(drawn=False)[0]
        return [most_recent_draw.draw_date.strftime("%B %d, %Y"), most_recent_draw.predicted_num_tickets_purchased, most_recent_draw.num_tickets_purchased, most_recent_draw.winners_categories, most_recent_draw.numbers_drawn]

'''
@receiver(models.signals.post_save, sender=Draw, dispatch_uid='update_game_funcs')
def update_game_funcs(sender, instance, **kwargs):
    if instance.drawn:
        # fitting the gompertz curve
        draws = sender.objects.exclude(drawn=False)
        xdata = array(draws.values_list('jackpot_amount', flat=True))
        ydata = array(draws.values_list('num_tickets_purchased', flat=True))
        prediction_params = instance.game.prediction_funcs['current_curve_parameters']
        popt, pcov = curve_fit(gompertz_curve, xdata, ydata, p0=prediction_params)
        current_curve_parameters = popt.tolist()
        # saving prediction params
        instance.game.prediction_funcs = {'previous_curve_parameters': prediction_params, 'current_curve_parameters': current_curve_parameters, 'pcov': pcov.tolist()}
        instance.game.save()
    if not instance.drawn:
        prediction_params = instance.game.prediction_funcs['current_curve_parameters']
        # predicting stuff
        p_num_tickets_purchased = gompertz_curve(instance.jackpot_amount, prediction_params[0], prediction_params[1], prediction_params[2], prediction_params[3])
        p_jackpot_probability, p_yield = powerball_expected_return(instance.jackpot_amount, p_num_tickets_purchased)
        # saving predictions
        sender.objects.filter(id=instance.id).update(predicted_num_tickets_purchased=p_num_tickets_purchased, predicted_jackpot_probability=p_jackpot_probability, predicted_yield=p_yield)
'''