# Raspberry-Car

#### 介绍
该小车实现了 自动避障，实时图像传输(网络摄像头)，目标检测（yolo5），ui控制（QT）
硬件采用树莓派4B, L298N驱动，CSI树莓派摄像头，6个红外传感器，4个轮胎+4个马达，12V电源+充电宝



#### 教程

##### 1.小车组装+操作系统安装等操作
##### 2.CSI摄像头激活
######     步骤1 分布执行以下命令行进行下载并安装最新的内核，GPU 固件及应用程序。
    sudo apt-get update
    sudo apt-get upgrade
######     步骤2 运行树莓派配置工具来激活摄像头模块.
    sudo raspi-config
######     ![输入图片说明](/image/1.png)
######     点击 ok
###### ![输入图片说明](/image/2.png)
######     选择Interface Options
######     ![输入图片说明](/image/3.png)
######     选择第一个，后面一直选择OK就行。
######     用如下命令使用摄像头。
    raspistill -v -o test.jpg
######     出现以下内容应该是ok了
######     ![输入图片说明](/image/4.png)

##### 3.python环境搭建
###### （1）python 下载
        sudo apt-get update
        sudo apt-get install python3.8
###### (2)opencv 下载
######         因为opencv存在一些依赖问题所以安装前需要提前安装一些内容
######         a.numpy 安装较新的版本
        安装：pip install numpy 
        升级：pip install --upgrade numpy
        卸载：pip uninstall numpy
        查看：pip list
######        b.如果报这个错 libcblas.so.3: cannot open shared object file: No such file or directory
        sudo apt-get install libatlas-base-dev
######         c.安装opencv
        pip install opencv-python  
######         下载可能会很慢，建议换源
        清华：https://pypi.tuna.tsinghua.edu.cn/simple
        阿里云：http://mirrors.aliyun.com/pypi/simple/
        中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
        华中理工大学：http://pypi.hustunique.com/       
        山东理工大学：http://pypi.sdutlinux.org/ 
        豆瓣：http://pypi.douban.com/simple/    
        pip install opencv-python  -i https://pypi.tuna.tsinghua.edu.cn/simple 临时用用也行  
        d.进入python导入cv2包没问题就下载好了
######     （3）安装GPIO相关库  
        pip install rpi.gpio
######     （4）安装CSI摄像头相关库
        pip install picamera
##### 4.  QT界面设计
QT界面是设计的一个显示图像信息以及简单的控制界面
##### 5.  实时图像传输
使用的是忘记了什么协议（这个是后面来补的）
##### 6.  自动避障
自动避障程序为本项目根据传感器数据编写的一套完整的避障程序
##### 7.  目标检测
目标检测部分使用是yolov5，内容对应在AI文件内



