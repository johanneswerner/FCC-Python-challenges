"""Solution for challenge 148: Tire Pressure Monitoring System."""

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
    pressures_bar = list(map(lambda x: x / CONVERSION_FACTOR, pressures_psi))
    return list(
        map(
            lambda x: "Low" if x < range_bar[0]
            else "High" if x > range_bar[1]
            else "Good",
            pressures_bar
        )
    )
