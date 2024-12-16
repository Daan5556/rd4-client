import requests

# Base URL for the waste calendar API
base_url = "https://data.rd4.nl/api/v1/waste-calendar"


def get_waste_calendar(postal_code: str, house_number: int, year: int, types: [str] = None,
                       house_number_extension: str = None):
    """
    Fetches the waste collection calendar for a specific address and year.

    Args:
        postal_code (str): The postal code of the address.
            Example: 1234AB
        house_number (int): The house number of the address.
            Example: 42
        year (int): The year for which to fetch the waste calendar.
            Example: 2000
        types (list of str, optional): A list of waste types to filter the results. Defaults to all types
            Example: ["residual_waste", "gft", "paper", "pruning_waste", "pmd", "best_bag", "christmas_trees"]
        house_number_extension (str, optional): An optional house number extension.
            Example: "A"

    Returns:
        dict: The first item in the waste calendar data if the request is successful, otherwise None.
    """
    # Parameters for the GET request
    params = {
        "postal_code": postal_code,
        "house_number": house_number,
        "year": year,
    }
    # Add optional parameters if provided
    if types:
        params["types[]"] = types
    if house_number_extension:
        params["house_number_extension"] = house_number_extension

    # Perform the GET request
    r = requests.get(base_url, params=params)
    # Check if the request was successful
    if 200 < r.status_code <= 300:
        return None

    # Parse the JSON response
    content = r.json()
    # Check if the response indicates success
    if not content.get("success"):
        return None

    # Return the first item in the calendar data
    return content["data"]["items"][0]
