CONVERSION_FACTOR = 14.5038

def tire_status(pressures_psi: list, range_bar: list) -> list:
    """Check the pressure status of the tires.

    The function returns a list of strings indicating the pressure status of each tire.
    `pressures_psi` is a list of tire pressures in psi. `range_bar` is a list of two
    floats indicating the minimum and maximum pressure levels for each tire. The
    function converts the pressures to bar and checks if each pressure is within the
    specified range.

        Args:
            pressures_psi (list): A list of tire pressures in psi.
            range_bar (list): A list of two floats indicating the minimum and maximum
                pressure levels for each tire.

        Returns:
            A list of strings indicating the pressure status of each tire.
        """
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
