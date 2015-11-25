# MoNiGuaJi
INIT 2015.11.25

## Part.总述
修改：
  账号 密码 课程名 单元名

脚本效果：

  运行脚本：填写的单元课程学习时长增加一小时，课程学习时长增加一小时
  
  一直开启脚本：总在线时长和挂机一样持续增加

## 湖北工业大学英语挂机脚本说明
By 写了一整天代码没去上课也没吃饭的kindJeff

### Part0.前提说明
#### **这个脚本执行之后会立即把你填写的书籍的单元挂机时长增加一小时，所以为了不让你有一个挂了数小时的单元，建议每次运行前一定要记得修改书籍和对应单元。**

前提条件：必须可以访问http://10.215.27.244/NPELS/  （必须是可联机的校内电信网或者学校局域网，包括湖工的WIFI）

### Part1.下载这个脚本
在页面上找到Download ZIP按钮，下载，并且全部解压

速度慢的话可以在度盘下载 http://pan.baidu.com/s/1qWN7sYS

会得到几个文件和一个名为Pyhton27的文件夹。

### Part2.修改个人信息
在解压出来文件夹目录找到MoNiGuaJi.py文件，右键选择使用记事本等编辑器打开

第7行 `account = ''` ，单引号中写入你的学号

第8行 `password='888888'`，单引号中写入你的密码（默认888888）

第9行 `book = 'College_English_NEW_Century_SecEdition_Integration_3'` ，单引号中写入书的英文名称（最下面有对应名称）

第10行 `unit = 'Unit_06'` ，单引号中写入单元的英文名称（第X单元：Unit_0X）

>**例：**第九行College_English_NEW_Century_SecEdition_Integration_1第十行Unit_06就代表新世纪大学英语（第二版）综合教程第一册 的 第六单元

保存MoNiGuaJi.py

### Part3.运行
右键MoNiGuaJi.py，选择打开方式，选择解压出的Python27文件夹的pyhton.exe

>另一种说法：右键点击MoNiGuaJi.py，选择用Python27文件夹下的python.exe打开

如果已经在网页或者客户端切换好班级，这个步骤可以省略，直接回车
>他会读取你的所有班级

>每个班级前面有一个对应的classNo，注意看仔细

>然后会列出你当前的classNo，如果classNo不是你想要的对应班级，输入想切换的classNo，保证你的输入是正确的，回车

出现一堆乱七八糟的东西，和一句`0 minutes`

**现在，你所填写的单元时长增加了一个小时**
![Foo](https://github.com/sljeff/MoNiGuaJi/raw/master/Photos/append60.png)

### Part4.等待
如果你现在关掉这个脚本，登陆挂机中心，会发现自己填写的单元挂机时长增加了一个小时，课程挂机时长也增加了一个小时。

但但但但但是，你的在线总时长没有变。

这就会出现奇怪的现象，课程时间瞬间增加一小时，在线时间不变

>在线总时间 0分钟   课程学时时间 60分钟

![Foo](https://github.com/sljeff/MoNiGuaJi/raw/master/Photos/strange.png)

在线时长的计算是在服务端验证的，所以没有办法一次性改变。

OK，这就是这个脚本的另一个作用——挂着它可以增加总学习时间和总在线时间。由于不能保证老师只看课程学习时间不看在线时间然后，发现其中的猫腻，为了万无一失，你可以一直开启这个脚本，不关闭它。只需要当它出现了`0 minutes`时把它最小化，不用管它，你的在线总时长会像在听力中心挂机一样不断增加。什么时候不想挂机了，关闭这个脚本即可。

![Foo](https://raw.githubusercontent.com/sljeff/MoNiGuaJi/master/Photos/always.png)

这个脚本的步骤完全模拟抓取的客户端的POST，可以放心使用。不放心的可以自己抓个包对比验证一下。

###PartPS.PS
好吧被同学打击了……写完总的感觉是脚本意义不是特别大，除了瞬间增加一小时的课程学习时间比较炫酷，剩下唯一的作用只是你可以不用像在网页端或者听力中心那样需要管它，不要不关闭它就能持续的增加课程学习时间和总体在线时间。
![Foo](https://github.com/sljeff/MoNiGuaJi/raw/master/Photos/time.png)
### PartMore.书籍的对应英文名
  新世纪大学英语快速阅读教程第一册
  College_English_NEW_Century_Fast_Reading_1

  （以此类推：新世纪大学英语快速阅读教程第二册  College_English_NEW_Century_Fast_Reading_2）

  新世纪大学英语综合教程第一册
  College_English_NEW_Century_Integration_1

  新世纪大学英语（第二版）综合教程第一册
  College_English_NEW_Century_SecEdition_Integration_1

  新世纪大学英语视听说教程第一册
  College_English_NEW_Century_Video_1

  新世纪大学英语（第二版）视听说教程（3rd Edition）第一册
  College_English_NEW_Century_Video_ThirdEdition_1

  大学英语（第三版）精读第一册
  College_English_third_Edition_Integration_1

  大学英语（第三版）听说第一册
  College_English_third_Edition_Listening_1

### PartMoreMore.备注

  MoNiGuaJi.py第72行
  
  `anHourAgo = time.strftime('%y.%m.%d %H:%M:%S',time.localtime(time.time()-3600))`

  修改为

  `anHourAgo = time.strftime('%y.%m.%d %H:%M:%S',time.localtime(time.time()))`

  可以让打开时所选单元时长不增加


By kindJeff
