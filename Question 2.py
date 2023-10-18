def martyr_count(martyr_name, catholic_martyrs, anglican_martyrs):
    if martyr_name in catholic_martyrs:
        return "Catholic"
    elif martyr_name in anglican_martyrs:
        return "Anglican"
    else:
        return "Unknown"
    

def is_uganda_martyr(martyr_name, catholic_martyrs, anglican_martyrs):
    return martyr_name in catholic_martyrs and martyr_name in anglican_martyrs



catholic_martyrs = ["Achileo Kiwanuka", "Adolphus LudigoMukasa","Ambrosius Kibuuka", "Anatoli Kiriggwajjo", "Andrew Kaggwa","Antanansio Bazzekuketta",
    "Bruno Sserunkuuma","Charles Lwanga","Denis Ssebuggwawo","Wasswa Gonzaga Gonza","Gyavira Musoke","James Buuzaabalyaawo",
    "John Maria Muzeeyi","Joseph Mukasa","Kizito Lukka", "Baanabakintu Matiya Mulumba", "Mbaga Tuzinde", "Mugagga Lubowa", "Mukasa Kiriwawanvu",
    "Nowa Mawaggali", "Ponsiano Ngondwe"]

anglican_martyrs = ["Aaron Lubega","Apollo Kivebulaya","Eria Sebukyala","Fredrick Kizza","George Kizza","James Hannington",
    "Janani Luwum","Joseph Balikuddembe","Kizito Mark Kakumba","Matia Mulumba","Nuhu Mbegu","Robert Munyagayirwa","Samwiri Mukasa",
    "Yefusa Namayanja","Yohana Mukasa","Yosefu Lugalama","Yowana Kitaka","Yowana Maria Mukasa","Yowana Mukiibi",
    "Yusufu Lugalama","Zakayo Lubega"]

new_anglican_martyrs = list(set(anglican_martyrs))
new_catholic_martyrs = list(set(catholic_martyrs))

martyr_name = input("Please enter martyr's name: ")

print(martyr_count(martyr_name, new_catholic_martyrs, new_anglican_martyrs))

print(is_uganda_martyr(martyr_name, catholic_martyrs, anglican_martyrs))




