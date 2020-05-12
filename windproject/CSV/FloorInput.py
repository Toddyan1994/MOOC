# floorinput.py 统计公寓楼户型
import csv
#调用csv模块
with open(r'windproject\CSV\assets.csv', 'a', newline='',encoding='GBK') as csvfile:
    #调用open()函数打开csv文件，传入参数：文件名“assets.csv”、追加模式“a”、newline=''。
    writer = csv.writer(csvfile, dialect='excel')
    # 用csv.writer()函数创建一个writer对象。
    header=(['小区名称', '地址', '建筑年份', '楼栋', '单元', '户室', '朝向', '面积'])
    writer.writerow(header)
    

title=input('请输入小区名称：')
address=input('请输入小区地址：')
year=input('请输入小区建造年份：')
block=input('请输入楼栋号：')


unit_loop = True
while unit_loop ==True:
    unit=input('请输入单元号：')
    start_floor=input('请输入起始楼层：')
    end_floor=input('请输入终止楼层：')

        # 开始输入模板数据
    input('接下来请输入起始层每个房间的门牌号、南北朝向及面积，按任意键继续')

    start_floor_rooms = {}
    floor_last_number = []
    
    room_loop = True
    while room_loop == True:
        last_number = input('请输入起始楼层户室的尾号:（如01，02）')
        floor_last_number.append(last_number)
        room_number = start_floor + last_number
        
        direction = int(input(f'请输入 {room_number} 的朝向(南北朝向输入1，东西朝向输入2)：' ))
        area = int(input(f'请输入 {room_number} 的面积，单位 ㎡ ：'))

        start_floor_rooms[room_number] = [direction, area]
        
        continued = input('是否需要输入下一个尾号？按 n 停止输入，按其他任意键继续：')

        if continued == 'n':
            room_loop = False
        else:
            room_loop = True
    
    unit_rooms = {}
    unit_rooms[start_floor] = start_floor_rooms
    
    for intfloor in range(int(start_floor) + 1, int(end_floor) + 1):
        floor_rooms = {}
        
        for i in range(len(start_floor_rooms)):
            number = str(intfloor) + floor_last_number[i]
            info = start_floor_rooms[start_floor + floor_last_number[i]]
            floor_rooms[number] = info
        
        unit_rooms[str(intfloor)] = floor_rooms
    with open(r'windproject\CSV\assets.csv', 'a', newline='', encoding='GBK')as csvfile:
        writer = csv.writer(csvfile, dialect='excel')
        for sub_dict in unit_rooms.values():
            for room, info in sub_dict.items():
                dire = ['', '南北', '东西']
                writer.writerow([title, address, year, block,
                                 unit, room, dire[info[0]], info[1]])

    unit_continue = input('是否需要输入下一个单元？按 n 停止单元输入，按其他任意键继续：')
    if unit_continue == 'n':
        unit_loop = False
    else:
        unit_loop = True

print('恭喜你，资产录入工作完成！')


        






       


