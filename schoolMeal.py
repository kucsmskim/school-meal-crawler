import requests
from bs4 import BeautifulSoup

#class SchoolMeal:


def getMenuBoard(num, day):
    # 크롤링 할 웹페이지 url
    url = 'https://www.koreapas.com/bbs/sik.php?back=1'
    # 위 url에 request를 보냄(get 방식)
    source_code = requests.get(url)
    # 해당 url의 소스 코드
    html = source_code.content
    # BeautifulSoup로 보기 쉽게 정리
    soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
    # 여기서 저는 학생회관 1층 식단을 뽑을 것
    name = ''
    if num == 0:
        # 애기능 생활관 2층(not implemented)
        name = '애기능 생활관'
    elif num == 1:
        # 안암학사 관리동 1층(not implemented)
        name = '기숙사'
    elif num == 2:
        # 산학관 1층(not implemented)
        name = '산학관'
    elif num == 3:
        # 교우회관 지하 1층(not implemented)
        name = '교우회관'
    elif num == 4:
        # 학생회관 1층
        name = '학생회관'
        menu = HakGuan(soup)

    getDayMenu(menu, name, day)


# HakGuan - 학생회관 1층의 학식 정보를 얻어오는 함수
def HakGuan(soup):
    # part에 'ol' 태그 안의 'li' 태그 안의 내용을 불러옴
    part = soup.select('ol > li')
    # 날짜는 따로 긁어오지 않아도 됨
    days = ['월', '화', '수', '목', '금', '토']
    # 메뉴를 담을 리스트 생성(가공 전)
    rawMenu = []
    # part 내에서 각각..
    for i in part:
        # 요일, 날짜 빼고 식단만
        rawMenu_t = i.select('div > p')
        # 그걸 rawMenu에 저장
        rawMenu.append(rawMenu_t)
    # 여러 개 중, 필요한 건 마지막 6개
    rawMenu = rawMenu[-6:]
    # menu를 담을 List
    menuList = []
    for foods in rawMenu:
        # 하루의 메뉴를 담을 리스트
        menu = []
        # 태그 내의 text를 가져옴, [0]은 list type이라서 붙임
        for i in range(len(foods[0].contents)):
            # 짝수 번째 요소들만 뽑기
            if i%2 == 0:
                menu.append(foods[0].contents[i])
        # 하루의 메뉴를 메뉴 리스트에 붙임
        menuList.append(menu)
    # 메뉴판 생성(dictonary 타입)
    board = {}
    # 요일 별로 메뉴판에 담기
    for i in range(len(menuList)):
        board[days[i]] = menuList[i]
    # 메뉴판을 반환
    return board


def getDayMenu(board, name, day):
    print(' _________________________')
    print('|   %s %s요일 메뉴  |' %(name, day))
    print('|_________________________|')
    for food in board[day]:
        print(' %13s ' %(food))

if __name__ == '__main__':
    # 학식 메뉴판을 받아오는 함수 getMenuBoard(num)
    # num --> 0: 애기능, 1: 안암학사(기숙사), 2: 산학관, 3: 교우회관, 4: 학생회관
    # 목요일
    getMenuBoard(4, '금')



'''
환경?
와이파이 어떻게 하지?
1. python 3.6.8 다운로드(맨 아래에 Windows x86 web-based installer, 맨 처음에 add Python 3.6 to PATH)
2. cmd에서 pip install requests
3. cmd에서, cd Desktop, mkdir mython, cd mython, code .
4. ctrl+`(1 왼쪽에)누르면 아래 terminal이 나옴
5. touch hello.py
6. 예제코드: print("Hello, World!") 작성
7. 아래 터미널에, python hello.py --> Hello, World! 출력 시, 환경 설정 완료

1. cmd에서 pip install beautifulsoup4
2. touch schoolMeal.py
3. 예제 코드: from bs4 import BeautifulSoup 
4. 아래 터미널에, python schoolMeal.py --> 아무 것도 안뜨면 됨
'''

'''
이건 장소, 이용시간, 전화번호 뽑는 코드
    # 여기서 고파스 들어가서 ctrl+f해서 <dd> 등등 보여주기
    # 이건 가져올 정보들의 목록
    rawIndex = soup.select('dl > dt')
    # 가공된 index를 담을 공간
    index_p = []
    # 각 raw index를 가공해서 index_p에 담음
    for data in rawIndex:
        index_p.append(data.string)
    # set을 이용해서 중복을 제거
    index_s = set(index_p)
    # 다루기 쉽게 하기 위해 다시 list로
    index = list(index_s)
    # 이제 실제 정보를 가져옴
    rawInfo = soup.select('dl > dd')
    # 가공한 정보를 담을 공간
    info = []        
    # 다시 가공
    for data in rawInfo:
        # None은 필요 없음
        if data.string != None:
            # None을 제외한 list 생성
            info.append(data.string.split(': ')[1])
    # 규칙 발견하기 --> 0 3 6 9 12: 위치, 1 4 7 10 13: 이용시간, 2 5 8 11 14: 연락처, zero base
    # 3n -> 위치, 3n + 1 -> 이용시간, 3n + 2 -> 연락처
#    for i in range(len(info)):
#        print(str(i) + ": " + info[i])
    # 각 index를 담을 list 생성
    place = []
    time = []
    phone = []
    for i in range(len(info)):
        if i%3 == 0:
            place.append(info[i])
        elif i%3 == 1:
            time.append(info[i])
        elif i%3 == 2:
            phone.append(info[i])
'''
