# auto-signin
Auto sign in
 
## 自动登录签到

目前支持：
### 1. 招商银行信用卡微信自动签到
### 2. 通用型自动签到
1. 先抓包找到cookie 填到user_cookies.json文件相应的地方
2. 在signin_template里填写header之类的数据
3. 设置crontab定时运行
4. 后台运行脚本nohup python -u signin.py > signin.log 2>&1 &



