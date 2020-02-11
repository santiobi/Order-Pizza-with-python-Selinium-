from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time



Firstname=input("First Name:")
Lastname=input("Last Name:")
email=input("Email:")
Phone=input("Phone Number:")

Place = input("Do you want the pizza to be delivered to a House,Apartment,Business or other?")
if Place != "House" and Place != "Apartment" and Place !="Business" and Place != "Other":
    print("Incorrect Name")
    Place = input("Do you want the pizza to be delivered to a House,Apartment,Business or other?")

Delivery=input("Do you want Carryout or Delivery?")
Food=input("Type the Pizza that you want\n"
           "Ultimate Pepperoni:Two layers of pepperoni sandwiched between provolone, Parmesan-Asiago and cheese made with 100% real mozzarella then sprinkled with oregano.\n"
           "Pacific Veggie:Roasted red peppers, fresh baby spinach, fresh onions, fresh mushrooms, tomatoes, black olives, feta, provolone, cheese made with 100% real mozzarella and sprinkled with a garlic herb seasoning.\n"
           "Buffalo Chicken:Grilled chicken breast, fresh onions, provolone, American cheese, cheddar, cheese made with 100% real mozzarella and drizzled with a hot sauce.\n"
           "Honolulu Hawaiian:Sliced ham, smoked bacon, pineapple, roasted red peppers, provolone and cheese made with 100% real mozzarella.\n"
           "Wisconsin 6 Cheese:Feta, provolone, cheddar, Parmesan-Asiago, cheese made with 100% real mozzarella and sprinkled with oregano.\n"
           "Spinach & Feta:Creamy Alfredo sauce, fresh spinach, fresh onions, feta, Parmesan-Asiago, provolone and cheese made with 100% real mozzarella.\n"
           "Pizza Name:")

if Food != "Ultimate Pepperoni" and Food !="Pacific Veggie" and Food != "Buffalo Chicken" and Food != "Honolulu Hawaiian" and Food != "Wisconsin 6 Cheese" and Food !="Spinach & Feta":
    print("Incorrect Name")
    Food = input("Type the Pizza that you want\n"
                 "Ultimate Pepperoni:Two layers of pepperoni sandwiched between provolone, Parmesan-Asiago and cheese made with 100% real mozzarella then sprinkled with oregano.\n"
                 "Pacific Veggie:Roasted red peppers, fresh baby spinach, fresh onions, fresh mushrooms, tomatoes, black olives, feta, provolone, cheese made with 100% real mozzarella and sprinkled with a garlic herb seasoning.\n"
                 "Buffalo Chicken:Grilled chicken breast, fresh onions, provolone, American cheese, cheddar, cheese made with 100% real mozzarella and drizzled with a hot sauce.\n"
                 "Honolulu Hawaiian:Sliced ham, smoked bacon, pineapple, roasted red peppers, provolone and cheese made with 100% real mozzarella.\n"
                 "Wisconsin 6 Cheese:Feta, provolone, cheddar, Parmesan-Asiago, cheese made with 100% real mozzarella and sprinkled with oregano.\n"
                 "Spinach & Feta:Creamy Alfredo sauce, fresh spinach, fresh onions, feta, Parmesan-Asiago, provolone and cheese made with 100% real mozzarella.\n"
                 "Pizza Name:")


if Place == "House":
    streetadress=input("Street Address:")
    zipcode=input("Zip Code:")
    city=input("City:")

if Place == "Apartment":
    buildingname=input("Building Name:")
    streetadress=input("Street Address:")
    apartmentnumber=input("Apartment Number#:")
    zipcode=input("Zip Code:")
    city=input("City:")

if Place == "Business":
    businessname= input("Business Name:")
    streetadress = input("Street Address:")
    zipcode = input("Zip Code:")
    city = input("City:")

if Place == "Other":
    streetadress = input("Street Address:")
    unit = input("unit#:")
    zipcode = input("Zip Code:")
    city = input("City:")



driver = webdriver.Chrome(executable_path=r"C:\Users\sobig\Documents\Programacion\Python\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.dominos.com/en/pages/order/#!/locations/search/?type=Delivery")
time.sleep(2)
element = driver.find_element_by_name("Address_Type_Select")
drp = Select(element)



#Delivery Place(House, apartment, business, other)

if Place == "House":
    drp.select_by_visible_text(" House ")
    driver.find_element_by_name("Street").send_keys(streetadress)
    driver.find_element_by_id("Postal_Code_Sep").send_keys(zipcode)
    time.sleep(2)
    driver.find_element_by_id("City_Sep").send_keys(city)

if Place == "Apartment":
    drp.select_by_visible_text(" Apartment ")
    driver.find_element_by_name("Location_Name").send_keys(buildingname)
    driver.find_element_by_name("Address_Line_2").send_keys(apartmentnumber)
    driver.find_element_by_name("Street").send_keys(streetadress)
    driver.find_element_by_id("Postal_Code").send_keys(zipcode)
    driver.find_element_by_id("City").send_keys(city)


if Place == "Business":
    drp.select_by_visible_text(" Business ")
    driver.find_element_by_name("Location_Name").send_keys(businessname)
    driver.find_element_by_name("Street").send_keys(streetadress)
    driver.find_element_by_name("Postal_Code").send_keys(zipcode)
    driver.find_element_by_name("City").send_keys(city)

if Place == "Other":
    drp.select_by_visible_text(" Other ")
    driver.find_element_by_name("Street").send_keys(streetadress)
    driver.find_element_by_name("Address_Line_2").send_keys(unit)
    driver.find_element_by_name("City").send_keys(city)
    driver.find_element_by_name("Postal_Code").send_keys(zipcode)


driver.find_element_by_xpath("//*[@id='locationSearchForm']/div/div[4]/button").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='locationsResultsPage']/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/a").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='entree-Pizza']/a").click()
time.sleep(3)


if Delivery == "Delivery":
        driver.find_element_by_id("Service_Method_Delivery").click()
        time.sleep(2)

if driver.find_element_by_xpath("//*[@id='genericOverlay']/section/header/button").is_displayed() == True:
    driver.find_element_by_xpath("//*[@id='genericOverlay']/section/header/button").click()
    time.sleep(2)

if Food == "Ultimate Pepperoni":
        driver.find_element_by_xpath("//*[@id='categoryPage2']/section/div/div[9]/div/a[1]").click()
        order = "Ultimate Pepperoni"
if Food == "Pacific Veggie":
        driver.find_element_by_xpath("//*[@id='categoryPage2']/section/div/div[4]/div/a[1]").click()
        order = "Pacific Veggie"
if Food == "Buffalo Chicken":
        driver.find_element_by_xpath("//*[@id='categoryPage2']/section/div/div[8]/div/a[1]").click()
        order = "Buffalo Chicken"
if Food == "Honolulu Hawaiian":
        driver.find_element_by_xpath("//*[@id='categoryPage2']/section/div/div[5]/div/a[1]").click()
        order = "Honolulu Hawaiian"
if Food == "Wisconsin 6 Cheese":
        driver.find_element_by_xpath("//*[@id='categoryPage2']/section/div/div[11]/div/a[1]").click()
        order = "Wisconsin 6 Cheese"
if Food == "Spinach & Feta":
        driver.find_element_by_xpath("//*[@id='categoryPage2']/section/div/div[12]/div/a[1]").click()
        order = "Spinach & Feta"

time.sleep(3)
driver.find_element_by_xpath("//*[@id='js-myOrderPage']/a").click()
time.sleep(2)

driver.find_element_by_xpath("//*[@id='genericOverlay']/section/div/div[2]/div/a").click()

time.sleep(5)

if driver.find_element_by_xpath("//*[@id='js-checkoutColumns']/aside/div[3]/a").is_displayed() == True:
    driver.find_element_by_xpath("//*[@id='js-checkoutColumns']/aside/div[3]/a").click()
else:
    print("")



time.sleep(4)
driver.find_element_by_name("First_Name").send_keys(Firstname)
driver.find_element_by_name("Last_Name").send_keys(Lastname)
driver.find_element_by_name("Email").send_keys(email)
driver.find_element_by_name("Callback_Phone").send_keys(Phone)
driver.find_element_by_xpath("//*[@id='orderPaymentPage']/form/div[5]/div/div[2]/div/div[4]/label/input").click()



print("you are ordering a",order)
confirmation = input("write ok if thats what you want, if it isnt, type no\n"
                     "Answer:")
if confirmation == "ok":
    driver.find_element_by_xpath("//*[@id='orderPaymentPage']/form/div[6]/div/div[3]/button").click()
if confirmation == "no":
    print("Reset")
