import requests,os,time
try:
	from faker import Faker
except ModuleNotFoundError:
	print("- Module eror • انت غير مثبت المكتبة المطلوبة جاري تثبيتها..")
	os.system('pip install faker')
try:
	import pyfiglet
except ModuleNotFoundError:
	print("- Module eror • انت غير مثبت المكتبة المطلوبة جاري تثبيتها..")
	os.system('pip install pyfiglet')
try:
	import webbrowser
except ModuleNotFoundError:
	print("- Module eror • انت غير مثبت المكتبة المطلوبة جاري تثبيتها..")
	os.system('pip install webbrowser')

try:
	import telebot
except ModuleNotFoundError:
	print("- Module eror • انت غير مثبت المكتبة المطلوبة جاري تثبيتها..")
	os.system('pip install telebot')
    
try:
	import user_agent
except ModuleNotFoundError:
	print("- Module eror • انت غير مثبت المكتبة المطلوبة جاري تثبيتها..")
	os.system('pip install user_agent')