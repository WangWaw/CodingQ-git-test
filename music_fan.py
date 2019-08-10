
#######单独使用beautifulsoup不能爬取动态网页的全部数据#######

from bs4 import BeautifulSoup
import requests
import csv
import time


for i in range(0, 1330, 35):
    print(i)
    time.sleep(2)
    # 网易云音乐歌单首页的url
    url = 'https://music.163.com/#/discover/playlist?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0' + str(i)
    # 单独使用BS得不到想要的数据，以下部分无效，删除
    #headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

    # headers = {
    #     ':authority': 'music.163.com',
    #     ':method': 'GET',
    #     ':path': '/discover/playlist?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0',
    #     ':scheme': 'https',
    #     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    #     'accept-encoding': 'gzip, deflate, br',
    #     'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    #     'cookie': 'mail_psc_fingerprint=83c63da580d3f9bd7603e0f0da364b5d; _iuqxldmzr_=32; _ntes_nnid=885ee14c27db8b6f6bc850358c7971c2,1550208206194; _ntes_nuid=885ee14c27db8b6f6bc850358c7971c2; WM_TID=UhDbwgA4N2VFFFVQQEctle2qluALJCNL; usertrack=CrHuclxnaYQI+rzTAymzAg==; nts_mail_user=lqbzyx2011@163.com:-1:1; playliststatus=visible; __oc_uuid=a2b06d70-7d39-11e9-b198-bbef682d23cf; NTES_CMT_USER_INFO=104112483%7Cwangwenhan92%40126.com%7Chttp%3A%2F%2Fcms-bucket.nosdn.127.net%2F2018%2F08%2F13%2F078ea9f65d954410b62a52ac773875a1.jpeg%7Cfalse%7Cd2FuZ3dlbmhhbjkyQDEyNi5jb20%3D; NTES_PASSPORT=1Wql88GOq8sMAsWWEw_Aq3FCjz_vWfKlhMGr2IBF3Bkv3hTL9O6EaHrgi0XjuO2dZtAdeiYJ1rXcBWKgeMk9ACTLQOII3PCjfxOabia6jd54hsPR.Hbo.iUQJs2nBzaOx77w3RcrVJMng_IBSAq88MLKTtQD.e9CbPMRnv3L0YMayIEKu3U1wvkHx; SERVER_ID=50; TOKEN=zJn3aD3VTmqijCUH; P_INFO=wangwenhan92@126.com|1564294999|0|mail126|00&99|shh&1564055886&mail126#shh&null#10#0#0|&0|mail126|wangwenhan92@126.com; MUSIC_EMAIL_U=062dca53a1a725cf5f7fd1e26fc2929ded19902973ea9ffdd4cf223193c8a8a33762595d2b67e9d292d799b2a366e631f214373604ecb38ff2f513a9c38b5dc7; NTES_SESS=aBNaZwtp4b1QR5YNHie1_VVfDy0askO028N.BN5vtsW_TirgUzYxslh.PV9mdzCGqudSWAOY302qbG2viGEsyxmgUrsc7OizCB1lstZ1n8sxsw1EmeQp.p6C.CBYYIBPRYwJkGcZSUF8tKLbtAWpjT8DHXm3dCAtWT8MjkdoD0RLNE3euRwSpn4MrcpRcPhQSdNPbdDn7UVrg; S_INFO=1565183111|1|0&60#3&80#|lqbzyx2011; ANTICSRF=a6ce64c5e758da3f3738c48be64befc6; WM_NI=o1IWsI4e14U77xD2qO%2BrlwyKVSsOBr%2BdGhPWAqdUXV3e%2Fpsh%2BeGTi12AJlgDncXhG9GyPGFeAs1j%2BVSKpA%2BY1caIx1EmgxoZz1Hz%2Bl8QF7WDgRsGv1pjjfiaWP6WOKPfdlk%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed3e152a2b0ae91e86db49a8ab6c54f869f9f85b73391e89eafd6649497aab7ee2af0fea7c3b92aadef87b8f243f8bbffd5d83df5a88cd3f445e9aea498fc41968dbdb0c17ae9bc8989d35d83afacb6db5ef1bbe191f264e9bb89b5ec3bf29f868de650aebd9889c63385a7a0a8c56f83adff8baa5e9195c0a2aa53f3bdafaafb3b87b3a999ee52baef889baa68fc8f8ad8d650a58ebda8f53bb4b6a687ec6b9590fab8ce4194baac8dea37e2a3; JSESSIONID-WYYY=PIrqhYO660UUPhCsDVH5wje6v43m%2BVVu6lz4XgXwU%2BMWlqyhlb7RBS%2FFfCSTmxj%5C1pqlj0%5C6JC6WP%5CDt9h7xh6R9lgpkRGY0zeOR%2BeQaJBp%2BB3sgHtgnkCAv90bdPJC0orF6wcV%2F2uBkqY8QZcx2o22r2JXnZFf0wD6DBQ49eX%2FQXWfO%3A1565273358528',
    #     'referer': 'https://music.163.com/',
    #     'sec-fetch-mode': 'nested-navigate',
    #     'sec-fetch-site': 'same-origin',
    #     'upgrade-insecure-requests': '1',
    #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    # }
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'cookie': 'mail_psc_fingerprint=83c63da580d3f9bd7603e0f0da364b5d; _iuqxldmzr_=32; _ntes_nnid=885ee14c27db8b6f6bc850358c7971c2,1550208206194; _ntes_nuid=885ee14c27db8b6f6bc850358c7971c2; WM_TID=UhDbwgA4N2VFFFVQQEctle2qluALJCNL; usertrack=CrHuclxnaYQI+rzTAymzAg==; nts_mail_user=lqbzyx2011@163.com:-1:1; playliststatus=visible; __oc_uuid=a2b06d70-7d39-11e9-b198-bbef682d23cf; NTES_CMT_USER_INFO=104112483%7Cwangwenhan92%40126.com%7Chttp%3A%2F%2Fcms-bucket.nosdn.127.net%2F2018%2F08%2F13%2F078ea9f65d954410b62a52ac773875a1.jpeg%7Cfalse%7Cd2FuZ3dlbmhhbjkyQDEyNi5jb20%3D; NTES_PASSPORT=1Wql88GOq8sMAsWWEw_Aq3FCjz_vWfKlhMGr2IBF3Bkv3hTL9O6EaHrgi0XjuO2dZtAdeiYJ1rXcBWKgeMk9ACTLQOII3PCjfxOabia6jd54hsPR.Hbo.iUQJs2nBzaOx77w3RcrVJMng_IBSAq88MLKTtQD.e9CbPMRnv3L0YMayIEKu3U1wvkHx; SERVER_ID=50; TOKEN=zJn3aD3VTmqijCUH; P_INFO=wangwenhan92@126.com|1564294999|0|mail126|00&99|shh&1564055886&mail126#shh&null#10#0#0|&0|mail126|wangwenhan92@126.com; MUSIC_EMAIL_U=062dca53a1a725cf5f7fd1e26fc2929ded19902973ea9ffdd4cf223193c8a8a33762595d2b67e9d292d799b2a366e631f214373604ecb38ff2f513a9c38b5dc7; NTES_SESS=aBNaZwtp4b1QR5YNHie1_VVfDy0askO028N.BN5vtsW_TirgUzYxslh.PV9mdzCGqudSWAOY302qbG2viGEsyxmgUrsc7OizCB1lstZ1n8sxsw1EmeQp.p6C.CBYYIBPRYwJkGcZSUF8tKLbtAWpjT8DHXm3dCAtWT8MjkdoD0RLNE3euRwSpn4MrcpRcPhQSdNPbdDn7UVrg; S_INFO=1565183111|1|0&60#3&80#|lqbzyx2011; ANTICSRF=a6ce64c5e758da3f3738c48be64befc6; WM_NI=o1IWsI4e14U77xD2qO%2BrlwyKVSsOBr%2BdGhPWAqdUXV3e%2Fpsh%2BeGTi12AJlgDncXhG9GyPGFeAs1j%2BVSKpA%2BY1caIx1EmgxoZz1Hz%2Bl8QF7WDgRsGv1pjjfiaWP6WOKPfdlk%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed3e152a2b0ae91e86db49a8ab6c54f869f9f85b73391e89eafd6649497aab7ee2af0fea7c3b92aadef87b8f243f8bbffd5d83df5a88cd3f445e9aea498fc41968dbdb0c17ae9bc8989d35d83afacb6db5ef1bbe191f264e9bb89b5ec3bf29f868de650aebd9889c63385a7a0a8c56f83adff8baa5e9195c0a2aa53f3bdafaafb3b87b3a999ee52baef889baa68fc8f8ad8d650a58ebda8f53bb4b6a687ec6b9590fab8ce4194baac8dea37e2a3; JSESSIONID-WYYY=PIrqhYO660UUPhCsDVH5wje6v43m%2BVVu6lz4XgXwU%2BMWlqyhlb7RBS%2FFfCSTmxj%5C1pqlj0%5C6JC6WP%5CDt9h7xh6R9lgpkRGY0zeOR%2BeQaJBp%2BB3sgHtgnkCAv90bdPJC0orF6wcV%2F2uBkqY8QZcx2o22r2JXnZFf0wD6DBQ49eX%2FQXWfO%3A1565273358528',
        'referer': 'https://music.163.com/',
        'sec-fetch-mode': 'nested-navigate',
        'sec-fetch-site': 'same-origin',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    }

    # headers = {
    #     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    #     'accept-encoding': 'gzip, deflate, br',
    #     'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    #     'cache-control': 'max-age = 0',
    #     'cookie': 'mail_psc_fingerprint=83c63da580d3f9bd7603e0f0da364b5d; _iuqxldmzr_=32; _ntes_nnid=885ee14c27db8b6f6bc850358c7971c2,1550208206194; _ntes_nuid=885ee14c27db8b6f6bc850358c7971c2; WM_TID=UhDbwgA4N2VFFFVQQEctle2qluALJCNL; usertrack=CrHuclxnaYQI+rzTAymzAg==; nts_mail_user=lqbzyx2011@163.com:-1:1; playliststatus=visible; __oc_uuid=a2b06d70-7d39-11e9-b198-bbef682d23cf; NTES_CMT_USER_INFO=104112483%7Cwangwenhan92%40126.com%7Chttp%3A%2F%2Fcms-bucket.nosdn.127.net%2F2018%2F08%2F13%2F078ea9f65d954410b62a52ac773875a1.jpeg%7Cfalse%7Cd2FuZ3dlbmhhbjkyQDEyNi5jb20%3D; NTES_PASSPORT=1Wql88GOq8sMAsWWEw_Aq3FCjz_vWfKlhMGr2IBF3Bkv3hTL9O6EaHrgi0XjuO2dZtAdeiYJ1rXcBWKgeMk9ACTLQOII3PCjfxOabia6jd54hsPR.Hbo.iUQJs2nBzaOx77w3RcrVJMng_IBSAq88MLKTtQD.e9CbPMRnv3L0YMayIEKu3U1wvkHx; SERVER_ID=50; TOKEN=zJn3aD3VTmqijCUH; P_INFO=wangwenhan92@126.com|1564294999|0|mail126|00&99|shh&1564055886&mail126#shh&null#10#0#0|&0|mail126|wangwenhan92@126.com; MUSIC_EMAIL_U=062dca53a1a725cf5f7fd1e26fc2929ded19902973ea9ffdd4cf223193c8a8a33762595d2b67e9d292d799b2a366e631f214373604ecb38ff2f513a9c38b5dc7; NTES_SESS=aBNaZwtp4b1QR5YNHie1_VVfDy0askO028N.BN5vtsW_TirgUzYxslh.PV9mdzCGqudSWAOY302qbG2viGEsyxmgUrsc7OizCB1lstZ1n8sxsw1EmeQp.p6C.CBYYIBPRYwJkGcZSUF8tKLbtAWpjT8DHXm3dCAtWT8MjkdoD0RLNE3euRwSpn4MrcpRcPhQSdNPbdDn7UVrg; S_INFO=1565183111|1|0&60#3&80#|lqbzyx2011; ANTICSRF=a6ce64c5e758da3f3738c48be64befc6; WM_NI=9%2Buph0BF7FdLxniQewLypyUIsHNBcZTrzADIZEEzbpmh2%2Bue2TEG%2BWNSpRVA6%2F6FifJwC8rCQ3CHYsCOZc6NQnLupRMZEgvAezSM8YTbjbDr9Ou9UFmmyJqGKSfEAPFuTTU%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee96e761b6a7b7a5dc48839a8ea6c44e828a8eafbb3385f1ad9bca339ab69e8ff52af0fea7c3b92afbf5bb91eb3c829af9a7e748bcb2a7b2e87d90a7c09ad843b19882a3e25298aeb6a2c7439a9b8b9be17cafb8feccf86ff28c8ba8aa5d8e8dc0b3d54bf6f1faa7ec6e8aa98dd9f14993ed8da9dc7981919684b54693b28496f35a8f868b88f54ba7a69daebb5398bea683c77afb91bbdad84eafb3b7abf44d898daaa6c45c86ab9cb5d837e2a3; JSESSIONID-WYYY=JTMeIANCzmO62XFXV4C5OGsUyB04DJOMP%2BpKm9zoBQehCWoZN%2FaD16Xpaule7%5CGoobuJPVNCo2Arlcy%2BQph1qIoIqqcl6Kgj0%2B9%2BKBRsriwuyiRx6%5CeFAvXQeDvzDOy8at2k%5C2HokkpTpFjAPFUtP0a%5CzZ2A7A4GXGG9uNZ0NQWPVOn2%3A1565451364868',
    #     'sec-fetch-mode': 'navigate',
    #     'sec-fetch-site': 'none',
    #     'sec-fetch-user': '?1',
    #     'upgrade-insecure-requests': '1',
    #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    # }
    # 创建储存歌单的文件
    # csv_file = open("playlist.csv", "w", encoding='utf-8-sig', newline='')
    # writer = csv.writer(csv_file)
    # writer.writerow(['标题', '播放数', '链接'])

    response = requests.get(url=url, verify=False, headers=headers)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    lis = soup.select('#m-pl-container')
    # print(len(lis))

    for j in range(len(lis)):
        # 获取播放数
        nb = lis[i].select('.nb')[0].get_text()
        if '万' in nb and int(nb.split("万")[0]) > 1000:
            # 获取播放数大于1000万的歌单封面
            msk = lis[j]['href']
            title = lis[j]['title']
            # 把封面标题，连接，播放数写到文件
            with open("playlist.csv", "w", encoding='utf-8-sig', newline='') as f:
                f.write(title + ',' + msk + ',' + nb + ' ')



