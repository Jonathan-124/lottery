import csv
import datetime
from draws.models import Draw


def import_past_draws_from_csv():
    with open('Powerball.csv', newline='') as csvfile:
        drawreader = csv.reader(csvfile)
        for row in drawreader:
            draw_date = datetime.datetime.strptime(row[0], '%m/%d/%y').date()
            num_tickets_purchased = row[1]
            jackpot_amount = row[2]
            _, created = Draw.objects.get_or_create(
                draw_date=draw_date,
                num_tickets_purchased=num_tickets_purchased,
                jackpot_amount=jackpot_amount,
            )


import_past_draws_from_csv()
# in pipenv shell CLI: python manage.py shell < import.py
