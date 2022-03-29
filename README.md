## 功能
简谱爬虫，自己输入歌曲名称即可抓取到对应的多个曲谱图片文件。

## 背景
- 吹笛子，弹电子琴，想参考点曲谱。
- 首先就是从网盘里下载打包好的，发现并没有资源，也搜不到，那就换个方向，从乐谱网站上下载好了，但是下载需要一直点啊点的，在我看来极其繁琐，性价比太低，如果能自动一下子都下载下来就好了，于是。。。那就用爬虫吧。

## 项目思路
1.  找一个能下载曲谱的网站，找到一个 http://www.jianpuw.com/ 。
2.  查看首页及单独歌曲页的源码，找到解析的方式。
3.  创建python虚拟环境，在虚拟环境内安装爬虫所需要的库。
4.  利用该站点的站内搜索功能来指定歌曲名称进行coding，调试。
5.  运行脚本保存到指定的路径内。

## 使用方法：
### 1. 创建环境

```
$ cd /Users/xxxx/yyy/zzz
$ pip install virtualenv
$ virtualenv MyCrawler
```

### 2. 安装所需的库

```
 $   pip install bs4
 $   pip install beautifulsoup4
 $   pip install requests
 $   pip install lxml
 $   pip install selenium
```

### 3. 安装 ChromeDriver
1.  先安装Chrome浏览器
2. 下载ChromeDriver: https://registry.npmmirror.com/binary.html?path=chromedriver/
3. 下载后的ChromeDriver可执行文件拷贝到第1步的虚拟环境python所在的目录下

> 提示：只能安装跟当前电脑上chrome浏览器版本一致的 ChromeDriver.

### 4. 执行脚本
- 使用方法：

```SHELL
$ source /Users/xxxx/yyy/zzz/MyCrawler/activate
$ python Num_Musical_Notation_Crawler.py 歌曲名称
```

- 示例

```SHELL
$ python Num_Musical_Notation_Crawler.py 精忠报国
==================================================  Start  ==================================================
精忠报国 http://www.jianpuw.com/htm/ld/3049.htm
=========================  Start to parse image page. =========================
None == http://www.jianpuw.com//images/logo.jpg
=========================  End of parse image page. =========================
IMG:  /XXX/XXX/XXX/精忠报国/logo.jpg
=========================  Start to parse image page. =========================
None == http://www.jianpuw.com//images/s.gif
=========================  End of parse image page. =========================
IMG:  /XXX/XXX/XXX/精忠报国/精忠报国/s.gif
=========================  Start to parse image page. =========================
精忠报国1 == http://www.jianpuw.com//img/6/t3/6dxn8nt3.jpg

....... (下面还有很多很多，这里只截取头部几个作为示意)
```

## 说明
- 在脚本中指定的路径下，以歌曲名称（即执行脚本时给定的关键字）来新建目录，图片名称不变，因为歌曲就一个名称，每首歌可能会抓到几十甚至几百个曲谱图片，图片以歌曲命名的话会不断重复覆盖，最终只能得到几个文件，所以图片名字还以网址上hash之后的原名，这样保证可以不被覆盖，也就不会有遗漏下载，自己挑选喜欢的曲谱图片即可，总有一个是自己喜欢的。

