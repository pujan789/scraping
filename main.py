# import statements
import csv
import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

# Class scraper
class Scraper():
    def __init__(self,link):
        self.link = link
        self.page_html = requests.get(link)
        self.soup = BeautifulSoup(self.page_html.text, 'html.parser')
    def get_price(self):
        return self.soup.find(class_="notranslate").text.replace("										","").replace("\n","").replace("$","").replace(".00","")

    def get_title(self):
        title = self.soup.select_one(selector="#itemTitle").text
        orignal_title = self.soup.select_one(selector="#itemTitle .g-hdn").text
        new_title = title.replace(orignal_title,"")
        return new_title

    def get_ITEM_DETAIL_SPECIFIES(self):
        list_of_details = []
        for i in range(len(self.soup.select(selector=".ux-labels-values__labels-content"))):
            list_of_details.append(self.soup.select(selector=".ux-labels-values__labels-content")[i].text)
            list_of_details.append(self.soup.select(selector=".ux-labels-values__values")[i].text)
        return list_of_details

    def get_DESCRIPTION(self):
        self.path = 'chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=self.path)
        self.driver.get(self.link)
        description_written = []
        time.sleep(2)
        iframe = self.driver.find_element(By.ID, "desc_ifr")
        self.driver.switch_to.frame(iframe)
        text = self.driver.find_elements(By.CSS_SELECTOR, "#ds_div div")
        change = False
        # print(text)
        if text == []:
            new_text = self.driver.find_elements(By.CSS_SELECTOR, "#ds_div font b")
            for a in new_text:
                description_written.append(a.text)
        else:
            for i in text:
                description_written.append(i.text)
                if description_written == []:
                    change = True
                    description_written = []


        return description_written



    def get_all(self):
        new_list = []
        new_list.append(self.get_title())
        new_list.append(self.link)
        new_list.append(self.get_price())
        new_list.append(self.get_ITEM_DETAIL_SPECIFIES())
        new_list.append(self.get_DESCRIPTION())
        self.driver.quit()
        return new_list


def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1


# Driver code
# s = ['Geeks', 'for', 'Geeks']
# print(listToString(s))

# CONSTANTS
ADD = 0
COUNT = 0
FILE_NAME_COUNT = 1
DATA = [['1934 Ford convertible/hardtop', 'https://www.ebay.com/itm/325349974084?hash=item4bc05ea044:g:w0wAAOSwzqJjKcDv', 'US 25,300', ['Condition:', 'New', 'Year:', '1934', 'VIN (Vehicle Identification Number):', '775379200172048', 'Mileage:', '55', 'Options:', 'Convertible', 'Interior Color:', 'purple', 'Sub Model:', 'custom', 'Body Type:', 'Convertible', 'Number of Cylinders:', '8', 'Transmission:', 'Automatic', 'Make:', 'Ford', 'Drive Type:', 'RWD', 'Fuel Type:', 'Gasoline', 'For Sale By:', 'Private Seller', 'Drive Side:', 'Left-hand drive', 'Exterior Color:', 'Gold', 'Model:', 'convertible/hardtop', 'Power Options:', 'Air Conditioning, Power Locks', 'Vehicle Title:', 'Rebuilt, Rebuildable & Reconstructed', 'Engine:', '454'], ['1934 Ford Coupe/Convertible /removable vinyltop/new\nNew interior\nClear NC title\nOver 8 years building from ground up includingcustom chassis, cab, and all body and fiberglass work\nCustom tubular frame and fiberglass body\nCustom one-off interior with high back racingvinyl seats, new matching carpet\n454 full race cam engine - 2 Eldebrock 650carbs (new carbs)\nCam andLifters, Hydraulic Flat Tappet, Advertised Duration 268/280, Lift .515/.520,Chevy, Big Block, \nAluminum intake/new\n700R4 reconditioned Trans\n9” Ford Rear   3:73 gears\n4 link rear suspension with coil\\over shocksat all 4 wheels\nJust painted this fall $10,000 paint job andbody work only\nOne year onlyMustang Sunburst Gold Metallic three stage paint with 4 coats of clear\nCustom from one end to end\na/c']],
['1979 Ford Granada', 'https://www.ebay.com/itm/255756737572?hash=item3b8c4a1c24:g:JQgAAOSwNIljLzbH', 'US 6,700', ['Condition:', 'Used', 'Year:', '1979', 'Mileage:', '43000', 'Model:', 'Granada', 'Vehicle Title:', 'Clean', 'Number of Cylinders:', '8', 'Make:', 'Ford', 'Body Type:', 'Coupe'], ['THIS GRANADA IS A RUST ROT FREE CAR , HAS THE ORIGINAL PAINT NEVER BEEN REPAINTED,NEVER HAVE ANY RUST REPAIR OR PATCH PANELS PUT IN IT,CAR HAS A 302 MOTOR THAT RUNS AND SOUNDS GREAT WITH NEW DUEL EXHAUST,NEW INTAKE WITH HOLLY 4 BARREL ON IT, LOTS OF NEW EXTRAS ON MOTOR, TIRES ARE NEW AND THEY ARE ON A NICE SET OF OLD SCHOOL CRAGER WHEELS, INSIDES ARE ALL ORIGINAL, THESE CARS ARE HARD TO FINE INTHIS  ORIGINAL SHAPE, THIS VEHICLE IS 43 YEARS OLD NOT A SH', 'O', 'W CAR BUT A GREAT DRIVER, ']],
['1932 Ford Model B', 'https://www.ebay.com/itm/195362367470?hash=item2d7c8127ee:g:KiYAAOSwxqZjJmrs', 'US 25,000', ['Condition:', 'Used', 'Year:', '1932', 'Mileage:', '1200', 'Interior Color:', 'Gray', 'Body Type:', 'Coupe', 'Number of Cylinders:', '8', 'Transmission:', 'Automatic', 'Make:', 'Ford', 'Drive Type:', 'RWD', 'Fuel Type:', 'Gasoline', 'For Sale By:', 'Private Seller', 'Drive Side:', 'Left-hand drive', 'Model:', 'Model B', 'Exterior Color:', 'Red', 'Power Options:', 'Power Windows', 'Vehicle Title:', 'Clean', 'Engine:', '350 SBC'], ['1932 FORD MODEL “B” 3-WINDOW COUPE\nFor sale only no trades\nENGINE:  SBC 350, 4 boldmains, 202 camel hump heads, comp cam, Holley 650 4 bbl, Wiend manifold, aluminum  radiator with Moon tank recovery, electric cooling fan, Sanderson ceramiccoated headers, polished aluminum fined valve covers, air cleaner and chromeOil pan.   I have a 6-duce setup (Holly carbs, dragstarmanifold, linkages, and fuel distribution block) ready to install that goeswith car.  Many misc extra parts.\n TRANSMISISON:  GM 700R4,Bowler shift kit, overdrive lockup, transmission fluid cooler, Lokkar shifterand chrome pan.\n DIFFERENTIAL:  Ford 9”, 355 reargear posi-traction unit.\n SUSPENSION: \n Front:  Lucky 7 straight axel with hairpins, spring,steering linkage, and heavy-duty shocks all\n             chrome plated.\n Rear: Triangulated 4 bar with Viking adjustable coil over shocks, all polished  stainless steel.\n BRAKES:  Power, four-wheeldisc, GM SS calipers, stainless steel braded brake lines, under floor frame  \n                 mounted brake pedal with mastercylinder and chrome dual diaphragm booster\n CHASSIS:  JW Rod Garage ‘32Ford perimeter chassis, tubular cross members and incorporating mounts\n                 for steering, engine,rear differential, and headlight/shock brackets.\n WHEELS & TIRES:  Torque Thrustwheels front: 16” rear: 17”, tires front: P215/60R16 rear: 265/70R17.\n STEERING:  Flaming River tiltsteering column, polished stainless steel, Flaming River rack & pinion steering.\n BODY:  Davviki LTD fiberglass1932 Ford 3-window coupe body with 3” chop top.\n INTERIOR: Work in progress.\n EXTERIOR:  Body and framecolor is blood red.  Pinstriping byGeorge Berenyi\n ELECTRIAL:  Power windows,tinted glass, Vintage Air heat a/c (not installed), Dolphin gauges with GPSspeedometer and Ididit wiring kit.          ', 'ENGINE:  SBC 350, 4 boldmains, 202 camel hump heads, comp cam, Holley 650 4 bbl, Wiend manifold, aluminum  radiator with Moon tank recovery, electric cooling fan, Sanderson ceramiccoated headers, polished aluminum fined valve covers, air cleaner and chromeOil pan.   I have a 6-duce setup (Holly carbs, dragstarmanifold, linkages, and fuel distribution block) ready to install that goeswith car.  Many misc extra parts.\n TRANSMISISON:  GM 700R4,Bowler shift kit, overdrive lockup, transmission fluid cooler, Lokkar shifterand chrome pan.', '', '', '', '', '', '', '', '', '', '', '', '', '', '']],
['1940 Ford Deluxe', 'https://www.ebay.com/itm/255731335105?hash=item3b8ac67fc1:g:gfsAAOSwNfxjJeWc', 'US 29,500', ['Condition:', 'Used', 'Seller Notes:', '“This is a new frame off restoration There is NO Warranty on this Car”', 'Year:', '1940', 'VIN (Vehicle Identification Number):', '185267992', 'Mileage:', '100', 'Options:', 'Convertible', 'Body Type:', 'Convertible', 'Number of Cylinders:', '8', 'Model:', 'Deluxe', 'Make:', 'Ford', 'Drive Type:', 'RWD', 'Vehicle Title:', 'Clean', 'Fuel Type:', 'Gasoline'], ['This is a Frame off restoration just completed  with just a few miles on the car.I have priced the car at 10 t0 15,000 dollars below value for a fast sell.There is very few test miles on the 40 so It will need some TLC.The following is a list of all the new parts on the car.', '', '', 'Chevy crate motor 350/ 265 hp', 'Holly Sniper EFI with Hyper Spark Distributor (MSD Distributor)', 'complete front end 2 inch doped Axel', 'Walker Radiator', ' ', 'Paint (car was stripped to bare metal) Color is Cloud mist grey a original color Frame was sandblasted', ' All new glass (passenger side has crack)', 'Folding top no power', 'Rebuilt Nova rear end with new 350 gears all new brake parts', 'New Tires and Rime', 'Tilt steering column', 'Dolphin gauges', 'Door handles and window handles', 'E Z Wiring', 'Rear tail lights', 'Re chrome bumpers', 'Quarter belt line moldings  All others were polished', 'New interior with original seats', '', 'Contact Jim Walker 915-633-1489 Home 915-740-3628 cell I will answer Text messages', '', 'Note: 40 Fords are difficult to Aline body panels I had to shim the front end 3/4 inch to get the Hood to Aline properly', 'Some of the body panels will need some work. I have tried to describe the car honestly call with questions.', '', '350 Transmission that I bought used Do not   know much about it', '', 'I have priced car for Quick Sale']],
['1939 Ford Other Deluxe Coupe', 'https://www.ebay.com/itm/304635182565?hash=item46edabfde5:g:62cAAOSwM4FjFlKw', 'US 4,950', ['Condition:', 'Used', 'Year:', '1939', 'VIN (Vehicle Identification Number):', '5040928', 'Mileage:', '36601', 'Body Type:', 'Coupe', 'Warranty:', 'Vehicle does NOT have an existing warranty', 'Trim:', 'Deluxe Coupe', 'Number of Cylinders:', '8', 'Transmission:', 'Manual', 'Model:', 'Other', 'Make:', 'Ford', 'Drive Type:', 'RWD', 'Vehicle Title:', 'Clean', 'Fuel Type:', 'Gasoline'], ['Car\nThe car is a 1939 Ford Deluxe Coupe with a 112 inch wheel base.  The engine is a 1948-53 8BA. This engine has no miles on it and was rebuilt approximately 25 years ago. It has fresh oil and oil filter but needs 1 water pump. It has 1949 Plymouth front and rear bumpers. The rest of the car is stock.  The engine runs perfectly and will drive onto a trailer but the brakes do not work. Please look at all photographs carefully. Clear title.\n\nSpare Parts\nSpare parts include the following:  hub caps, 1940 front brake hubs and drums, windshield assembly, steering box, stainless trim, steering column, hood and trunk hinges, door handles, regulator, relay, thermostat, emergency brake cable, battery box, wiring harness, oil filter, rear window seal, windshield regulator, motor mounts, fuel line, original instrument cluster, fuel tank, speedometer cable, master cylinder, 4 brake lines, 4 wheel cylinders, front wheel bearings races and seals, shop manuals, repair manuals, parts lists, technical manuals, reproduction parts catalogs, 1940 front axle assembly, 1940 rear axle assembly.  Plus, whatever else is in the photographs. Again, please look carefully at all photographs.\n\nThe car is titled in Florida in my name and is sold as-is.    The car, spare parts and title will be released once payment has cleared. Please do not place a bid unless you plan to complete the transaction if you are the high bidder at the end of the auction. If you’re paying with cash the funds will be paid at my local bank due to counterfeit concerns.   Final payment can also be wired. The vehicle needs to be picked up within 30 days of auction completion.', '', 'Car\nThe car is a 1939 Ford Deluxe Coupe with a 112 inch wheel base.  The engine is a 1948-53 8BA. This engine has no miles on it and was rebuilt approximately 25 years ago. It has fresh oil and oil filter but needs 1 water pump. It has 1949 Plymouth front and rear bumpers. The rest of the car is stock.  The engine runs perfectly and will drive onto a trailer but the brakes do not work. Please look at all photographs carefully. Clear title.\n\nSpare Parts\nSpare parts include the following:  hub caps, 1940 front brake hubs and drums, windshield assembly, steering box, stainless trim, steering column, hood and trunk hinges, door handles, regulator, relay, thermostat, emergency brake cable, battery box, wiring harness, oil filter, rear window seal, windshield regulator, motor mounts, fuel line, original instrument cluster, fuel tank, speedometer cable, master cylinder, 4 brake lines, 4 wheel cylinders, front wheel bearings races and seals, shop manuals, repair manuals, parts lists, technical manuals, reproduction parts catalogs, 1940 front axle assembly, 1940 rear axle assembly.  Plus, whatever else is in the photographs. Again, please look carefully at all photographs.\n\nThe car is titled in Florida in my name and is sold as-is.    The car, spare parts and title will be released once payment has cleared. Please do not place a bid unless you plan to complete the transaction if you are the high bidder at the end of the auction. If you’re paying with cash the funds will be paid at my local bank due to counterfeit concerns.   Final payment can also be wired. The vehicle needs to be picked up within 30 days of auction completion.']],
['1940 Ford Deluxe', 'https://www.ebay.com/itm/325290191870?hash=item4bbcce6bfe:g:jA0AAOSwoidiaGxC', 'US 30,000', ['Condition:', 'Used', 'Year:', '1940', 'VIN (Vehicle Identification Number):', '00000000000000000', 'Mileage:', '16300', 'Options:', 'CD Player, Leather Seats', 'Body Type:', 'PANEL', 'Number of Cylinders:', '8', 'Transmission:', 'Automatic', 'Model:', 'Deluxe', 'Make:', 'Ford', 'Drive Type:', 'FWD', 'Vehicle Title:', 'Clean', 'Fuel Type:', 'Gasoline'], ['********* OFFERED AT NO RESERVE *************  TAKE A LOOK AT THE VIDS..... ***** VIN PLATE WAS LOST AND NOW FOUND AND REMOUNTED ON  FIRE WALL. LAST PHOTO!!!!  ********\nhttps://youtu.be/XQWfvDssOJM  (https://youtu.be/MmPSwgLdg1o)))   WE CAN PROUDLY SAY THIS IS AN AWARD WINNER. WE HAD GONE TO AN LOCAL CAR SHOW AND CAME HOME WITH A TROPHY IN OUR CLASS. 1935-1945. AWARD GOES WITH NEW OWNER. THIS IS ONE OF THE BEST ALL STEEL BODY 1940 FORD PANEL DELIVERY THAT YOU WILL COME ACROSS. ABSOLUTELY RUST FREE. ALWAYS KEPT INSIDE. PHOTOS DO NOT DO THIS JUSTICE. HAS A MUSTANG II FRONT SUSPENSION, POWER WINDOWS, DRIVER AND PASSENGER POWER SEATS, POWER STEERING, FRONT POWER DISK BRAKES AND DRUMS IN REAR, WITH A GREAT WORKING COLORED BACK UP CAMERA. LET\'S NOT LEAVE OUT THAT IT HAS AN AWESOME KENWOOD STEREO AND CD PLAYER WITH HOOK UP FOR YOUR IPOD. SOUND SYSTEM THAT\'S OUT OF THIS WORLD. A/C THAT KEEPS YOU COOL DURING THE WARM DAYS AND NIGHTS. HEATER THAT KEEPS YOU COZY WARM IN FALL AND WINTER. ALL GAUGES INCLUDING GAS GAUGE WORK AS THE SHOULD. TURN SIGNALS TOO. POWERED BY A 350 V8 THAT RUNS EXCELLENT. STARTS UP EVERY TIME. THE 700R TRANSMISSION SHIFTS SMOOTH AND EFFORTLESS. GREAT, EXCELLENT LOOKING DAILY DRIVER, OR ADD YOUR BUSINESS LOGO. DRIVE ANYWHERE WITH CONFIDENCE. SITTING ON 15 INCH BF GOODRICH TIRES WITH CUSTOM CHROME AMERICAN RACING RIMS.VERY RARE TO FIND SPARE TIRE COVER. OAK WOOD FLOOR THAT IS IN GREAT CONDITION. I KNOW EVERYONE SAYS WHEN YOU DRIVE "THEIR CAR" YOU WILL GET SMILES AND THUMBS UP..... THIS IS SO SO TRUE WITH THIS PANEL. NO RATTLES OR SQUEAKS IN THIS CLASSIC. APPRAISED IN 2005 BY VINTAGE APPRAISALS SERVICE. PERFORMED BY RON DUNN. AVERAGE RETAIL IN 2005 WAS AT $55,000. APPRAISAL SUMMARY WILL BE INCLUDED WITH SALE. $500.00 NON REFUNDABLE DEPOSIT WITHIN 24 HOURS OF AUCTION SALE. ALL SHIPPING CHARGES ARE BUYER\'S RESPONSIBILITY. SOLD AS IS. NO WARRANTIES IMPLIED. Ω PLEASE LOOK AT OUR VIDEOS BELOW *** JUST CLICK THE LINK BELOW.... ASK ANY Q\'S******** FEW MORE VIDS: BELOW CHECK THEM OUT PLEASE!!!! ( (https://youtu.be/XQWfvDssOJM(https://youtu.be/MmPSwgLdg1o)))', '', '', '']]
]
LINK_TO_SCRAP = ["https://www.ebay.com/itm/325349974084?hash=item4bc05ea044:g:w0wAAOSwzqJjKcDv","https://www.ebay.com/itm/255756737572?hash=item3b8c4a1c24:g:JQgAAOSwNIljLzbH","https://www.ebay.com/itm/195362367470?hash=item2d7c8127ee:g:KiYAAOSwxqZjJmrs","https://www.ebay.com/itm/255731335105?hash=item3b8ac67fc1:g:gfsAAOSwNfxjJeWc","https://www.ebay.com/itm/304635182565?hash=item46edabfde5:g:62cAAOSwM4FjFlKw","https://www.ebay.com/itm/325290191870?hash=item4bbcce6bfe:g:jA0AAOSwoidiaGxC"]
header = ["Name","Product link","Price","Item_specifics","Description"]
entire_data = []

for link in LINK_TO_SCRAP:


    scrape = Scraper(link=link)
    data = scrape.get_all()

    # data = DATA[ADD]
    ADD += 1
    entire_description = ""
    data[4] = listToString(data[4])
    data[4] = data[4].replace("\n"," ")

    new_data_option = data[3][::2]
    actual_string = ""
    for i in range(len(new_data_option)):
            new_data_option = data[3][::2]
            new_data_values = data[3][1::2]
            str_to_append = f"{new_data_option[i]} {new_data_values[i]}, "
            actual_string += str_to_append
    data[3] = actual_string
    entire_data.append(data)

with open(file=f"output.csv", mode='w',encoding="utf-8") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    csvwriter.writerows(entire_data)








