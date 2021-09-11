monthCoversions = {
"Jan":"Janaury",
"Feb":"February",
"Mar":"March",
"Apr":"April",
"May":"May",
"Jun":"June",
"Jul":"July",
"Aug":"August",
"Sep":"Septemeber",
"Oct":"October",
"Nov":"November",
"Dec":"December",
}

print(monthCoversions["Nov"])
# OR
monthCoversions.get("Nov")
# OR
print(monthCoversions.get("Jov", "I meant November")) # assingns s defualt value if it wasn't defined