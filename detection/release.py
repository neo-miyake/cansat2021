import time

from sensor.envirionmental import bme280


def pressdetect_release(thd_press_release, t_delta_release):
    '''
    気圧による放出判定
    '''
    global press_count_release
    global press_judge_release
    try:
        pressdata = bme280.bme280_read()
        prevpress = pressdata[1]
        time.sleep(t_delta_release)
        pressdata = bme280.bme280_read()
        latestpress = pressdata[1]
        deltP = latestpress - prevpress
        if 0.0 in pressdata:
            print("bme280rror!")
            press_count_release = 0
            press_judge_release = 2
        elif deltP > thd_press_release:
            press_count_release += 1
            if press_count_release > 1:
                press_judge_release = 1
                print("pressreleasejudge")
        else:
            press_count_release = 0
            press_judge_release = 0
    except:
        press_count_release = 0
        press_judge_release = 2
    return press_count_release, press_judge_release


# def releasejudge(thd_p_release):


if __name__ == "__main__":
    thd_press_release = 0.3
    pressreleasecount = 0
    pressreleasejudge = 0
    t_delta_release = 3
    bme280.bme280_setup()
    bme280.bme280_calib_param()

    while True:
        press_count_release, press_judge_release = pressdetect_release(thd_press_release, t_delta_release)
        print(f'count:{pressreleasecount}\tjudge{pressreleasejudge}')
        if pressreleasejudge == 1:
            print('Press')
        else:
            print('unfulfilled')

# def gpsdetect(anyalt):
#     global gpsdata
#     global GAreleasecount
#     gpsreleasejudge = 0
#     try:
#         gpsdata = gps.readGPS()
#         Pregpsalt = gpsdata[3]
#         time.sleep(1)
#         gpsdata = gps.readGPS()
#         Latestgpsalt = gpsdata[3]
#         daltGA = Latestgpsalt - Pregpsalt
#         #print(str(Latestgpsslt)+"   :   "+str(Pregpsalt))
#         if daltGA > anyalt:
#             GAreleasecount += 1
#             if GAreleasecount > 2:
#                 gpsreleasejudge = 1
#                 print("gpsreleasejudge")
#             else:
#                 gpsreleasejudge = 0
#     except:
#         print(traceback.format_exc())
#         GAreleasecount = 0
#         gpsreleasejudge = 2
#     return GAreleasecount, gpsreleasejudge

# if __name__=="__main__":
#
# 	bme280.bme280_setup()
# 	bme280.bme280_calib_param()
# 	gps.openGPS()
#
# 	while True:
# 		_, gpsreleasejudge = gpsdetect(10)
# 		if gpsreleasejudge == 1:
# 			print('gps')
# 		else:
# 			print('gps unfulfilled')
#
# 		_, pressreleasejudge = pressdetect(0.3)
# 		if pressreleasecount == 1:
# 			print('Press')
# 		else:
# 			print('unfulfilled')
