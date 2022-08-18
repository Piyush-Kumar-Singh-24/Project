import phonenumbers
from phonenumbers import carrier ,geocoder ,timezone

mobileno= input("Enter mobile number with country code: ")
mobileno= phonenumbers.parse(mobileno)

timezone = print(timezone.time_zones_for_number(mobileno))

geocoder = print(geocoder.description_for_number(mobileno,"en"))

print("Valid mobile number : ",phonenumbers.is_valid_number(mobileno))
print("Checking possibility of number : ",phonenumbers.is_possible_number(mobileno))
