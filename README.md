# Raspberry-Car

#### 介绍
该小车实现了 自动避障，实时图像传输(网络摄像头)，目标检测（yolo5），ui控制（QT）
硬件采用树莓派4B, L298N驱动，CSI树莓派摄像头，6个红外传感器，4个轮胎+4个马达，12V电源+充电宝



#### 教程

### 小车组装+操作系统安装等操作
### CSI摄像头激活
    步骤1 分布执行以下命令行进行下载并安装最新的内核，GPU 固件及应用程序。
    sudo apt-get update
    sudo apt-get upgrade
    步骤2 运行树莓派配置工具来激活摄像头模块.
    sudo raspi-config
    ![输入图片说明](image/1.png)
    点击 ok
    ![输入图片说明](image/2.png)
    选择Interface Options
    ![输入图片说明](image/3.png)
    选择第一个，后面一直选择OK就行。
    用如下命令使用摄像头。
    raspistill -v -o test.jpg
    出现以下内容应该是ok了
    ![输入图片说明](image/4.png)
### python环境搭建
    （1）python 下载
        sudo apt-get update
        sudo apt-get install python3.8
    (2)opencv 下载
        因为opencv存在一些依赖问题所以安装前需要提前安装一些内容
        a.numpy 安装较新的版本
            安装：pip install numpy 
            升级：pip install --upgrade numpy
            卸载：pip uninstall numpy
            查看：pip list
        b.如果报这个错 libcblas.so.3: cannot open shared object file: No such file or directory
            sudo apt-get install libatlas-base-dev    
        c.安装opencv
            pip install opencv-python  
            下载可能会很慢，建议换源
            清华：https://pypi.tuna.tsinghua.edu.cn/simple
            阿里云：http://mirrors.aliyun.com/pypi/simple/
            中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
            华中理工大学：http://pypi.hustunique.com/
            山东理工大学：http://pypi.sdutlinux.org/ 
            豆瓣：http://pypi.douban.com/simple/
            pip install opencv-python  -i https://pypi.tuna.tsinghua.edu.cn/simple 临时用用也行
        d.进入python导入cv2包没问题就下载好了
    （3）安装GPIO相关库
        pip install rpi.gpio
    （4）安装CSI摄像头相关库
        pip install picamera
4.  QT界面设计
5.  实时图像传输
6.  自动避障
7.  目标检测

#### 使用说明

1.  xxxx
2.  xxxx
3.  xxxx

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request


#### 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
