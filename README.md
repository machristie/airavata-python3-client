
# Running

* copy airavata-client.ini.template to airavata-client.ini and change properties
* install Python 3
* create a virtual environment and activate it
```
python3 -m venv ENV
. ENV/bin/activate
```
* install dependencies
```
pip install -r requirements.txt
```

# Generating Thrift Stubs

The thrift stubs are committed into the repo. These notes are on how I
generated the thrift stubs and can be useful if needing to regenerate them.

Thrift 0.10.0 is required to generate Python 3 compatible Thrift stubs.

I decided to use Docker to run Thrift 0.10.0, but that isn't necessary. To
use Docker for Thrift
* download [Thrift 0.10.0 tarball](https://thrift.apache.org/) and untar it
* in thrift-0.10.0 run the following
```
docker build -t thrift-0.10.0 .
```
* checkout [airavata](https://git-wip-us.apache.org/repos/asf?p=airavata.git) and run thrift
```
cd airavata/thrift-interface-descriptions
mkdir target
docker run --rm -v "$PWD:/data" thrift-0.10.0 --gen py -r -o /data/target /data/airavata-apis/airavata_api.thrift
```
* then copy the generated files into the current directory
```
cp -r target/gen-py/ /path/to/this/repo
```

## Error: DataReplicaLocationModel is not defined

      (ENV) BL-UITS-RTLT021:airavata-python3 machrist$ python test.py 
      Traceback (most recent call last):
        File "test.py", line 2, in <module>
          from apache.airavata.api import Airavata
        File "/Users/machrist/Documents/Airavata/airavata-python3/apache/airavata/api/Airavata.py", line 13, in <module>
          from .ttypes import *
        File "/Users/machrist/Documents/Airavata/airavata-python3/apache/airavata/api/ttypes.py", line 14, in <module>
          import apache.airavata.model.ttypes
        File "/Users/machrist/Documents/Airavata/airavata-python3/apache/airavata/model/ttypes.py", line 24, in <module>
          import apache.airavata.model.data.replica.ttypes
        File "/Users/machrist/Documents/Airavata/airavata-python3/apache/airavata/model/data/replica/ttypes.py", line 67, in <module>
          class DataProductModel(object):
        File "/Users/machrist/Documents/Airavata/airavata-python3/apache/airavata/model/data/replica/ttypes.py", line 97, in DataProductModel
          (12, TType.LIST, 'replicaLocations', (TType.STRUCT, (DataReplicaLocationModel, DataReplicaLocationModel.thrift_spec), False), None, ),  # 12
      NameError: name 'DataReplicaLocationModel' is not defined

Problem is that DataReplicaLocationModel is defined after DataProductModel

Solution was to reorder the generated Python code.

