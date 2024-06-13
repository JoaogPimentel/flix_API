from django.db import models

NATIONALITY_CHOICES = (
    ('Afghanistan', 'Afghan'), ('Albania', 'Albanian'), ('Algeria', 'Algerian'), ('Andorra', 'Andorran'), ('Angola', 'Angolan'),
    ('Antigua and Barbuda', 'Antiguan or Barbudan'), ('Argentina', 'Argentine'), ('Armenia', 'Armenian'), ('Australia', 'Australian'),
    ('Austria', 'Austrian'), ('Azerbaijan', 'Azerbaijani'), ('Bahamas', 'Bahamian'), ('Bahrain', 'Bahraini'), ('Bangladesh', 'Bangladeshi'),
    ('Barbados', 'Barbadian'), ('Belarus', 'Belarusian'), ('Belgium', 'Belgian'), ('Belize', 'Belizean'), ('Benin', 'Beninese'),
    ('Bhutan', 'Bhutanese'), ('Bolivia', 'Bolivian'), ('Bosnia and Herzegovina', 'Bosnian or Herzegovinian'), ('Botswana', 'Motswana'),
    ('Brazil', 'Brazilian'), ('Brunei', 'Bruneian'), ('Bulgaria', 'Bulgarian'), ('Burkina Faso', 'Burkinabé'), ('Burundi', 'Burundian'),
    ('Cabo Verde', 'Cabo Verdean'), ('Cambodia', 'Cambodian'), ('Cameroon', 'Cameroonian'), ('Canada', 'Canadian'),
    ('Central African Republic', 'Central African'), ('Chad', 'Chadian'), ('Chile', 'Chilean'), ('China', 'Chinese'), ('Colombia', 'Colombian'),
    ('Comoros', 'Comoran'), ('Congo, Democratic Republic of the', 'Congolese (Democratic Republic)'), ('Congo, Republic of the', 'Congolese (Republic)'),
    ('Costa Rica', 'Costa Rican'), ('Croatia', 'Croatian'), ('Cuba', 'Cuban'), ('Cyprus', 'Cypriot'), ('Czech Republic', 'Czech'),
    ('Denmark', 'Danish'), ('Djibouti', 'Djiboutian'), ('Dominica', 'Dominican'), ('Dominican Republic', 'Dominican'),
    ('East Timor (Timor-Leste)', 'Timorese'), ('Ecuador', 'Ecuadorian'), ('Egypt', 'Egyptian'), ('El Salvador', 'Salvadoran'),
    ('Equatorial Guinea', 'Equatorial Guinean'), ('Eritrea', 'Eritrean'), ('Estonia', 'Estonian'), ('Eswatini', 'Swazi'), ('Ethiopia', 'Ethiopian'),
    ('Fiji', 'Fijian'), ('Finland', 'Finnish'), ('France', 'French'), ('Gabon', 'Gabonese'), ('Gambia', 'Gambian'), ('Georgia', 'Georgian'),
    ('Germany', 'German'), ('Ghana', 'Ghanaian'), ('Greece', 'Greek'), ('Grenada', 'Grenadian'), ('Guatemala', 'Guatemalan'), ('Guinea', 'Guinean'),
    ('Guinea-Bissau', 'Bissau-Guinean'), ('Guyana', 'Guyanese'), ('Haiti', 'Haitian'), ('Honduras', 'Honduran'), ('Hungary', 'Hungarian'),
    ('Iceland', 'Icelandic'), ('India', 'Indian'), ('Indonesia', 'Indonesian'), ('Iran', 'Iranian'), ('Iraq', 'Iraqi'), ('Ireland', 'Irish'),
    ('Israel', 'Israeli'), ('Italy', 'Italian'), ('Jamaica', 'Jamaican'), ('Japan', 'Japanese'), ('Jordan', 'Jordanian'),
    ('Kazakhstan', 'Kazakhstani'), ('Kenya', 'Kenyan'), ('Kiribati', 'I-Kiribati'), ('Korea, North', 'North Korean'), ('Korea, South', 'South Korean'),
    ('Kosovo', 'Kosovar'), ('Kuwait', 'Kuwaiti'), ('Kyrgyzstan', 'Kyrgyzstani'), ('Laos', 'Lao'), ('Latvia', 'Latvian'), ('Lebanon', 'Lebanese'),
    ('Lesotho', 'Basotho'), ('Liberia', 'Liberian'), ('Libya', 'Libyan'), ('Liechtenstein', 'Liechtensteiner'), ('Lithuania', 'Lithuanian'),
    ('Luxembourg', 'Luxembourgish'), ('Madagascar', 'Malagasy'), ('Malawi', 'Malawian'), ('Malaysia', 'Malaysian'), ('Maldives', 'Maldivian'),
    ('Mali', 'Malian'), ('Malta', 'Maltese'), ('Marshall Islands', 'Marshallese'), ('Mauritania', 'Mauritanian'), ('Mauritius', 'Mauritian'),
    ('Mexico', 'Mexican'), ('Micronesia', 'Micronesian'), ('Moldova', 'Moldovan'), ('Monaco', 'Monegasque'), ('Mongolia', 'Mongolian'),
    ('Montenegro', 'Montenegrin'), ('Morocco', 'Moroccan'), ('Mozambique', 'Mozambican'), ('Myanmar', 'Burmese'), ('Namibia', 'Namibian'),
    ('Nauru', 'Nauruan'), ('Nepal', 'Nepali'), ('Netherlands', 'Dutch'), ('New Zealand', 'New Zealand'), ('Nicaragua', 'Nicaraguan'),
    ('Niger', 'Nigerien'), ('Nigeria', 'Nigerian'), ('North Macedonia', 'Macedonian'), ('Norway', 'Norwegian'), ('Oman', 'Omani'),
    ('Pakistan', 'Pakistani'), ('Palau', 'Palauan'), ('Palestine', 'Palestinian'), ('Panama', 'Panamanian'), ('Papua New Guinea', 'Papua New Guinean'),
    ('Paraguay', 'Paraguayan'), ('Peru', 'Peruvian'), ('Philippines', 'Filipino'), ('Poland', 'Polish'), ('Portugal', 'Portuguese'),
    ('Qatar', 'Qatari'), ('Romania', 'Romanian'), ('Russia', 'Russian'), ('Rwanda', 'Rwandan'), ('Saint Kitts and Nevis', 'Kittitian or Nevisian'),
    ('Saint Lucia', 'Saint Lucian'), ('Saint Vincent and the Grenadines', 'Vincentian'), ('Samoa', 'Samoan'), ('San Marino', 'Sammarinese'),
    ('Sao Tome and Principe', 'São Toméan'), ('Saudi Arabia', 'Saudi Arabian'), ('Senegal', 'Senegalese'), ('Serbia', 'Serbian'),
    ('Seychelles', 'Seychellois'), ('Sierra Leone', 'Sierra Leonean'), ('Singapore', 'Singaporean'), ('Slovakia', 'Slovak'),
    ('Slovenia', 'Slovenian'), ('Solomon Islands', 'Solomon Islander'), ('Somalia', 'Somali'), ('South Africa', 'South African'),
    ('South Sudan', 'South Sudanese'), ('Spain', 'Spanish'), ('Sri Lanka', 'Sri Lankan'), ('Sudan', 'Sudanese'), ('Suriname', 'Surinamese'),
    ('Sweden', 'Swedish'), ('Switzerland', 'Swiss'), ('Syria', 'Syrian'), ('Taiwan', 'Taiwanese'), ('Tajikistan', 'Tajikistani'),
    ('Tanzania', 'Tanzanian'), ('Thailand', 'Thai'), ('Togo', 'Togolese'), ('Tonga', 'Tongan'), ('Trinidad and Tobago', 'Trinidadian or Tobagonian'),
    ('Tunisia', 'Tunisian'), ('Turkey', 'Turkish'), ('Turkmenistan', 'Turkmen'), ('Tuvalu', 'Tuvaluan'), ('Uganda', 'Ugandan'),
    ('Ukraine', 'Ukrainian'), ('United Arab Emirates', 'Emirati'), ('United Kingdom', 'British'), ('United States', 'American'),
    ('Uruguay', 'Uruguayan'), ('Uzbekistan', 'Uzbekistani'), ('Vanuatu', 'Ni-Vanuatu'), ('Vatican City (Holy See)', 'Vatican'),
    ('Venezuela', 'Venezuelan'), ('Vietnam', 'Vietnamese'), ('Yemen', 'Yemeni'), ('Zambia', 'Zambian'), ('Zimbabwe', 'Zimbabwean')
)


class Actor(models.Model):

    name = models.CharField(max_length=200)
    birthday = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=100, choices=NATIONALITY_CHOICES, blank=True, null=True)
    
    def __str__(self):
        return self.name
    