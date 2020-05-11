import  os

def counting(hours, evening, wday, laplus, superv, date):

    
    # Tarvittavat string muutetaan int
    hours_flo = float(hours)
    evening_flo = float(evening)
    laplus_flo = float(laplus)

    # Lasketaan palkka per asia
    # perustunnit, if lausella vähennetään ruokatauko
    if hours_flo > 7:
        hours_flo = hours_flo - 0.5
    hours_sal = hours_flo * 12.09

    # iltalisä
    evening_sal = evening_flo * 5.35

    # lauantailisä
    laplus_sal = laplus_flo * 4.1

    # sunnuntailisä jos työpäivä on su
    suplus_sal = 0
    if wday == "su":
        suplus_sal = hours_flo * 12.09
        #ruokataukoa ei tarvitse tässähuomioida, su ei ruokataukoja
    
    # vastuulisä
    if superv == "y":
        superv_sal = hours_flo * 1
    else:
        superv_sal = 0

    # palkka yhteensä
    sal_is = round(float(hours_sal) + float(evening_sal) + float(laplus_sal) + float(suplus_sal) + float(superv_sal), 1)

    

    return sal_is