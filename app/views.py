from rest_framework.response import Response
from rest_framework.decorators import api_view
from zk import ZK, const

# Create your views here.
@api_view(['GET'])
def get(request):
    conn = None
    zk = ZK(ip = request.query_params.get('ip'), port = int(request.query_params.get('port') or 0) or 4370, timeout = 3)
    try:
        conn = zk.connect()
        conn.disable_device()
        attlogs = map(lambda x: {'uid': x.user_id, 'time': x.timestamp, 'state': x.punch}, conn.get_attendance())
    finally:
        if conn:
            conn.disconnect()
    return Response(attlogs)
