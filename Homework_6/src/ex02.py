import re

def solution(files):
    answer = sorted(files, key=lambda x: (re.findall('\D+', x.lower())[0], int(re.findall('\d+', x.lower())[0])))
    return answer


print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]))
print(solution(['muzi1.txt', 'MUZI1.txt', 'muzi001.txt', 'muzi1.TXT']))