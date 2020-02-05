#导入模块
import serial

#功能选择
print("-----功能选择开始-----")
print("0  -  串口测试")
print("1  -  串口监控（暂未完成）")
print("2  -  645-2007报文监控（暂未完成）")
print("3  -  1376.1报文监控（暂未完成）")
print("4  -  OOP报文监控（暂未完成）")
#str_func = input("请输入功能编码：")
str_func = "0"
print("-----功能选择结束-----")

if str_func == "0":
    #获取可用串口列表
    print("-----获取可用串口列表开始-----")
    import serial.tools.list_ports
    port_list = list(serial.tools.list_ports.comports())
    print(port_list)
    if len(port_list) == 0:
        print("无可用串口")
    else:
        for i in range(0,len(port_list)):
            print(port_list[i])
    print("-----获取可用串口列表结束----------")
    print("")

    str_port = input("请输入串口序号数字：")
    str_bps = input("请输入串口波特率：")
    str_parity = input("请输入校验方式(N,0,E)：")

    #打开端口写数据
    try:
        #设置端口
        #portx = 'COM3'
        portx = 'COM'+str_port

        #设置波特率,标准值之一。
        #bps = 115200
        bps = str_bps

        #设置校验方式
        parityx = str_parity

        #设置超时时间：None为永远等待，O为立即返回请求结果。其他值为等待超时时间。单位为秒
        timex = 1

        #设置字节超时时间
        inter_byte_timeoutx = 1
        

        #打开串口，并得到串口对象
        ser = serial.Serial(portx,bps,parity = parityx,timeout = timex,inter_byte_timeout = inter_byte_timeoutx)

        #显示串口详情
        print("-----显示串口参数详情开始-----")   
        print("串口参数详情：",ser)
        print("-----显示串口参数详情结束----------")
        print("")
    
        #写数据
        print("-----写gbk编码字符串开始-----")
        result = ser.write("我是东晓东".encode("gbk"))
        print("写字符总字节数：",result)
        print("-----写gbk编码字符串结束----------")
        print("")
    
        #十六进制发送，验证上传
        #print("-----写16进制字符开始-----")
        #result = ser.write(chr(0x06).encode("utf-8"))
        #print("写16进制字节总数：",result)
        #print("-----写16进制字符结束----------")
        #print("")
    
        #十六进制读取，读一个字节
        #print("-----读取一个字节开始-----")
        #print(ser.readline().decode("gbk"))
        #print("-----读取一个字节结束----------")
        #print("")
    
        #print(ser.read())#读一个字节
        #print(ser.read(10).decode("gbk"))#读10个字节
        #print(ser.readline().decode("gbk"))#读一行
        #print(ser,readlines())#读取多行，返回列表。必须匹配超时（timeout）使用
        #print(ser.in_waiting)#获取输入缓冲区的剩余字节数
        #print(ser.out_waiting)#获取输出缓冲区的字节数

        #循环接收数据，此为死循环，可用线程实现
        print("-----循环接收数据开始----------")
        while True:
            if ser.in_waiting:
                str = ser.read(ser.in_waiting).decode("gbk")
                if str == "exit":#退出标志
                    break
                else:
                    print(portx,"收到数据：",str)
        print("-----循环接收数据结束----------")

    
        #关闭串口
        ser.close()

    except Exception as e:
        print("---串口异常---:",e)
else:
    if str_func == "1": # 1  -  串口监控（暂未完成）
        print("串口监控功能暂未完成")
    else:
        if str_func == "2": # 2  -  645-2007报文监控（暂未完成）
            print("645-2007报文监控功能暂未完成")
        else:
            if str_func == "3": # 3  -  1376.1报文监控（暂未完成）
                print("1376.1报文监控功能暂未完成")
            else:       
                if str_func == "4": # 4  -  OOP报文监控（暂未完成）
                    print("OOP报文监控暂未完成")
                else:
                    print("所选功能暂不支持")
    
    


    
