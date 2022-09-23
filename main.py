from datetime import date
from time import sleep
from progress.bar import Bar
import datetime



date_to_compare = datetime.datetime(2022, 12, 31) # Replace with whatever you want
date_today = datetime.datetime.now() 
day_today = date.today().day
year_today = date.today().year
year_next = year_today +1

dict_seasons = {"Lente_begin": datetime.datetime(year_today, 3, 20), "Lente_einde": datetime.datetime(year_today, 6, 21),
                "Zomer_begin": datetime.datetime(year_today, 6, 21),  "Zomer_einde": datetime.datetime(year_today, 9, 23),
                "Herst_begin": datetime.datetime(year_today, 9, 23),  "Herst_einde": datetime.datetime(year_today, 12, 21),
                "Winter_begin": datetime.datetime(year_today, 12, 21), "Winter_einde":  datetime.datetime(year_next, 3, 20)
                }    


if ((date_today>= dict_seasons["Lente_begin"]) and (date_today< dict_seasons["Lente_einde"])):
    progress_bar_limit = 25
    get_current_season = "Lente"

        
elif ((date_today>= dict_seasons["Zomer_begin"]) and (date_today< dict_seasons["Zomer_einde"])):
    progress_bar_limit = 50
    get_current_season = "Zomer"

        
elif ((date_today>= dict_seasons["Herst_begin"]) and (date_today< dict_seasons["Herst_einde"])):
    progress_bar_limit = 75
    get_current_season = "Herst"

        
elif ((date_today>= dict_seasons["Winter_begin"]) and (date_today< dict_seasons["Winter_einde"])):
    progress_bar_limit = 100       
    get_current_season = "Winter"

        
with Bar("Seizoen-progress over een jaar: ") as bar:
    for i in range(progress_bar_limit):
        sleep(0.02)
        bar.next()   
        
  


#Get current day number:
today = datetime.date.today()
future = datetime.date(year_today,12,31)
diff = future - today
day_number = 365 - int(diff.days)


if get_current_season == "Lente":
    range_calc = 93
    min_value = 78
    
elif get_current_season == "Zomer":
    range_calc = 94
    min_value = 171
    
elif get_current_season == "Herst":
    range_calc = 89
    min_value = 265
    
elif get_current_season == "Winter":
    range_calc = 89
    min_value = 265

# calculating the 
correctedStartValue = day_number - min_value
percentage = (correctedStartValue * 100) / range_calc
end_value = int(round(percentage, 0))

with Bar("Seizoen-progress dit seizoen:   ") as bar:
    for i in range(end_value):
        sleep(0.02)
        bar.next()   
        
