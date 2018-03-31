{"filter":false,"title":"main.py","tooltip":"/main.py","ace":{"folds":[],"scrolltop":213,"scrollleft":0,"selection":{"start":{"row":18,"column":10},"end":{"row":18,"column":10},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":17,"state":"start","mode":"ace/mode/python"}},"hash":"8504365db4bf9e580002fbe57e108e1ada88ccc8","undoManager":{"mark":8,"position":8,"stack":[[{"start":{"row":0,"column":0},"end":{"row":36,"column":0},"action":"insert","lines":["from __future__ import print_function # Python 2/3 compatibility","import boto3","","dynamodb = boto3.resource('dynamodb', region_name='us-west-1')","","","table = dynamodb.create_table(","    TableName='Swipes',","    KeySchema=[","        {","            'AttributeName': 'year',","            'KeyType': 'HASH'  #Partition key","        },","        {","            'AttributeName': 'title',","            'KeyType': 'RANGE'  #Sort key","        }","    ],","    AttributeDefinitions=[","        {","            'AttributeName': 'year',","            'AttributeType': 'N'","        },","        {","            'AttributeName': 'title',","            'AttributeType': 'S'","        },","","    ],","    ProvisionedThroughput={","        'ReadCapacityUnits': 10,","        'WriteCapacityUnits': 10","    }",")","","print(\"Table status:\", table.table_status)",""],"id":1}],[{"start":{"row":12,"column":10},"end":{"row":16,"column":9},"action":"remove","lines":["","        {","            'AttributeName': 'title',","            'KeyType': 'RANGE'  #Sort key","        }"],"id":2},{"start":{"row":12,"column":9},"end":{"row":12,"column":10},"action":"remove","lines":[","]}],[{"start":{"row":10,"column":30},"end":{"row":10,"column":34},"action":"remove","lines":["year"],"id":3},{"start":{"row":10,"column":30},"end":{"row":10,"column":31},"action":"insert","lines":["L"]},{"start":{"row":10,"column":31},"end":{"row":10,"column":32},"action":"insert","lines":["o"]},{"start":{"row":10,"column":32},"end":{"row":10,"column":33},"action":"insert","lines":["c"]},{"start":{"row":10,"column":33},"end":{"row":10,"column":34},"action":"insert","lines":["a"]},{"start":{"row":10,"column":34},"end":{"row":10,"column":35},"action":"insert","lines":["t"]},{"start":{"row":10,"column":35},"end":{"row":10,"column":36},"action":"insert","lines":["i"]},{"start":{"row":10,"column":36},"end":{"row":10,"column":37},"action":"insert","lines":["o"]},{"start":{"row":10,"column":37},"end":{"row":10,"column":38},"action":"insert","lines":["p"]},{"start":{"row":10,"column":38},"end":{"row":10,"column":39},"action":"insert","lines":["n"]}],[{"start":{"row":10,"column":38},"end":{"row":10,"column":39},"action":"remove","lines":["n"],"id":4},{"start":{"row":10,"column":37},"end":{"row":10,"column":38},"action":"remove","lines":["p"]}],[{"start":{"row":10,"column":37},"end":{"row":10,"column":38},"action":"insert","lines":["n"],"id":5}],[{"start":{"row":17,"column":30},"end":{"row":17,"column":31},"action":"remove","lines":["N"],"id":10}],[{"start":{"row":17,"column":30},"end":{"row":17,"column":31},"action":"insert","lines":["S"],"id":11}],[{"start":{"row":16,"column":30},"end":{"row":16,"column":34},"action":"remove","lines":["year"],"id":12},{"start":{"row":16,"column":30},"end":{"row":16,"column":31},"action":"insert","lines":["L"]},{"start":{"row":16,"column":31},"end":{"row":16,"column":32},"action":"insert","lines":["o"]},{"start":{"row":16,"column":32},"end":{"row":16,"column":33},"action":"insert","lines":["c"]},{"start":{"row":16,"column":33},"end":{"row":16,"column":34},"action":"insert","lines":["a"]},{"start":{"row":16,"column":34},"end":{"row":16,"column":35},"action":"insert","lines":["t"]},{"start":{"row":16,"column":35},"end":{"row":16,"column":36},"action":"insert","lines":["i"]},{"start":{"row":16,"column":36},"end":{"row":16,"column":37},"action":"insert","lines":["o"]},{"start":{"row":16,"column":37},"end":{"row":16,"column":38},"action":"insert","lines":["n"]}],[{"start":{"row":19,"column":0},"end":{"row":22,"column":10},"action":"remove","lines":["        {","            'AttributeName': 'title',","            'AttributeType': 'S'","        },"],"id":13},{"start":{"row":18,"column":10},"end":{"row":19,"column":0},"action":"remove","lines":["",""]}]]},"timestamp":1522483995552}