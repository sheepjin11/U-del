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
                "text": "BHC 울산범서점 정보입니다 전화번호 : 052-245-1922, 운영 시간 : 12시 - 24시, 2마리 이상 배달가능 감사합니다",
                "message_button": {
                      "label": "메뉴판 보기",
                       "url": "http://mbymadmin.reddot.kr/data/upload/12247/0.jpg"
                }
            }
                
        }
    elif u"깻잎" in content:
        dataSend = {
            "message": {
                "text": "깻잎칩킨 울산범서점 정보입니다 전화번호 : 052-223-8844, 운영 시간 : 17시 - 26시, 감사합니다",
                "message_button": {
                      "label": "메뉴판 보기",
                       "url": "http://mbymadmin.reddot.kr/data/upload/20332/8561_FILE1.jpg"
                }
            
            }
        }    
    elif u"비버스" in content:
        dataSend = {
            "message": {
                "text": "비버스치킨 천상구영점 정보입니다 전화번호 : 052-246-5582, 운영 시간 : 17시 - 26시, 감사합니다",
                "message_button": {
                      "label": "메뉴판 보기",
                       "url": "http://wiki.unist.in/wiki/images/0/04/%EB%B9%84%EB%B2%84%EC%8A%A4_%EC%B9%98%ED%82%A8_%EB%A9%94%EB%89%B4.png"
                }
            
            }
                    
        }
    elif u"치킨파티" in content:
        dataSend = {
            "message": {
                "text": "치킨파티 천상구영점 정보입니다 전화번호 : 052-247-9300, 운영 시간 : 11시 - 26시, 감사합니다",
                "message_button": {
                      "label": "메뉴판 보기",
                      "url": "www.googledrive.com/host/1Z16DliYBv9D9m5g9qJ80z5g9EtKkAk7e/치킨파티.jpg"
                }
            
            }
                    
        }
    elif u"쌀을품은닭" in content:
        dataSend = {
            "message": {
                "text": "쌀을 품은 닭 천상구영점 정보입니다 전화번호 : 052-211-9274, 운영 시간 : 시, 감사합니다",
                # "message_button": {
                #       "label": "메뉴판 보기",
                #       "url": "file:///Users/YJ/Downloads/KakaoTalk_Photo_2017-11-07-20-13-23.jpeg"
                # }
            
            }
                    
        }
    elif u"올꼬꼬" in content:
        dataSend = {
            "message": {
                "text": "올꼬꼬 천상구영점 정보입니다 전화번호 : 052-212-9989, 운영 시간 : 17시 - 26시, 감사합니다",
                "message_button": {
                      "label": "메뉴판 보기",
                      "url": "https://lh3.googleusercontent.com/_uWoiDCRu4qoctIsFhwvw-Z2Hwa-Wv4B5oA-X25Tbw3aZKjOSldIAxzFzIQivsA7-NdB31J6O7oH6js=w2230-h1192-rw"
                }
            
            }
                    
        }
    elif u"구어조은닭" in content:
        dataSend = {
            "message": {
                "text": "구어조은닭 천상구영점 정보입니다 전화번호 : 052-245-9279, 운영 시간 : 17시 - 25시, 감사합니다",
                "message_button": {
                      "label": "메뉴판 보기",
                      "url": "https://lh6.googleusercontent.com/baKFosavnteOtYj77ueljHH37_4o8kYT-En8ExcPmdhLbPMN5ySEv9MCpMlr9Aud0dCxLg5foBGpfV8=w2230-h1280-rw"
                }
            
            }
                    
        }
    elif u"기똥찬" in content:
        dataSend = {
            "message": {
                "text": "기똥찬 파닭 정보입니다 전화번호 : 052-245-9281, 운영 시간 : 18시 - 25시, 2인분 이상 배달가능 감사합니다",
                "message_button": {
                      "label": "메뉴판 보기",
                      "url": "https://lh3.googleusercontent.com/tKwg-d6Kd664VrrutyHm3eJlBuIDgXmfLynYsgaj9MdtrPjCkBxiqQS_zEZYP_fY7_UYejINkMkjDzg=w2230-h1192-rw"
                }
            
            }
                    
        }
    elif u"쫄파촌닭" in content:
        dataSend = {
            "message": {
                "text": "쫄파촌ㄷ 정보입니다 전화번호 : 052-245-9281, 운영 시간 : 18시 - 25시, 2인분 이상 배달가능 감사합니다",
                "message_button": {
                      "label": "메뉴판 보기",
                      "url": "https://lh6.googleusercontent.com/QsdBOUPK9QEsaaeO5dYW4W1NOCFREmF1qVf2-wBdGcqS6CRzmPoqQ7HsIIdT9yI85UkLgPjA=w2230-h1192-rw"
                }
            
            }
                    
        }
    elif u"기똥찬" in content:
        dataSend = {
            "message": {
                "text": "기똥찬 파닭 정보입니다 전화번호 : 052-245-9281, 운영 시간 : 18시 - 25시, 2인분 이상 배달가능 감사합니다",
                "message_button": {
                      "label": "메뉴판 보기",
                      "url": "https://lh3.googleusercontent.com/tKwg-d6Kd664VrrutyHm3eJlBuIDgXmfLynYsgaj9MdtrPjCkBxiqQS_zEZYP_fY7_UYejINkMkjDzg=w2230-h1192-rw"
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