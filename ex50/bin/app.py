# -*- coding: utf-8 -*-

import os
from flask import Flask, request, jsonify

 
app = Flask(__name__)
 
 
 
@app.route('/keyboard')
def Keyboard():
 
    dataSend = {
        "type" : "buttons",
        "buttons" : ["치킨", "기타 메뉴"]
    }
 
    return jsonify(dataSend)
 
 
 
@app.route('/message', methods=['POST'])
def Message():
    
    dataReceive = request.get_json()
    content = dataReceive['content']
 
    if content == u"치킨":
        dataSend = {
            "message": {
                "text": "어느 치킨집을 원하시나요?"
            }
        }
    elif content == u"기타 메뉴":
        dataSend = {
            "message": {
                "text": "찾는 업체명을 알려주세요!"
            }
        }
    elif u"BHC" in content:
        dataSend = {
            "message": {
                "text": "BHC 정보입니다 전화번호 : 052-245-1922, 운영 시간 : 12시 - 24시, 2마리 이상 배달가능 감사합니다",
                "message_button": {
                      "label": "메뉴판 보기",
                       "url": "http://mbymadmin.reddot.kr/data/upload/12247/0.jpg"
                }
            }
                
        }
    elif u"깻잎" in content:
        dataSend = {
            "message": {
                "text": "깻잎칩킨 정보입니다 전화번호 : 052-223-8844, 운영 시간 : 17시 - 26시, 감사합니다",
                "message_button": {
                      "label": "메뉴판 보기",
                       "url": "http://mbymadmin.reddot.kr/data/upload/20332/8561_FILE1.jpg"
                }
            
            }
        }    
    elif u"비버스" in content:
        dataSend = {
            "message": {
                "text": "비버스치킨 정보입니다 전화번호 : 052-246-5582, 운영 시간 : 17시 - 26시, 감사합니다",
                "message_button": {
                      "label": "메뉴판 보기",
                       "url": "https://drive.google.com/open?id=0B9xxWy_rtyBwQkJvV0hQbWpnSGM"
                }
            
            }
                    
        }
    elif u"치킨파티" in content:
        dataSend = {
            "message": {
                "text": "치킨파티 정보입니다 전화번호 : 052-247-9300, 운영 시간 : 11시 - 26시, 감사합니다",
                "message_button": {
                      "label": "메뉴판 보기",
                      "url": "https://drive.google.com/open?id=1JOUsiKr2fT7DQRTao7vuY6j7sb74NUPZ"

                }
            
            }
                    
        }
    elif u"쌀을품은닭" in content:
        dataSend = {
            "message": {
                "text": "쌀을 품은 닭  정보입니다 전화번호 : 052-211-9274, 운영 시간 : 모름, 감사합니다",
                "message_button": {
                      "label": "메뉴판 보기",
                      "url": "https://drive.google.com/open?id=1QKI1Qg05ksjj2H6dqA-Gcov-J4qkcHG4"
                }
            
            }
                    
        }
    elif u"올꼬꼬" in content:
        dataSend = {
            "message": {
                "text": "올꼬꼬  정보입니다 전화번호 : 052-212-9989, 운영 시간 : 17시 - 26시, 감사합니다",
                "message_button": {
                      "label": "메뉴판 보기",
                      "url": "https://drive.google.com/open?id=1391j5m6yIVGlu95Zna6nvGN6zwx1vh9t"
                }
            
            }
                    
        }
    elif u"구어조은닭" in content:
        dataSend = {
            "message": {
                "text": "구어조은닭  정보입니다 전화번호 : 052-245-9279, 운영 시간 : 17시 - 25시, 감사합니다",
                "message_button": {
                      "label": "메뉴판 보기",
                      "url": "https://drive.google.com/open?id=1aUc0qg4VbwzxpRV6I1FV_Vmudui2Q6lv"
                }
            
            }
                    
        }
    elif u"기똥찬" in content:
        dataSend = {
            "message": {
                "text": "기똥찬 파닭 정보입니다 전화번호 : 052-245-9281, 운영 시간 : 18시 - 25시, 2인분 이상 배달가능 감사합니다",
                "message_button": {
                      "label": "메뉴판 보기",
                      "url": "https://drive.google.com/open?id=1ZsnLePMh3JDX2flXjtFcs_LjA2Tq14qP"
                }
            
            }
                    
        }
    elif u"쫄파촌닭" in content:
        dataSend = {
            "message": {
                "text": "쫄파촌닭 정보입니다 전화번호 : 052-246-8090, 운영 시간 : 12시 - 25시, 감사합니다",
                "message_button": {
                      "label": "메뉴판 보기",
                      "url": "https://drive.google.com/open?id=1cQbLo30-bqOTriqZIyNcnAXG76nf5bk1"
                }
            
            }
                    
        }
        
    elif u"네네" in content:
        dataSend = {
            "message": {
                "text": "네네치킨 정보입니다 전화번호 : 052-248-9982, 운영 시간 : , 감사합니다",
                "message_button": {
                      "label": "메뉴판 보기",
                      "url": "https://drive.google.com/open?id=1DTGJ4kmo2tJuAPnb2ic2LBBImqttizSN"
                }
            
            }
                    
        }
    elif u"달감" in content:
        dataSend = {
            "message": {
                "text": "네네치킨 정보입니다 전화번호 : 052-245-7279, 운영 시간 : 17시 ~ 24시, 3마리 이상 무료배달 감사합니다",
                "message_button": {
                      "label": "메뉴판 보기",
                      "url": "https://drive.google.com/open?id=1f49j1q5K--HIqqUAaK2HSjjnuS7LTJcg"
                }
            
            }
                    
        }
    elif u"또래오래" in content:
        dataSend = {
            "message": {
                "text": "또래오래 정보입니다 전화번호 : 052-212-9433, 운영 시간 : 12시 ~ 24시, 감사합니다",
                "message_button": {
                      "label": "메뉴판 보기",
                      "url": "https://drive.google.com/open?id=1hLJL3fIpFGShPdGYq7Zf-ChCgyoQg0XZ"
                }
            
            }
                    
        }
    elif u"마쯔리" in content:
        dataSend = {
            "message": {
                "text": "마쯔리 정보입니다 전화번호 : 052-246-8258, 운영 시간 : 모름, 3만원 이상 배달가능 감사합니다",
                "message_button": {
                      "label": "메뉴판 보기",
                      "url": "https://drive.google.com/open?id=1jjN-yUoLToLMTLrYZQiaggdg-sjjkRju"
                }
            
            }
                    
        }
    elif u"돈우" in content:
        dataSend = {
            "message": {
                "text": "돈우 정보입니다 전화번호 : 052-923-9292, 운영 시간 : 16시 ~ 21시 30분, 2만원 이상 배달가능 감사합니다",
                "message_button": {
                      "label": "메뉴판 보기",
                      "url": "https://drive.google.com/open?id=14_hpDSVX4xjErv2eJ5R3rcZ77VYsJ3N3"
                }
            
            }
                    
        }
    
    elif u"배터지는" in content:
        dataSend = {
            "message": {
                "text": "배터지는 생동까스 정보입니다 전화번호 : 052-211-2360, 운영 시간 : 모름 ~ 23시, 2만원 이상 배달가능 감사합니다",
                "message_button": {
                      "label": "메뉴판 보기",
                      "url": "https://drive.google.com/open?id=1b3_k2DbbegDXNbD0Wash1meAf6l67lTe3"
                }
            
            }
                    
        }
    
    elif u"빨강떡볶이" in content:
        dataSend = {
            "message": {
                "text": "빨강떡볶이 정보입니다 전화번호 : 052-248-3449, 운영 시간 : 모름, 감사합니다",
                "message_button": {
                      "label": "메뉴판 보기",
                      "url": "https://drive.google.com/open?id=1YBUXlaEQrK908ok9VjPV42toN7xoXfKD"
                }
            
            }
                    
        }
    elif u"빨봉" in content:
        dataSend = {
            "message": {
                "text": "빨봉분식 정보입니다 전화번호 : 052-211-8083, 운영 시간 : 11시 ~ 21시, 2만원 이상 배달가능, 배달비 3000원 감사합니다",
                "message_button": {
                      "label": "메뉴판 보기",
                      "url": "https://drive.google.com/open?id=1lPmTz-wqzy5KhhbDRNhseGeRRIzZukM9"
                }
            
            }
                    
        }
    elif u"아방궁" in content:
        dataSend = {
            "message": {
                "text": "아방궁 정보입니다 전화번호 : 052-211-1149, 운영 시간 : 모름, 두 그릇 이상 배달가능 감사합니다",
                "message_button": {
                      "label": "메뉴판 보기",
                      "url": "https://drive.google.com/open?id=1WEHUk5-KhNeCHwpwWOhh2NIjNF5NuYoW"
                }
            
            }
                    
        }
    elif u"수인" in content:
        dataSend = {
            "message": {
                "text": "빨강떡볶이 정보입니다 전화번호 : 052-245-3050, 운영 시간 : 모름, 2만원 이상 배달가능 감사합니다",
                "message_button": {
                      "label": "메뉴판 보기",
                      "url": "https://drive.google.com/open?id=1NgqeD7oWSPelpUpmmi5Ky8tuTN4mSa3V"
                }
            
            }
                    
        }
    elif u"연탄불고기" in content:
        dataSend = {
            "message": {
                "text": "달인의 연탄불고기 정보입니다 전화번호 : 052-222-2378, 운영 시간 : 11시 ~ 29시, 감사합니다",
                "message_button": {
                      "label": "메뉴판 보기",
                      "url": "https://drive.google.com/open?id=1pLBRROg5b7-r1ciFALG_7pkuTHQVSjy5"
                }
            
            }
                    
        }
    elif u"엽기떡볶이" in content:
        dataSend = {
            "message": {
                "text": "동대문 엽기떡볶이 정보입니다 전화번호 : 052-243-8592, 운영 시간 : 모름, 17000원 이상 배달가능, 배달비 2000원 감사합니다",
                "message_button": {
                      "label": "메뉴판 보기",
                      "url": "https://drive.google.com/open?id=1Y0VnvmtZiRYWPuzpp_mw9zSaEe-ATCey"
                }
            
            }
                    
        }
    elif u"치탕" in content:
        dataSend = {
            "message": {
                "text": "탕수육 코리아 정보입니다 전화번호 : 052-211-9934, 운영 시간 : 모름, 감사합니다",
                "message_button": {
                      "label": "메뉴판 보기",
                      "url": "https://drive.google.com/open?id=1wQrtXrpKH3RxHM1c0IkGWY_ovgNeabLj"
                }
            
            }
                    
        }
    
    
    
   
    
    else:
        dataSend = {
            "message": {
                "text": "등록되지 않은 업체입니다"
            }
        }
 
    return jsonify(dataSend)
 
 
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 8080)