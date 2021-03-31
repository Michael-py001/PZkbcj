# coding:utf-8
import sys
import io
import urllib.request
import http.cookiejar
from bs4 import BeautifulSoup
from http import cookiejar
import math
import base64
import re
import course_data_clear
import datetime
import get_time
import time



# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码
def handle_weekTime(time, is_danshuang):
    """
    使用
    元组转成列表，再排序
    :param time: [('', '', '1-5'), ('', '', '6-8')]
    :return:
    """
    new_list = []
    append_time = 1
    for each_time in time:
        if(append_time<6):
            list_time = list(each_time)
            new_list.append(list_time)
            append_time += 1
        else:
            break
    # print(new_list)
    sort_list = []
    temp_list = []

    final_str = ""  # 存放最终的结果
    if (len(new_list) >= 1):

        for one_time in new_list:

            for inner_time in one_time:
                if(inner_time!=""):
                    temp_list.append(inner_time)
                # print("inner_time:", inner_time)
                # if ("," in inner_time and is_danshuang == 0):

                if ("," in inner_time):  # 如果只有,逗号，则分开不排序
                    # print("逗号")
                    one_list = inner_time.split(",")

                    for i in one_list:
                        # sort_list_1 = []
                        # print(i)
                        if ("-" in inner_time):
                            # sort_list_1.append(i)
                            sort_list.append(i)
                        elif (i != ""):
                            sort_list.append(i)
                    if (is_danshuang != 0):
                        # print("!!!单双周！")
                        # print(sort_list)
                        # return sort_list
                        final_str = ",".join('%s' % id for id in sort_list)
                    else:
                        final_str = str(sort_list[0]) + "-" + str(sort_list[len(sort_list) - 1])
                        # print("###")
                        # print("sort_list:", sort_list)
                        final_str = ",".join('%s' % id for id in sort_list)  # 遍历sort_list，把所有元素改成字符串
                        # return  sort_list
                elif ("-" in inner_time and "," not in inner_time):
                    print("!!!")
                    one_list = inner_time.split("-")
                    for i in one_list:
                        sort_list_2 = []
                        if (i != ""):
                            sort_list.append(int(i))
                    sort_list.sort()  # 排序
                    if (is_danshuang != 0):
                        print("单双周！")
                        # print(sort_list)
                        # return sort_list
                    else:
                        final_str = str(sort_list[0]) + "-" + str(sort_list[len(sort_list) - 1])
                        # print("@@@")
                        # print(final_str)
                elif("-" in inner_time):
                    print("inner_time1:",inner_time)
                else:  # 如果只有一个数字
                    # print("只有一个数字：", inner_time)
                    if (inner_time != ""):
                        print("inner_time2:",inner_time)
                        sort_list.append(int(inner_time))
                        # final_str = str(sort_list[0]) + "-" + str(sort_list[len(sort_list) - 1])
                        final_str = ",".join('%s' % id for id in sort_list)

        if(len(sort_list)>2):
            # print("sort_list!111!:", sort_list)
            # print("temp_list:", temp_list)
            # print(type(sort_list[2]))
            temp_list_2 = []
            for i in sort_list:
                if (len(sort_list) > 5):
                    print("88888888")
                    final_str = str(sort_list[0]) + "-" + str(sort_list[len(sort_list) - 1])
                elif (int(sort_list[2]) - int(sort_list[1]) != 1):
                    final_str = ",".join(temp_list)
                # print(temp_list)

                # print(i)
            # print(temp_list)
            for item in temp_list:
                # print(item)
                # temp_list.append(item.spilt("-"))
                if("-" in item):
                    temp = item.split("-")
                    for i in temp:
                        temp_list_2.append(i)
                else:
                    temp_list_2.append(item)
            if ("20" in temp_list_2):
                # print("删除20周")
                temp_list_2.remove("20")
                # print("replace前",final_str)
                # print(type(final_str))
                final_str = final_str.replace(",20","")
                # print("replace后", final_str)
            # print("删除后temp_list_2：",temp_list_2)
            if(len(temp_list_2)>=4):

                if(temp_list_2[1]==temp_list_2[3]):
                    final_str = temp_list_2[0]+"-"+temp_list_2[len(temp_list_2)-1]
                    # print("final_str1:",final_str)
                elif (temp_list_2[0] == temp_list_2[2]):
                    final_str = temp_list_2[0] + "-" + temp_list_2[len(temp_list_2) - 1]
                    # print("final_str2:", final_str)
            # print("temp_list_2:",temp_list_2)
            # print("final_str:",final_str)
                    # else:
                    #     continue
                # final_str = str(sort_list[0]) + "-" + str(sort_list[len(sort_list) - 1])

        if("," in final_str):
            temp__same_list = final_str.split(",")
            if(temp__same_list[0]==temp__same_list[1]):
                final_str = temp__same_list[0]
        # print("final_str:", final_str)
        return final_str

        # return final_str
    else:
        # print(new_list)
        return str(new_list)

def handle_course_name(name_list):
    # print("name_list:",name_list)
    if(len(name_list)>1):
        same_index = [] #重复下标列表
        temp_list = [] #存放元组转为列表的内容
        for name in name_list:
            name = list(name)
            for temp in name:
                if(temp!=""and temp!="周次"):
                    temp_list.append(temp)
        # print("temp_list:",temp_list)
        for i in range(len(temp_list)):

            for j in range(i+1,len(temp_list)):
                # print(j)
                # print("i:",i,"j:",j)
                if(temp_list[j]==temp_list[i]):
                    if(j not in same_index):
                        same_index.append(j)
                        # print("重复index:",same_index,temp_list[j],temp_list[i])

                else:
                    continue

        # print("same_index:",same_index)
        # print("temp_list:",temp_list)
        temp_name_list = []
        for i in range(len(same_index)):
            temp_name_list.append(temp_list[i])
        # print("temp_name_list:",temp_name_list)
        if (len(same_index) != 0):
            for i in range(0,len(same_index)):
                temp_list.remove(temp_name_list[i])  # 删除index位置的元素
        #     for i in range(len(temp_list)):
        #         temp_list.pop(same_index[i]) #删除index位置的元素
        # print("最后结果：",temp_list)

        return temp_list
    elif(len(name_list)==1):
        print(list(name_list[0]))
        return list(name_list[0])
    else:
        return []

def handle_courseTime(time):
    """
    :param regex: ['[01-02-03-04节]', '[01-02-03-04节]'] // ['01-02-03-04节']
    :return:
    """
    # print(type(time))
    # print(len(time))
    # print("time:",time)
    if(len(time)==1):
        str_time = "".join(time).split("-")
        # print(str_time[0]+'-'+str_time[len(str_time)-1])
        final_time = str_time[0]+'-'+str_time[len(str_time)-1]
        # print(final_time)
        return final_time
    elif(len(time)>1):
        total_time_list=[]
        for i in time:
            str_time = "".join(i)
            total_time_list.append(str_time)
        first_time = total_time_list[0].split("-")
        last_time = total_time_list[len(total_time_list)-1].split("-") #先找出第一个和最后一个，取出头和尾拼接成01-04

        final_str = first_time[0] +"-"+ last_time[len(last_time)-1]
        # print(final_str)
        return  final_str
    else:
        return ""
def post_login(userName, password):
    """
    账号登录
    :param userName: 学号
    :param password: 密码
    :return: opener 带有cookie的
    """
    # userName = str(input("请输入学号"))
    # pwd = str(input("请输入密码"))

    userName = int(userName)
    pwd = str(password)
    # get_pwd(userName, pwd)
    # 登录时需要POST的数据
    data = {'userAccount': userName,
            'userPassword': '',
            'encoded': get_pwd(userName, pwd)  # 调用处理方法，转换数据
            }
    post_data = urllib.parse.urlencode(data).encode('utf-8')
    # print(post_data)

    # 设置请求头
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': 'http://qzjw.peizheng.edu.cn/jsxsd/'
    }

    # 登录时表单提交到的地址（用开发者工具可以看到）
    login_url = ' http://qzjw.peizheng.edu.cn/jsxsd/xk/LoginToXk'
    # 构造登录请求
    req = urllib.request.Request(login_url, headers=headers, data=post_data)
    # 构造cookie
    cookie = http.cookiejar.CookieJar()
    # 由cookie构造opener
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    # 发送登录请求，此后这个opener就携带了cookie，以证明自己登录过
    resp = opener.open(req)  # 此步骤必须有！！！
    # print(resp)
    # print(cookie)
    cookieStr = ""
    for item in cookie:
        cookieStr = cookieStr + item.name + "=" + item.value + ";"
    # 舍去最后一位的分号
    # print(cookieStr)

    # # 登录后才能访问的网页
    # url = 'http://qzjw.peizheng.edu.cn/jsxsd/framework/xsMain.jsp'
    #
    # # 构造访问请求
    # req = urllib.request.Request(url, headers=headers)
    #
    # resp = opener.open(req)
    # return opener  #返回带有cookie的opener
    def get_all_kebiao(week):
        '''
        查询全部课表，week不传
        此方法的入口为课表查询页
        :param week: 传入的第几周，不填则默认是全部
        :return: 返回一整理好的一周课表
        '''
        data = {'cj0701id: ': '',
                'zc': "",  # 周次week，不填则默认是全部
                'demo': '',
                'xnxq01id': '2018-2019-1',
                'sfFD': '1',
                'kbjcmsid': "94F0A92D34E04A4DE05347080A0A60EF",


                }
        post_data = urllib.parse.urlencode(data).encode('utf-8')

        # 设置请求头
        headers = {
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'http://qzjw.peizheng.edu.cn/jsxsd/xskb/xskb_list.do',
        }

        # 登录时表单提交到的地址（用开发者工具可以看到）
        login_url = 'http://qzjw.peizheng.edu.cn/jsxsd/xskb/xskb_list.do'

        # 构造登录请求
        req = urllib.request.Request(login_url, headers=headers, data=post_data)
        # 获取的网页数据
        resp = opener.open(req)  # 此处的opener是post_login的参数 带有cookie
        # 打印网页
        # print(resp.read().decode('utf-8'))
        soup = BeautifulSoup(resp, 'lxml', from_encoding='utf-8')
        # print(soup)
        table_tr = soup.find('table').find_all('tr')  # 取得所有tr行，一行包括星期1-5的课
        # print(table_tr[1])
        monday = []
        tuesday = []
        wednesday = []
        thurday = []
        firday = []
        satruday = []
        sunday = []
        hole_course = []
        id = 0
        course_name = [""]  # 保存不重复的课程名
        num_1 = 1  # 从1开始，过滤表头行

        for i in range(6):
            print(num_1)
            # 数据清洗
            tr_list_one = str(table_tr[num_1])  # 把findall取得的list转为str
            td_list = tr_list_one
            td_list_2 = re.sub('\n+', '', td_list)  # 去掉空行
            td_list_3 = "".join(td_list_2.split())  # 去掉空白
            # print(td_list_3)
            match = re.compile(r'<tdalign="center"height="28"valign="top"width="123">(.*?)</td>')
            final = match.findall(td_list_3)  # 取得每一个td的内容
            num_1 += 1
            # print(final)
            num = 0  # index递增
            # 获取每个div
            course_list_final = []

            for j in final:  # 在每个td里取出div的有用数据
                match_2 = re.compile(r'<div[^>]*>(.*?)</div>')
                final_2 = match_2.findall(final[num])
                # print("final_2:",final_2)
                course_list_final.append(final_2)  # 添加到新的数组
                num += 1
            # print(course_list_final)
            course_list_final_2 = []  # 清洗得到每一列的单一信息，去除重复display:none的数据
            for j in course_list_final:
                course_list_final_2.append(j[1])  # 去掉两条数据中的没用的一条
            # print(course_list_final_2)
            each_course = []
            # 搜索课程
            course_week = 0

            for h in course_list_final_2:
                course_week +=1
                is_danshuang = 0 #是否单双周
                print(h)
                if("双周" in h):
                    print("双周！")
                    is_danshuang = 2
                elif("单周" in h):
                    is_danshuang = 1
                list = {}
                # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                match_3 = re.compile(r'<fonttitle="老师">(.*?)</font>')
                final_3 = match_3.findall(h)
                if(len(final_3)>1):
                    final_3 = final_3[0]
                final_3="".join(final_3)
                print("final_3教师:",final_3)
                # match_4 = re.compile(r'<fonttitle="周次\(节次\)">(.*?)\(周\)')
                # match_4 = re.compile(r'>(\w-\w?),(\w+\w+)|(\w-\w+)\(')
                # match_4 = re.compile(r'>(\w-\w?),(\w+-\w+)\(') #处理1-2 有横杆的
                match_4 = re.compile(r'>([\w,\w]+)\(|(\w-\w)\(|(\w+-\w+),(\w+-\w+)|(\w+-\w+)\(',re.A) # 处理多种情况
                final_4 = match_4.findall(h)
                final_4 = handle_weekTime(final_4,is_danshuang)
                print("final_4周次：",final_4)
                week_list = []#处理判断单双周
                if(len(final_4)>2):
                    for week in final_4.split(","):
                        if("-" not in week):
                            # print("week:",week)
                            week_list.append(int(week))
                        elif("-" in week):
                            break
                    if(len(week_list)>2):
                        for i in range(len(week_list)):
                            if (week_list[i] % 2 == 0):
                                # print("偶数：", week_list[i])
                                is_danshuang = 2
                            elif (week_list[i] % 2 != 0):
                                # print("奇数：", week_list[i])
                                is_danshuang = 1
                            else:
                                is_danshuang = 0
                            # for j in range(i+1,len(week_list)):
                            #     if(week_list[j]%week_list[i]==0):
                            #         if(week_list[j]%2==0):
                            #             print("偶数：",week_list[j])
                            #             is_danshuang = 2
                            #         elif (week_list[j] % 2 != 0):
                            #             print("奇数：", week_list[j])
                            #             is_danshuang = 1
                            #     else:
                            #         print("!!!!!!!!!!!!!!!!!",week_list[j],week_list[i])
                            #         is_danshuang = 0
                            #         break
                # final_4 = handle_courseTime_regex(final_4)
                # match_7 = re.compile(r'\[(.*)节\]')
                match_7 = re.compile(r'\[(\w{0,2}[-\w]+)\w\]')
                final_7 = match_7.findall(h)
                final_7 = handle_courseTime(final_7)
                print("final_7节次：:",final_7)

                match_5 = re.compile(r'<fonttitle="教室">(.*?)</font>')
                final_5 = match_5.findall(h)
                if(len(final_5)>1):
                    final_5 = "".join(final_5[0])
                elif(len(final_5)==0 or len(final_5)==1):
                    final_5 = "".join(final_5)
                elif(len(final_5)>1):
                    final_5 = final_5[0]
                print("final_5教室：",final_5)
                match_6 = re.compile(r'(\w+)<span>|(\w+)?<br/>|(\w+).*\)<br/>|(\w+（\w）)')  # 课程名称 python中\w可以匹配中文，因为默认Unicode包含中文
                final_6 = match_6.findall(h)
                final_6 = handle_course_name(final_6)
                is_in_course_name = False #是否出现多个课程名称标记
                # if(len(final_6)==1):  #如果只有一个，把列表转换成字符串
                #     final_6 = "".join(final_6)
                for name in final_6:
                    if(name not in course_name ):
                        course_name.append(name)
                        # final_6 = name
                    elif(name in course_name ):
                        print("final_6:",final_6)
                        is_in_course_name = True
                        continue
                if(is_in_course_name==True):
                    print("final_6!!!!:",final_6)
                    if(final_6[0]==""):
                        print("11111")
                        final_6 = final_6[1]
                    elif(len(final_6)==1):
                        print("2222")
                        final_6 = "".join(final_6)
                    else:
                        print("3333")
                        final_6 = final_6[0]
                elif(len(final_6)==1):
                    final_6 = "".join(final_6)
                elif(len(final_6)==2):
                    print("2222222222")
                    try:
                        if(int(final_6[1])):
                            final_6 = final_6[0]
                    except:
                        final_6 = final_6[0]
                        print("final_6出错")
                print("final_6课程名称：",final_6)
                # print("所有课程：","final_3:",final_3,"final_4:",final_4,"final_5:",final_5,"final_6:",final_6,"final_7:",final_7)
                if (final_3 != "" and final_4 != "" and final_6 != "" and final_7 != ""):
                    # print(bool(final_3==""))
                    list["course_name"] = final_6
                    list["week_time"] = final_4
                    list["day_time"] = final_7
                    list["classroom"] = final_5
                    list["teacher_name"] = final_3
                    list["is_danshuang"] = is_danshuang
                    list["weekly_time"] = course_week
                    print("is_danshuang:",is_danshuang)
                    each_course.append(list)  # each_course是每一行的数据，需要提取整理成每一天
                    # print("~~~~~~~~~~~~~~~~~~~~~~~~~")
                elif(final_3==""):
                    continue
                # print(list)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~")

            # print(each_course) #每一行的课程名称
            # monday.append(each_course[0])
            # tuesday.append(each_course[1])
            # wednesday.append(each_course[2])
            # thurday.append(each_course[3])
            # firday.append(each_course[4])
            # satruday.append(each_course[5])
            # sunday.append(each_course[6])
            # print(each_course)
            # hole_course
            # print("course_name:",course_name)
            # 删除重复的课程
            show_num = 0
            for course in each_course:
                # print(course)
                if(course not in hole_course):
                    hole_course.append((course))
                else:
                    # print("跳过")
                    continue
        print(hole_course)
        same_course_time_list = [] #weekly_time保存拼接 20周专用
        same_index = []
        is_20_week = False
        for course in hole_course:
            if(course["week_time"] =="19" or course["week_time"]=="20"):
                print("20周！！")
                is_20_week = True
                same_index.append(hole_course.index(course))
                print("same_index:",same_index)
                same_course_time_list.append(int(course["weekly_time"]))

        same_course_time_list.sort()
        print("same_course_time_list:", same_course_time_list)
        print(hole_course)
        temp_name_list = []
        #提取出重复的课程，供下面remove
        for i in range(len(same_index)):
            temp_name_list.append(hole_course[same_index[i]])
        # print("temp_name_list:",temp_name_list)
        # print("@@:",hole_course[same_index[len(same_index)-1]])
        # 把20周的weekly_time拼接成一个
        if(is_20_week):
            hole_course[same_index[len(same_index) - 1]]["weekly_time"] = same_course_time_list
        # 去除重复的课程
        for j in range(len(same_index)-1):
            hole_course.remove(temp_name_list[j])


        # print(hole_course)
        # print("same_index:",same_index)
        # final_weekly_time = same_course_time_list[0]+"-"+same_course_time_list[len(same_course_time_list)-1]
        # hole_course[len(same_index)-1]["weekly_time"] = final_weekly_time
        # print(hole_course)


        # 添加ID
        for item in hole_course:
            item["id"] = id
            id +=1
        print(hole_course)
        # hole_week = {}  # 存放一整个星期每一天的课程信息
        # hole_week["星期一"] = monday
        # hole_week["星期二"] = tuesday
        # hole_week["星期三"] = wednesday
        # hole_week["星期四"] = thurday
        # hole_week["星期五"] = firday
        # hole_week["星期六"] = satruday
        # hole_week["星期日"] = sunday

        # print(hole_week)
        # day_course = course_data_clear.clear_data(each_course)
        # print(day_course)
        # return day_course  # 返回一个处理后的一周课表 类型为dict
    # 获取一周的课表 需要在login模块里使用
    def get_kebiao(week):
        '''
        此方法的入口为课表查询页
        :param week: 传入的第几周，不填则默认是全部
        :return: 返回一整理好的一周课表
        '''
        data = {'cj0701id: ': '',
                'zc': "",  # 周次week，不填则默认是全部
                'demo': '',
                'xnxq01id': '2020-2021-1',
                'sfFD': '1',
                'kbjcmsid': "94F0A92D34E04A4DE05347080A0A60EF",


                }
        post_data = urllib.parse.urlencode(data).encode('utf-8')

        # 设置请求头
        headers = {
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'http://qzjw.peizheng.edu.cn/jsxsd/xskb/xskb_list.do',
        }

        # 登录时表单提交到的地址（用开发者工具可以看到）
        login_url = 'http://qzjw.peizheng.edu.cn/jsxsd/xskb/xskb_list.do'

        # 构造登录请求
        req = urllib.request.Request(login_url, headers=headers, data=post_data)
        # 获取的网页数据
        resp = opener.open(req)  # 此处的opener是post_login的参数 带有cookie
        # 打印网页
        # print(resp.read().decode('utf-8'))
        soup = BeautifulSoup(resp, 'lxml', from_encoding='utf-8')
        # print(soup)
        table_tr = soup.find('table').find_all('tr')  # 取得所有tr行，一行包括星期1-5的课
        # print(table_tr[1])
        monday = []
        tuesday = []
        wednesday = []
        thurday = []
        firday = []
        satruday = []
        sunday = []
        num_1 = 1  # 从1开始，过滤表头行
        for i in range(7):
            # 数据清洗
            tr_list_one = str(table_tr[num_1])  # 把findall取得的list转为str
            td_list = tr_list_one
            td_list_2 = re.sub('\n+', '', td_list)  # 去掉空行
            td_list_3 = "".join(td_list_2.split())  # 去掉空白
            # print(td_list_3)
            match = re.compile(r'<tdalign="center"height="28"valign="top"width="123">(.*?)</td>')
            final = match.findall(td_list_3)  # 取得每一个td的内容
            num_1 += 1
            # print(final)
            num = 0  # index递增
            # 获取每个div
            course_list_final = []
            for i in final:  # 在每个td里取出div的有用数据
                match_2 = re.compile(r'<div[^>]*>(.*?)</div>')
                final_2 = match_2.findall(final[num])
                # print("final_2:",final_2)
                course_list_final.append(final_2)  # 添加到新的数组
                num += 1
            # print(course_list_final)
            course_list_final_2 = []  # 清洗得到每一列的单一信息，去除重复display:none的数据
            for j in course_list_final:
                course_list_final_2.append(j[1])  # 去掉两条数据中的没用的一条
            # print(course_list_final_2)
            each_course = []
            # 搜索课程
            for h in course_list_final_2:
                print(h)
                list = {}
                # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                match_3 = re.compile(r'<fonttitle="老师">(.*?)</font>')
                final_3 = match_3.findall(h)
                # print(final_3)
                match_4 = re.compile(r'<fonttitle="周次\(节次\)">(.*?)\(周\)')
                final_4 = match_4.findall(h)
                print("final_4周次：",final_4)
                # final_4 = handle_courseTime_regex(final_4)
                match_7 = re.compile(r'\[(.*)节\]')
                final_7 = match_7.findall(h)
                #
                print("final_7节次：:",final_7)

                match_5 = re.compile(r'<fonttitle="教室">(.*?)</font>')
                final_5 = match_5.findall(h)
                print("final_5教室：",final_5)
                match_6 = re.compile(r'^(\w*)')  # 课程名称 python中\w可以匹配中文，因为默认Unicode包含中文
                final_6 = match_6.search(h).group(1)
                print("final_6课程名称：",final_6)
                # 把列表转为字符串
                final_33 = "".join(final_3)
                final_44 = "".join(final_4)
                final_444 = final_44.replace("[", "").replace("]", "")
                final_55 = "".join(final_5)
                final_66 = "".join(final_6)
                final_77 = "".join(final_7)
                # print(final_6)
                list["课程名称"] = final_66
                list["周次"] = final_444
                list["节次"] = final_77
                list["教室"] = final_55
                list["老师"] = final_33
                each_course.append(list)  # each_course是每一行的数据，需要提取整理成每一天
                # print(list)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~")
            # print(each_course)
            monday.append(each_course[0])
            tuesday.append(each_course[1])
            wednesday.append(each_course[2])
            thurday.append(each_course[3])
            firday.append(each_course[4])
            satruday.append(each_course[5])
            sunday.append(each_course[6])

        hole_week = {}  # 存放一整个星期每一天的课程信息
        hole_week["星期一"] = monday
        hole_week["星期二"] = tuesday
        hole_week["星期三"] = wednesday
        hole_week["星期四"] = thurday
        hole_week["星期五"] = firday
        hole_week["星期六"] = satruday
        hole_week["星期日"] = sunday

        # print(hole_week)
        day_course = course_data_clear.clear_data(hole_week)
        # print(day_course)
        return day_course  # 返回一个处理后的一周课表 类型为dict

    #获取整个学期的课表
    def get_hole_kebiao():
        whole_week_course = {}
        week_num = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '十一', '十二', '十三', '十四', '十五', '十六', '十七', '十八',
                    '十九', "二十"]
        for i in range(8, 10):
            each_week_course = [get_kebiao(i)]  #调用函数
            # print(each_week_course)
            whole_week_course["第" + week_num[i] + "周"] = each_week_course
        # print(whole_week_course)
        # for i in whole_week_course:
        # print(whole_week_course["第一周"])
    # get_kebiao()
    get_all_kebiao(1)
    # get_hole_kebiao()
    # print(resp.read().decode('utf-8'))
    # get_hole_kebiao()
    #暂时不用的模块 从首页课表获取课名
    def get_kebiao_1():
        """
        此方法为获取首页的课表
        :return:
        """
        time = datetime.datetime.now().strftime('%Y-%m-%d')
        data = {'rq': str(time),
                'sjmsValue': '94F0A92D34E04A4DE05347080A0A60EF',

                }
        post_data = urllib.parse.urlencode(data).encode('utf-8')

        # 设置请求头
        headers = {
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': 'http://qzjw.peizheng.edu.cn/jsxsd/framework/xsMain_new.jsp?t1=1',
            'X - Requested - With': 'XMLHttpRequest'
        }

        # 登录时表单提交到的地址（用开发者工具可以看到）
        login_url = 'http://qzjw.peizheng.edu.cn/jsxsd/framework/main_index_loadkb.jsp'

        # 构造登录请求
        req = urllib.request.Request(login_url, headers=headers, data=post_data)
        # 获取的网页数据
        resp = opener.open(req)
        # 打印网页
        # print(resp.read().decode('utf-8'))
        soup = BeautifulSoup(resp, 'html5lib', from_encoding='utf-8')
        # print(soup)
        course = soup.find_all("p")
        # print(course)
        # print(resp)
        course_list = []  # 存放初始数据
        for i in course:
            data = i['title']
            new_data = data.replace('<br/>', "")
            course_list.append(new_data)
        # print(course_list)
        for i in course_list:
            print(i, end='\n')

        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        new_course_list = []
        for j in course_list:
            if j not in new_course_list:
                new_course_list.append(j)
        for i in new_course_list:
            print(i, end='\n')

    #获取个人信息
    def get_info():
        """
        此方法为获取个人信息
        :return:
        """

        # 设置请求头
        headers = {
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
            'Referer': 'http://qzjw.peizheng.edu.cn/jsxsd/framework/xsMain.jsp',
        }
        # 登录时表单提交到的地址（用开发者工具可以看到）
        login_url = 'http://qzjw.peizheng.edu.cn/jsxsd/framework/xsMain_new.jsp?t1=1'
        # 构造请求  GET方法不用传入data
        req = urllib.request.Request(login_url, headers=headers)
        # 获取的网页数据
        resp = opener.open(req)
        # 打印网页
        # print(resp.read().decode('utf-8'))
        soup = BeautifulSoup(resp, 'lxml', from_encoding='utf-8')
        # print(soup)
        course = soup.find_all("div",class_='middletopdwxxcont')   #寻找div的内容
        info = {}
        name = ["姓名","学号","院系","专业","班级"]
        index = 0
        for i in course[1:]:  #第一个div为空字符，从下标1开始
            # print(name[index])
            info[name[index]] = i.get_text()
            index +=1
        print(info)


    get_info()
    # get_kebiao()
    # 获取成绩的模块 需要在login模块里使用
    def get_grade(time):
        """

        :param time: 学期  #2019-2020-1
        :return:
        """
        term = str(time)
        data = {'kksj': term,
                'kcxz': '',
                'kcmc': '',
                'xsfs': 'all'

                }
        post_data = urllib.parse.urlencode(data).encode('utf-8')

        # 设置请求头
        headers = {
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'http://qzjw.peizheng.edu.cn/jsxsd/kscj/cjcx_query',
            'X - Requested - With': 'XMLHttpRequest'
        }

        # 登录时表单提交到的地址（用开发者工具可以看到）
        login_url = 'http://qzjw.peizheng.edu.cn/jsxsd/kscj/cjcx_list'
        # 构造登录请求
        req = urllib.request.Request(login_url, headers=headers, data=post_data)
        # 获取的网页数据
        resp = opener.open(req)
        # soup2 = BeautifulSoup(resp, 'html5lib', from_encoding='utf-8').prettify()
        soup = BeautifulSoup(resp, 'lxml', from_encoding='utf-8')
        #找到GPA
        GPA_match = re.findall(r"平均学分绩点:(.*) 平均学分绩点",str(soup))
        GPA = "".join(GPA_match).strip()  #转为字符串，去掉空白

        # 从页面中找到table中的每个tr
        each_course = soup.find('table').find_all('tr')[1:]
        # each_course
        # print(each_course)
        big_list = []
        for i in each_course:
            # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            # b = str(i).strip()
            b = re.sub("\n+", " ", str(i))  # 去掉空行
            c = ''.join(b.split())  # 去掉空白

            match = re.compile(r'<td[^>]*>(.*?)</td>')  # 找到td中的内容
            final = match.findall(c)
            # print(final)
            # print("科目："+final[3]+" 成绩："+final[5]+" 等级："+final[6]+" 学分："+final[9]+" 类型："+final[16])
            each_dict = {}
            each_dict["科目"] = final[3]
            each_dict["成绩"] = final[5]
            each_dict["等级"] = final[6]
            each_dict["学分"] = final[9]
            each_dict["类型"] = final[16]
            # 添加到大数组
            big_list.append(each_dict)
        #添加GPA到list
        big_list.append({"GPA": GPA})
        # print(big_list)
        return big_list
    #获取所有学期的成绩
    def get_hole_grade():
        #学号
        user_num = userName
        #调用方法，获取学号前四位，学期数
        term_data = get_time.get_time(user_num)
        #获取学期数
        term_num = get_time.get_data(term_data[0],term_data[1])
        index = 0
        big_list = {}
        for i in term_num:
            big_list[term_num[index]] = get_grade(i)
            index +=1
        print(big_list)
        return big_list

    # get_hole_grade()


def get_pwd(userName, pwd):
    '''
    处理encode的模块
    :param userName: 学号
    :param pwd: 密码
    :return: 返回处理后的encode
    '''
    # 学号加密处理
    user_name = str(userName)
    bytes_name = user_name.encode("utf-8")
    bs64_name = str(base64.b64encode(bytes_name))
    # 密码加密处理
    pwd = str(pwd)
    bytes_pwd = pwd.encode("utf-8")
    bs64_pwd = str(base64.b64encode(bytes_pwd))
    # 获取处理后的数据
    match = re.compile(r"\b'(.*)\'")
    result_name = str(match.findall(bs64_name)[0])
    result_pwd = str(match.findall(bs64_pwd)[0])
    # 拼接字符串
    final_result = result_name + "%%%" + result_pwd
    # 返回数据
    return final_result


# get_pwd(201751709114,'19980203qqqq')
if __name__ == '__main__':
    time1 = time.time()
    post_login(201751709088, 'hwt15220725649')
    time2 = time.time()

    print("耗时：%f秒"%(time2-time1))

