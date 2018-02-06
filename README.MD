# Aria2Agent
aria2的代理,这个项目的目的是实现远程操作没有外网ip的aria2。
# 原理
* websocket监控aria2各种事件
* 调用aria2 JsonRpc接口操作aria2
* 使用mqtt协议内外网通讯

# 项目进展
树莓派调试中，问题应该不大，最终希望可以跑在openwrt的路由器上。

树莓派raspbian系统pip安装的软件，bin目录是`/home/pi/.local/bin` 该目录默认没有在环境变量PATH中，所以pip安装后无法直接启动，需要先配置环境变量.
