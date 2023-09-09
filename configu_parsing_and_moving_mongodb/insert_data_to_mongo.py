import pymongo
from pprint import pprint
from parsing import trace_func



def mongo_update():
    client = pymongo.MongoClient('localhost', 27017)
    data_list_to_insert = trace_func()
    #print(client)
    mydb = client["parsed_config"]
    mycollec = mydb["traceroute_data"]

    #databse_names = client.list_database_names()
    #pprint(collection_names)

    delete_record = mycollec.delete_many({})
    inserted_data = mycollec.insert_one(data_list_to_insert)

    print(delete_record.deleted_count,"documents deleted")
    collection_names = mydb.list_collection_names()
    
    document_count_in_collection = mycollec.count_documents({})
    print("total number of documents collected :", document_count_in_collection)

    # for db_name in databse_names:
    #    print(db_name)

if __name__ == '__main__':
    mongo_update()
    

