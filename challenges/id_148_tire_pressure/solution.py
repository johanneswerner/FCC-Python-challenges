CONVERSION_FACTOR = 14.5038

def tire_status(pressures_psi, range_bar):
    pressures_bar = [pressure / CONVERSION_FACTOR for pressure in pressures_psi]

    pressures_eval = []
    for element in pressures_bar:
        match element:
            case _ if element < range_bar[0]:
                pressures_eval.append("Low")
            case _ if element > range_bar[1]:
                pressures_eval.append("High")
            case _:
                pressures_eval.append("Good")

    return pressures_eval
