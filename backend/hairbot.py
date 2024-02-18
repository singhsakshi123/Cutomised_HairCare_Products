import random
import nltk

def chatbot_response(user_input):
    user_input = user_input.lower()

    # Greetings
    if any(greeting in user_input for greeting in ["hi", "hello", "hey"]):
        return random.choice(["Hi there!", "Hello!", "Hey! How can I help you today?"])

    # Developer information
    elif "who developed you" in user_input:
        return "I was developed by HairVise."

    # How are you
    elif "how are you" in user_input:
        return "I'm just a computer program, so I don't have feelings, but thanks for asking!"
    
    # Hair care tips
    elif "share few hair care tips" in user_input:
        return """Certainly! Here are some hair care tips to help you maintain healthy and beautiful hair:

        1. Regular Washing: Wash your hair regularly to keep it clean, free from dirt, oil, and product buildup. Use a mild shampoo suitable for your hair type and scalp condition.

        2. Conditioning: Condition your hair after every wash to keep it moisturized, smooth, and manageable. Use a conditioner that matches your hair type and focus on the ends where hair tends to be drier.

        3. Avoid Hot Water: Rinse your hair with lukewarm or cool water instead of hot water, as hot water can strip away natural oils and leave your hair dry and brittle.

        4. Limit Heat Styling: Minimize the use of heat styling tools such as flat irons, curling irons, and blow dryers, as excessive heat can damage the hair cuticle and lead to breakage. When using heat styling tools, always apply a heat protectant spray first.

        5. Protect from Sun: Protect your hair from the sun's harmful UV rays by wearing a hat or using a hair product with UV protection when spending time outdoors for extended periods.

        6. Trim Regularly: Get regular trims every 6-8 weeks to remove split ends and prevent further damage. This helps maintain the health and appearance of your hair.

        7. Be Gentle: Handle your hair gently, especially when wet, as it is more susceptible to breakage and damage. Avoid brushing or combing wet hair and use a wide-toothed comb to detangle.

        8. Healthy Diet: Eat a balanced diet rich in vitamins, minerals, and protein to nourish your hair from the inside out. Foods like eggs, fish, nuts, fruits, and vegetables promote healthy hair growth.

        9. Hydration: Drink plenty of water to keep your body and hair hydrated. Dehydration can lead to dry, brittle hair, so aim to drink at least 8 glasses of water a day.

        10. Avoid Overwashing: While it's important to keep your hair clean, overwashing can strip away natural oils and lead to dryness and irritation. Wash your hair 2-3 times a week, or as needed based on your hair type and activity level.

        By following these hair care tips, you can keep your hair healthy, strong, and beautiful."""
    
    # Home remedies
    elif "share few home remedies for hair care" in user_input:
        return """ Certainly! Here are some effective home remedies for hair care:

        1. Coconut Oil Massage: Coconut oil is rich in fatty acids that nourish the hair and scalp. Massage warm coconut oil into your scalp and hair, leave it on for at least 30 minutes or overnight, then wash it out with shampoo. This helps moisturize the scalp, reduce protein loss from the hair, and promote healthy hair growth.

        2. Egg Mask: Eggs are packed with protein, vitamins, and minerals that can strengthen hair and promote growth. Beat one or two eggs and apply the mixture to your hair and scalp. Leave it on for about 20 minutes, then rinse with cool water and shampoo. This helps repair damaged hair, add shine, and improve texture.

        3. Yogurt and Honey Mask: Mix plain yogurt and honey in equal parts and apply it to damp hair. Leave it on for 20-30 minutes, then rinse thoroughly with lukewarm water. Yogurt helps moisturize the hair while honey adds shine and softness. This mask also helps soothe the scalp and reduce dandruff.

        4. Avocado Hair Mask: Mash a ripe avocado and mix it with a tablespoon of olive oil or coconut oil. Apply the mixture to your hair, focusing on the ends, and leave it on for 30-60 minutes before rinsing with shampoo. Avocado is rich in vitamins and antioxidants that nourish and hydrate the hair, making it soft and shiny.

        5. Aloe Vera Gel: Apply fresh aloe vera gel directly to your scalp and hair and leave it on for 30 minutes to an hour before rinsing with water. Aloe vera has moisturizing and soothing properties that can help reduce scalp irritation, promote hair growth, and add shine to the hair.

        6. Apple Cider Vinegar Rinse: Mix equal parts of apple cider vinegar and water and use it as a final rinse after shampooing. This helps remove buildup, balance the pH of the scalp, and add shine to the hair. Be sure to dilute the vinegar with water to avoid irritation.

        7. Green Tea Rinse: Brew green tea and let it cool to room temperature. Use it as a final rinse after shampooing to strengthen the hair, reduce shedding, and promote healthy hair growth. Green tea is rich in antioxidants and vitamins that nourish the hair follicles.

        8. Onion Juice Treatment: Blend an onion and extract the juice. Apply the onion juice to your scalp and leave it on for 30-60 minutes before rinsing with water and shampoo. Onion juice contains sulfur, which can improve blood circulation to the scalp, stimulate hair follicles, and promote hair growth.

        These home remedies can help nourish, strengthen, and improve the overall health of your hair. However, if you have any scalp conditions or allergies, it's best to consult with a dermatologist before trying these remedies.
        """

    # Hair care product details
    # Aloe Vera Gel
    elif "details about aloe vera gel" in user_input:
        return """ Aloe Vera Gel:
        - Aloe vera gel is a natural gel-like substance extracted from the leaves of the aloe vera plant.
        - Benefits for hair: Aloe vera gel is moisturizing and soothing for the scalp, helping to reduce itching and irritation.
        It also contains enzymes that promote healthy hair growth, strengthen hair strands, and add shine to the hair.
        """
    
    # Rosemary Oil
    elif "details about rosemary oil" in user_input:
        return """ Rosemary oil:
        - Rosemary oil is an essential oil extracted from the leaves of the rosemary plant (Rosmarinus officinalis).
        - Benefits for hair: Rosemary oil is known for its ability to stimulate hair growth by improving circulation to the scalp. It can help prevent hair loss, strengthen hair follicles, and promote thicker, healthier hair. Additionally, it has antimicrobial properties that may help alleviate dandruff and other scalp conditions.
        """
    
    # Rosemary Shampoo
    elif "details about rosemary shampoo" in user_input:
        return """ Rosemary shampoo:
        - Rosemary shampoo is a hair care product infused with rosemary extract or rosemary oil.
        - Benefits for hair: Similar to rosemary oil, rosemary shampoo can help stimulate hair growth, strengthen hair, and improve scalp health. It may also provide a refreshing and invigorating experience due to its natural fragrance.
        """
    
    # Biotin Gummies
    elif "details about biotin gummies" in user_input:
        return """ Biotin gummies:
        - Biotin gummies are dietary supplements containing biotin, a B-vitamin essential for hair, skin, and nail health.
        - Benefits for hair: Biotin is often touted for its role in promoting healthy hair growth. It can strengthen hair follicles, reduce hair shedding, and improve the overall condition of the hair.
        """
    
    # Hair growth serum
    elif "details about hair growth serum" in user_input:
        return """Hair growth serum:
        - Hair growth serum is a topical product designed to stimulate hair follicles and promote hair growth.
        - Benefits for hair: Hair growth serums typically contain ingredients such as minoxidil, peptides, or botanical extracts that can nourish the scalp, improve blood circulation, and encourage the growth of new hair follicles. They are often used to address hair thinning or balding.
        """
    
    # Tea tree oil
    elif "details about tea tree oil" in user_input:
        return """Tea tree oil:
        - Tea tree oil is an essential oil derived from the leaves of the tea tree (Melaleuca alternifolia).
        - Benefits for hair: Tea tree oil has antifungal and antibacterial properties that can help treat dandruff, scalp acne, and other scalp conditions. It also has a cooling sensation and can help unclog hair follicles, promoting healthy hair growth.
        """
    
    # Ketoconazole shampoo
    elif "details about ketoconazole shampoo" in user_input:
        return """Ketoconazole shampoo:
        - Ketoconazole shampoo is a medicated shampoo containing ketoconazole, an antifungal agent.
        - Benefits for hair: Ketoconazole shampoo is commonly used to treat dandruff and seborrheic dermatitis, which can contribute to hair loss if left untreated. By addressing the underlying fungal infection, ketoconazole shampoo can help improve scalp health and promote healthier hair growth.
        """
    
    # Pure black sesame oil
    elif "details about pure black sesame oil" in user_input:
        return """Pure black sesame oil:
        - Pure black sesame oil is oil extracted from black sesame seeds.
        - Benefits for hair: Black sesame oil is rich in nutrients like vitamin E, minerals, and antioxidants, which can nourish the scalp and promote hair growth. It helps to strengthen hair follicles, prevent premature graying, and improve overall hair health.
        """
    
    # Argan oil
    elif "details about argan oil" in user_input:
        return """Argan oil:
        - Argan oil is a plant oil derived from the kernels of the argan tree native to Morocco.
        - Benefits for hair: Argan oil is rich in fatty acids and vitamins A, C, and E, which moisturize the scalp, improve hair elasticity, and promote healthy hair growth. It can help repair damaged hair, reduce frizz, and add shine and softness to the hair.
        """
    
    # Dermatologist suggestion
    elif "suggest dermatologist near me" in user_input:
        location = input("Can you please specify the location where you want a dermatologist? ")
        return get_dermatologists_by_location(location)

    # Default response
    else:
        return "I'm sorry, I didn't understand that. If you have specific questions, feel free to ask!"

def get_dermatologists_by_location(location):
    # Define dermatologists data for different locations
    dermatologists_data = {
        "mumbai": [
            {"name": "Dr. Debraj Shome", "clinic": "The Esthetic Clinics, 1st Floor, Kohli Villa, Next to Shopper's Stop, S V Road, Andheri West, Mumbai - 400058", "contact": "+91-7028065165"},
            {"name": "Dr. Rinky Kapoor", "clinic": "The Esthetic Clinics, 1st Floor, Kohli Villa, Next to Shopper's Stop, S V Road, Andheri West, Mumbai - 400058", "contact": "+91-8875643219"},
            {"name": "Dr. Priya J Talageri", "clinic": "Dr. Talageri's Clinic, Linking Road, Bandra West, Mumbai - 400050", "contact": "+91-9821061039"},
            {"name": "Dr. Dhananjay Chavan", "clinic": "Rejoice Aesthetic Experts, Ground floor, Laxmi Palace, near Haveli Hotel, Gandhi Chowk, Mulund West, Mumbai - 400080", "contact": "+91-7710019973"},
            {"name": "Dr. Ruchi Amin", "clinic": "Derma Miracle Skin & Hair Transplant Clinic, M.G. Road, Ghatkopar East, Mumbai - 400077", "contact": "+91-8451094444"}
        ],
        "delhi": [
            {"name": "Dr. Simal Soin", "clinic": "Aayna Clinic, Ambawatta One, H 5/5, Ground Floor, Kalka Das Marg, Mehrauli, New Delhi - 110030", "contact": "+91-7042297304"},
            {"name": "Dr. Kavish Chouhan", "clinic": "DermaClinix - The Complete Skin & Hair Solution Center, D-9, Ground Floor, Green Park Main, New Delhi - 110016", "contact": "+91-8588827963"},
            {"name": "Dr. Pankaj Chaturvedi", "clinic": "DHI India - Delhi, S-27, Near Gurudwara, Greater Kailash 1, New Delhi - 110048", "contact": "+91-8888900900"},
            {"name": "Dr. Deepali Bhardwaj", "clinic": "Skin & Hair Clinic, D-306, Defence Colony, New Delhi - 110024", "contact": "+91-9810975706"},
            {"name": "Dr. Vivek Mehta", "clinic": "Pulastya Skin Clinic, A1/304, Safdarjung Enclave, New Delhi - 110029", "contact": "+91-9716022666"}
        ],
        "kolkata": [
            {"name": "Dr. Jayanta Bain", "clinic": "Bain Clinic, 1/4, Sarat Bose Road, Near Minto Park, Kolkata - 700020", "contact": "+91-9831518327"},
            {"name": "Dr. Anup K. Das", "clinic": "Dr. Das's Clinic, 95, Harish Mukherjee Road, Bhowanipore, Kolkata - 700025", "contact": "+91-98300 95114"},
            {"name": "Dr. Satyabrata Ganguly", "clinic": "Hair Transplant Clinic, 39A, Park Street, Kolkata - 700016", "contact": "+91-9831043350"},
            {"name": "Dr. Souvik Adhikari", "clinic": "The Hair Clinic, 174, Sarat Bose Road, Kolkata - 700029", "contact": "+91-9831277977"},
            {"name": "Dr. Prasanta Basak", "clinic": "Kolkata Hair & Skin Clinic, 163/1A, Prince Anwar Shah Road, Opp. South City Mall, Lake Gardens, Kolkata - 700045", "contact": "+91-9830120005"}
        ],
        "hyderabad": [
            {"name": "Dr. Venkata Ramana Yamani", "clinic": "HairSure Hair Transplant Center, 3rd Floor, Above SBH Bank, Opp KFC, Road No:1, Banjara Hills, Hyderabad - 500034", "contact": "+91-9030221919"},
            {"name": "Dr. Kiran Kumar A", "clinic": "Celestee Skin, Laser & Hair Clinic, Plot No. 303, Near KFC & Above Khazana Jewellery, 100 Feet Road, Ayyappa Society, Madhapur, Hyderabad - 500081", "contact": "+91-9908104374"},
            {"name": "Dr. A. Sridevi", "clinic": "Oliva Skin & Hair Clinic, 1st Floor, Above Karachi Bakery, Beside Astoria Hotel, RTC Cross Roads, Hyderabad - 500020", "contact": "+91-7207906741"},
            {"name": "Dr. Shruti Sharma", "clinic": "HairSure Hair Transplant Center, 3rd Floor, Above SBH Bank, Opp KFC, Road No:1, Banjara Hills, Hyderabad - 500034", "contact": "+91-9030221919"},
            {"name": "Dr. Srinivas Kandula", "clinic": "Dr. Srinivas Kandula's Clinic, 2nd Floor, KSR Towers, Beside Indian Oil Petrol Pump, Kukatpally, Hyderabad - 500072", "contact": "+91-9849994435"}
        ],
        "chennai": [
            {"name": "Dr. Arihant Surana", "clinic": "The Hairsmith Clinic, 55, TTK Road, Alwarpet, Chennai - 600018", "contact": "+91-9840051917"},
            {"name": "Dr. Gokulakannan", "clinic": "Vibes Healthcare Ltd, No.52, Ground Floor, Brindavan Street, West Mambalam, Chennai - 600033", "contact": "+91-8870120670"},
            {"name": "Dr. Jayanthy Ravindran", "clinic": "Skin & Hair Clinic, 44/95, First Floor, Above ICICI Bank, Ranga Road, Mylapore, Chennai - 600004", "contact": "+91-9840017701"},
            {"name": "Dr. Shahul Hameed", "clinic": "Dr. Shahul's Clinic, No. 100, Nungambakkam High Road, Nungambakkam, Chennai - 600034", "contact": "+91-9841023289"},
            {"name": "Dr. A. Murali Moorthy", "clinic": "DermaClinix - The Complete Skin & Hair Solution Center, 17/7, Shanthi Nagar, Opposite to HDFC Bank, Adyar, Chennai - 600020", "contact": "+91-8588827963"}
        ],
        "patna": [
            {"name": "Dr. Shweta Singh", "clinic": "Skin & Hair Clinic, 10/75, Kankarbagh Road, Patna - 800020", "contact": "+91-9334110569"},
            {"name": "Dr. Alok Ranjan", "clinic": "Aesthetic Beauty Clinic, Indrapuri Road, Khajpura, Patna - 800014", "contact": "+91-9431097811"}
        ]
    }

    location = location.lower()
    if location in dermatologists_data:
        dermatologists = dermatologists_data[location]
        response = f"Sure, here are some dermatologists in {location.title()}:\n"
        for dermatologist in dermatologists:
            response += f"{dermatologist['name']}\nClinic Address: {dermatologist['clinic']}\nContact: {dermatologist['contact']}\n\n"
        return response
    else:
        return "I'm sorry, I don't have information for dermatologists in that location."

# Main loop
def chat():
    print("Welcome to the Hair Bot!")
    print("How can I assist you today?")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Hair Care Bot: Goodbye! If you have more questions, feel free to ask.")
            break
        else:
            response = chatbot_response(user_input)
            print("Hair Care Bot:", response)

# Start Conversation 
chat()