import pika
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.basic_publish(exchange='fission-workflow',
                      routing_key='fission',
                      body='{"function-name": "last", "git-url": "https://github.com/omer5yerushalmi/fission-workflow-example.git", "env-name": "python"}')
