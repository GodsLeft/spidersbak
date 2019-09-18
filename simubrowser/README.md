# 这是一个简单的爬虫，模拟浏览器操作
- huataidemo.py是完整版的爬虫
- parseresult.py
    + 将新的问题解析出来    
    + 将去重过滤已经爬过的问题

# 后期可以改进的地方
- 边爬取边解析
- 多线程或者多进程的爬取
- 分布式爬取redis

# 在使用的过程中出现的问题
- 在爬取了400页之后，输入问题，就反映的很慢
    + 通过刷新浏览器
    + 超时等待
- 在处理等待时间上，要有所改进，比如超过太长时间就刷新(目前只是固定次数刷新)

# bugs
- 在使用plantomJS的时候，发现无法向iframe当中输入数据，但是使用chromedriver的时候却可以

# 参考文章
- http://blog.csdn.net/huilan_same/article/details/52386274
    + 如何向iframe当中输入
