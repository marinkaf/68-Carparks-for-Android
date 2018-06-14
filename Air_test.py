# -*- encoding=utf8 -*-
__author__ = "ittes"


"""
import logging
logging.getLogger("airtest").setLevel(logging.WARNING)
"""

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(force_restart=False)
from airtest.core.api import *
from airtest.core.android.adb import ADB
adb = ADB()
from airtest.core.android.adb import *
from airtest.core.android.minicap import *
from airtest.core.android.minitouch import *
from unittest import TestCase



# глобальные переменные МЕНЯТЬ
connection = connect_device('Android:///192.168.1.47:5555')
package_name="com.yandex.maps.testapp.testing"

# функции

def SearchInMenuAndClick(val):
    """Ищем элементы и сравниваем текст"""
    while poco(text=val).exists()==False:
        swipe([100, 500],0, vector=[0, -0.5])
    else:
        poco(text=val).click()

def ManeMenu():
    """определяем что находимся в главном меню, вверху списка"""
    TestApp_titl=poco("android:id/list").child("android:id/title").get_text()
    Experiments=poco("android:id/list").child("android.widget.LinearLayout")[1].child("android.widget.RelativeLayout").child("android:id/title").get_text()
    About=poco("android:id/list").child("android.widget.LinearLayout")[1].child("android.widget.RelativeLayout").child("android:id/title").get_text()
     
    if ((TestApp_titl=="TestApp.testing") and (About=="About") and (Experiments=="Experiments")):
        return True
    else:
        return False        
        
def Carparks(package_name):
    """Определяем что в разделе Carparks"""
    Back_text=poco(package_name+":id/back").get_text()
    Hidenearbycarparks_text=poco(package_name+":id/carparks_nearby_hide_button").get_text()
    # Whereismycar_text=poco(package_name+":id/last_park_place").get_text()
    # Detectorenabled_text=poco(package_name+":id/carparks_detector_checkbox").get_text()
    # Carparks_text=poco(package_name+":id/carparks_checkbox").get_text()
    # Events_text=poco(package_name+":id/carparks_events_checkbox").get_text()
    # Nightmode_text=poco(package_name+":id/carparks_night_mode_checkbox").get_text()
    if ((Hidenearbycarparks_text=="Hide nearby carparks") and (Back_text=="< Back")):
        # and (Whereismycar_text=="Where is my car?") and (Detectorenabled_text=="Detector enabled") and (Carparks_text=="Carparks") and (Events_text=="Events") and (Nightmode_text=="Night mode")):
        return True
    else:
        return False
       
          
def ClickOnCheckboxFindText(package_name,Text_element):
    """Снимаем/ставим галочку. Проверяем что состояние чекбокса изменилось."""
    before_attribute=poco(text=Text_element).attr('checked')
    poco(text=Text_element).click()
    after_attribute=poco(text=Text_element).attr('checked')
    if before_attribute!=after_attribute:
        return True
    else:
        return False
        
def CleanAndStartAPP(package_name):
    clear_app(package_name)
    start_app(package_name)
    sleep(3)

    
# ******************mapkit-68: [Android]Раздел Carparks (for Android) *************************

''' Preconditions'''
'''Очищаем данные и запускаем приложение'''
CleanAndStartAPP(package_name)
'''Проверяем что приложение запустилось и открылось основное меню'''
ManeMenu()

'''STEPS'''
'''1.Зайти в раздел Carparks
Результат: Раздел открылся. На экране присутствует галочка с надписью “Detector enabled”. На экране на карте отмечены парковки.'''
SearchInMenuAndClick("Carparks")
Carparks(package_name)

'''2.Снять галочку “Detector enabled” '''
'''Приложение не крешится, работает стабильно.'''
ClickOnCheckboxFindText(package_name,"Detector enabled") 
sleep(3) 
Carparks(package_name) #после снятия галочки проверяем, что мы по-прежнему в нужном разделе




