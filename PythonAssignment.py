print("            Python Assignment - 1")
print("Yashasvi Dutt sharma \n SAP ID - 500123200 \n BATCH - 52")
print("\n\n Do You Want a car ?\n")
doyouwantacar = input("Yes Or NO : ")
if "Yes" in doyouwantacar:
    while "Yes" in doyouwantacar:
    
        budget = int(input("Enter Your Budget \n 20 Lakhs OR 50 Lakhs OR 1 CRORE : "))
        if budget <= 20 and budget >=10 :
            print("What Type Of Car Do You want under 20 Lakhs ? \n 1.SUV   2.HATCHBACK   3.SEDAN")
            typecartwenty = input()
            if "Hatchback" in typecartwenty:
                print("This Is The List of TOP Rated Available Hatchback Cars in India Under 20 Lakhs \n 1. Citroen eC3 - Rs. N/A\n 2. Maruti Baleno - Rs. 6.66 - 9.88 Lakh\n 3. Hyundai i20 - Rs. 7.04 - 11.21 Lakh\n 4. Toyota Glanza - Rs. 6.86 - 10.00 Lakh")
            elif "SUV" in typecartwenty:
                print("This Is The List of TOP Rated Available SUV Cars in India Under 20 Lakhs \n 1. Hyundai Creta N Line - Rs. 16.82 - 20.45 Lakh\n 2. Tata Harrier - Rs. 15.49 - 26.44 Lakh\n 3. Tata Safari - Rs. 16.19 - 27.34 Lakh\n 4. MG Hector Plus - Rs. 17.00 Lakh")
            else:
                print("This Is The List of TOP Rated Available SEDAN Cars in India Under 20 Lakhs \n 1. Honda City Hybrid eHEV - Rs. 18.99 - 20.49 Lakh\n 2. Hyundai Verna - Rs. 11.00 - 17.42 Lakh\n 3. Volkswagen Virtus - Rs. 11.56 - 19.41 Lakh\n 4. Skoda Slavia - Rs. 11.53 - 19.13 Lakh")
        elif budget <=50 and budget>=20:
            print("What Type Of Car Do You want under 50 Lakhs ? \n SUV   HATCHBACK   SEDAN")
            typecarfifty = input()
            if "Hatchback" in typecarfifty:
             print("This Is The List of TOP Rated Available Hatchback Cars in India Under 50 Lakhs \n 1. MINI Cooper - Rs. 41.95 - 42.53 Lakh\n 2. MINI Countryman - Rs. 47.75 - 49.00 Lakh\n 3. MINI Cooper SE - Rs. 53.00 - 55.00 Lakh\n")
            elif "SUV" in typecarfifty:
                print("This Is The List of TOP Rated Available SUV Cars in India Under 50 Lakhs \n 1. Toyota Fortuner - Rs. 33.43 - 51.44 Lakh\n 2. MG Gloster - Rs. 37.50 - 43 Lakh\n 3. BMW X1 - Rs. 49.50 - 52.50 Lakh\n 4. Audi Q3 - Rs. 43.81 - 53.17 Lakh")
            else:
                print("This Is The List of TOP Rated Available SEDAN Cars in India Under 50 Lakhs \n 1. BMW 2 Series - Rs. 43.90 - 46.90 Lakh\n 2. Mercedes-Benz A-Class Limousine - Rs. 43.80 - 46.30 Lakh\n 3. Audi A4 - Rs. 45.34 - 53.50 Lakh\n 4. Toyota Camry - Rs. 46.17 Lakh")
        elif budget <=100 or budget>=1:
            print("What Type Of Car Do You want under 1 Crore ? \n SUV   HATCHBACK   SEDAN")
            typecarcrore = input()
            if "Hatchback"in typecarcrore:
                    print("This Is The List of TOP Rated Available Hatchback Cars in India Under 1 Crore \n 1. Mercedes-Benz AMG A 45 S - 93.40 Lakh\n 2. Mercedes-Benz AMG GLE Coupe - 1.05 Cr")
            elif "SUV" in typecarcrore:
                    print("This Is The List of TOP Rated Available SUV Cars in India Under 1 Crore \n 1. Range Rover Velar Price - Rs. 87.90 Lakh\n 2. Land Rover Defender - Rs. 93.55 Lakh - 2.30 crore\n 3. Volvo XC90 - Rs. 1.01 crore\n 4. Jaguar F-Pace - Rs. 72.90 Lakh")
            else:
                    print("This Is The List of TOP Rated Available SEDAN Cars in India Under 1 Crore \n 1. BMW 6 Series - Rs. 73.50 - 76.90 Lakh\n 2. Volvo S90 - Rs. 68.25 Lakh\n 3. Maserati Ghibli - 1.15 - 1.93 Cr\n 4. Audi A8 L - Rs. 1.34 - 1.63 Cr")
        doyouwantacar = input("Yes Or NO : ")
else :
    print("Thank You ! ")