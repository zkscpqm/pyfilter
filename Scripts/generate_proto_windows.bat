..\venv\Scripts\python.exe -m grpc_tools.protoc -I..\pyfilter\proto --grpc_python_out=../pyfilter/src/transport/proto --python_out=../pyfilter/src/transport/proto ..\pyfilter\proto\filter_service\*.proto
