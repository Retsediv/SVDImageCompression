# SVDImageCompression
## A variation of SVD based image compression algorithm. SSVD(Shuffled SVD)

В ході роботи над алгоритмом було розроблено спершу звичайний SVD алгоритм, а потім і розширений SSVD із простим інтерфейсом у вигляді функції, котра стискає будь яке зображення із заданим рангом та розміром блоків.


### Дані, на яких проводились експерименти

   У своїй роботі автори узагальнюють алгоритм до квадратних, чорно-білих зображень. В результаті роботи було реалізовано метод стискання зображень будь якого розміру та навіть кольорових зображень, хоча, як було виявлено пізніше SVD(SSVD) не надто добре підходить до кольорових зображень.

Алгоритм на вході приймає матрицю зображення, а також кілька додаткових параметрів:

1. mode - “grayscale” чи “rgb”. Режим роботи: чорно-білі або кольорові зображення
2. block_size - розмір блоків для операції перемішування(п. 1 опису алгоритму)
3. rank - ранг матриці, до котрої ми хочемо стиснути початкову

На виході ми отримаємо матрицю стисненого зображення.

## Опис експерименту
   Для експерименту була вибрана відома фотографія Lena, котра дуже часто наводиться у прикладах зі стисканням зображень і також присутня в оригінальній роботі, тому в результаті цього було зручно і легко порівняти власні результати та ті, котрі отримали автори статті.
	
**Приклад виклику функції для SSVD стискання:**
```
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import svd_algo.compress_image as ci

# Open the image and convert it to numpy.arrray
img = Image.open('test_image.jpg')
img = np.array(img)



# Compress the rgb image with rank=30 and size of blocks=16
compressedImage = ci.compress_image(
coloredImg, 
mode='rgb', 
block_size=16, 
rank=30
)

# Display the compressed image
plt.figure(figsize=(12,6))
plt.imshow(compressedImage);
```

У репозиторії є jupyter-notebooks, у котрих покроково показана реалізації та використання кожного методу(звичайного SVD, чорно-білого SSVD, кольорового SSVD) а також есперименти та порівняння, котрі проводились(папка examples).

Початкове зображення:

![Original Lenna image](https://upload.wikimedia.org/wikipedia/en/2/24/Lenna.png)

Порівняння стискання чорно-білих зображень за допомогою SVD, SSVD(block size=8) та SSVD(block size=16)

![Grayscale images compression comparison](https://lh3.googleusercontent.com/0vt0cQWbIEhiwjdho0nCt5MJrza-eIbe1s3ayoJ17mD2yxBDyT1N9VKftKGvKFMSJwOawlzhqiHQXDgija-QyUbdyCgLmWZUOLuE1fptQB24Chvg6PRrru9HNxZquvVzeb9MY3J2514fGbfsj_DTwoNdOMZDenkASqf_njflorXfA3VeFWZsE50u5I_Um31mjfgZQqfT_ivqW6D9V_AcFpd-on-jdwxEADtNDLEoIZuiugSf0FF_FLgKXblQjUpsGbtQU3sTT_F5_RBlNIvBROQZI5qwtdn4qkdS7WemsbspQqK17BIa04JvqLFBa7FTU-WN1DVKBXdeP9gw2ansN1T0Q3xJXZ4Eylp-d_HNas3QqwyvJagxuHCrJqeMwf6lIA7jReqFrYDu5ywgV2HJsrV6Gb6d-BAETJvmjKHRtxMGwzwwf2av15oerHHODsLMdADwkdFFcKoOkIAepkil6vH7NyoyDuOrA5o1SgW4N_7l6eecKnEKegwrYJm1eRrJ4CKK1szspiViu3xZLsUKcmwhM122bgSb30RwbdRDKE9zYp0dUE8Btc-zRqKoO2qXSDLMHtFD83haEAMYSwqkiaiHeXJeFzspG1jfVZWaqzIqwATjN0eFfE6alFeK16dcXp4bxAkHVHMvpKp63AnawlxhGlOCzbBxUbs=w435-h974-no)

Порівняння стискання кольорового  зображення за допомогою SVD та SSVD(block size=16)
![Colored image compression comparison](https://lh3.googleusercontent.com/RqNLTxUWHPZ-5E14WUMnxv7hw_R57Z2gMj4hQJuaMwjDv_hAtyPEMNuMXq5r3kpSTSuok6wt6cXMfNimYmivLckP4BkuASG2poOOfr-2txMqJqP_jY-kKsgTcowamL8Nlut4DTxWodMU3Rm5j9HMG2AabtRkOpJfZ-xaC9UgvkFTSHtvBrlWHcpzg04nJeLyFzVdHVnihCPJSUg5VW2LArHmDjEqEErifJ2DbYPZDY3wukG86DcPmuswnYTH_ufOlKASNeRiuom8POIKUuxEvUKGeKB5MsfZGzkKOhjPpmLGWD0qqm7lWvT8VrXPXn7wtKgb1U9P3ox5sEgYeutJfJot0JGSflvvB6G3UpxwsD2CKNf3CZwANRdH2WUUAfea4nyTdV7PL4mD_wz1Jz9o3WJ9aTn2Ws3euo9LGhYvKrZi7nxtaBw9oIjDZov00E8Zwpiezr2KE5IjFrgosKm1BKeqLaXVQZ6ixhBX2uUw9sSACSuhyO0vSFTYJT05YA-1f3XGHYKOwSa_KP2n8cpsBgk-zpCPsmRFDwVpU69om6A53jGDFZCe84-x0CYGj2WW8RJz6mHFrPCB13JtNCARJAo1jTZl9M4xmPlUnLnxlm4EOIdrXPdOQdq336L377whSB_I3GTiRdL48J4UGXYGEpJbTk9r4zx1B1o=w499-h974-no)

Також для такої фотографії було визначено кількість елементів(в матриці зображення) до початку стиснення та після проведення стиснення(скільки елементів потрібно зберігати, щоб потім отримати коректну апроксимацію зображення). 
![Image size comparasion(elements in matrices)](https://lh3.googleusercontent.com/D08gnR3UyHfHyK6EIb-GiXv3sArnOEsMDD1eOEdguRcluxNo_Lb-V4cv_avuaHmobXknK1DGHqgUkQ8vAOTssRE_WnMo5SRV11RXgKU3tJV7eEdlCBbEOXU4GX8c0o539fWUIC_y0BqJpzU5zxFLXqiNsbXQ_Q9jR8BGtDIJSZubcZD3S1TXrkrqMsgtwp30mLBMOsktBwizexSW7hxieuNw0AK7X68KMisypdeepg-YFdCAndWxZeB7cuCVnNMH4mZLZjpmMKeECyhaEc4_AAAU0EHF7Ka6iZgYOAqBbwMJsU1aN8_rFxtoIzoViu3AnXFfHiuMWC0gPOWNR67c_O67n38NXwEQQWwKwuU2i_DSv2kjvrgHvgkZ3eMVYKLjWTYtr05VuBOwNU7FCKOuG5-Op1ahK4nMiv61ceDK5QTyp_PC3tPaX3dsDHS3E9SNAwW-TnkWDPhSC5aqMiVAsk6xqKrZTrcIffP1v7oL4DolC-FywdoV5Djuxe_X7e6oI-gzHgDeVWXjVjscidNFO0gwy3MizbL-CW69oMerFGcqlpnKfhdLEb6loOeXIxNLLmaB60r22EI6_JP43n39AbWzJrGA5KQ1M8PrdK9HBnfwuCSeHEZZmZEH33zFWZMPpZXSAnRo3D3pnOto3y26bcKu1RP23t8RL5s=w1180-h449-no)

Після цього я спробував записати ці матриці у файл у бінарному вигляді(можливість бібліотеки numpy). Результати(значення в кілобайтах):

![Image size comparasion(in kb)](https://lh3.googleusercontent.com/qEhhEdaoekpcdY8brpQsVRnfcWNGl6q4nrKpVr9NrRyZ3xVkMuxvCyVW-yfee3H4pea59yRe5M2yyFfPt6FL-UdlnlF94Q1CESnVEWrq8Xs4Nx86wP1jVHQ8utORtLpSTyjLm582gJIPBRlsqnuc8bVk-CruVeklrbg4Mao17iBwLG7tH2uGiICSKCLC5xWpSdXMUFOlH9uB-sy1KQhe2ibtfsQluJxHIF7mVbyXEeKjmjDw_bkrplqdUxei2GCti6d4EB_tk29boMQmjrPNWz5-OT3MEm-1XVquY_twiXaFPq8BzIVsBR2HtZToL-m__3fvDuzeFVn5UoG110XQvRIvXngs2ctIGDRWgJOphpzvRxPWXi-nAORTxMuT_ISUNuKySbQbAlfftmXWT7ibxIfkHNpzHw3o3elTJs2YFqni26RqLCJMEb6tL36MQX2bL99ecS-QGvmB4-AeSfDRM4b9ZRz4Ru4nWpag6yKuPqfyHy75zp8PWWXsvZSytWxiKsGJiOU1qAOZWBeQTnO2YitmPjirc2ytrIAAH2mexugIg4mEkz0dXf2zY3ANI5gNfMAdOQOxTbz4KdHuNsY5KtKBcJv_bSEuVoTXlmViPxeUUerjmWvjOVvp_BPgutnIU9BDb6OZ8p7fyLLEogTCtcNqmGLISINimDo=w1175-h434-no)

Весь код цього порівняння є у файлі **examples/CompareQualityAndSize.ipynb** 
Багато прикладів стискання різних зображень та роботи із ними є у файлах: **BasicSVDImageCompression.ipynb**, **ColoredSVDImageCompression.ipynb**, **ExtendedSVDImageCompression.ipynb**
	
## Висновки

   В результаті роботи над алгоритмом стискання зображень було детально вивчено базовий алгоритм SVD та його застосування у різних сферах. Я розібрався із бібліотеками numpy, matplotlib та PIL. Навчився працювати із зображеннями, їх “трансформуванням” у звичайні матриці, розбиттю кольорового зображення на різні “шари”(червоний, зелений та синій) та подальшою обробкою. Написано відповідну реалізацію алгоритму, описану у оригінальній статті, а також зроблено вдосконалення алгоритму для роботи із будь якими зображеннями.
   Найбільшу складність викликало математичне усвідомлення SVD алгоритму, його подальша реалізація та те, що автори статті наводять усі приклади для чорно-білих, квадратних зображень і потрібно було самостійно робити узагальнення роботи алгоритму для будь якого зображення. 
   Незрозумілим залишилось bit allocation strategy та uniform quantization. Через брак інформації не зрозуміло до кінця як це працює і як реалізувати ці ідеї.
