#未安装Twisted， 暂不能运行
from twisted.internet import protocol, reactor

HOST = 'localhost'
PORT = 21567

class TSClntProtocol(protocol.Protocol):
	def sendData(self):
		data = input('> ')
		if data:
			print('...sending %s...' % data)
			self.transport.write(data)
		else:
			self.transport.loseConnection()
		
	def connectionMade(self):
		self.sendData()
		
	def dataReceived(self, data)
		print(data)
		self.sendData()
		
class TSClntFactory(protocol, ClintFactory):
	protocol = TSClntProtocol
	clientConnectionLost = clientConnectionFailed = lambda self, connector, reason: reactor.stop()
	
reactor.connectTCP(HOST, PORT, TSClntFactory())
reactor.run()
