## 头脑王者辅助
### 使用方法
1. 将json题库导入到mongodb中
2. 设置手机代理——ip为电脑ip，端口为8080（也可自行定义，启动mitmproxy时 -p 端口号 设置端口 ）
3. mitmproxy -s tn.py 启动交互界面后，按e即可查看
### 说明
- 捕获到题目后，查找题库，显示结果。若题库没有该题，则自行回答即可
- 代码会将新出现的题存入库中，再遇见就不怂了
- 题库已有16000多题，基本够用了
### 题库来源： https://github.com/zhuweiyou/weixin-game-helper









