{"filter":false,"title":"update.py","tooltip":"/update.py","undoManager":{"mark":-1,"position":-1,"stack":[[{"start":{"row":19,"column":0},"end":{"row":30,"column":1},"action":"remove","lines":["response = table.update_item(","    Key={","        'Location': \"location\"","    },","    UpdateExpression=\"set info.price = :prce, info.quantity=:amt, info.timee=:tme\",","    ExpressionAttributeValues={","        ':prce': 6,","        ':amt': 20,","        ':tme': \"5-6\"","    },","    ReturnValues=\"UPDATED_NEW\"",")"],"id":67},{"start":{"row":19,"column":0},"end":{"row":23,"column":5},"action":"insert","lines":["    response = table.get_item(","        Key={","            'Location':\"location\"","        }","    )"]}]]},"ace":{"folds":[],"scrolltop":10,"scrollleft":0,"selection":{"start":{"row":17,"column":0},"end":{"row":17,"column":32},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1522508360736,"hash":"4dcd6cc026458bc582110e19f448e6e31a4bfdd0"}