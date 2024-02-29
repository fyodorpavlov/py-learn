import random
import datetime

start_date = datetime.date(2023, 1, 1)
end_date = datetime.date(2023, 12, 31)

random_date = start_date + datetime.timedelta(days=random.randint(0, (end_date - start_date).days))
print("Random date in 2023:", random_date)
