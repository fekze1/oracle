def questionChoose(ID):
    if (ID in range(16, 47, 10)):
        return "Живое?"
    if (ID == 15 or ID == 25):
        return "Растение?"
    if (ID == 35 or ID == 55):
        return "Млекопитающее?"