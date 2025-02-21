from source.utils.consts import MAIL_API_KEY, MAIL_API_SECRET, EMAIL

from mailjet_rest import Client


def setup_send_mail(name: str, surname: str, email: str):
    api_key = MAIL_API_KEY
    api_secret = MAIL_API_SECRET
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    name = name.lower().capitalize()
    surname = surname.lower().capitalize()
    data = {
        'Messages': [
            {
                "From": {
                    "Email": EMAIL,
                    "Name": "MieszkaMy"
                },
                "To": [
                    {
                        "Email": f"{email}",
                        "Name": f"{name} {surname}"
                    }
                ],
                "Subject": "Dziękujemy za kontakt!",
                "TextPart": "Dziękujemy za kontakt❤️ Odpowiemy na Państwa zgłoszenie tak szybko jak to możliwe! W "
                            "międzyczasie zapraszamy do zapoznania się z naszą pozostałą ofertą 😊",
                "HTMLPart": """
                                <div style="text-align: center; font-family: Arial, sans-serif; padding: 40px;">
                                    <h2 style="color: #E74C3C; font-size: 28px; font-weight: bold;">
                                        Dziękujemy za kontakt ❤️
                                    </h2>
                                    <p style="font-size: 18px; color: #333; font-weight: bold;">
                                        Odpowiemy na Państwa zgłoszenie tak szybko, jak to tylko możliwe!
                                    </p>
                                    <p style="font-size: 16px; color: #666;">
                                        W międzyczasie zapraszamy do zapoznania się z naszymi pozostałymi ofertami 😊
                                    </p>
                                    <a href="https://mieszkamy.onrender.com" 
                                       style="display: inline-block; margin-top: 20px; padding: 10px 20px; 
                                              background-color: #E74C3C; color: white; text-decoration: none; 
                                              border-radius: 5px; font-size: 16px;">
                                        Przejdź do MieszkaMy
                                    </a>
                                </div>
                            """
            }
        ]
    }
    result = mailjet.send.create(data=data)
    return result
