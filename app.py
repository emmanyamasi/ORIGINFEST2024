from flask import Flask, request, jsonify
import africastalking

app = Flask(_name_)

# Initialize Africastalking SDK
username = "Bandit0"
api_key = "atsk_ca3f9bf43cf2589c2bd916e64d43f9ed218a03a3693c250bebfda31c483922b43d3c9d34"  # Add your API key here

africastalking.initialize(username, api_key)
ussd = africastalking.USSD

@app.route('/ussd', methods=['POST'])
def ussd_menu():
    session_id = request.values.get('sessionId', None)
    service_code = request.values.get('serviceCode', None)
    phone_number = request.values.get('phoneNumber', None)
    text = request.values.get('text', None)

    text_array = text.split('*')
    user_response = text_array[-1]
    
    # Determine language choice
    if text == "":
        # Initial language selection
        response = "CON Welcome to Jamii Initiative.\n"
        response += "Choose your language:\n"
        response += "1. English\n"
        response += "2. Kiswahili"

    elif text == "1":
        # English Main Menu
        response = "CON Jamii Initiative App Services.\n"
        response += "1. Request Information/Services\n"
        response += "2. Report an Issue\n"
    
    elif text == "1*1":
        # English - Request Information
        response = "CON What information/Service do you need?\n"
        response += "1. Health\n"
        response += "2. Education\n"
        response += "3. Security"
      
    
    elif text == "1*1*1":
        # English - Health Information
        response = "CON Reach the following services For immediate Help \n"
        response += "1. Medical Centre(DeKUT) Contact-0724721258\n"
        response += "2.Ambulance(DeKUT) Contact-0743311543\n"
        response += "3. Guidance&Counselling Contact-0724721258\n"
        response += "4. St John's Ambulance Contact-0721611555\n"
        response += "5. Other (PGH) Contact-0612030819\n"

    elif text == "1*1*2":
        # English - Education Information
        response = "CON Reach the following services For immediate Help \n"
        response += "1. Academic office(DeKUT) Contact-0713123021\n"
        response += "2.Marketing Department(DeKUT) Contact-0713835965\n"
        response += "3. Huduma Centre Contact-0700000000\n"
        response += "4. County Director of Education Office Contact-0202892000\n"
        response += "5. Other (Chief Bomas) Contact-0745534323\n"

    elif text == "1*1*3":
        # English - Security Information
        response = "CON Reach the following services For immediate Help \n"
        response += "1. Security Office(DeKUT) Contact-0756455343\n"
        response += "2.Kabiruini Police Station Contact-0788765645\n"
        response += "3. Other (Security Guards) Contact-0798765434\n"
    
    elif text == "1*2":
        # English - Report an Issue
        response = "CON What issue are you reporting?\n"
        response += "1. Road Damage\n"
        response += "2. Water Outage\n"
        response += "3. Power Outage\n"
        response += "4. Hostel Management\n"
    
    elif text == "1*2*1":
        # English - Report Road Damage
        response = "Report to KENHA(Nyeri) Contact-0765453423.THANK YOU FOR USING JAMIII INITIATIVE."
    
    elif text == "1*2*2":
        # English - Report Water Outage
        response = "Report to NYEWASCO(Nyeri) Contact-0756453423.THANK YOU FOR USING JAMIII INITIATIVE."
    
    elif text == "1*2*3":
        # English - Report Power Damage
        response = "Report to KPLC(Nyeri) Contact-0790876545.THANK YOU FOR USING JAMIII INITIATIVE."
    
    elif text == "1*2*4":
        # English - Report Hostel Management
        response = "Report to DEKUTSO Contact-0720445672.THANK YOU FOR USING JAMIII INITIATIVE."
    # Kiswahili Language Flow
    elif text == "2":
        # Kiswahili Main Menu
        response = "CON Karibu kwenye Jamii Initiative.\n"
        response += "1. Omba Taarifa/Huduma\n"
        response += "2. Ripoti Tatizo\n"
       
    elif text == "2*1":
        # Kiswahili - Request Information
        response = "CON Unahitaji taarifa gani?\n"
        response += "1. Afya\n"
        response += "2. Elimu\n"
        response += "3. Usalama"
      
    
    elif text == "2*1*1":
        # Kiswahili - Health Information
        response = "CON Fikia huduma zifuatazo kwa msaada wa haraka \n"
        response += "1. Kituo cha Tiba(DeKUT) Mawasiliano-0724721258\n"
        response += "2. Ambulance(DeKUT) Mawasiliano-07433115432\n"
        response += "2.Marketing Department(DeKUT) Contact-0713835965\n"
        response += "3. Msaada na Ushauri Mawasiliano-0724721258\n"
        response += "4. St John's Ambulance Mawasiliano-0721611555\n"
        response += "5. Nyingine (PGH) Mawasiliano-0612030819\n"

    elif text == "2*1*2":
        # Kiswahili - Education Information
        response = "CON Fikia huduma zifuatazo kwa msaada wa haraka \n"
        response += "1. Ofisi ya Masomo(DeKUT) Mawasiliano-0713123021\n"
        response += "2. Idara ya Masoko(DeKUT) Mawasiliano-0713835965\n"
        response += "3. Huduma Centre Mawasiliano-0700000000\n"
        response += "4. Ofisi ya Mkurugenzi wa Elimu wa Kaunti Mawasiliano-0202892000\n"
        response += "5. Nyingine (Ofisi ya Mjumbe) Mawasiliano-0723435445\n"

    elif text == "2*1*3":
        # Kiswahili - Security Information
        response = "CON Fikia huduma zifuatazo kwa msaada wa haraka \n"
        response += "1. Ofisi ya Usalama(DeKUT) Mawasiliano-0723432322\n"
        response += "2. Kituo cha Polisi Kabiruini Mawasiliano-0764345423\n"
        response += "3. Nyingine (Walinzi wa Usalama) Mawasiliano-0788665544\n"
    
    
    elif text == "2*2":
        # Kiswahili - Report an Issue
        response = "CON Tatizo gani unaripoti?\n"
        response += "1. Uharibifu wa Barabara\n"
        response += "2. Ugavi wa Maji\n"
        response += "3. Kukatika kwa Umeme\n"
        response += "4. Nyingine"
    
   
      # Kiswahili - Report Road Damage
    elif text == "2*2*1":
        response = "END Ripoti kwa KENHA (Nyeri)-0765453423.ASANTE KWA KUTUMIA JAMII INIATIVE."
    elif text == "2*2*2":
        response = "END Ripoti kwa NYEWASCO (Nyeri)-0756453423.ASANTE KWA KUTUMIA JAMII INIATIVE."
    elif text == "2*2*3":
        response = "END Ripoti kwa KPLC (Nyeri)-0790875545.ASANTE KWA KUTUMIA JAMII INIATIVE."
    elif text == "2*2*4":
        response = "END Ripoti kwa DEKUTSO-0720445672.ASANTE KWA KUTUMIA JAMII INIATIVE."
    
    elif text == "2*3":
        # Kiswahili - Request a Service
        response = "CON Unahitaji huduma gani?\n"
        response += "1. Huduma za Afya\n"
        response += "2. Msaada wa Kielimu\n"
        response += "3. Nyingine"
    
    elif text == "2*3*1":
        # Kiswahili - Request Health Service
        response = "END Ombi lako la huduma za afya limepokelewa. Tutawasiliana nawe hivi karibuni.ASANTE KWA KUTUMIA JAMII INIATIVE."
    
    else:
        # Invalid option handling
        response = "END Invalid option selected. Please try again."

    return response

if _name_ == '_main_':
    app.run(debug=True, port=5000)
