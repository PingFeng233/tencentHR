# tencentHR
django还原腾讯招聘网站


该项目是用django搭建的一个web应用,基本的登录,注册,页面信息展示,搜索多条件筛选,以及发布招聘岗位,上传简历,投递简历等功能都已实现;
但是还有很多地方还没有完善,用户注册没有加token验证,密码修改的功能没有做,等有空再完善一下

招聘岗位数据是用scrapy爬虫获取的,源码附上:
https://github.com/PingFeng233/TencentHR_crawl

项目已经用openresty + gunicorn 用wgsi部署在服务器上了
地址:http://120.77.250.162:23333/index
测试账号:
企业版: 账号:张三 密码:123456 部门:招聘部
个人版: 账号:张三 密码:123456
