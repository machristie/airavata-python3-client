
from apache.airavata.api import Airavata
from apache.airavata.api.ttypes import *
from apache.airavata.model.workspace.ttypes import *
from apache.airavata.model.security.ttypes import AuthzToken

from thrift import Thrift
from thrift.transport import TSSLSocket
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:
    # Create a socket to the Airavata Server
    # TODO: validate server certificate
    transport = TSSLSocket.TSSLSocket('gw56.iu.xsede.org', 9930, validate=False)
    # transport = TSocket.TSocket('gw56.iu.xsede.org', 9930)

    # Use Buffered Protocol to speedup over raw sockets
    transport = TTransport.TBufferedTransport(transport)

    # Airavata currently uses Binary Protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a Airavata client to use the protocol encoder
    airavataClient = Airavata.Client(protocol)

    # Connect to Airavata Server
    transport.open()

    projectLists = airavataClient.getUserProjects(AuthzToken("dummy-token"), "seagrid", "marcus-user", -1, 0);

    print(projectLists)

    # Close Connection to Airavata Server
    transport.close()

except Thrift.TException as tx:
    print(tx.message)
    raise tx

