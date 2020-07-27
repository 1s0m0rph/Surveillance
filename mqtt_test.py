import paho.mqtt.client as mqtt

MQTT_SERVER = "localhost"#TODO figure out how to scan for available external connections here
MQTT_TOPIC = "test_topic"

def on_connect(client, user_data, flags, result_code):
	print("Connected. Result code: {}".format(result_code))
	
	client.subscribe(MQTT_TOPIC)
	
def on_message(client, user_data, msg):
	print("Topic: {}; payload: {}".format(msg.topic,msg.payload))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_SERVER)

client.loop_forever()
