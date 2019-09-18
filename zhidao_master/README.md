# 使用说明
## 1.启动redis
```bash
# 可以使用自己的redis.conf配置文件
redis-server redis.conf
```

## 2.将要爬取的内容写入到tocrawl.txt文件当中

## 3.启动爬虫
```bash
# 后台执行程序，注意这个程序不会自行终止
python runspider.py -master 1 > log 2>&1 &
```

## 4.查看爬虫爬取进度
```bash
redis-cli

# 显示还有多少内容需要爬取，当为0的时候表明已经爬取完毕
llen zhidaospider:start_urls

# 显示已经爬取的数目
llen zhidaospider:items
```

## 5.终止爬虫
```bash
# 当爬取完毕 或者 要终止的时候
# 文件存储在 items.txt当中
ps aux | grep runspider | grep -v grep| awk -F ' ' '{print $2}' | xargs kill -9

# 还要关掉一个sh 启动爬虫的脚本

# 进入redis命令行
redis-cli
# 清除redis当中的内容
flushdb

# 关闭redis
shutdown
```

# some idea
- http://blog.csdn.net/yancey_blog/article/details/53887924
- http://blog.csdn.net/howtogetout/article/details/51633814
- 目前这个爬虫的架构还不是很好，可以将其中shell的部分分离出来
- 可以将主机放置在一个文件当中，像hadoop安装包那样，意见分布式爬取，一键分布式收集结果，一键停止所有进程
- 将配置爬取多少条的，写到配置文件当中
- 可以将爬取多少条数据放到redis内存当中
    + 从redis当中读取需要爬取的条目，可以动态的改变需要爬取的条目

## 如何添加下载中间件，UserAgent
- http://www.cnblogs.com/zhaof/p/7345856.html

## 为什么会使用redis
- 这是一个分布式爬虫，稍作修改可以使用多台机器进行分布式爬取
