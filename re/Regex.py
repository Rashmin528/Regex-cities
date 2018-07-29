import re

Major_cities = ["500003", # Hyderabad, Andhra Pradesh 
                 "791111", # Itanagar, Arunachal Pradesh  
                 "781001", # Assam, Dispur
                 "803211", # Bihar, Patna
                 "490042", # Raipur, Chhattisgarh  
                 "403001", # panaji, Goa
                 "382007", # Gandhinagar, Gujurat
                 "133301", # Chandigarh, Haryana
                 "171210", # Shimla, Himachal Pradesh
                 "180001", # Jammu and Kashmir,Srinagar and Jammu
                 "834001", # Ranchi, Jharkhand
                 "560008", # Bengaluru, Karnataka
                 "605036", # Thiruvananthapuram, Kerala
                 "462001", # Bhopal, Madhya Pradesh
                 "400011", # Mumbai, Maharashtra
                 "795001", # Imphal, Manipur
                 "793001", # Shillong, Meghalaya
                 "796001", # Aizawl, Mizoram
	       	 "797001", # Kohima, Nagaland
		 "750019", # Bhubaneswar, Odisha
		 "133301", # Chandigarh, Punjab
		 "302001", # Jaipur, Rajasthan
		 "737101", # Gangtok, Sikkim
		 "600003", # Chennai, Tamil Nadu
		 "500003", # Telangana, Hyderabad
		 "799001", # Agartala, Tripura
		 "226001", # Lucknow, Uttar Pradesh
		 "248001", # Dehradun, Uttarakhand
		 "700028", # Kolkata, West Bengal
		 "110012", # Delhi
		 "605001", # Pondicherry
		 "50T0P4", # Not Valid
		 "680GR1", # Not  Valid 
                ]


for PIN in Major_cities:
    a = re.search(r"\d{4}|\d{6}", PIN)

    if a:
        print(PIN + " matched!")
    else:
        print(PIN + " is not valid PIN !")

#python3 Regex.py
