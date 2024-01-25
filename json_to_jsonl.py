import jq
import json

# Opening JSON file 
f = open('products_feed_2024-01-09-0402.json') 
data = json.load(f)

payload = jq.compile(".products[] as $parent | $parent.localizedAttributes.en_XD.name as $productname | $parent | {code, brand, $productname, salesAreaProperties}").input_value(data).text()

#payload = iter(jq.compile(".products[] as $parent | $parent.localizedAttributes.en_XD.name as $productname | $parent | {code, brand, $productname, salesAreaProperties}").input_value(data))

# Opening a file for writing
file_object = open("output.txt", "w")
file_object.writelines(payload)


# for tuple in payload:
#   #print(tuple)
#   file_object.writelines(tuple)

#print(payload)
file_object.close()

