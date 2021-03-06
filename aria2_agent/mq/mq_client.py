# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import logging
import json
import threading


class MQClient(object):
    client = None
    on_close = None
    
    def __init__(self, device_id):
        self.device_id = device_id
    
    def connect(self):
        """连接"""
        self.client = mqtt.Client()
        self.client.on_connect = self.on_mq_connect
        self.client.on_disconnect = self.on_mq_disconnect
        self.client.on_message = self.on_mq_message
        
        self.client.username_pw_set('aria2', 'aria2')
        
        def run(client, fail_callback):
            try:
                client.connect("10.211.55.5", 1883, 60)
                client.loop_forever()
            except BaseException, e:
                print('连接远程服务器失败 %s' % str(e))
                fail_callback()
        
        t1 = threading.Thread(target=run, name='mq', args=(self.client, self.on_close))
        t1.start()
    
    def close(self):
        """关闭连接"""
        self.client.disconnect()
    
    def on_mq_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print "已连接到远程服务器..."
        else:
            print "远程服务器连接失败，稍候重试，错误码 %d" % rc
        
        queue = "aria2_read/%s" % self.device_id
        print('订阅 %s' % queue)
        client.subscribe(queue)
    
    def on_mq_disconnect(self, client, userdata, rc):
        """mq断开"""
        print('mq 断开')
    
    def publish(self, msg_id, message):
        """发布消息"""
        msgWapper = json.dumps({'msgId': msg_id, 'message': message})
        self.client.publish('aria2_write', msgWapper)
