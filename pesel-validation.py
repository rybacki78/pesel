def months(mm: str) -> tuple:
    """
    checking if month (digit 3 and 4 from entered PESEL) is correct acc. to PESEL rules
    return True, month name and month length when correct
    """

    months_31 = {
        "01": "January",
        "81": "January",
        "21": "January",
        "41": "January",
        "61": "January",
        "83": "March",
        "03": "March",
        "23": "March",
        "43": "March",
        "63": "March",
        "85": "May",
        "05": "May",
        "25": "May",
        "45": "May",
        "65": "May",
        "87": "July",
        "07": "July",
        "27": "July",
        "47": "July",
        "67": "July",
        "88": "August",
        "08": "August",
        "28": "August",
        "48": "August",
        "68": "August",
        "90": "October",
        "10": "October",
        "30": "October",
        "50": "October",
        "70": "October",
        "92": "December",
        "12": "December",
        "32": "December",
        "52": "December",
        "72": "December",
    }
    months_30 = {
        "84": "April",
        "04": "April",
        "24": "April",
        "44": "April",
        "64": "April",
        "86": "June",
        "06": "June",
        "26": "June",
        "46": "June",
        "66": "June",
        "89": "September",
        "09": "September",
        "29": "September",
        "49": "September",
        "69": "September",
        "91": "November",
        "11": "November",
        "31": "November",
        "51": "November",
        "71": "November",
    }
    months_feb = {
        "82": "February",
        "02": "February",
        "22": "February",
        "42": "February",
        "62": "February",
    }

    if mm in months_31:
        return (True, months_31[mm], "long")
    elif mm in months_30:
        return (True, months_30[mm], "short")
    elif mm in months_feb:
        return (True, months_feb[mm], "feb")
    else:
        print(f"Month number ({mm}) is not correct.")
        return (False, "", "")


# main loop
while True:
    pesel = input("\nEnter PESEL (11 digits): ")

    # checking if user enters 11 digits
    if pesel.isdigit() != True or len(pesel) != 11:
        print("It is not 11 digits.")
        continue

    year_slice = pesel[0:2]
    month_slice = pesel[2:4]
    day_slice = pesel[4:6]
    sex_slice = pesel[9:10]

    # checking month
    month_correct, month_name, month_length = months(month_slice)
    if month_correct != True:
        continue

    # converting two first digits to four-digit year
    if 81 <= int(month_slice) <= 92:
        year = 1800 + int(year_slice)
    elif 1 <= int(month_slice) <= 12:
        year = 1900 + int(year_slice)
    elif 21 <= int(month_slice) <= 32:
        year = 2000 + int(year_slice)
    elif 41 <= int(month_slice) <= 52:
        year = 2100 + int(year_slice)
    elif 61 <= int(month_slice) <= 71:
        year = 2200 + int(year_slice)

    # checking if year is leap year
    leap = 0
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        leap = 1

    # checking day digits
    days = int(day_slice)
    if days < 1 or days > 31:
        print("Month can't have less than 1 more than 31 days.")
        continue
    elif days > 30 and month_length == "short":
        print(f"{month_name} can't have more than 30 days.")
        continue
    elif days > 28 and leap == 0 and month_length == "feb":
        print(f"{month_name} in {year} had only 28 days.")
        continue

    # sex
    sex = int(sex_slice)
    if sex % 2 == 0:
        sex_name = "female"
    else:
        sex_name = "male"

    # checksum validation
    pesel_as_list = [int(i) for i in pesel]
    checksum = (
        9 * pesel_as_list[0]
        + 7 * pesel_as_list[1]
        + 3 * pesel_as_list[2]
        + 1 * pesel_as_list[3]
        + 9 * pesel_as_list[4]
        + 7 * pesel_as_list[5]
        + 3 * pesel_as_list[6]
        + 1 * pesel_as_list[7]
        + 9 * pesel_as_list[8]
        + 7 * pesel_as_list[9]
    )
    if checksum % 10 != pesel_as_list[10]:
        print("PESEL is not valid.")
        continue

    print("PESEL is valid.")
    print(f"Belongs to {sex_name} born on {days} {month_name} {year}.")
