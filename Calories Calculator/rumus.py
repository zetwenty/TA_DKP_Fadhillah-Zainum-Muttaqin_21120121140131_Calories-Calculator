# Berdasarkan rumus Harris-Benedict yang telah direvisi oleh Roza dan Shizgal (1984)
# BMR laki-laki = 88.362 + (13.397 x BB kg) + (4.799 x TB cm) – (5.677 x umur tahun)
# BMR Wanita = 447.593 + (9.247 x BB kg) + (3.098 x TB cm) – (4.330 x umur tahun)
def male_bmr(berat, tinggi, umur):
    # Calculate male bmr
    return 88.362 + (13.397 * berat) + (4.799 * tinggi) - (5.677 * umur) 

def female_bmr(berat, tinggi, umur):
    # Calculate female BMR
    return 447.593 + (9.247 * berat) + (3.098 * tinggi) - (4.330 * umur) 


# IMT = Berat Badan (kg) : (Tinggi Badan (m) x Tinggi Badan (m))
def bmi_cal(berat, tinggi):
    # Calculate male BMI
        return berat / ((tinggi / 100) * (tinggi / 100))

# Men:
# CB = T * (0.6309*H + 0.1988*W + 0.2017*A - 55.0969) / 4.184   ||| (T = durasi, H = detakJ, W = berat, A = umur)
# Women:
# CB = T * (0.4472*H - 0.1263*W + 0.074*A - 20.4022) / 4.184    ||| (T = durasi, H = detakJ, W = berat, A = umur)
def male_caloriesB(detakJ, berat, umur, durasi):
    # Calculate male calories burned based on heart rate and duration
    return (
        durasi * ((0.6309 * detakJ) + (0.1988 * berat) + (0.2017 * umur) - 55.0969) / 4.184
    )
    #     (-55.0969 + (0.6309 * detakJ) + (0.1988 * (berat / 2.205)) + (0.2017 * umur))
    #     / 4.184
    # ) * durasi

def female_caloriesB(detakJ, berat, umur, durasi):
    # Calculate female calories burned based on heart rate and duration
    return (
        durasi * ((0.4472 * detakJ) - (0.1263 * berat) + (0.074 * umur) - 20.4022) / 4.184
    )
    #     (-20.4022 + (0.4472 * detakJ) - (0.1263 * (berat / 2.205)) + (0.074 * umur))
    #     / 4.184
    # ) * durasi